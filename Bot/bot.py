import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.filters.command import CommandObject
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

TOKEN = "8532184522:AAFYzJW6fqVncmxX_dbmYFqFdJWC9MBF_OY"

bot = Bot(TOKEN)
dp = Dispatcher()

orders_db = {}

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить заказ")],
        [KeyboardButton(text="Посмотреть заказы")],
        [KeyboardButton(text="Изменить заказ")],
        [KeyboardButton(text="Удалить заказ")],
    ],
    resize_keyboard=True
)


class OrderForm(StatesGroup):
    name = State()
    item = State()
    time = State()
    edit_id = State()  


@dp.message(Command("basket"))
async def basket_cmd(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=menu)


@dp.message(lambda msg: msg.text == "Добавить заказ")
async def add_order(message: types.Message, state: FSMContext):
    await message.answer("1. Как вас зовут?")
    await state.set_state(OrderForm.name)


@dp.message(OrderForm.name)
async def step_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("2. Что вы хотите заказать?")
    await state.set_state(OrderForm.item)


@dp.message(OrderForm.item)
async def step_item(message: types.Message, state: FSMContext):
    await state.update_data(item=message.text)
    await message.answer("3. Когда привести заказ?")
    await state.set_state(OrderForm.time)


@dp.message(OrderForm.time)
async def step_time(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    orders_db.setdefault(user_id, [])

    data = await state.get_data()
    data["time"] = message.text

    order_id = len(orders_db[user_id]) + 1
    data["id"] = order_id

    orders_db[user_id].append(data)

    await state.clear()
    await message.answer(f"Заказ №{order_id} добавлен!", reply_markup=menu)


@dp.message(lambda msg: msg.text == "Посмотреть заказы")
async def show_orders(message: types.Message):
    user_id = str(message.from_user.id)

    if user_id not in orders_db or len(orders_db[user_id]) == 0:
        await message.answer("У вас нет заказов.")
        return

    text = "Ваши заказы:\n\n"
    for order in orders_db[user_id]:
        text += (
            f"ID: {order['id']}\n"
            f"Имя: {order['name']}\n"
            f"Заказ: {order['item']}\n"
            f"Время: {order['time']}\n\n"
        )

    await message.answer(text)


@dp.message(lambda msg: msg.text == "Удалить заказ")
async def ask_delete(message: types.Message):
    await message.answer("Введите ID заказа для удаления:")


@dp.message(lambda msg: msg.text.isdigit())
async def delete_order(message: types.Message):
    user_id = str(message.from_user.id)
    order_id = int(message.text)

    if user_id not in orders_db:
        await message.answer("У вас нет заказов.")
        return

    before = len(orders_db[user_id])
    orders_db[user_id] = [o for o in orders_db[user_id] if o["id"] != order_id]

    if len(orders_db[user_id]) == before:
        await message.answer("Заказ с таким ID не найден.")
        return

    for i, o in enumerate(orders_db[user_id], start=1):
        o["id"] = i

    await message.answer("Заказ удалён!", reply_markup=menu)


@dp.message(lambda msg: msg.text == "Изменить заказ")
async def update_start(message: types.Message, state: FSMContext):
    await message.answer("Введите ID заказа для изменения:")
    await state.set_state(OrderForm.edit_id)


@dp.message(OrderForm.edit_id)
async def update_step_ask_field(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Введите корректный ID (число).")

    user_id = str(message.from_user.id)
    order_id = int(message.text)

    if user_id not in orders_db or order_id > len(orders_db[user_id]):
        return await message.answer("Заказ с таким ID не существует.")

    await state.update_data(edit_id=order_id)
    await message.answer("Введите новое имя:")
    await state.set_state(OrderForm.name)  


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я твой бот по заказам.", reply_markup=menu)


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
