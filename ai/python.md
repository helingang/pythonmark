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
5. `globles()['name'] = 'Sam'` 直接命名法(globles()是个字典)
6. `dir(__builtins__)`内置电池:常用的`str len`都在里面
7. 先从`locals()`中寻找,再从`globles()`中,最后从`__builtins__`中寻找