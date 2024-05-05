from typing import Callable

def generator_numbers(text: str):
    words = text.split()
    for word in words:
        if word.replace('.', '', 1).isdigit():
            yield float(word)

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total_profit = sum(numbers_generator)
    return total_profit

text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
total_income = sum_profit(text,generator_numbers)
print(f"Загальний дохід: {total_income}")