from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    def refund(self,amount):
        pass

class CreditCardPayment:
    def pay (self,amount):
        return f'Оплата {amount} сом прошла норм'
    
    def refund (self,amount):
        return f'возврат {amount} сом выполнен'

class CryptoPayment:
    def pay (self, amount):
        return f'Перевод {amount} сом выполнен'
    def refund (self,amount):
        return f'возврат {amount} сом прошел норм'
    
payments = [CreditCardPayment(), CryptoPayment()]
        
for payment in payments:
            print(payment.pay(777))
            print(payment.refund(666))






from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start (self):
        pass
    def get_materials(self):
        pass
    def end (self):
        pass

class PythonCourse(Course):
    def start(self):
        return 'чтото там с пайтоном'
    
    def get_materials(self):
        return 'материалы:принты,потолки,С#'

    def end (self):
        return 'конец'

    
class MatrhCourse(Course):
    def start(self):
        return 'Матика'
    def get_materials(self):
        return 'материалы:линейки,отвертки,ядерный реактор'
    def end(self):
        return 'Конец'

courses = [PythonCourse(), MatrhCourse()]
for course in courses:
    print("_" * 60 )
    course.start()
    course.get_materials()
    course.end()





from abc import ABC, abstractmethod
class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass
    def deliver(self):
        pass

class AirDelivery(Delivery):
    def calculate_cost(self, distance):
        cost = distance * 15 
        return f'Стоимость леталки ({distance} км): {cost} сом.'

    def deliver(self):
        return 'Посылка отправлена леталкой.'
    
class GroundDelivery(Delivery):
    def calculate_cost(self, distance):
        cost = distance * 5 
        return f'Стоимость наземной пасилкэ({distance} км): {cost} сом.'

    def deliver(self):
        return' Посылка доставляется самокатом.'
    
class SeaDelivery(Delivery):
    def calculate_cost(self, distance):
        cost = distance * 3 
        return f'Стоимость морской селедки ({distance} км): {cost} сом.'

    def deliver(self):
        return 'Посылка отправлена морским аллигатором.'

deliveries = [ AirDelivery(), GroundDelivery(),SeaDelivery()]

distance = 1200

for delivery in deliveries:
        print("-" * 60)
        delivery.calculate_cost(distance)
        delivery.deliver()





class BankAccount:
    def __init__(self, owner, balance, pin):
        self.__owner = owner       
        self.__balance = balance    
        self.__pin = pin            

    def deposit(self, amount, pin):
        if pin != self.__pin:
           return' Неверный PIN-код. Доступ запрещён.'
            

        if amount <= 0:
            return' Сумма должна быть положительной.'

        self.__balance += amount
        return f' Пополнение: {amount} сом. Новый баланс: {self.__balance} сом.'

    def withdraw(self, amount, pin):
        if pin != self.__pin:
           return' Неверный PIN-код. Доступ запрещён'
        
        if amount <= 0:
            return' Сумма должна быть положительной.'

        if amount > self.__balance:
           return' Недостаточно средств на счёте'
        

        self.__balance -= amount
        return f' Снятие: {amount} сом. Остаток: {self.__balance} сом.'

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            return'Старый PIN введён неверно.'

        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            return '  Новый PIN должен состоять из 4 цифр.'

        self.__pin = new_pin
        return 'PIN-код успешно изменён!'

    def get_info(self, pin):
        if pin != self.__pin:
            return '  Неверный PIN-код. Доступ запрещён.'

        return f' Владелец: {self.__owner}, Баланс: {self.__balance} сом.'





class UserProfile:
    def __init__(self, email, password):
        self.__email = email          
        self.__password = password   
        self._status = "basic"        

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            print(f" Добро пожаловать, {self.__email}!")
            return True
        print(" Неверный логин или пароль. Доступ запрещён.")
        return False

    def upgrade_to_premium(self):
        if self._status == "premium":
            print("премка уже имеется")
        else:
            self._status = "premium"
            print(" поздравляю! теперь ты вип про хакер читер ")

    def get_info(self):
        print(f"Email: {self.__email}")
        print(f"Статус: {self._status}")



    

class Product:
    def __init__(self, name, price):
        self.name = name            
        self.price = price          
        self.__discount = 0         

    def get_price(self):
        discounted_price = self.price * (1 - self.__discount / 100)
        return round(discounted_price, 2)

    def set_discount(self, discount, is_admin=False):
        if not is_admin:
            print(" Доступ запрещён. Только администратор может установить скидон.")
            return

        if discount < 0 or discount > 100:
            print(" Скидка должна быть от 0 до 100%.")
            return

        self.__discount = discount
        print(f" Скидка {discount}% успешно установлена для товара '{self.name}'.")






class TextFile:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f" Открыт текстовый файл '{self.name}'.")


class ImageFile:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f" Открыто изображение '{self.name}'.")


class AudioFile:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f" Воспроизведён четкий репчик '{self.name}'.")


def open_all(files):
    for file in files:
        file.open()

if __name__ == "__main__":
    files = [
        TextFile("notes.txt"),
        ImageFile("photo.png"),
        AudioFile("song.mp3"),
        TextFile("todo.txt")
    ]

    open_all(files)





class Car:
    def __init__(self, fuel_consumption, speed):
        self.fuel_consumption = fuel_consumption  
        self.speed = speed                        

    def move(self, distance):
        time = distance / self.speed
        fuel_needed = distance * self.fuel_consumption / 100
        print(f" Атайс проедет {distance} км за {time:.2f} ч, потратит {fuel_needed:.2f} л топлива.")
        return time


class Truck:
    def __init__(self, fuel_consumption, speed):
        self.fuel_consumption = fuel_consumption
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        fuel_needed = distance * self.fuel_consumption / 100
        print(f" Бутылка проедет {distance} км за {time:.2f} ч, потратит {fuel_needed:.2f} л топлива.")
        return time


class Bicycle:
    def __init__(self, speed):
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        print(f" Велоси проедет {distance} км за {time:.2f} ч. Топливо не требуется.")
        return time

def simulate_transport(transport_list, distance):
    for transport in transport_list:
        transport.move(distance)

    transports = [Car(fuel_consumption=8, speed=100),Truck(fuel_consumption=20, speed=80), Bicycle(speed=25)]

    simulate_transport(transports, distance=200)





class Student:
    def access_portal(self):
        print(" Студент: играет в игры")


class Teacher:
    def access_portal(self):
        print(" Преподаватель: сидт")


class Administrator:
    def access_portal(self):
        print(" Администратор: спит")


users = [Student(), Teacher(), Administrator(), Student(),Teacher()]

for user in users:
        user.access_portal()



