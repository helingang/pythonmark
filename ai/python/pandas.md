# panda和matplotlib

## pandas
<img src="./pandas/Pandas-1.jpg" style="width:100%">
<img src="./pandas/Pandas-2.jpg" style="width:100%">
<img src="./pandas/Pandas-3.png" style="width:100%">

### pandas
- 以列为核心,一行是一个样本
- 取哪一列
    - `pd.salary`
    - `pd['salary']`
- `apply(func, *args)` 对每一行的某列进行操作,操作内容在函数里
    - `pd.salary.apply(test, 'qwe')`



- `Series` 看成列
    ```
    df1 = pd.Series({'a': 1, 'b': 2, 'c': 3}, index=['a', 'b'])
    df2 = pd.Series({'a': 10, 'b': 20, 'c': 30}, index=['a', 'b', 'c'])
    print(df1 + df2)
    print(df1)
    print(df2)
    ```

- `DataFrames`

- 案例
    ```
    df = pd.read_csv('./DataAnalyst.csv', encoding='gb2312')
    arr = df.salary.str.split('-')
    arr_df = pd.DataFrame(arr.tolist(), columns=['bottom', 'top'])
    arr_df['top'] = arr_df['top'].str[:-1]
    arr_df['bottom'] = arr_df['bottom'].str[:-1]
    arr_df.head()


    # 加工salary字段
    def get_salary(salary, method='None'):
        arr = salary.split('-')
        if len(arr) == 1:
            bottom = arr[0].upper()
            bottom = bottom[:bottom.find('K')]
            top = bottom
        else:
            bottom = arr[0][:-1]
            top = arr[1].upper()
            top = top[:top.find('K')]
        if method == 'top':
            return top
        elif method == 'bottom':
            return bottom


    df['bottomSalary'] = df.salary.apply(get_salary, method='bottom')
    df.bottomSalary = df.bottomSalary.astype('int')  # 类型转换
    df['topSalary'] = df.salary.apply(get_salary, method='top')
    df.topSalary = df.topSalary.astype('int')  # 类型转换
    df['avgSalary'] = (df['bottomSalary'] + df['topSalary']) / 2

    # print(df.groupby('companyShortName').avgSalary.agg(['count','mean']).sort_values(by='count',ascending=False))
    # select companyShortName,count(*) as count, average(avgSalary) from table group by companyShortName order by count

    # print(df.city.value_counts()) # 按city统计(聚合函数count)
    # print(df.avgSalary.describe()) # 查看平均工资
    # print(df.groupby(['city', 'education']).avgSalary.mean()) # 按city和education分组,查看平均工资的均值, .mean()会自动舍弃非数字列
    # print(df.groupby(['city', 'education']).avgSalary.mean().unstack()) # .unstack()把内层索引展开到列上
    # print(df.groupby('companyShortName').avgSalary.agg(['count', 'mean']).sort_values(by='count', ascending=False)) # agg聚合函数count mean;sort_values(by='', ascending=)根据值或者索引排序ascending升序/降序
    # print(df.groupby('city').companyShortName.value_counts())
    # print(df.groupby('city').positionName.value_counts())

    # def topN(df, n=5):
    #     counts = df.value_counts()
    #     return counts.sort_values(ascending=False)[:n]
    # print(df.groupby(['city']).companyShortName.apply(topN))
    ```

## matplotlib
<img src="./matplotlib/Matplotlib.png" style="width:100%">

### matplotlib