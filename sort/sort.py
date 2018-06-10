list = [12, 33, 23, 900, 100, 1]

def sortList(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                a = list[j + 1]
                list[j + 1] = list[j]
                list[j] = a
    return list
print(sortList(list))