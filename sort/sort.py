list = [12, 33, 23, 900, 100, 1]
list2 = [1, 2, 3, 5, 4]

# 冒泡排序
def sortList1(list):
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

# 选择排序
# 找到最大/最小的数与
def sortList2(list):
    length = len(list)
    for i in range(0, length):
        mk = i
        for j in range(i, length):
            if list[i] > list[j]:
                mk = j
        temp = list[i]
        list[i] = list[mk]
        list[mk] = temp
    return list

print(sortList2(list))