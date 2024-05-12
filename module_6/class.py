"""
Таким чином клас — це форма для випікання, а ось готове печиво — це об'єкти класу.
"""
class User:
    name = 'Anonymous'
    age = 15

user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name)
print(user2.age)


"""
Атрибут класу – це змінна, яка визначена на рівні класу, а не екземпляра класу. 
Це означає, що вона спільна для всіх екземплярів цього класу. Атрибути класу 
використовуються для зберігання даних, які повинні бути однаковими для всіх об'єктів класу.
"""
class MyClass:
    class_attribute = "I am a class attribute" 



"""
Поле класу (іноді називається "атрибут екземпляра") – це змінна, яка визначена на рівні 
окремого екземпляра класу. Кожен екземпляр класу має свій власний набір полів, які можуть 
приймати різні значення для різних екземплярів. Полем може бути будь-який об'єкт Python. 
Зазвичай це змінна, або контейнер (словник, список, рядок тощо). Поля класу використовуються 
для зберігання даних, що специфічні для кожного окремого об'єкта.
"""
class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу

obj1 = MyClass(5)
obj2 = MyClass(10)  
"""Тут об'єкти obj1 та obj2 мають різні значення поля instance_field. У obj1 значення поля 
instance_field дорівнює 5, а у obj2 значення instance_field - 10. 
"""



"""
Метод класу — це функція, яка оперує з полями класу та/або аргументами, які передаються у метод.
У будь-якого методу класу завжди повинен бути, принаймні, один аргумент self, це вимога 
синтаксису Python, оскільки інтерпретатор під час виклику методу обов'язково передасть першим 
аргументом сам об'єкт, а потім уже всі аргументи, які були передані під час виклику.
"""
# Я не зовсім зрозуміла нащо тут два рази у кінці bob.say_name() і чому якщо видалити один з них то виводити буде тільки bob.set_age()

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Boris', 34)

bob.say_name()
bob.set_age(25)
bob.say_name()



class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")

first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()


class Person:
    count = 0

    def __init__(self):
        self.count = 10

person = Person()
print(person.count)  # 10
print(Person.count)  # 0



class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


