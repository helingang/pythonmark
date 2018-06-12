# 排序
## 冒泡排序
1. 思路
    1. 两两交换,第一次排序后最大值在末尾
    2. 第n趟排序需要排序n - 1次(n个数)
2. 实现
```
def sortList(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                a = list[j + 1]
                list[j + 1] = list[j]
                list[j] = a
    return list
```
3. 优化
    1. 如果数组在当前趟数不需要排序,则表示可以直接beark,减少循环的趟数
```
def sortList(list):
    for i in range(0, len(list) - 1):
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
```

## 选择排序
1. 思路
    1. 趟数为n - 1(n个数)
    2. 定义标志位,每趟循环比较标志位的元素与其他元素,找到最大值/最小值,并更新标志位
    3. 将最大值/最小值与标志位交换位置
2. 实现
```
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
```
## 插入排序
1. 思路
    1. 将元素按序放入已有序的数组中
2. 实现
```
def sortList3(list):
    newList = []
    if len(newList) == 0:
        newList.append(list[0])
    for i in range(1, len(list)):
        mk = 0
        for j in range(0, len(newList)):
            if list[i] > newList[j]:
                mk = j + 1
        newList.insert(mk, list[i])
    return newList
```

## 快速排序(二分)