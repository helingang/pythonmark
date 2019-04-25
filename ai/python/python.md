## 基础
- `exec('print(1)')` 解析字符串
- `a = eval('2 * 2')` 解析表达式
- 交换赋值
    ```
    a, b=b, a
    print(a, b)
    ```
- 解包和收集
    ```
    # unpack解包
    l1 = [1, 2, 3, 4, 5, '6']
    a, b, c, d, e, f = l1
    print(a, b, c, d, e)

    # *号收集
    a, *b, c = l1
    print(a, b, c)

    # *号展开,针对序列
    l1 = [1, 2, 3, 4]
    s1 = 'julyedu.com'
    print([*l1, *s1])

    # *号展开,针对字典
    d1 = {'name':  'machine learning 5th', 'add':  'BJ,SH,*'}
    [*d1], {**d1, 'date':  '2018-7-30'}

    l1 = [[3, 4, 5]]
    a = l1
    b, = l1  # 这里的意思是解l1这个包
    print(a, b)
    ```
- `globles()['name'] = 'Sam'` 直接命名法(globles()是个字典)
- `dir(__builtins__)`内置电池: 常用的`str len`都在里面(`__builtins__.name = 'Sam'`)
- `LEGB`
    - `locals(最低)–>enclosing(闭包)–>globals–>builtin(最高)`
    - `locals` 一般是函数内部
    - 先从`locals()`中寻找,再从`enclosing`中寻找,再从`globles()`中,最后从`__builtins__`中寻找
    - 同一层楼中不能同名
- 小整数暂存区(-5 ~ 256)
    ```
    a=77;b=77
    a is b  # True   #小整数缓存池,只有同一个位置.目的是把常用的东西放在缓存池,减小开销
    a = 998;
    b = 998
    a is b  # False
    ```
- 字符驻留
    ```
    str_c='Python 3.5'
    str_d='Python 3.5'
    str_c is str_d#False 有些稍特殊的字符串,Python认为复用性不大,于是被分配到堆上,不会在内存池中检查.因此这是两个对象.内存地址不一样
    ```
- 深浅拷贝
    ```
    import copy
    a = [1, 2, 3, [4, 5, 6]]
    b = a  # 赋值
    c = copy.copy(a)  # shallow copy
    d = copy.deepcopy(a)  # Deep copy
    ```
- 列表推导式
    - `[x + 1 for x in range(30) if x % 3 == 0]`
- `random.sample(list, num)` 取样
    ```
    import random
    a = [x for x in range(100)]
    print(random.sample(a, 5))
    ```

- `traceback` 追踪
    ```
    import traceback, sys
    try: 
        a = 1 / 0
    except Exception as e: 
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        print(exc_type, exc_value, exc_traceback_obj)
        traceback.print_exc()
    ```
- 斐波那契数列
    ```
    def fib(i): 
        n, a, b = 0, 0, 1
        while n < i: 
            print(b)
            a, b = b, a + b
            n += 1
        return
    fib(6)
    ```
- 迭代器(有`__next__()`方法)一定是可迭代对象(可以使用`for`来遍历),可迭代对象不一定是迭代器
## 函数
- 三元表达式
- 偏函数(固定了部分参数的函数)
    ```
    import functools

    a = int('10', base=32)
    print(a)

    int8 = functools.partial(int, base=8)
    b = int8('10')
    print(b)
    ```
    ```
    import functools

    def test(a=10):
        print(a)
    test()

    test1 = functools.partial(test, a=20)
    test1()
    ```
- 修改函数的默认值
    ```
    def test(a=1, b=2):
    print(a + b)

    test() # 3
    test.__defaults__=(3, 4)
    test() # 7
    ```

- `lambda` 匿名函数

- `map reduce filter`内置高阶函数(参数是函数)
    - `map`映射函数
        ```
        l1 = [1, 2, 3, 4, 5]
        l2 = [11, 12, 13, 14, 15]

        print(list(map(lambda x, y: x + y, l1, l2)))
        # [12, 14, 16, 18, 20]
        ```
    - `reduce`
        ```
        from functools import reduce
        l1 = [1, 2, 3, 4, 5]
        print(reduce(lambda x,y:x*y,l1)) # 两两运算后返回value继续运算
        ```
    - `filter`过滤函数
        ```
        l1 = [1, 2, 3, 4, 5]
        print(list(filter(lambda x:x>3,l1)))
        print(list(filter(lambda x:True if x%2==0 else False,l1)))
        ```
- `sorted`函数
    ```
    d1 = sorted([('a', 1), ('b', 3), ('c', 6)], key=lambda x: x[1], reverse=True)
    # [('c', 6), ('b', 3), ('a', 1)]
    ```

- 闭包
    - 通过`__closure__`属性来实现:所有的函数对象都有一个__closure__属性，如果它是一个闭包函数，那么它包含一个cell objects元组
        ```
        def o():
            a = 'qwe'
            def i():
                print(a[:-2])
                return a
            return i

        a = 'asd'
        r = o()
        print(o.__closure__)
        print(r.__closure__)
        print(r.__code__.co_freevars)

        # None
        # (<cell at 0x00000263C9907348: str object at 0x00000263C9846538>,)
        # ('a',)
        ```
## 面向对象
- `isinstance(o, t)`
- `issubinstance(cls, classinfo)`
- 类方法
- 静态方法(没有实例初始化的时候也能使用,没有实例变量)
## 扩展
- 栈和栈帧

    ```
    import dis

    def test(a, b): 
        c = a + b
        return c

    dis.dis(test)

    95          0 LOAD_FAST               0 (a)
                2 LOAD_FAST               1 (b)
                4 BINARY_ADD
                6 STORE_FAST              2 (c)

    96          8 LOAD_FAST               2 (c)
                10 RETURN_VALUE
    ```

    1. Python中栈的分类: 
        > 用户栈: 函数被调用时,会专门为其分配用户栈内存,用户栈内存除用来存储变量外,还包括字节码参数和返回值所需空间.
        > 系统栈: 用于机器执行,用户栈用于代码执行状态.
    2. Python中栈的作用: 
        > 栈用于指令执行,与线程绑定.函数调用与执行都依赖于线程栈上存储的上下文和执行状态.
    3. 栈帧(Stack Frame)
        > 线程栈这块内存中,每个被调用函数都分配着一块区域 Call stack是函数调用堆栈(运行时函数的调用过程),除返回地址,还有为函数提供参数,局部变量存储空间等
    4. 调用函数时的内存变化: 
        > **函数每次调用,都会新建栈帧**,用于局部变量和执行过程存储.执行完成后,栈帧内存被回收,同时释放相关对象.


- 栈帧对象PyFrameObject
    ```
    def test(): 
        return id(locals())

    print(test())#Create New StackFrame
    print(test())#Create Another New StackFrame

    2439859900488
    2439859902432
    ```

    1. 查看栈帧对象PyFrameObject
        > PyFrameObject,栈帧表示程序运行时函数调用栈中的某一帧。函数没有属性可以获取它，因为它在函数调用时才会产生想要获得某个函数相关的栈帧，则必须在调用这个函数且这个函数尚未返回时获取。

        >sys._getframe()方法可以获取当前栈帧   
        >>_back:  调用栈的前一帧   
        >>f_code:  栈帧对应的code对象   
        >>f_locals:  用在当前栈帧时与内建函数locals()相同，但你可以先获取其他帧然后使用这个属性获取那个帧的locals()   
        >>f_globals:  用在当前栈帧时与内建函数globals()相同，但你可以先获取其他帧……   
        >>f_builtins -> dict key:   python的内置函数名  

        ```
        import sys

        def func():
            frame = sys._getframe()
            print(frame.f_locals)
            print(frame.f_globals)
            print(frame.f_back.f_locals)
            # 你可以打印frame的各个域
            # print(s)

        func()
        ```

        ```
        import sys, dis

        def A():
            x = 'func A'
            B()

        def B():
            C()

        def C():
            c_var = 'test'
            f = sys._getframe(0)  # 向上2级，获取A栈帧,1获取B,0是当前
            print('frame及遍历---------------------------------------------------------------')
            print(f.f_code.co_name, '栈帧类型和对象:', type(f), f)
            #     print('遍历:',dir(f))
            print('名字空间---------------------------------------------------------------')
            #     print('函数所在模块的的名字空间f_globalsa或直接globals():',f.f_globals)#返回函数所在模块的的名字空间
            #     print('frame f_builtins:',f.f_builtins)#A人   
            print(f.f_code.co_name, '名字空间f_locals（运行期）:', f.f_locals)  # A名字空间（运行期）
            print('代码对象---------------------------------------------------------------')
            print(f.f_code.co_name, '代码对象f_code:', f.f_code)  # A代码对象
            print(f.f_code.co_name, '代码对象f_fileno:', f.f_lineno)  # 所在文件行数   
            print(f.f_code.co_name, '最后执行指令的偏移量f_lasti:', f.f_lasti)  # A最后执行指令的偏移量

            print('栈帧对象---------------------------------------------------------------')
            print(f.f_code.co_name, ' frame f_back:', f.f_back)  # 前一帧对象
            print(f.f_code.co_name, ' frame f_trace:', f.f_trace)  # trace对象

            print('f_code,---------------------------------------------------------------')
            print('该f_code即为对应函数的代码对象-------------------------')
            #     print('遍历f_code:',dir(f.f_code))
            print('co_stacksize', f.f_code.co_stacksize)

        A()


        # frame及遍历---------------------------------------------------------------
        # C 栈帧类型和对象: <class 'frame'> <frame at 0x0000018B70F983D8, file 'D:/ai/test.py', line 129, code C>
        # 名字空间---------------------------------------------------------------
        # C 名字空间f_locals（运行期）: {'c_var': 'test', 'f': <frame at 0x0000018B70F983D8, file 'D:/ai/test.py', line 134, code C>}
        # 代码对象---------------------------------------------------------------
        # C 代码对象f_code: <code object C at 0x0000018B711AB780, file "D:/ai/test.py", line 125>
        # C 代码对象f_fileno: 137
        # C 最后执行指令的偏移量f_lasti: 126
        # 栈帧对象---------------------------------------------------------------
        # C  frame f_back: <frame at 0x0000018B70FDF5E8, file 'D:/ai/test.py', line 122, code B>
        # C  frame f_trace: None
        # f_code,---------------------------------------------------------------
        # 该f_code即为对应函数的代码对象-------------------------
        # co_stacksize 5
        ``` 

        ```
        import sys
        print(sys._current_frames())  # 返回一个dict,所有栈帧
        ```

- 垃圾回收
    - ⼀个对象的引⽤数为0,Python虚拟机就会回收这个对象的内存.当引⽤计数为0时，该对象⽣命就结束了