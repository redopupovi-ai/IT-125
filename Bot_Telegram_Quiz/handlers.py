from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from quiz_data import Quiz

class BotHandlers:
    def __init__(self, bot):
        self.router = Router()
        self.bot = bot
        self.quiz = Quiz()
        self.user_data = {}  
        self.register_handlers()

    def register_handlers(self):
       
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_quiz, Command("quiz"))
        self.router.callback_query.register(self.handle_answer)

    async def start_command(self, message: types.Message):
        await message.answer(
            "Привет \n"
            "Я бот-викторина. У меня есть вопросы с картинками!\n"
            "Напиши /quiz чтобы начать игру "
        )

    async def start_quiz(self, message: types.Message):
        user_id = message.from_user.id
      
        self.user_data[user_id] = {
            "correct": 0, 
            "wrong": 0, 
            "q_index": 0
        }
        await self.send_question(message.chat.id, user_id)

    async def send_question(self, chat_id, user_id):
        data = self.user_data[user_id]
        q_data = self.quiz.get_question(data["q_index"])

        if not q_data:
            await self.finish_quiz(chat_id, user_id)
            return

        buttons = []
        for i, opt in enumerate(q_data["options"]):
            buttons.append([InlineKeyboardButton(text=opt, callback_data=f"ans_{i}")])
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

        try:
            photo = FSInputFile(q_data["image"])
            await self.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=f"Вопрос №{data['q_index'] + 1}:\n\n{q_data['question']}",
                reply_markup=keyboard
            )
        except Exception as e:
            await self.bot.send_message(
                chat_id, 
                f"Ошибка загрузки фото: {e}\n\n{q_data['question']}", 
                reply_markup=keyboard
            )

    async def handle_answer(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data = self.user_data.get(user_id)

        if not data:
            await callback.answer("Начните викторину заново через /quiz")
            return

        q_data = self.quiz.get_question(data["q_index"])

        selected_index = int(callback.data.split("_")[1])
        selected_answer = q_data["options"][selected_index]

        if selected_answer == q_data["correct"]:
            data["correct"] += 1
            await callback.answer("Верно!")
        else:
            data["wrong"] += 1
            await callback.answer(f"Ошибка! Правильно: {q_data['correct']} ")

        data["q_index"] += 1
        
        try:
            await callback.message.delete()
        except:
            pass

        await self.send_question(callback.message.chat.id, user_id)

    async def finish_quiz(self, chat_id, user_id):
        res = self.user_data[user_id]
        total = self.quiz.total_questions()
        
        result_text = (
            "Викторина завершена!\n\n"
            f" Правильных ответов: {res['correct']}\n"
            f" Неправильных ответов: {res['wrong']}\n"
            f"Всего вопросов: {total}"
        )
        
        await self.bot.send_message(chat_id, result_text, parse_mode="Markdown")
        
        del self.user_data[user_id]