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