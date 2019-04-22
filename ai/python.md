## 基础
1. `exec('print(1)')` 解析字符串
2. `a = eval('2 * 2')` 解析表达式
3. 交换赋值
    ```
    a,b=b,a
    print(a,b)
    ```
4. 解包和收集
    ```
    #unpack解包
    l1=[1,2,3,4,5,'6']
    a,b,c,d,e,f=l1
    print(a,b,c,d,e)

    #*号收集
    a,*b,c=l1
    print(a,b,c)
    
    #*号展开,针对序列
    l1=[1,2,3,4]
    s1='julyedu.com'
    print([*l1,*s1])

    #*号展开,针对字典
    d1={'name':'machine learning 5th','add':'BJ,SH,*'}
    [*d1],{**d1,'date':'2018-7-30'}

    l1=[[3,4,5]]
    a=l1
    b,=l1
    print(a,b)
    ```