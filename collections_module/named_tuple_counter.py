# import collections

# # Створення іменованого кортежу Person
# Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# # Створення екземпляра Person
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# person_1 = Person("Liza", "Breeze", 28, "Kolt", 12547)

# # Виведення різних атрибутів іменованого кортежу
# print(person.first_name)       
# print(person.post_index) 
# print(person.age)        
# print(person[3])         


# print(person[0])
# print(person_1.age)
# print(person_1.last_name)


# import collections

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f'This is a cat {cat.nickname}, {cat.age}-year-old cat, his owner is {cat.owner}')


# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)
"""
OR
"""
# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)

"""
Один з найпопулярніших методів Counter - це most_common(),\
який повертає список елементів та їх частоту, починаючи з тих які зустрічаються найчастіше
"""
# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))
"""
підрахувати кількість кожної літери у рядку
"""
# from collections import Counter

# # Створення Counter з рядка
# letter_count = Counter("banana")
# print(letter_count)

"""
підрахунок слів в тексті
"""
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")




