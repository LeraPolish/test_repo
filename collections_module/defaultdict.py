"""
ми звертаємось до ключа, який ще не існує, defaultdict автоматично створює
для нього новий список і це не призводить до помилок в коді.
"""
# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)

"""
defaultdict використовує int як функцію за замовчуванням, що означає, 
що кожен новий ключ має ініційоване значення 0
"""
# d = defaultdict(int)

# # Збільшення значення для кожного ключа
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1

# print(d)

"""
список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова
"""
# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)
"""
можемо скористатися defaultdict із collections та 
задати значенням за замовчуванням порожній список
"""
# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))



