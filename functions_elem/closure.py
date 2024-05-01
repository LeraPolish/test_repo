"""
1. Внутрішня функція має доступ до змінних, визначених 
у області видимості зовнішньої функції.
2. Зовнішня функція повертає внутрішню функцію як результат своєї роботи.
3. Після завершення роботи зовнішньої функції, внутрішня функція зберігає 
доступ до цих змінних, що відіграє важливу роль у певних програмних патернах та алгоритмах.
"""
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
my_func()


"""
Ми створимо замикання, яке буде зберігати інформацію про кількість разів виклику функції.
"""
from typing import Callable

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count

    return increment

# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
