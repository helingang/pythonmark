## 变量
1. 直接量
```
var
```
2. 通过对象的方法定义
```
var str = new String('hello');
var str = String('hello');
var arr = new Array(1,2,3);
var arr = new Array(2); //只有一个数字时,声明数组的长度为2
```

## 操作标签
### 获取标签-执行事件
```
document.getElementById('box').onclick = function(){alert(1)}
```

#### 元素
节点/DOM对象/元素

#### JS获取元素的方式
- 通过id获取(静态获取)
```
获取单个元素
document.getElementById('');
```

- 通过class获取
```
document.getElementsByClassName(''); //IE8+,获取的是类数组
```

- 通过标签名获取
```
document.getElementsByTagName(''); //获取的是类数组
```

- 通过name获取
```
document.getElementsByName(''); //获取的是类数组
```

- 通过选择器获取(性能较差)
```
querySelector(); //获取单个元素,能匹配多个时只获取第一个
querySelectorAll(); //获取的是类数组
```

- 备注
    - 通过id获取时,前缀必须是document,其他地方获取时,前缀可以是某个节点对象

- 获取Head`document.head`
- 获取body`document.body`
- 获取title`document.title`


### JS操作标签的属性
- 操作合法属性
    - 修改id: `document.getElementById('box1').id = 'box2'`
    - 修改class: `document.getElementById('box').className = 'box2'`
- 操作自定义属性
    - `x.getAttribute('abc')`
    - `x.setAttribute('abc', '123')`
    - `x.removeAttribute('abc')`

### JS操作CSS样式
- `oDiv.style.width`

## 循环
- for
- while
- do while

## 条件
- if
- switch

## 函数
- 匿名函数

- 有名函数

- 函数表达式的自执行
    ```
    (function(){}());
    (function(){})();
    +function(){}();
    -function(){}();
    ~function(){}();
    !function(){}();
    ```

- 传参
    - 定参
    - 不定参

## call,apply,bind
### call()
- 在函数执行阶段改变`this`指向,`call`会帮助前面的函数执行
- `call`的第一个参数代表`this`的执行,其他实参依次对应原函数的形参
    ```
    function test() {
        console.log(this)
    }
    test.call(document);
    ```

### apply()
- 在函数执行阶段改变`this`指向,`apply`会帮助前面的函数执行
- `apply`的第一个参数代表函数的`this`指向,数组的第一个实参对应原函数第一个形参

### bind() (不支持IE8及以下)
- 在函数引用时改变`this`指向,`bind`不会帮助前面的函数执行,当函数被执行时改变`this`指向

### 使用三个方法的时机
1. `call`和`apply`在函数需要自执行且需要改变`this`指向时使用
2. `bind`在函数是被动执行(例如事件函数)时或者是函数作为参数传入(因为此时函数还未执行)时且需要改变`this`时使用

3. `bind`
    ```
    oBox1.onclick = function () {
        console.log(this);
        fn.call(this);
    };
    function fn() {
        if ( this.style.backgroundColor === 'black' ) {
            this.style.backgroundColor = 'red'
        } else {
            this.style.backgroundColor = 'black'
        }
    }
    ```


## 定时器
- `setInterval(fn, time, p1, p2)`
    - 规则与setTimeout相同
- `setTimeout(fn, time, p1, p2)`

- 执行
    - `setTimeout(fn, 1000)`
    - `setTimeout( function (){}, 1000)`
- 执行(需要传参)
    - `setTimeout( fn.bind(null, 1, 2), 1000)`
    - `setTimeout( fn, 2000, 1, 2)`
- `clearTimeout() / clearInterval()`

- 设置定时器会在到达时间后将代码添加到任务队列中
    ```
    function fib(i) {
        if (i === 1) {
            return 1
        }
        if (i === 2) {
            return 1
        } else {
            return fib(i - 1) + fib(i - 2)
        }
    }

    console.log(fib(40));

    setTimeout(function () {
        console.log('100ms')
    }, 1000);

    ```

## requestAnimationFrame()
- window下的属性
- 形式等同于`setTimeout(fn, 13)`
- 刷新频率自动调整与浏览器一致
- 不兼容IE8及以下
- 主要用于做动画
- CSS3底层用这个写的
- 同一页面有多个时会统一执行,但是`setTimeout()`会单独执行
- 兼容
    ```
    window.requestAnimationFrame = window.requestAnimationFrame || function (fn) {
        setTimeout(fn, 13)
    };
    window.cancelAnimationFrame = window.cancelAnimationFrame || function (t) {
        clearTimeout(t)
    };
    ```

## getComputedStyle(oBox).width
- 兼容IE
    ```
    function getStyle(obj, attr) {
        return getComputedStyle ? getComputedStyle(obj)[attr] : obi.currentStyle[attr]
    }

    function getObj(obj) {
        return obj.currentStyle || getComputedStyle(obj)
    }

    console.log(getObj(oBox1).width);
    ```

## Math对象
- `max`和`min`
    - `Math.max(a, b, c, d)`
    - `Math.min(a, b, c, d)`
    - `Math.max.apply(Math, arr)`

- 取整方法
    - `Math.ceil()`
    - `Math.floor()`
    - `Math.round()`

- `random()`
    - 返回两个参数的随机值(默认0-1)
- 其他方法
    - `Math.abs()`
    - `Math.pow()`a**b
    - `Math.sin()`
    - `Math.PI`
    - `num.toFixed(n)`保留n位小数

## 时间对象
- 创建
    - `var d = Date()`
    - `var d = new Date()`
    - `var d = new date`
    - `var d = Date.now()`
    - `var d = new Date('2018/10/11)`
    - `var d = new Date(789854613232)`
- Date对象方法
    - get
        - `d.getFullYear()`
        - `d.getMonth() + 1`
        - `d.getDate()`
        - `d.getDay`获取星期
        - `d.getHours()`
        - `d.getMinutes()`
        - `d.getSeconds()`
        - `d.getMilliseconds()`
        - `d.getTime()`
        - `Date.UTC(year, month, date...)`返回毫秒数
        - `d.getTimezoneOffset()`获取与0时区相差的分钟数
    - set
        - `d.setFullYear(2020)`
        - ...
    - 转字符串
        1. `d.toUTCString()` //Fri, 09 Feb 2018 05:18:20 GMT;转化成格林尼治时间
        2. `d.toTimeString()` //12:54:41 GMT+0800 (中国标准时间)
        3. `d.toDateString()` //Wed Feb 07 2018
        4. `d.toLocaleTimeString()` //下午12:54:41
        5. `d.toLocaleDateString()` //2018/2/7
        6. `d.toLocaleString()` //2018/2/7 下午12:54:41
    - Date对象间的运算
        - `var xd = new Date() - new Date(2030)`返回毫秒

## 作用域
    - 全局作用域,全局变量和全局函数可以通过window.形式访问
    - 局部作用局,只有内部可以访问,内部声明的变量会覆盖外部变量

## JS代码解析

    - 从上到下
    - 预解析
        - 寻找var变量以及函数声明(不会找函数表达式,相当于函数表达式也被赋值成undefined),变量会赋值成undefined,把整个函数声明拿到内存空间中
        - 同级作用域的定义过程中变量名与函数重名,保留函数
        - 重名函数,保留后面的函数
```
alert(a);
var a = 10;
alert(a);
function a(){alert(20);}
alert(a);
var a = 30;
alert(a);
function a(){alert(40);}
alert(a);
//function a(){alert(40);}    10   10   30  30  
```
```
var a = 10;
alert(a);
a();
function a(){alert(20);}
//10 报错
```
```
a();
var a = function(){alert(1);};
a();
var a = function(){alert(2);};
a();
var a = function(){alert(3);};
a();
//报错
```
```
if(!("a" in window)){
    var a = 10;
 }
 console.log(a); 
 //undefined
 //定义阶段if true ,执行阶段if false
```
```
var a = 10;
x();
function x(){var a= 20;y();}
function y(){alert(a)};
//10
//函数的作用域,是看在哪里定义的,而不是在哪里执行的,y函数中的a无法访问x函数中的a,y函数中的a可以访问全局的a
```

## 闭包
[学习Javascript闭包（Closure） - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2009/08/learning_javascript_closures.html)
### 什么是闭包
1. 外部函数函数内部嵌套内部函数(作用域的嵌套)
2. 内部函数引用了外部函数中的参数或变量
3. 内部函数中的变量,参数不会被垃圾回收机制回收(关闭浏览器才会回收)
### 特性
1. 全局变量不会被回收
2. 绑定了事件的对象不会被回收(如果函数中使用this则会被回收,参见[02-解析顺序 闭包.wmv])
### 用处
1. 能够读取其他函数内部的变量
2. 让这些变量的值始终保存在内存中
```
var a = 10;
var b = fn();//和fn()()是两个不同的闭包
b();//21
b();//22
fn()();//21 
fn()();//21
function fn(){
    var a = 20;
    return function(){
        a++;
        alert(a);
    }
}
```
```
for(var i=0;i<aLi.length;i++){
    !function(x){
        aLi[x].onclick = function(){
            alert(x);
        }
    }(i)
}
//保存了aLi长度个闭包,每个闭包中的i分别为1,2,3...
```