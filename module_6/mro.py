"""
Багаторівневе наслідування та Method Resolution Order (MRO).

Багаторівневе наслідування - це коли клас наслідує від іншого класу, який вже є похідним класом. 
Це створює "ланцюжок" наслідування, де можливості передаються через декілька рівнів.
"""
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"

my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))
