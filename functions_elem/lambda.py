print((lambda x, y: x + y)(5, 3))  # Виведе 8

"""
Лямбда-функції часто використовуються як аргументи для функцій вищого порядку, 
таких як map(), filter() або sorted(). Наприклад зворотне сортування списку для sorted():
"""
nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)


"""
Функція map() є функцією вищого порядку, що означає, що вона приймає іншу функцію як аргумент. 
map() використовується для застосування заданої функції до кожного елемента об'єкта ітерації, 
наприклад списку, та повертає ітератор, який виробляє результати.
"""
# напишемо за допомогою map генератор, який підносить числа із списку numbers до квадрату:
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)
# Якщо ми хочем отримати список, а не генератор то код можна записати так:
numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)
# Можна застосувати map до декількох списків:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))
# Для двох списків ми теж можемо використати list comprehensions допомоги функції zip
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)



"""
Функція filter
"""
even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

print(list(even_nums))

# Не обов'язково використовувати lambda функцію.
def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums))


some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

"""
Розглянемо, як можна замінити filter() на list comprehensions:
"""
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)
# Для рядка літер:
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join([x for x in some_str if x.islower()])
print(new_str)


"""
Функція any
"""
# Перевіримо чи наявний хоч один елемент в списку який є істинним?
nums = [0, False, 5, 0]
result = any(nums)  
print(result)


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result)


"""
Функція all
"""
# перевірка, чи всі елементи у списку істинні?
nums = [1, 2, 3, 4]
result = all(nums)  
print(result)
# Чи всі елементи списку є парними?
nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even)
# Чи всі слова у списку мають велику початкову букву?
words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)





