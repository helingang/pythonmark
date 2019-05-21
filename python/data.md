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

- `np.matmul(n1, n2)` 矩阵乘积


- numpy数组也支持切片
    ```
    n1 = np.random.randint(0, 10, 5)
    print(n1 > 9) # [False False  True False  True]

    print(n1) # [3 4 9 0 2]
    n1[n1 > 5] = 0
    print(n1) # [3 4 0 0 2]
    ```

- 运算
    - `np.random.random((2,3)) + 2`
    - `np.random.random((2,3)) + np.random.random((1,3))`
    - `n1.sum() sum(n1) np.sum(n1, axis=0, keepdims=True)`
    - `n1.dot(n2) np.matmul(n1, n2)` 矩阵乘法(建议用后者)








# pandas
<!-- - 纳入了大量库和一些标准的数据模型,提供了高效地操作数据集所需的工具,pandas提供了大量能使我们快速便捷地处理数据的函数和方法
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

- 缺失数据处理 -->

- Series 一维的数据结构
    - `pd.Series(data=, index=, name=)`
        - data可以是list或者dict
    - 类型是`pandas.core.series.Series`
    - 使用numpy的一维数组构建Series
        - `pd.Series(data=np.random.random(5), index=list('abcde'))`
    - `s.astype(np.int)` 修改s中值的类型
    - 操作Series
        ```
        cities = {
            'Beijing': 55000,
            'Shanghai': 60000,
            'Shenzhen': 60000,
            'Hangzhou': 30000,
            'Guangzhou': 35000,
            'Suzhou': None
        }
        p = pd.Series(data=cities, name='hlgtest2')

        print(p['Beijing':'Shenzhen'])
        print(p[['Beijing','Shanghai']])
        print(p[:-1] + p[1:]) # 对应的index相加
        print('sad' in p) # False
        print(p.get('beijing', 0))
        print(gdp_less_50000 = p < 50000) # print(p[p < 50000])
        print(p.median()) # 中位数
        print(p[p > p.median()])
        ```
    - `p.describe()`

- Dataframe 表格
    - `pd.DataFrame(data, index=list('ABCDEF'))` data是个json格式,key是表格的列,value是一个Series
    - `p.loc['A']` 取行
    - `p.city p['city']` 取列
    - `s.iloc[0:2, 0:2]` 取行和列(只能指定index)
    - `s.loc[['A','C'],'city':'population']` 取A和C行,取city~population列
    - `p.values` 返回numpy的二维数组
    - 取值和赋值
        - `s.at['A', 'city'] = 'BEIJING'`
    - `s['westcity'] = s['city'] == 'Chongqing'`
    - 加行
    - `isnull` `notnull`
        - `pk['Type 2'].isnull()` 查看`Type 2`这个字段为空有哪些,返回一个Series
    - csv文件操作
        - `pk = pd.read_csv('./Pokemon.csv', sep=';')` 分隔符是`;`
        - `s = pd.read_csv('./GOOG.csv', index_col=0, parse_dates=['Date'])` 第0列当做index,把Date列转为日期类型
        - `s.to_csv('./test.csv')`
    - `reindex`
        - `p.reindex(list('ABCDE'), fill_value=0)` 重新设置p的index值
    - `drop`
        - `s.drop(['A', 'C'])` 删除index为A和C的行
        - `s.drop('city', axis=1)` 删除city列
    - `df1.corr()` 查看列与列的关系度(接近1正相关,接近-1负相关,0时相关性很低)
    - `df1.info()` 查看dataframe的信息
    - `nvda.set_index('Date', inplace=True)`
    - `df1.sort_values('Vol')`

- groupby和aggregate
    - `groupby`
        - `df1.groupby(['Name','Year'], sort=False)` 返回groupby对象
        - `group_by_name.groups` 查看分组
        - `group_by_name.describe()`
        - `group_by_name.get_group('Nan')`
    - `aggregate` groupby之后一般要做一些aggregate操作
        - `group_by_name.aggregate(sum)`
        - `group_by_name.agg([np.sum,np.mean,np.std])` 每一列求sum,mean,std
        - `group_by_name.agg({"Bonus": np.sum, "Salary": np.sum, "Year": (lambda x: list(x)[0])})` 对每列进行不同的聚合操作
        - `group_by_name.aggregate(lambda x: list(x)[0])` 取每个分组的第一行
        - 其他api
            - `.size()` 每个分组展示计数
            - `.mean()` 计算每个分组的平均值
            - `.median()` 中位数


- filter
    - SQL中的having和where
        ```
        df = pd.DataFrame({"A": np.arange(8), "B":list("aaabbbcc")})
        df.groupby("B").filter(lambda x: x.A.sum() == 3)
        ```

- 表格的拼接
    - `concat`
        - 1
            ```
            df1 = pd.DataFrame({'apts': [55000, 60000],'cars': [200000, 300000],},index = ['Shanghai', 'Beijing'])
            df2 = pd.DataFrame({'cars': [150000, 120000],'apts': [25000, 20000],},index = ['Hangzhou', 'Najing'])
            df3 = pd.DataFrame({'apts': [30000, 10000],'cars': [180000, 100000],},index = ['Guangzhou', 'Chongqing'])
            r1 = pd.concat([df1,df2,df3])
            r = pd.concat([df1,df2,df3], keys=['x','y','z'])

            df4 = pd.DataFrame({'salaries': [10000, 30000, 30000, 20000, 15000]},index = ['Suzhou', 'Beijing', 'Shanghai', 'Guangzhou', 'Tianjin'])
            r3 = pd.concat([df4,r1], sort=True, axis=1, join='inner')
            ```
        - 2
            - `pd.concat([df1, s1], axis=1)`
        
    - `append`
        - `df1.append(df2, sort=False)`
        - `df1.append(s2)` append一个row到df中

    - `merge`
        - `pd.merge(df1, df4, on="city", how="right")`














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


- 通过pandas绘制
    - 折线图
        ```
        nvda = pd.read_csv("data/NVDA.csv", index_col=0, parse_dates=[0])
        nvda["Open"].plot()

        df = pd.DataFrame(np.random.randn(10, 4))
        df.plot()
        ```

    - 条形图
        ```
        df = pd.DataFrame(np.random.rand(10, 4), columns=list("abcd"))
        df.plot.bar(figsize=(8,6))
        # stacked=True 堆叠柱状图
        # figsize=(8,6) 图形大小

        df.plot.barh(stacked=True, figsize=(8,6), alpha=0.5)
        # barh 水瓶条形图
        ```

    - 直方图
        ```
        df = pd.DataFrame({"a": np.random.randn(1000)+1, "b":np.random.randn(1000), "c": np.random.randn(1000)-1})
        df.plot.hist(bins=30, alpha=0.5)
        # bins 箱子数量
        # alpha 透明度
        ```
    
    - 箱型图
        ```
        df = pd.DataFrame(np.random.rand(10, 5), columns=list("ABCDE"))
        df.plot.box()
        # (离散点), 最大值, 上四分位, 中位数, 下四分位, 最小值, (离散点)
        ```

    - 区域块图形
        试一试堆积条形图
        ```
        df = pd.DataFrame(np.random.rand(10, 3), columns=list("ABC"))
        df.plot.area()
        ```
    
    - 散点图
        ```
        df = pd.DataFrame(np.random.randn(50, 4), columns=list("abcd"))
        df.plot.scatter(x="a", y="b")

        s = np.random.randn(100, 1)
        a = 100 + s
        b = 10 + s
        df = pd.DataFrame(np.concatenate([a, b], 1), columns=list("ab"))
        df.plot.scatter(x="a", y="b")
        ```

    - 饼状图
        ```
        df = pd.DataFrame(
            {
                'mass': [0.330, 4.87 , 5.97],
                'radius': [2439.7, 6051.8, 6378.1]
            },
            index=['Mercury', 'Venus', 'Earth']
        )
        df.plot.pie(y="mass")
        ```


- 使用matplotlib绘制
    - 步骤
        1. 导入 matplotlib 包相关工具包
        2. 准备数据，numpy 数组存储
        3. 绘制原始曲线
        4. 配置标题、坐标轴、刻度、图例
        5. 添加文字说明、注解
        6. 显示、保存绘图结果
    - 案例1
        ```
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd
        import matplotlib as mpl

        x = np.linspace(-np.pi,np.pi, 200)
        s = np.sin(x)
        c = np.cos(x)

        plt.rcParams['font.family'] = ['SimHei']

        ax = plt.subplot(111)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_position(('data',0))
        ax.spines['bottom'].set_position(('data',0))

        plt.plot(x,s, label=r'$y=sin{x}$',linewidth=2, linestyle=':')
        plt.plot(x,c,label=r'$y=cos{x}$', linewidth=3,linestyle='--')

        plt.xlim(x.min()*1.1, x.max()*1.1)
        plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'])
        plt.ylim(c.min()*1.1, c.max()*1.1)
        plt.yticks([1,-1],['$-1$','$-1$'])

        plt.legend()
        plt.title("正弦和余弦")

        t = 2 * np.pi / 3
        plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
        plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.5, linestyle="--")
        plt.annotate(r'$\cos(\frac{2\pi}{3})$', xy=(t, np.cos(t)), xycoords="data", xytext=(-90, -50), textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        ```