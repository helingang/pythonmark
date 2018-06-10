# 排序
## 冒泡排序
1. 思路
    1. 两两交换,第一次排序后最大值在末尾
    2. 第n趟排序需要排序n - 1次(n个数)
2. 片段
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
