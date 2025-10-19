        #БАНК

class Account:
    def __init__(self,pin, balance , account_number):
        self.__pin = pin 
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self,amount,pin):
        if pin == self.pin:
            if amount > 0:
                self.balance += amount
                
    def withdraw(self, amount ,pin):
        if pin == self.pin:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
               
    def get_balance(self,pin):
        if pin == self.__pin:   
            return self.__balance     


             #Продукты  

class Product:
    def __init__(self,price):
        self.__price = price

    def set_discount(self,percent):
        self.__price -= self.__price * (percent / 10)
        if self.__price < 0:
            self.__price = 0

    def final_price(self):
        return self

        #Студенты

class Course:
    def __init__(self,name,students,max):
        self.name = name
        self.max = max
        self.students = students

    def add_student(self,name):
        if len(self.students) < max:
            self.students.append(name)
    
    def remove_student(self,name):
        if name in self.students:
            self.students.remove(name)

    def get_students(self):
        return self.students.copy()


            #Заряд часов

class SmartWatch:
    def __init__(self,battery):
        self.__battery = battery

    def use(self,minutes):
        drain = minutes / 10
        self.__battery -= drain
        if self.__battery < 0:
            self.__battery = 0

    def charge(self,percent):
        self.__battery += percent
        if self.__battery > 100:
            self.__battery = 100
        
    def get_battery(self):
        return self.__battery

                #Транспорт
class Transport:
    def __init__(self,speed,vmestimost):
        self.speed = speed
        self.vmestimost = vmestimost
    def travel_time(self,distance):
        return distance / self.speed

class bus(Transport):
    pass

class train(Transport):
   pass

class airplane(Transport):
    def travel_time(self, distance):
        base_time = super(). travel_time(distance)
        return base_time * 0,8


          #Доставка

class order:
    def __init__(self,num):
        self.num = num
    def calcute_total(self):
        return self.num
    
class DinelnOrder(order):
    def __init__(self, ):
        return self.num * 10
    
class takeowerorder(order):
    def calcute_total(self):
        return self.num * 22
    
class deliverorder(order):
    def calcute_total(self):
        return self.num * 666

            #Персонажи с игры

class Character:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    def attack(self):
        pass
class warrior (Character):
    def __init__(self, name, health, attack):
      super().__init__(name, health, attack, "sword")   
    def attack(self):
        return self.attack * 2
    
class mage (Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack, "posoh")
    def attack(self):
        return self.attack * 666
    
class archer (Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack,"bow")
    def attack(self):
        return self.attack * 3
    

        #Медиафайлы

class MediaFile:
    def __init__(self,name,duration):
        self.name = name 
        self.duration = duration
    def play (self):
        pass

class AudioFile(MediaFile):
    def play(self):
        return f'{self.name} воспроизводится как аудио ({self.duration} мин)'
    
class VideoFile(MediaFile):
    def play(self):
        return f'{self.name} воспроизводится с изображением {self.duration}мин'
    
class Podcast(MediaFile):
    def play(self):
        return f'{self.name} воспроизводится эпизод {self.duration}мин'


        #Че то с банком

from abc import ABC, abstractclassmethod

class PaymentSystem (ABC):
        @abstractclassmethod

        def process_payment(self,amount):
            pass
class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        return amount * 8583


class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        return amount * 2222


class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        return amount * 111
    

        #Животные

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
class Lion(Animal):
    def eat(self):
        return "Лев ест людей,ммм ням ням"

    def sleep(self):
        return "Лев спит в космической тарелке"


class Elephant(Animal):
    def eat(self):
        return "Слон ест барабаны"

    def sleep(self):
        return "Слон спит в кровати"


class Snake(Animal):
    def eat(self):
        return "Змея ест слонов"

    def sleep(self):
        return "Змея спит"


    #Документы

from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def save(self):
        pass

class WordDocument(Document):
    def open(self):
        return "документ открыт"

    def edit(self):
        return "Редактирование "

    def save(self):
        return "документ сохранён"


class PdfDocument(Document):
    def open(self):
        return "PDF документ открыт"

    def edit(self):
        return "Редактирование  документа ограничено"

    def save(self):
        return "документ сохранён"


class SpreadsheetDocument(Document):
    def open(self):
        return "Таблица открыта"

    def edit(self):
        return "Редактирование таблицы"

    def save(self):
        return "Таблица сохранена"
    


    #Lesson

from abc import ABC, abstractmethod

class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass
class VideoLesson(Lesson):
    def start(self):
        return "Видеоурок начинается: воспроизведение видео"
    
class QuizLesson(Lesson):
    def start(self):
        return "Квиз-урок начинается: откройте тест"

class TextLesson(Lesson):
    def start(self):
        return "Текстовый урок начинается: откройте текстовый материал"
    

    #Email

class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Email отправлен с сообщением: {message}"


class SMSNotification(Notification):
    def send(self, message):
        return f"SMS отправлено с сообщением: {message}"


class PushNotification(Notification):
    def send(self, message):
        return f"Push уведомление отправлено с текстом: {message}"
    

    #Фигуры

import math

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    

    #Работа

class Employee:
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        return "Менеджер планирует задачи "

class Developer(Employee):
    def work(self):
        return "Разработчик пишет код и исправляет баги"

class Designer(Employee):
    def work(self):
        return "Дизайнер че то рисует"
    

    #Magic

class Spell:
    def cast(self, target):
        pass

class FireSpell(Spell):
    def cast(self, target):
        return f"{target} горит"

class IceSpell(Spell):
    def cast(self, target):
        return f"{target} замерз"

class HealingSpell(Spell):
    def cast(self, target):
        return f"{target} лютый отхил"









