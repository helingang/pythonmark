# python的解释器
1. 官方CPython: C语言开发,最广泛的解释器
2. IPython: 一个交互式,功能增强的Cpython
3. PyPy: Python语言写的Python解释器,JIT(just in time)技术,**动态**编译Python代码
4. Jython: Python的源代码编译成Java的字节码,跑在JVM(java 虚拟机)上
5. IronPython: 与Jython类似,运行在.Net平台上的解释器,Python代码被编译成.Net字节码

# 基础知识
## 数据类型
### 数字
1. 整数
    1. 不区分`long`和`int`
    2. 长度没限制
    3. 进制(十六进制 0x;二进制 0b)
    4. 布尔, True(1), False(0)
2. 浮点型(科学计数法)
    1. 1.23*10<sup>9</sup>等于`1.23e9`
    2. 浮点型计算是不精确的,例如`1.2 - 1`得到0.19999999999999996
        1. 精确小数计算
```
# 定点数(精确小数)
import decimal
a = decimal.Decimal('1.2')
b = decimal.Decimal('1')
print(a - b)
```
### 字符串
1. 使用'或",使用'''或"""可跨行
2. 字符串前加r或者R,表示字符串不做特殊处理(不做转义)

### 总结
1. `int str bool float complex tuple bytes`不可变
2. `list set dict bytearray`可变

## 基础语法
### 转义字符
1. `\n`换行
2. `\t`制表符
3. `\b`退格BackSpace
4. `\r`回车,当前位置移到本行开头(退格到开头)
5. `\0`代表空字符
6. `\a`系统提示音
### 缩进
1. 4空格缩进
### 续行
1. 在行尾使用\
2. 如果使用各种括号,认为括号内是一个整体,内部跨行不用\
### 标识符
1. 字母,下划线和数字组成
2. 字符或下划线开头
3. 不能是关键字
4. 大小写敏感
### 常量
1. python无法定义常量
### 字面常量
1. 一个单独的量,例如`12,'abc'`(放在内存中固定不变的)
### 变量

## Python语言类型
1. Python是**动态**语言,**强类型**语言
2. 静态编译语言: 事先声明变量类型,类型不能改变,编译时检查
3. 动态编译语言: 不用事先声明类型,随时可以赋值为其他类型,编程时不知道是什么类型
4. 强类型语言: 不同类型之间操作(例如打印),必须转成同一类型
5. 弱类型语言: 不同类型之间可以隐式转换(JS打印)

## 运算符
### 算数运算符
`+ - * / //(整除) % **(幂)`
#### math模块

### 位运算符
`&(与: 都是1才为1,否则为0) |(或: 都是0才为0,否则为1) ~(位运算符非) ^(异或: 相同取0,不同取1) <<(左移) >>(右移)`
1. `~`: 12的二进制为1100,按位取反后为1101,十进制则为-13
1. `&`与: 都是1才为1,否则为0
2. `|`或: 都是0才为0,否则为1
3. `~`非: 按位取反再加1
4. `^`异或: 相同取0,不同取1
5. `<<`左移: 乘以2的x次方,`9<<2`等于`9*4=36`
6. `>>`右移: 除以2的x次方

### 比较运算符
1. `== != > < >= <=`
2. 返回布尔值
3. `1 < '1' Fales`比较数据类型, `1 < 'a' 报错`类型不一致, `'1' > '2' False`比较ASCII码
4. `4 > 3 > 1`链式比较
### 赋值运算符
1. `a = min(3, 5)`
2. `+= -= *= /= %= **= //=`
3. `x = y = z = 1`
### 身份运算符
1. `is, is not`
2. `isinstance(obj, 对象类型)` 判断是否有构造关系
### 成员运算符
1. `in, not in`
### 逻辑运算符
1. 与或非`and or not`
2. 短路运算符
    1. and: 如果第一个表达式为False,后面就没必要计算了,则逻辑表达式一定为False
    2. or: 如果第一个表达式True,后面就没有必要计算了,表达式一定为True
3. not > and > or

### 原码,反码,补码,负数
#### 原码(对人友好)
1. 5 => 0b101, 1 => 0b1, -1 => -0b1, bin(-1), 在最高位为0时表示正数,最高位为1时表示负数
#### 反码
1. 正数的反码与原码相同
2. 负数的反码**符号位不变**其余按位取反
#### 补码(计算机使用)
1. 正数的补码与原码相同
2. 负数的补码**符号位不变**其余按位取反后加1
#### 负数表示法
1. 数字电路的CPU的运算器实现了加法器,但是没有减法器,减法是转换成加法
2. 负数在计算机中使用补码存储, -1的补码是1111 1111(8位是一个字节)
3. 5-1 => 5+(-1)直觉上是0b101-0b1,其实计算机中是0b00000101 + 0b11111111,溢出位舍弃


## 字符串和编码
### 字符编码
计算机底层都是二进制,但是表示都是16进制(因为2进制太长)

计算机只能处理数字, 如果要处理文字, 就要把文字转换成数字, 最早计算机设计是8个比特(bit)作为一个字节(byte),所以一个字节的最大整数是255,比如两个字节能表示的最大整数是65535

ASCII码指的是字母和一些字符,例如A是65

中国制定GB2312编码,把中文编进去.而其他国家有各自的标准,混合使用会出现乱码

而Unicode统一了所有的编码,Unicode通常用两个字节表示一个字符,而ASCII编码是一个字节

字符`A`的ASCII编码是十进制的65,二进制的`01000001`;<br>
字符`0`的ASCII编码是十进制的48,二进制的`00110000`;<br>
汉字`中`已经超出ASCII编码的范围,用Unicode编码是十进制的20013,二进制的`01001110 00101101`<br>
把ASCII编码的`A`用Unicode表示,只需要在前面补零,然而英文全部用Unicode表示的话需要多一倍的存储空间,所以Unicode出现"可变编码长"->`utf-8`,`utf-8`把Unicode字符根据不同的数字大小编码成1-6个字符,**常用的英文字母被编码成1个字节**,**汉字通常是3个字节**,生僻的字符被编码成4-6个字节,因此用utf-8传输英文字符就能节省空间

|字符|ASCII|Unicode|utf-8|
|:-:|:-:|:-:|:-:|
|A|01000001|00000000 01000001|01000001|
|中|x|01001110 00101101|11100100 10111000 10101101|

结论:<br>
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码<br>
用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

<img src="./images/encode.png" width=50%>

### python字符串
python的字符串类型是str,在内存中是Unicode表示,一个字符对应若干个字节,如果要在网络上传输,或者保存在磁盘中,就需要把str变为以字节为单位的bytes,python对bytes类型的数据用`b`前缀表示,例如
```
x = b'ABC'
bytes(b'abc') # 二进制字符串对象
bytearray(b'a') # 二进制字符串数组对象
```
解码与编码:
```
# b'ABC'
print('ABC'.encode('ascii'))
# 报错,因为ascii不理解中文
print('中'.encode('ascii'))

# b'ABC'
print('ABC'.encode('UTF-8'))
# b'\xe4\xb8\xad'
print('中'.encode('UTF-8'))
```
```
print(b'\xe4\xb8\xad'.decode('utf-8'))
print(b'ABC'.decode('utf-8'))
```
```
# URL编码
from urllib import parse
s = '中国'
print(parse.quote(s))
```

### 字符串的使用
1. `len()`
len计算str的字符数,计算bytes的字节数
```
# 3
print(len(b'\xe4\xb8\xad'))

# 2
print(len('AB'))
```

2. 字符串方法(不改变原字符串)
    1. 查
        1. `str.index(value)`
        2. `str.count(value)`
        3. `str.find(value, a, b)`从下标a-下标b(a,b可选参数)开始获取value的下标,未找到返回-1
        4. `str.isdigit()`判断字符串中是否全部都是数字
        5. `str.isalpha()`判断字符串中是否全部都是字母
        6. `str.endswith(value)`判断字符串是否以value开头
        7. `str.startswith(value)`判断字符串是否以value开头
        8. `str.islower()`
        9. `str.isupper()`
    2. 改(返回新的字符串)
        1. `str.upper()`将字母大写并返回字符串
        2. `str.lower()`
        3. `str.strip()`去除两边空格
        4. `str.lstrip()`
        5. `str.rstrip()`
        6. `str.capitalize()`下标为0的字符大写
        7. `str.title()`将单词首字母大写
        8. `str.split(value, x)`以value为界切割x(可选)次后返回list列表,不填参数默认切割空格
        9. `str.join(list/tuple)`返回组合的字符串
        10. 
    3. 删
        1. `str.replace(old, new, x)`在字符串中将x个old替换成new
    4. 增
        1. `拼接`

3. 字符串拼接
    1. 拼接
        1. `'123 %s %s'%(123, 456)`      
        2. `'%.1f'%1.23`一位小数
        3. `'%-6.1f'%1.23`一位小数,后补齐6个字符
        4. `'%6.1f'%1.23`一位小数,前补齐6个字符
    2. `format()`
        >`'{0}的成绩提升了{1:.1f}分'.format('小明',21,45123)`小明的成绩提升了21.0分
        
        > `'123{0}{1}'.format(456, 789)'`

        > `'{0}{1}{a}'.format('000','111', a = '123')`

        > `'{a:^10.2f} {0} {b:.2%}'.format(1.2345, a = 2.345, b = 3.45)`^/</>(居中/左/右)对齐

        > `a = '123{}'.format print(a(456))`把`'123{}'.format`当做一个函数
    3. `format_map(dict)`
        >`'123{a}{b}'.format_map({ 'a': 1,'b': 2})`
4. 字符串格式化
    1. 占位符

        |占位符|替换内容|
        |:-:|:-:|
        |%d|整数|
        |%f|浮点型|
        |%s|字符串|
        |%r|与%s类似,但是打印时不会去掉字符串的引号|
        |%x|十六进制整数|
        |%c|ascii码|
        |%o|八进制|
        |%e|科学计数|

        >`'%s is %d years old,he has %.1f money' %('tom', 1000, 1.1)` tom is 1000 years old,he has 1.1 money


## 使用list和tuple
### list
1. `len()`
2. 增
    1. `l.append(value)`
    2. `l.insert(index, value)`
    3. `l.extend(value)`插入str,list或tuple;(拆开分别插入在最后面)
3. 删
    1. `l.pop(index)`通过索引删除(参数不填则默认为-1)
    2. `l.remove(value)`通过值删除(相同元素只删除第一个)
    3. `l.clear()`全部清除
4. 改
    1. `l[index] = value`
5. 查
    1. `l.index(value)`根据value获取下标(重复则取第一个)
    2. `l.count(value)`根据value获取出现次数
6. 其他方法
    1. `l.copy()`浅拷贝(会重新开辟一个内存地址存放这个list,修改内层的list,原list受到影响)
    2. `l.reverse()`反转
    3. `l.sort(reverse = False)`(参数默认为False)表示从小到大排序
7. 切片
    1. `list1[1:4:1]`
    2. `list1[-2:-4:-1]`
8. 列表的**深复制**
    1. 即使修改内层的list,原list不受影响
    2. 例子
        ```
        import copy
        li = ['1', ['2'], 3]
        deeplist = copy.deepcopy(li)
        ```
### tuple
1. 一旦初始化则不能修改,所以更加安全
2. `tuple[index]`
3. 查
    1. `t.index(value)`
    2. `t.count(value)`
4. 只有一个元素的tuple必须加逗号来消除歧义
    1. `t = (1, )`
5. 内部如果某个元素是list,则这个list可以被修改

### 不同类型之间转化
`l = list(s)`
`t = tuple(l)`

## 使用dict和set
### dict
1. 3.6以后是有序的
2. 增
    1. `d.copy()`浅复制
    2. `d.setdefault(key, value)` 设置keyvalue,不填写value则value默认为None,有则查无则增,返回value值
    3. `dict.fromkeys(list1/dict1/set1, v)`提取key与value组成新的字典
3. 删
    1. `d.pop(key)`key必填
    2. `d.popitem()`删除最后一个
    3. `d.clear()`
4. 改
    1. `d.update(d1)`
5. 查
    1. `d[key]`
    2. `d.get(key, msg)`
    3. `d.keys()`
    4. `d.values()`
    5. `d.items()`
6. dict用空间换取查询效率
7. dict的key不可变,这种通过key计算位置的算法称为哈希算法

### set
1. 是key(不可变对象)的集合,但不存储value
2. 创建set时需要list作为输入集合
    1. `s = set([1, 2])`
3. 特性
    1. 没有重复的元素
    2. set是无序的不存在索引取值
    3. 3.6版本以后是可变的
4. 增
    1. `s.add(key)`
5. 删
    1. `s.pop()`删除第一个
    2. `s.clear()`
    3. `s.remove(key)`
6. 改
    1. `s.update()`
7. 查
    1. `s1.isdisjoint(s2)` s1是否与s2没有交集,如果没有交集返回True
    2. `s1.issubset(s2)` s1是否包含于s2
    3. `s1.issuperset(s2)` s1是否包含s2
8. set集合的运算
    1. `& | -`

### 对象的可变性
1. 字符串,数字,tuple是不可变对象.而list,dict等是可变对象,不可以作为key保存
2. 修改不可变对象
    1. 使用切片
    2. 修改可变对象(list等)时,内存地址不变
    3. 强行修改不可变对象(字符串,元祖等)时,内存地址被修改

# 条件控制和循环
1. if三目运算

```
# 打印1或者2
print(1) if a > 1 else 2
```

2. while

循环while
注: break不仅跳出while而且跳出else,continue跳出当前循环,else表示循环完成后执行的语句
```
while 条件:
    code
else:
    code
```

3. for
    1. `for i in obj`只循环**可迭代的对象**(序列类型, 散列类型)
    2. `for i in range(x, y, z)`range(x, y, z)就可以看成可迭代对象, [x, y), z是步长默认为1
```
for i in range(0, 20):
    if i % 5 == 0:
        continue
    print(i)
else:
    print('123')
```

# 函数
1. 默认返回None
2. 返回多个值时实际返回tuple
3. 参数
    1. 必备参数
    2. 默认参数
    3. 不定长参数
        1. `*args`类型为元祖
        2. `**kwargs`类型为字典
4. 传参
    1. 位置传参
    2. 指定传参

```
def test(a, *args, b = 5, **kwargs):
    print(a, args, b, kwargs)

test(1, 2, 3, 4, b = 10, q = 10, w = 11)
test(1, *(2, 3), b = 10, **{'w': 10, 'c': 11})

```

5. 常用内置函数
    1. `dir()`
    2. `min max sum sorted reversed sum`
    3. enumerate 返回可以枚举的对象
    4. `eval` 运算字符串中的表达式
    5. `exec` 解析字符串
    6. `filter(函数名称, 参数列表)` 默认返回 返回值为True(或者1)时的参数组成的列表
    7. `map(函数名称, 参数列表)` 返回 返回值组成的列表
    8. `zip(序列类型1, 序列类型2)` 将两个序列类型组合成字典

6. 匿名函数
    1.  `lambda 参数: 表达式`
    2. 一般用在做一些简单的操作
```
print(list(filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6]))
```
7. 函数作用域
    1. 函数内部可以访问函数外面的变量
    2. 优先在函数内部找,然后在外部找
    3. 函数内部如果没有声明全局变量则不能修改外部的变量(外部的变量默认是全局的)(如果这个对象是可变的例如list set dict,则不用声明globle全局变量)
    4. 声明全局变量globle, 声明局部变量nonlocal
    5. 外部无法访问局部变量
```
a = 1
def test():
    a = 2
    def a1():
        nonlocal a
        a = a + 1
        print(a) # 3
    a1()
    print(a) # 3
test()
print(a) # 1
```

8. 闭包
    1. 闭包是函数内部和外部沟通的桥梁
```
def test():
    a = 1
    def a1():
        print(a)
    return a1

a = test()
a()
```

9. 递归
    1. 注意需要跳出的条件
    2. 占用内存较大
```
def test(a):
    if a <= 1:
        return 1
    return test(a - 1) * a

print(test(6))
```

10. 回调函数
    1. 参数是函数被传入
    2. 注意触发回调函数的条件
```
def a():
    print('a回调函数')

def b(fn, q):
    if q == 1:
        fn()

b(a, 1)
```


# 文件操作
1. `open`
    1. `open(file_path, mode, encoding = 'utf-8')`
    2. 返回**文件对象**,可以操作文件
    3. 参数
        1. `mode`
            1. `r`只读: 默认
            2. `w`只写(不能读): 文件存在则覆盖,没有则创建
            3. `a`追加模式(不能读): 文件存在则追加写入,否则创建
            4. `+`附加模式(读和写)打开一个磁盘文件
                1. 可与r,w,a,+组合
                2. `r+`表示r与w,以r为主,不会创建和覆盖文件,光环默认在0位置
                3. `w+`表示r与w,以w为主,存在则覆盖,不存在则创建
                4. `a+`表示a与r,以a为主,存在时不会覆盖,不存在时创建
            5. `b`附加模式
                1. 二进制模式(默认为文本(字符串)模式)
                2. 可与r,w,a组合
        2. `encoding`
        3. `errors`
            1. `ignore` 忽略错误
    4. `api`
        1. `f = open('test.py', mode = 'w+')`
        2. `f.read(a)`
            1. 从游标处读取文件a(默认为最后)个内容(str),并移动游标,如果游标在最后则read内容为空
        3. `f.readline()` 读取一行
        4. `f.readlines()` 读取所有数据
            1. 返回的是列表,以行尾界限
        5. `f.write(data)` 写入内容并移动游标
        6. `f.writelines(data)`写入多行
            1. 需要自己加换行符
        7. `f.flush()`
            1. 刷新缓冲: 通常在write后写,将内存中残留的数据写入到硬盘和文件中
            2. 在单独 写 的时候会有写缓冲,在单独 读 的时候会有读缓冲,写缓冲和读缓冲是分开的
        8. `f.seek(0)`
            1. 设置游标到下标为0的位置: 下次read的时候从游标处开始阅读,下次write的时候则会以覆盖的形式写入(而不是插入的方式)
        9. `f.tell()` 返回游标的位置
        10. `f.close()` 关闭文件
            1. 如果不关闭的话占用内存
        11. `f.closed` 查看文件是否被关闭
2. 打开临时文件
    1. 在内存中打开文件,返回文件对象
        > `f = io.StringIO('123')`
        
        > `f = io.BytesIO(b'123')`
    2. `f.getvalue`无视光标的位置获取所有值
    3. 其他api与open相同
3. `with as`
    1. 不需要关闭文件,with语句执行完后会自动执行`f.close()`
    2. 使用`\`可以打开多个文件



# os模块
- `os.getcwd()`显示当前路径
- `os.listdir(path = path)`显示当前目录内容,path默认为当前路径
- `os.chdir(path)`切换到目标路径(类似于cd)
- `os.mkdir(path = path, mode = mode)`创建目录
- `os.rmdir(path)`删除文件夹
- `os.remove(path)`删除文件
- `os.rename(path, name)`重命名
- `os.path.join(path1, path2)`以`/`拼接路径
- `os.path.dirname(path)`获取文件所在文件夹的绝对路径
- `os.path.basename()`获取文件名
- `os.path.abspath(fileName)`获取文件的绝对路径
- `os.path.relpath(file, path)`返回'相对于path路径访问file'的相对路径
- `os.path.getsize(path)`返回文件大小(字节)
- `os.path.getctime(path)`返回创建时间
- `os.path.getmtime(path)`返回修改时间
- `os.path.exists(path)`判断文件或文件夹是否存在
- `os.path.isdir(path)`判断是否是文件夹
- `os.path.isfile(path)`判断是否是文件
- `os.system('sl')`执行linux命令sl

# 类
### 类的属性和方法的声明和调用
```
class Student:
    # 初始化实例时执行的方法
    # 双下划线方法会在特定的实际触发
    def __init__(self, height):
        # 定义每个实例的属性
        self.height = height
    
    # 析构函数
    # 所有代码执行完后自动执行,会销毁实例的地址
    # del 可以删除一个变量的地址
    def __del__(self):
        print('销毁')
    
    # 定义公有属性1
    name = 'Sam'
    age = 15

    # 定义私有属性1(可以用类名或者实例名调用)
    _sex = 'male'

    # 定义私有属性2
    # 无法通过类型或者实例名调用
    # 如何访问私有属性: `Student._Student__weight`,`Student()._Student__weight`
    __weight = 100

    # 定义方法
    # self代表实例
    def study(self):
        print(self.__eat())

    # 私有方法与属性的声明和调用相同
    def __eat(self):
        print(self.age)

# 定义公有属性2
Student.level = 1

# 调用属性1 类名.属性名
print(Student.level)

# 调用属性2 实例名.属性名
print(Student().age)

# 定义属性3(只属于这个实例)
s = Student()
s.math = 20
print(s.math)
```

### 继承
- 参数为空时默认继承`object`类
- `object`类是所有类的父类
- 括号中填写类的名字即可继承,会调用父类的方法和属性
- 访问顺序: 自己类的属性或方法 -> 父类 -> 继续往上查找直到`object`
- `类名.__bases__`: 查看某个类的直接父类(基类),返回tuple,注意不能`实例名.__bases__`

#### 多继承
`class Son(Father, Mother):`

#### 重写
- 在子类中重写一个方法,方法名与父类中方法名相同
- 重写后如何使用父类的方法:
    1. `父类类名.eat(self)`
    2. `super().方法()`

#### 查看类的继承顺序
1. mro方法在类被创建时就被创建了
2. `类名.mro()`
3. `类名.__mro__`
4. 注意私有属性只有前面有下划线

### 面向对象
1. 封装
2. 继承
3. 多态
    1. 对同一间事情,会做出不同的反应
```
class Animal:
    def run(self):
        print('Run')
class Dog(Animal):
    def run(self:)
        print('RunRun')
class Rabbit(Animal):
    def run(self:)
        print('RunRunRun')
```

```
class Father: 
    def init(self, name, age): 
        self.name = name 
        self.age = age 
        self.__money = 300
    def eat(self):
        print('Father eat')

class Mother: 
    def init(self, day): 
        self.day = day
    def cook(self):
        print(self.age)
    def eat(self):
        print('Mother eat')

# 优先调用自己的初始化方法,其次Father, Mother...

class Son(Father, Mother):
    def __init__(self, name, age, day):
        # 重写属性
        self.name = name
        self.age = age
        self.day = day
    # 重写方法
    def eat(self):
        print('son eat')
        # 调用父类的方法 父类类名.eat(self)
        Father.eat(self)
        Mother.eat(self)
        # super().方法
        # 这里Father的eat方法覆盖了Mother的eat方法
        super().eat()
```


### 魔术方法
1. 在特定的时机自己调用,比如`__init__`,`__del__`
2. 双下划线开头和结尾,魔术方法让类的表现形式更丰富
3. `__add__`
    1. 在遇到`+`号时执行的方法
```
class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # other指另一个实例
    def __add__(self, other):
        return self.x + other.y

a = Calc(3, 5)
b = Calc(4, 6)
# 在遇到+加法时,将a这个实例传给self,b这个实例传给other
print(a + b)
```
4. `__str__`和`__repr__`
    1. 在`print`打印**实例**时触发
    2. 直接执行时优先调用`__str__`,其次`__repr__`,再其次打印类的地址
    3. 在交互模式下优先调用`__repr__`,其次打印类的地址
    4. 必须使用`return`,并且需要返回字符串`str`
```
class Dog:
    def __str__(self):
        return '__str__'
    def __repr__(self):
        return '__repr__'
a = Dog()
print(a)
```

5. `__call__`实例在调用时触发
```
class Dog:
    def __call__(self, *args, **kwargs): 
        print('call')
a = Dog()
a()
```

6. `__new__`
    1. 在创建实例时触发
    2. 实例是通过`__new__`方法里面创建的
    3. 实例化时,先进入`__new__`,但是只有返回一个实例`object.__new__(cls)`时,才会进入`__init__`方法
    4. `cls`代表类本身
```
class Food:
    def __init__(self, name):
        self.name = name
        print('__init__')
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return object.__new__(cls)

a = Food('eg')
print(a)
```



7. 其他魔术方法
`__add__(self, other) __sub__(self, other)`等


### 单例模式
1. 原理: 通过重写`__new__`方法,让`__new__`只能进行一次实例创建
2. 优点: 节省内存
3. 第二次创建时其实没有真正创建,而是去引用第一次创建的实例,只是同一个实例的不同名字
```
class Food:
    __instance = None
    def __init__(self, name):
        self.name = name
        print('__init__')
    
    def __new__(cls, *args, **kwargs):
        print('__new__')
        if cls.__instance == None:
            # 创建一个实例,并赋值给私有属性,下次实例化时如果存在则不会再创建实例
            cls.__instance = object.__new__(cls)
        return cls.__instance
a = Food('x')
b = Food('y')
print(a == b) # True
```
### 定制属性访问
1. 获取属性
    1. `getattr(类名/实例名, 'name')` -> `obj.name`
    2. `__getattr__`
        1. 魔术方法: 在没有获取到属性时触发
    3. `a.__getattribute__('name')`
2. 修改属性
    1. `__setattr__`在设置属性时触发
    2. `setattr(类名/实例名, 'name', value)`修改/增加
3. 删除属性
    1. `delattr(类名, 'name')` -> `del obj.name`
    2. `__delattr__`
4. 查询属性
    1. `hasattr(类名/实例名, 'name')`

### 描述符
```
class Base:
    # self -> Base的实例
    # instance -> A的实例
    # owner -> A这个类
    def __get__(self, instance, owner):
        print('__get__')
    def __set__(self, instance, value):
        print('__set__')
    def __delete__(self, instance):
        print('__delete__')

class A:
    # 属性是一个实例
    base = Base()

a = A()
a.base
a.base = 1
del a.base
```

### 装饰器
1. 本质是函数
2. 在不修改原函数的基础上增加功能
```
# 自定义装饰器函数dog
# 使用dog函数装饰test函数
# 装饰器函数会传入函数名
def dog(fun):
    def pig():
        print('dog--------')
        fun()
        print('-----------')
    return pig

# 相当于执行dog函数并把test作为参数传入:
# test = dog(test) -> test 相当于 pig
# test就是dog函数执行(test作为参数)后的返回值, 把test看成pig
@dog #这句话相当于 test = dog(test)
def test():
    print('test')

test()
```

3. 内置装饰器
    1. `@property`
        1. 将方法可以作为属性访问
    2. `@staticmethod`
        1. 断绝方法与类的联系,相当于独立函数
        2. 没有self参数
    3. `@classmethod`
        1. cls代表类本身

```
class Base:
    @property
    def study(self):
        return self

    @staticmethod
    def eat():
        print(Base.study)
        return 'eat'

    @classmethod
    def sleep(cls):
        print(cls)

a = Base()
print(a.study)
```

4. 类装饰器
    1, 必须定义初始化方法和`__call__`方法

```
class Base:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        self.fun()
        print('call')

@Base # test = Base(test)
def test():
    print('test')

```