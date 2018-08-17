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
- 使用普通一维数组生成numpy一维数组
    ```
    l = [10, 11, 21]
    arr = np.array(data)
    print(type(arr)) # <class 'numpy.ndarray'>
    ```
- 循环生成数组
    - `arr = np.arange(1, 20, 2)`1-20,步长为2
- 生成连续的数组
    - `a = np.linspace(0, 5.0, num=50)`生成50个(默认)0-5.0的数字组成数组
- 查看数组形状`arr.shape`
- 快速生成数组
    - `np.zeros(10)` 生成包含10个0的数组
    - `np.zeros((3, 6))` 生成3*6的二维数组
        ```
        arr = np.zeros((2, 3))
        arr[0] = [1, 2, 3]
        ```
    - `np.empty(5)` 数组元素未初始化
        

- numpy数组也支持切片
    - 注意二维数组的列数需相等否则会出现`IndexError`异常
    - **对切片的任何修改会直接反映到源数组上**
        ```
        arr = np.array([[40, 50, 60], [60, 70, 80], [10, 20, 30]])
        arr[:, 1] # 多重切片: 取三行的第二列
        ```

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
    
        plt.figure(0) # 绘制第一张画布
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