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
7. `LEGB`
    - `local–>enclosing–>global–>builtin`
8. 先从`locals()`中寻找,再从`globles()`中,最后从`__builtins__`中寻找
9. 小整数暂存区(-5 ~ 256)
    ```
    a=77;b=77
    a is b#True   #小整数缓存池，只有同一个位置。目的是把常用的东西放在缓存池，减小开销
    a=998;b=998
    a is b#False
    ```
10. 字符驻留
    ```
    str_c='Python 3.5'
    str_d='Python 3.5'
    str_c is str_d#False 有些稍特殊的字符串，Python认为复用性不大，于是被分配到堆上，不会在内存池中检查。因此这是两个对象。内存地址不一样
    ```
11. 深浅拷贝
    ```
    import copy
    a=[1,2,3,[4,5,6]]
    b=a#赋值
    c=copy.copy(a)#shallow copy
    d=copy.deepcopy(a)#Deep copy
    ```
12. 列表推导式
    - `[x + 1 for x in range(30) if x % 3 == 0]`
13. `random.sample(list, num)` 取样
    ```
    import random
    a = [x for x in range(100)]
    print(random.sample(a, 5))
    ```