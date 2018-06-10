list = [12, 33, 23, 900, 100, 1]
list2 = [1, 2, 3, 5, 4]

def sortList(list):
    for i in range(0, len(list) - 1):
        print(i)
        isChange = 0
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                a = list[j + 1]
                list[j + 1] = list[j]
                list[j] = a
                isChange = 1
        if isChange == 0:
            break
    return list

print(sortList(list2))