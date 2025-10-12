class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    

    def eat(self, food):
        return f' {self.name} кушает {food}'

    def sleep(self, hours):
        return f'{self.name} спит {hours} часов'
    
    def __str__(self):
        return f"Имя: {self.name}\n Возвраст: {self.age} лет"
    
class Mammal(Animal):
    def __init__(self, age, name, color):
        super(). __init__(age, name)
        self.color = color

    def weight(self,kg):
        return f"{self.name}животное весит{kg}кг"
    
    def __str__(self):
        return super().__str__() + f"\nЦвет шерсти:{self.color}"
    
class Bird(Animal):
    def __init__(self, age, name,color):
        super().__init__(age, name)
        self.color = color

    def height(self,m):
        return f"{self.name}рост животного {m} M"
    
    def __str__(self):
        return super().__str__() + f"\nЦвет перьев {self.color}"
    
class cat(Mammal):
    def __init__(self, age, name, color):
        super().__init__(age, name, color)
        self.color = color 

    def meow(self):
        return f'{self.name} мяукает:МЯУУУ'
    
    def __str__(self):
        return super().__str__() + f"\nЦвет {self.color}"
    
class lion(Mammal):
    def __init__(self, age, name,color, favorite_food):
        super().__init__(age, name,color )
        self.favorite_food = favorite_food

    def meeow(self):
        return f"{self.name} мяукает:МРРРЯУУ"
    
    def __str__(self):
        return super().__str__() + f"\n Любимая еда: {self.favorite_food}"
    
class crow(Bird):
    def __init__(self, age, name, color):
        super().__init__(age, name, color)
        self.color = color

    def carrr(self):
        return f"{self.name} кар:CARRR"
    
    def __str__(self):
        return super().__str__() + f"\n Цвет перьев:{self.color}"
    
class Zoo_show:
    def __init__(self,animals):
        self.animals = animals
        self.show = {
            "Млекопитающие":{"cash":100, "infa": "Тройное ультра сальто"},
            "Птицы":{"cash":200, "infa":"ультра мощное КАР"}
        }
        
    def show_info(self):
        print("Информация о шоуу:")
        for show, info in self.show.items():
            print(f"\n {show}:")
            print(f"Цена билет: {info['cash']} сом")
            print(f"Описание:{info['infa']}")

    def ticket(self,shows_name):
        if shows_name in self.show:
            info = self.show [shows_name]
            print(f"\n Шоу выбрано '{shows_name}'. Цена билетика: {info['cash']} сом")
            print(f"Описание: {info['infa']}")
            print("\nЖивотные,учавствующие в шоу:")
            for animal in self.animals:
                if (shows_name == "Млекопитающие"and isinstance(animal,Mammal)):
                 print(f"- {animal.name}")
                elif shows_name == "Птицы"and isinstance(animal,Bird):
                  print(f"- {animal.name}")
        else:
            print("Нету такого,другое выбирай")
    
cat = cat(2, "Барсик", "белый")
lion = lion(3,"БаРсикХ2","Бежевый", "Люди")
crow = crow(1,"Невер","Чернее-черного")

animal_list = [cat,lion,crow]

zoo_show = Zoo_show(animal_list)
zoo_show.show_info()

while True:
    choice = input("\nВведите название шоу (Млекопитающие / Птицы) или 'выход' чтобы выйти: ").strip().capitalize()
    
    if choice.lower() == "выход":
        print("Пока")
        break
    if choice not in zoo_show.show:
        print("Нету такого,выбери другое")
        continue
    zoo_show.ticket(choice)