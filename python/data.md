# 环境部署
- anaconda安装
    - anaconda命令
```
conda upgrade -all
# 查看所有库
conda list
conda install package(=version)
conda remove package
conda search
```

- [python库下载](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

- 常用工具
    - spyder
    - cmd中`jupyter-notebook`

# numpy
- [练习题](https://github.com/rougier/numpy-100)
<!-- - 主要用于矩阵操作和运算
- 使用普通一维数组生成numpy一维数组
    ```
    l = [10, 11, 21]
    arr = np.array(data, dtype=np.float64)
    print(type(arr)) # <class 'numpy.ndarray'>
    arr2 = arr.astype(np.int32)
    ```
- 循环生成数组
    - `arr = np.arange(1, 20, 2)`1-20,步长为2
- 生成多维数组
    - `arr = np.ndarray((2, 3))`两行三列
    - `arr = np.ndarray([[1, 2], [2, 3]])`
- 生成连续的数组
    - `a = np.linspace(0, 5.0, num=50)`生成50个(默认)0-5.0的数字组成数组
- 查看数组形状`arr.shape`
- 快速生成数组
    - `np.zeros(10)` 生成包含10个0的数组
    - `np.zeros((2, 3))` 生成两行三列数组
    - `np.full((2, 3), 8)` 生成两行三列数组,并且元素都为8
    - `np.zeros((3, 6))` 生成3*6的二维数组
        ```
        arr = np.zeros((2, 3))
        arr[0] = [1, 2, 3]
        ```
    - `np.empty(5)` 数组元素未初始化(可能有任何数字)
    - `np.eye(3)`生成3x3的对角线矩阵 -->
- `np.zeros()` 生成值为0的对象
    - `np.zeros(4)`
    - `np.zeros((2,3))`
- `np.ones()` 生成值为1的数组
    - `np.ones((2, 3))` 生成2*3数组,值为1
- `np.full()`
    - `np.full((3,4),1)` 生成3*4的数组,元素是1
- `np.array(data)` 生成制定的数组
- `np.linspace()` 生成连续n个元素的一维数组
    - `np.linspace(0,20,5)` 一共5个元素,均匀分配到0-20
- `n1.arange()` 生成连续的一维数组
    - `n1.arange(0,20,1)` 1是步长
- `n1.size` 获取元素的个数
- `n1.reshape()` 修改n1的形状
    - `np.zeros(6).reshape((2,3))`
- `np.nonzero(n1)` 寻找一维数组不为0的下标
    - `np.nonzero(np.array( [1,2,0,0,4,0]))`
- `np.eye(n)` 生成n*n的数组
- `np.random` 使用随机数生成数组
    - `np.random.random((3,4))` 生成3*4的数组
    - `np.random.randint(0,10,(3,3))` 生成3*3的数组,值在区间[0,10)中
    - `np.random.normal(0, 1, (3,4))` 生成均值为0,方差为1的3*4的数组
- `np.empty((3,3))` 生成3*3数组,值是内存空间的任意值
- `n1.max();n1.min()`
- `n1.mean()`
- 创建边框为1,内部为0的二维数组
    ```
    n1 = np.full((10,10), 1)
    n1[1:-1,1:-1] = 0
    print(n1)
    ```
- 在二维数组外增加一个边框
    ```
    np.pad(np.full((3,3),1),1,'constant')
    ```
- `np.nan np.inf`
    ```
    print(0 * np.nan) # nan
    print(np.nan == np.nan) # False
    print(np.inf > np.nan) # False
    print(np.nan - np.nan) # nan
    print(np.nan in set([np.nan])) # True
    print(0.3 == 3 * 0.1) # False
    ```
- `np.diag`
    ```
    np.diag(1+np.arange(4), k=-1) # k=-1: 低于对角线

    [[0 0 0 0 0]
     [1 0 0 0 0]
     [0 2 0 0 0]
     [0 0 3 0 0]
     [0 0 0 4 0]]
    ```

- 


- numpy数组也支持切片
    ```
    n1 = np.random.randint(0, 10, 5)
    print(n1 > 9) # [False False  True False  True]

    print(n1) # [3 4 9 0 2]
    n1[n1 > 5] = 0
    print(n1) # [3 4 0 0 2]
    ```


- 数学运算








# pandas
- 纳入了大量库和一些标准的数据模型,提供了高效地操作数据集所需的工具,pandas提供了大量能使我们快速便捷地处理数据的函数和方法
- `Series`有序并且有索引
    1. 用数组生成`Series`
        - `obj = pandas.Series([10, 20, 30], index = ['a', 'b', 'c'])`
        - `obj`
        - `obj.values`
        - `obj.index`
        - `obj['a']`,`obj[['a', 'b']]`
        - `obj[obj > 15]`找出大于15的元素
        - `'a' in obj`判断下标是否存在

    2. 利用字典生成`Series`
        - `o = pandas.Series({'a': 1, 'b': 2, 'c': 3}, index = ['q', 'w', 'e', 'r'])`
        - index需要匹配key,否则会显示NaN
        - Series相加,相同索引部分会叠加

- `DataFrame`
    1. 生成`DataFrame`
        - `data = {'name': ['Sam', 'Jack'], 'age': [20, 16]}`
        - `o = pandas.DataFrame(data, columns = ['name', 'age', 'sex'])`指定列的顺序,不存在的列显示为NaN
        - `o['name']`,`o.name`
        - `o['sex'] = o.name == 'Sam'`新增/修改一整列的值
        - `o.columns`查看列名
    2. `DataFrame`
        - 指定行,不存在的显示为NaN
            ```
            data = {
                'name': {
                    1: 10,
                    2: 20
                },
                'age': {
                    100: 11,
                    200: 21
                }
            }
            o = pandas.DataFrame(data, columns = ['name', 'age'])
            print(o)
            ```
        - `o.T`转置,行列相互转化
- 操作Excel数据
    - 读取
        ```
        df = pandas.read_excel('1.xlsx', sheet_name = 0)
        ```
    - 写入
        ```
        out = pandas.ExcelWriter('2.xlsx')
        df.to_excel(out)
        out.save()
        ```

- 缺失数据处理


# Matplotlib
- 流程式制图
    - 绘制折线图`plt.plot`
        ```
        import matplotlib.pyplot as plt
        x = [i ** 2 for i in range(5)]
        y = [11, 13, 17, 21, 22]
    
        x1 = [10, 8, 7, 3]
        y1 = [3, 6, 7, 8]
    
        plt.figure(figsize=(10, 10), dpi=100) # 绘制第一张画布
        plt.plot(x, y, 'o-', label ='line_1') # 绘制o-图(^- .-)
        
        plt.figure(1) # 绘制第二张画布
        plt.plot(x1, y1, label ='line_2')
        plt.xlabel('x数据')
        plt.ylabel('y数据')
        plt.title('标题')
        plt.legend() # 用于显示每条线的名称
        plt.show()
        ```
    
    - 绘制普通条形图`plt.bar`
        ```
        x = numpy.arange(1, 10, 2)
        y = x ** 2
        plt.bar(x, y)
        plt.axis([0, 20, 0, 500]) # 定义x和y轴的刻度
        # plt.xlim() # 单独定义x轴的刻度
        # plt.ylim() # 单独定义y轴的刻度
        plt.show()
        ```
    - 绘制分布图(查看数据在区间中的分布情况)`plt.hist`
        ```
        x = numpy.random.randint(1, 100, 50)
        bins = [0, 20, 40, 60, 80, 100] # 表示关注的区间
        plt.hist(x, bins, rwidth=1)
        plt.show()
        ```
    
    - 绘制散点图`plt.scatter`
        ```
        x = numpy.random.randint(1, 100, 50)
        y = numpy.random.randint(1, 100, 50)
    
        x1 = numpy.random.randint(1, 100, 50)
        y1 = numpy.random.randint(1, 100, 50)
    
        plt.scatter(x, y, color='r')
        plt.scatter(x1, y1, color='blue')
    
        plt.show()
        ```
    
    - 饼图`plt.pie`
        ```
        lable = 'a', 'b', 'c', 'd'
        size = [10, 20, 25, 45]
        
        fig, ax = plt.subplots()
        
        explods = 0, 0.1, 0, 0 # 突出显示
        
        ax.pie(size, labels=lable, autopct='%1.1f%%', shadow=True, startangle=90, explode=explods)
        
        ax.axis('equal') # 正圆
        
        plt.show()
        ```

- 面向对象制图
    ```
    # fig: 底图;ax: 图像
    fig, ax = plt.subplots() # 初始化
    ax.scatter(x, y)
    plt.show()
    ```
    
- 绘制多个子图
    ```
    x = [i ** 2 for i in range(5)]
    y = [11, 13, 17, 21, 22]
    # 绘制两行三列的第一个位置
    plt.subplot(2, 3, 1) 
    plt.plot(x, y, 'o-', label='line1')
    plt.legend()
    plt.show()
    ```