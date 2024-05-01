import random

# Создаем список для хранения уже выбранных чисел
chosen_numbers = []

# Пока не выбраны все числа от 1 до 5
while len(chosen_numbers) < 5:
    # Генерируем случайное число
    new_number = random.randint(1, 5)
    
    # Проверяем, было ли уже выбрано это число
    if new_number not in chosen_numbers:
        # Если число еще не выбиралось, добавляем его в список выбранных
        chosen_numbers.append(new_number)
        print(new_number)

# Когда все числа были выбраны, программа завершает работу
print("Все числа были выбраны")
