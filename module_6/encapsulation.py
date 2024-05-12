"""
Інкапсуляція в програмуванні, зокрема в об'єктно-орієнтованому програмуванні (ООП), є одним 
із ключових принципів, який полягає в приховуванні внутрішньої структури класу та захисті його 
даних від прямого доступу ззовні. Цей принцип дозволяє обмежити доступ до певних компонентів 
класу (полів і методів), забезпечуючи контроль над тим, як ці дані використовуються та змінюються.
"""
# Захищені (Protected) атрибути та методи.
# Вони позначаються одним підкресленням _ на початку імені.
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())



"""
Приватні (Private) атрибути та методи

В Python не існує справжньої приватності для атрибутів класів, як це реалізовано, наприклад, 
у Java. Python використовує так зване "перетворення імен" для забезпечення цього рівня 
інкапсуляції. Атрибути, що вважаються приватними позначаються двома підкресленнями __ і 
не можуть бути доступні безпосередньо ззовні класу.
"""
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
print(p.__is_admin)
# Як видно з цього прикладу, доступу за допомогою p.__is_admin немає.
# Насправді було лише змінене ім'я поля, щоб запобігти випадковому доступу до нього, 
# але воно все одно доступно ззовні класу. Змінене ім'я формується як знак підкреслювання, 
# ім'я класу та ім'я змінної.
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
print(p._Person__is_admin)
"""
Тож можна, за бажанням, отримати доступ до поля __is_admin через вираз p._Person__is_admin, 
що загалом нічого не захищає.

Щоб реалізувати методи доступу до приватного поля __is_admin у класі Person, ми можемо 
використати той самий підхід, що і до захищеного поля _is_active
"""
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

        
p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())
"""
У цьому прикладі, метод get_is_admin дозволяє отримати значення поля __is_admin, а метод 
set_is_admin дозволяє його змінити. Це забезпечує контрольований доступ до приватного поля, 
дозволяючи внести необхідну логіку перевірки або обробки при зміні значення.
"""

