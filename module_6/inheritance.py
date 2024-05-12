"""
Inheritance (НАСЛЕДОВАНИЕ)

Наслідування - це механізм ООП, який дозволяє одному класу переймати властивості та методи 
іншого класу. У Python це робиться шляхом оголошення класу, який "наслідується" від іншого класу.

Базовий або батьківський клас (superclass) це клас, від якого наслідуються властивості та методи.

Похідний або дочірній клас (subclass) це клас, який наслідує властивості та методи від базового класу.
"""
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"

class Cow(Animal):  
    def make_sound(self):
        return "Moo"

my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"

"""
У похідних класах можна визначати власні конструктори. Якщо ми хочемо зберегти поведінку 
базового класу і додати нові властивості, ми можемо використовувати конструкцію super() для 
виклику конструктора базового класу.
"""
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):

    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_cow.make_sound())  # Виведе "Moo"

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"

