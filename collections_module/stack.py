# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")

"""
Спочатку створимо стек та додамо декілька елементів
"""
stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
"""
Переглянемо верхній елемент:
"""
print(peek(stack))  # Виведе 'c'
"""
Видалимо верхній елемент:
"""
print(pop(stack))  # Виведе 'c'

