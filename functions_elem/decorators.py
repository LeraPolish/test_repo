"""
ми не хочемо міняти її код з якоїсь причини. Але нам потрібно додати логування 
до цієї функції, виводити в консоль щоразу, коли вона викликається, з якими аргументами 
її викликали і що вона повернула в результаті.
"""
def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

complicated = logger(complicated)
print(complicated(2, 3))
"""
Декоратори використовуються з синтаксисом @
"""
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))


"""
модуль functools, це необхідно для збереження метаданих оригінальної функції, 
яку ми декоруємо. Функція functools.wraps допомагає в цьому, зберігаючи інформацію 
про оригінальну функцію, як-от ім'я функції та документацію.
"""
from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)
