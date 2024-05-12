# data = [1, 2, 3, 4, 5, 6]
# print(*map(lambda n: n % 2, data))

# data2 = [1, 2, 3, 4, 5, 6]
# result = map(lambda n: n % 2, data)
# print(set(result))

def get_ost(data):
    result = []
    for n in data:
        ost = n % 2
        result.append(ost)
    return result


data = [1, 2, 3, 4, 5, 6]
ost_1 = get_ost(data)
print(*ost_1)