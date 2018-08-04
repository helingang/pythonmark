## 标签
- `h`标签
    - `h1`-`h6`标题标签
    - h标签自动换行
    - `h1`-`h6`权重降低
- `p`标签
    - p标签后面的元素自动换行
- `b`标签
- `span`标签
- `strong`强调标签
- `pre`标签
- `del`标签
- `em`强调标签
- `sup`上标签
- `sub`下标签
- `a`标签
    - a不能直接套a标签
    - `href='跳转的链接'`
    - `target='规定如何跳转'`默认为`_self`
    - `href`中输入docx可进行下载,输入html进行跳转,输入mailto可发送邮件
    - `title=''`鼠标悬停提示
    - 锚点跳转(a标签可以使用name或id,其他标签必须使用id)
- `img`标签
    - 支持宽高
    - 支持margin
    - 横排显示
    - 能设置`text-align`(在父级中设置),也支持`line-height`
    - 能设置`vertical-align`
    - 标签中间的空格被解析
    - 不支持`margin auto`(因为行内块元素,浮动,定位均不支持`margin auto`)
    - 如何居中: 给父元素添加`text-align:center`
    - img标签四要素
        - `alt`描述图片信息: 对seo搜索产生影响,搜索引擎通过alt搜索图片
        - `width`
            - 一般写原图的宽度,写给搜索引擎看的,如果未写的话会被搜索引擎降级,因为百度等搜索引擎需要根据原图进行适当的压缩以节省加载资源.
            - 对浏览器的性能也有影响(应预先限定图片的尺寸大小,否则在图片加载过程中会更新图片的排版信息,产生大量的重排,从而影响性能)
        - `height`
        - `src` 文件路径
        - `title` 提示信息
- `audio`
    - `autoplay`就绪后自动播放
    - `controls`显示控件
    - `loop`音频结束后重新开始播放
    - `preload`音频在页面加载时进行加载,并预备播放,如果使用'autoplay'则忽略该属性
    - `src`
- 列表标签
    - 无序列表
        - ul和li必须一起出现
        - ul与li之间不能嵌套
        - li与li之间不能嵌套
        - li里面可以嵌套
        - 行内样式type: disc,circle,squ
    - 有序列表
        - ol和li必须一起出现
        - ol和li之间不能嵌套
        - li与li之间不能嵌套
        - li里面可以嵌套
        - 行内样式type: A,a,I,i
    - 自定义列表`dl dt dd`

## 盒模型
### 边框线
- 边框线类型
```
border-style:solid;
none:无边框
solid:实线
dashed:虚线
dotted:点状线
groove:3d凹槽
ridge:3d垄状
inset:3d inset边框
outset:3d outset边框
```

- 颜色
```
border-color: red
```

- 位置
```
border-top: 1px solid red;
```
### 内外边距
- 外边距
- 内边距

### 元素类型
#### 块级元素
1. 块级元素会占据一行的位置,它后面的元素内容会换行显示,块级元素里面可以放任何内容,主要用来布局,支持宽高和内外边距
2. div h1-h6 ul li ol li p table form h1-h6 和 p 标签不能套块级元素
#### 行内元素
1. 行内元素只占据内容所占的位置,其他内容在他后面显示,但是行级元素里面不能放块级元素,不支持宽高,行内元素可以嵌套行元素,但不能嵌套行内元素
2. a b span i em del

### 元素类型转换
```
display: none;
display: block;
display: inline;
display: inline-block;
```

### 外边距合并
#### 垂直方向的合并
1. 垂直相遇的两个盒子会出现外边距合并的情况(水平的不会合并),合并后取较大的值

#### 嵌套盒子的合并
1. 当两个盒子之间没有外边距或者边框分开时,给里面的盒子加上外边距,会自动把外边距合并到外面的盒子上
2. **解决办法**:给外面的盒子加上内边距或者边框线,可以把border或者padding当成边框框住里面的盒子,使里面的盒子和外面盒子的外边距不相

### 背景属性
#### 背景颜色
```
background-color: red;
background-color: #f99;
background-color: rgba(0, 0, 0, .5);
```

#### 背景图片
```
background-image: url('xx');
background-image: none;
```

#### 背景图片的重复方式
```
不重复
background-repeat:no-repeat;

水平方向重复
background-repeat:repeat-x;

竖直方向重复
background-repeat:repeat-y;

默认值
background-repeat:repeat;
```

#### 背景图片的位置
```
background-position:x y;
```
1. 关键词写法 top/bottom/left/right/center
2. 百分比写法
3. 具体的数值
4. 只给一个数值时,另一个数值默认为center

#### 背景关联
```
背景图像相对于元素固定(默认值)
background-attachment:scroll;

背景图像相对于窗体固定
background-attachment:fixed;
```

#### 背景图片尺寸大小
```
数值写法
background-size:100px

百分比写法(根据父级宽高决定)
background-size:50% 50%

定宽或者高,另一个值自动适应
background-size:200px auto;
background-size:auto 200px;

将背景图像等比缩放到宽度或者高度与容器的宽度或高度相等,背景图像始终被包含在容器内
background-size:contain;

将背景图像等比缩放到完全覆盖容器,背景图像有可能超出容器
background-size:cover;
```

#### 多背景
```
background-image:url(''), url('')
```

#### 背景图片的起始区域
```
从padding位置开始(默认)    
background-origin:padding-box;

从内容区域开始
background-origin:content-box;

从边框线开始
background-origin:border-box;
```

#### 背景图片的裁剪(遮盖)
```
从border位置开始裁剪(默认)
background-clip:border-box;

从内容区域开始裁剪
background-origin:content-box

从padding位置开始裁剪
background-clip:padding-box;

背景显示在文字字体上
-webbackground-clip:text;
```

#### 复合写法
```
url;平铺;背景图片位置;背景图片起始位置;背景图片大小;背景图片裁剪位置;背景颜色(在多背景时必须写在最后)
background:url('') no-repeat 10px 20px/cover,url('') repeat-x 10px 20px/cover content-box padding-box #666;
```

## 字体
### 颜色
```
color: red
```

### 字体类型
```
font-family:'微软雅黑','宋体'
@宋体 SimSun
@黑体 SimHei
@微软雅黑 Microsoft YaHei
```

###字体大小
```
百分比的字体大小是根据父级字体大小决定,1em等于父元素字体大小,1rem等于根标签字体的大小
font-size:10px;
font-size:50%;
font-size:1em;
font-size:1rem;
```
### 字体倾斜
```
定义斜体(默认为normal)
font-style:italic;
font-style:oblique;
```
###字体粗细
```
定义粗的字体
font-weight:bold;

定义更粗的字体
font-weight:bolder;

定义更细的字体
font-weight:lighter;

默认
font-weight:normal;

数值范围100-900
font-weight:100;
```
###小型大写字母
```
font-variant:small-caps;
```
### 行高
```
为**父级元素或本身**添加适当的line-height属性可以文字上下居中
	
line-height:10px;

百分比和em的行高大小是根据本身字体大小来决定的
line-height:50%;
line-height:1em;
```
### 字体复合写法
```
字体粗细 小型大写 斜体 字体大小/行高 颜色
font:bold small-caps italic 12px/1.2(em) '微软雅黑';
```

### 新增字体样式
```
@font-face{
	font-family:'muma';
	src:url('');
}

div{
    font-size: 40px;
    font-family: muma;
}
```

## 文本样式
### 文本大小写
```
字母大写
text-transform:uppercase;

首字母大写
text-transform:capitalize;

字母小写
text-transform:lowercase;
```
###文本对齐方式
```
为**父级元素**添加text-align属性可以使元素对齐

左对齐
text-align:left;

居中
text-align:center

右对齐
text-align:right

两端对齐
text-align:justify;
```


###首行缩进
```
适用于块级元素

text-indent:10px;

em是根据本身字体大小决定的
text-indent:1em;
```
###本文修饰
```
text-decoration:none;
text-decoration:underline;
text-decoration:overline;
text-decoration:line-through;
```
###字间距
```
letter-spacing:10px;
letter-spacing:1em;
```
###词间距
```
word-spacing:10px;
word-spacing:1em;
```
###文本不换行
```
white-space:nowrap;
```
###单词内换行
```
word-break:break-all;
```
###文本省略号
```
text-overflow:ellipsis;
```
### HTML5单行省略号
```
white-space: nowrap;
text-overflow: ellipsis;
overflow: hidden;
```
### HTML5多行省略号(chrome)
```
/*老版的弹性盒模型*/
display:-webkit-box;

/*规定字体垂直显示*/
-webkit-box-orient:vertical;

/*规定显示几行*/
-webkit-line-clamp:2;

overflow:hidden;
```
###元素溢出隐藏
```
隐藏溢出容器的内容且不出现滚动条
overflow:hidden;

隐藏溢出容器的内容,溢出的内容产生滚动条
overflow:scroll;

对溢出的内容不做处理,内容可能会超出容器
overflow:visible;

根据内容决定
overflow:auto;
overflow-x:
overflow-y:
```

## 多元素组合选择器
### 多元素选择器
```
同时匹配所有的class和li元素
class , li{}
``` 
### 子元素选择器
```
匹配所有class元素的子元素span
class > span {}
```
### 毗邻元素选择器
```
匹配紧随p元素之后的同级元素div
p + div {}
```
### 属性选择器
```
匹配拥有属性href的元素
[href]{}

匹配属性class的值完全等于box的元素
[class='box']{}

匹配属性class的值包含或完全等于box的元素(不是模糊搜索,要有空格,表示一个class有多个值,有几个值是根据空格来决定的)
[class~='box']{}

匹配class属性中以box-开头或者值完全等于box的元素
[class|='box']{}

匹配拥有href属性且属性class的值为box的div元素
div[href][class='box']{}
```
PS:**选择父级元素**(例如hover子元素时,改变父级元素),通过js学习

## HTML5新增选择器
### 关联选择器
```
选择span后的所有p标签
span ~ p{}

<span>啦啦啦</span>
<p>啊啊啊</p>
<div>哟哟哟</div>
<p>嗯嗯嗯</p>
<p>哦哦哦</p>
```
### 属性选择器
```
选择属性src并且以im开头的元素
[src^='im']{}

选择属性src并且以ng结尾的元素
[src$='ng']{}

选择属性src并且包含es的元素
[src*='es']{}

<img src="images/1.png" alt="">
<img src="images/2.png" alt="">
<img src="images/3.png" alt="">
```
### 伪类选择器
#### of-type
- first-of-type
- last-of-type
```
选择li li是父级元素中的第一个li
li:first-of-type{}
选中class a1 a2

选择li li是父级元素中的最后一个li
li:last-of-type{}
选中class a4 a6

<ul>
    <li class='a1'>
        <ul>
            <li class='a2'></li>
            <li class='a3'></li>
            <li class='a4'></li>
        </ul>
    </li>
    <li class='a5'></li>
    <li class='a6'></li>
</ul>
```	
- only-of-type
```
选择父元素中唯一的p标签(只能有一个p标签)
p:only-of-type{}
选中 class a2

<div>
    <span class='a1'></span>
    <p class='a2'></p>
    <span class='a3'></span>
</div>
```
- nth-of-type(){}
- nth-last-of-type(){}
```
选择第4个p元素
p:nth-of-type(4){}
选择 class a6

选择倒数第4个p元素
p:nth-last-of-type(4){}
选择 class a2

<div class="box">
    <p class='a1'></p>
    <p class='a2'></p>
    <p class='a3'></p>
    <em class='a4'></em>
    <span class='a5'></span>
    <p class='a6'></p>
    <p class='a7'></p>
</div>
```
#### child
- only-child
```
选择父元素中唯一的一个子元素p(有且只有一个子元素p)
p:only-child{}

<div>
    <p></p>
</div>
```
- nth-child(2){}
- nth-child(2n){} 偶数
- nth-child(even){} 偶数
- nth-child(2n-1){} 奇数
- nth-child(odd){} 奇数
- first-child{}
- last-child{}
- nth-last-child(1){}
```
选择父元素的第二个子元素并且类型为p标签
p:nth-child(2){}
选择class a2

选择序号为偶数的子元素,并且类型为p标签
p:nth-child(2n){}
p:nth-child(even){}
选择 class a2 a4 a6

选择序号为奇数的子元素,并且类型为p标签
p:nth-child(2n-1){}
p:nth-child(odd){}
选择 class a1 a3 a5

选中第一个子元素,并且类型为p标签
p:first-child{}
选择 class a1

选中最后一个子元素,并且类型为p标签
p:nth-last-child(1){}
p:last-child{}
选择 class a6

<div>
    <p class='a1'></p>
    <p class='a2'></p>
    <p class='a3'></p>
    <p class='a4'></p>
    <p class='a5'></p>
    <p class='a6'></p>
</div>
```
#### empty
```
选择没有内容的p标签
p:empty{}
选择 class a2

<p class='a1'>啊啊啊</p>
<p class='a2'></p>
<p class='a3'><span></span></p>
```
#### target
**选中被锚点激活的标签**
```
点击a后.选中被锚点激活的p标签
p:target{}

<div>
    <a href="#a3" class='a1'>啊啊啊</a>
    <a href="#a4" class='a2'>嗯嗯嗯</a>
</div>
<p id='a3'></p>
<p id='a4'></p>
```
#### enabled
```
选择可以被操作的input元素
input:enabled{}

<input type="text">
```
#### disabled
```
选择不能被操作的input元素
input:disabled{}

<input type="text" disable='disable'>
```
#### checked
```
选择被选中的input元素(单选框radio,复选框checkbox)
input:checked{}

<input type="checkbox">
```
#### selection
```
选择被用户选中的input(选中输入框的文字)
input::selection{}

<input type="text">
```
#### not
```
选中除了class为a2的span标签
span:not(.a2){}

<div>
    <span class='a1'></span>
    <span class='a2'></span>
    <span class='a3'></span>
</div>
```

## 特殊符号
```
&nbsp; 空格
&lt; 小于
&gt; 大于
&quot; 双引号
&copy; 版权
```

## 伪类选择器
```
伪类:没有为元素定义类名可以通过样式的方式给元素添加特殊效果

规定所有未被点击的链接
:link

匹配所有已被点击的链接
:visited

匹配鼠标悬停其上的元素
:hover

匹配鼠标已经按下,还没有释放的元素
:active

鼠标指针被-定位(点击)时,例如:input,a 
:focus
input:focus{background:red;}
```
## 伪元素选择器
**默认为行内元素,属性必须加上content:''**
```
(通过样式的方式)在元素前面添加内容
:before

(通过样式的方式)在元素后面添加内容
:after
```

## 选择器优先级
### 基本选择器的优先级

> 通配符 < 标签 < 类class < id

### 后代选择器优先级的多种情况
1. 比较顺序
    - 定位越精准优先级越高
    - 当id个数不相等时,id个数多的优先级高
    - 当id个数相等时,class个数多的优先级高
    - 当class和id个数相等时,元素选择器个数多的优先级高
**PS:!important 可以提升优先级但是不建议使用**

## 样式优先级

### 引入外部样式
写在head中,css文件开头写入 @charset 'utf-8'
```
<link rel='stylesheet' type='text/css' href='' />
```
### 导入外部样式
写在< style >标签的第一行,css文件开头写入 @charset 'utf-8'
```
@import'css/index.css'
```
整个网页加载完成后才加载此样式,先加载标签再加载样式,导致网页加载闪屏问题,此样式不建议使用

### 内部样式
用于单个页面

### 行内样式
用于本地调试

### 外部样式
主要使用

### 优先级
外部样式 = 内部样式 (下面的样式覆盖上面的样式)
行内元素 优先级最高

## 常用css3样式

### 圆角属性
```
四个角
border-radius:10px;

左上右下,右上左下
border-radius:10px 20px;

左上,右上坐下,右下
border-radius:10px 20px 30px;

左上,右上,右下,左下
border-radius:10px 20px 30px 40px;

右上角
border-top-right-radius:20px;

圆形
border-radius:50%;
```
### 盒子阴影
```
水平偏移 竖直偏移 羽化半径 阴影大小 阴影颜色 内部阴影
box-shadow:0px 0px 10px 20px #368 inset;
```
### 文本阴影
```
文本阴影:水平偏移 垂直偏移 模糊的距离 阴影颜色
文本阴影可以包含多个值,用逗号隔开	
text-shadow:5px 5px 10px red
```
## 浮动

**定义:**使元素脱离文档流,按照指定方向发生移动,遇到父级边界或者相邻的浮动元素停了下来

**文档流 定义:**文档中可显示对象在排列时所占用的位置/空间(在页面中占位置),元素在不添加css样式时在浏览器上遵循最基本的排列规则时所展现出来的样子

**脱离文档流:**在页面中不占位置

### 浮动的几种情况
- 任何类型的元素都可以浮动
- 浮动的元素默认由内容撑开宽度和高度(父级和子级都浮动,不设置父级的宽高,父级会被子级的宽高撑开)
- 浮动的元素漂浮在空中,可能会挡住html中后面的元素(后面的元素向上排列,被浮动的元素挡住)
- 如果浮动元素的高度不同.那么当它们向下移动时可能被其他浮动元素卡主
- 父级宽度不够的时候,浮动元素会掉下来,掉下来的元素会继续执行浮动
- 创建浮动框可以使文本围绕(后面的盒子向上移动,盒子中的文字围绕浮动元素)
 
### 浮动元素和inline-block的对比
- 都支持横排显示
- 都支持高度和宽度
- 都是默认内容撑开高度和宽度
- 都支持margin,但是都不支持margin auto
- float脱离文档流,inline-block不脱离
- 浮动提升半层层级,inline-block会解析空格

### 清除浮动
**原因:**如果父级未设置高度,浮动会导致父元素的塌陷,所以要清除浮动.浮动元素不能清除浮动
1. 子级方法
    - 子级(浮动元素的最后添加空标签(需是块级元素),然后在空标签添加样式clear:both;)
2. 父级方法
    - 问题:扩展性不好,一般高度不写死
    增加高度
    - 问题:解析空格,不支持margin auto
    display:inline-block;
    - 问题:需要配合宽度使用
    overflow:hidden;
    - 问题:需要配合宽度使用
    after{content:'',display:block;clear:both}

## 最小和最大宽度
```
max-width:100px;
min-width:100px;
```


## 定位
### 相对定位
```
position:relative;
```
1. 相对于没有定位之前的位置**(相对于原本的位置)进行位移**,元素保留其未定位之前的形状,它原本所占的空间保留

2. 可以通过left,top,right,bottom或者px百分比(**百分比参数是相对于父级,前提是父级必须有高度或者宽度**)规定位置

3. **移动前的位置 不脱离文档流**

4. **不影响元素本身的特性**,块级还是块级,行内还是行内,如果没有给定位值,那么元素对没有影响

5. **支持margin auto**

### 绝对定位
```
position:absolute;
```
1. 相对于最近的已经定位的父元素进行定位(父元素可以是相对定位,也可以是绝对定位,一般遵循父相子绝)(例如全部使用绝对定位,只要最顶级的父级元素一移动,整个界面都会变)

2. **如果没有设置定位值.对元素没有影响**,不会去寻找已定位的父元素进行定位

3. 可以通过left,top,right,bottom或者px百分比(相对于父级)规定位置

4. **完全脱离文档流**(浮动提升半层,文字围绕.但是定位提升一层,文字被覆盖)

5. **行内元素绝对定位后支持宽高**

6. **块级元素绝对定位后内容撑开宽高**

7. 如果父级没有定位,相对于已经定位的祖先元素(如果祖先元素没有定位,则相对于body)

8. **不支持margin auto**

### 使用定位和其他的方式使盒子居中
1. 使用定位
    > top:50%;left:50%;margin-top:-盒子高度的一半;margin-left:-盒子宽度的一半;
2. 使用定位
    > top:0px;left:0px;right:0px;bottom:0px;margin:auto;
3. 使用vertical-align
	1. **将文字和图片完全上下居中**,添加vertical-align:center到图片和文字标签中
	2. **将盒子绝对居中**,向父级添加text-align:center和line-height,向自己添加vertical-align:middle;
4. [多种水平垂直居中的方法](https://www.jianshu.com/p/868389ddf199)

### 多行文字居中
1. **父级元素**(块级元素)设置line-height为父级元素的高度
2. **子元素**(文本所在)设置以下属性
```
line-height:14px;
vertical-align:middle;
display:inline-block;
```

### 固定定位
```
position:fixed;
```
相对于浏览器窗口定位,与绝对定位特性一致

### 层级
```
z-index:
```
1. 改变元素的层级:**只对已经定位的元素有效,只能跟同级元素对比**,不能父子对比,默认值为0

## vertical-align
1. [w3c vertical-align属性](http://www.w3school.com.cn/cssref/pr_pos_vertical-align.asp)
    - 定义**行内元素和行内块元素**的**基线**相对于该元素所在行的基线的垂直对齐方式
    - 只支持inline  inline-block 元素.Vertical-align主要用于图片和文字的对齐,**块级元素不适用(因为块级元素默认要换行)**
```
元素的顶端与一行中最高元素的顶端对齐
vertical-align:top;

此元素放置在父元素的中部
vertical-align:middle;

元素的底端与一行中最低元素的底端对齐
vertical-align:bottom;
```
以上值受line-height影响(例如:如果不设置line-height,文字可能就跑到顶部了,然后图片也跟着跑到了顶部)
```
元素(框)的顶端与父元素字体的顶端对齐
vertical-align:text-top;

元素(框)的底端与父元素字体的底端对齐
vertical-align:text-bottom;

默认 父元素放在元素的基线上
vertical-align:baseline;
```
以上的值不受line-height影响,受**父元素字体**的font-size的影响

## 鼠标样式
1. [CSS cursor 属性](http://www.w3school.com.cn/cssref/pr_class_cursor.asp)
2. 属性:auto,pointer,move,text,wait,help...
```
cursor:default;
cursor:url('cursor/Hello.cur'),pointer;
```

## 表单

1. 表单是一个包含表单元素的区域
```
<form action='' method='get' target='' name=''>
    <fieldset>
        <legend>个人资料</legend>
    </fieldset>
</form>
```

### form表单的属性(块级元素)
> action: 规定提交到后台的地址,可以写地址,也可以写.asp或者.php文件,是后台人员提供的

> method: 规定如何提交到后台

> get: 会直接在地址栏显示提交的表单数据,一般用逗号或者&隔开.适用条件:需要对传输性能有要求

> post: 会隐藏提交的表单数据,分段传,先解码,解码之后由服务器决定如何传输数据.适用条件:对安全性有要求

> target='' 提交表单时规定如何处打开

> name: 名字

> fieldset: 将表单内相关元素分组

> legend: 标签为fieldset元素定义标题
```
<input type='' name='' value='' placeholder='' id='' />
```
### input的属性(行内块元素)
> type=''
> text 文本输入框
```
用户名:<input type='text' name='text' value='' placeholder='请输入用户名' />
```

> password 密码输入框 
```
密码:<input type='password' name='password' value='' placeholder='请输入用户名' />
```

> radio 单选按钮 
```
性别:<input type='radio' name='sex' value='man' id='idman'/>
<label for='idman'>男</label>
<input type='radio' name='sex' value='woman' id='idwoman' />
<label for='idwoman'>女</label>
```
name值需相同,value值应不相同,id与for对应

> checkbox 复选框 
```
<input type='checkbox' id='work' />
<label for='work'>爱好一:写作业</label>
<input type='checkbox'/>爱好二:敲代码
<input type='checkbox'/>爱好三:吃饭睡觉
id与for对应
```

> submit 提交 
`<input type='submit' value='点击确定'>`

> reset 重置
`<input type='reset' value='点击以清空'>`

>  button 普通按钮
一般用于启动js脚本`
`<input type='button' value='点击我启动js'>`


> hidden 隐藏文本域(不需要用户看到但是需要执行的,在页面中不占据位置);
`<input type='hidden' value='' name='' >`
可用于隐藏后台上传参数`

> file 上传按钮
`<input tyle='file'>`

> textarea 文本域
```
<textarea rows='' cols=''>
	文本域的文本
</textarea>
```
1. rows cols规定行数和列数
2. 禁止拖动的样式属性:{resize:none;resize:both;resize:vertical;resize:horizontal;}`

> select/option 下拉选框
```
出生年月:
<select size='3'>
	<option>1990</option>
	<option>1991</option>
	<option>1992</option>
	<option selected='selected'>1993</option>
</select>
```
1. selected 默认显示
2. size='3' 规定显示3项

> color 调色板

> 改变`placeholder`颜色
```
input::-webkit-input-placeholder{
    color: red;
}
```

### input的其他通用属性
>name

>value

>id

>checked

>disabled

>outline

>**label的属性**

>for

## 表格
```
<table border='1'>
	<thead>
		<tr>
			<th>这是th表头</th>
		</tr>
		<tr>
			<td>姓名</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>李逍遥</td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<td>这是tfoot信息</td>
		</tr>
	</tfoot>
</table>
```
### 表格的样式
1. 合并单元格
    - 合并左右单元格(跨列)
        - `colspan=''`

    - 合并上下单元格(跨行)
        - `rowspan=''`

2. 表格的样式
    - 指定单元格边界之间的水平与垂直间距
        - `border-spacing:X Y;`


    - 相邻边被合并(使用此参数后第一个参数无效,使用此参数后table设置padding也无效)
        - `border-collapse:collapse;`

    - 边框独立
        - `border-collapse:separate;`	

    - 重置表格默认样式
        - `table{border-collapse:collapse;}`
        - `table th,table td{padding:0;}`

### 表格的性质
- 单元格默认平分表格table的宽度
- 当table有宽度,但是td没有宽度时,单元格的宽度会被转换成百分比
- 当td有宽度时,单元格的宽度会根据实际的宽度比例来换算
- 表格的每一列都必须都宽度(宽度变成0的时候表格会被内容撑开)
- th的内容默认左右居中并加粗
- td的内容默认上下居中并左对齐
- **td,th没有margin属性**
- 表格的宽度由table决定
- 表格的同一行/列会继承最大值
- 单元格里面可以放任何元素(div,img等)
- 表格是一行一行加载的

## 框架
### 内联框架框架的基本属性
- 框架在seo搜索中不会被抓取,并且加载效率也不高
- 内联框架iframe元素类型是inline-block
```
<iframe src='' width='' height=''>
</iframe>
```
#### 内联框架的内部样式
- 规定是否显示框架周围的边框
    - `frameborder:none/1;`
- 规定是否在框架中显示滚动条
    - `scrolliing:yes/no;`
- 规定框架的名称
    - `name:'';`


### 框架集frameset的基本属性
- 框架在seo搜索中不会被抓取,并且加载效率也不高
- 与body同级,不能与body一起出现
- 不支持内部样式
```
<frameset rows='200px,300px'>
    <frame src='http://juejin.im' />
    <frame src='http://juejin.im' />
</frameset>
```
### 框架集frameset的属性
- 上下布局(参数数量与frame数一致)
    - `rows='%/px/*'`
- 左右布局(参数数量与frame数一致) 
    - `cols='%/px/*'`
- 整体设置子框架是否可调整范围
    - `noresize='noresize'`
- 整体设置边框的大小
    - `frameborder=''`
- 设置边框的颜色
    - `borderclor=''`
- frameset可以包含frameset

### 导航框架的设计
```
<frameset rows='20%,*'>
    <frame src='' />
    <frameset cols='20%,*'>
        <frame src='left-bottom.html' />
        <frame src='' name='A' />
    </frameset>
</frameset>

left-bottom.html
<a href='right-bottom.html#last' target='A'>
    我是title中的菜单
</a>

right-bottom.html
<a href='' id='last'>
    我是body中的a标签
</a>
```

## 样式的继承

### inherit
```
a{color:inherit;}
```
## 网站图标

### 引入网站图标icon
```
<link rel='shrotcut icon' type='images/x-icon' href='' />
```


## h5简介
1. 目的: 为了在移动设备上支持多媒体

### 新特性
1. 语义特性:HTML5赋予网页更好的意义和结构
2. 本地存储特性:基于HTML5开发的网页APP拥有更短的启动时间,更快的联网速度,这些全得得益于HTML APP Cache,以及本地存储功能
3. 设备兼容特性:HTML5为网页应用开发者们提供了更多功能上的优化选择,带来了更多体验功能的有时.HTML5提供了前所未有的数据与应用接入与开放接口.使外部应用可以直接与浏览器内部的数据直接相连,例如视频影音可以直接与microphones以及摄像头相连
4. 连接特性:HTML5拥有更有效的服务器推送技术,Server-Sent Event和WebSockets就是其中两个特性,这两个特性能够帮助我们实现服务器将数据推送到客户端的功能
5. 网页多媒体特性:支持网页端的Audio,Video等多媒体功能,与网站自带的APPS,摄像头,影音功能相得益彰
6. 三维 图形以及特效特性:基于SVG,Canvas,WebGL以及CSS3的3D功能
7. 性能与集成特性:HTML5通过XMLHttpRequest2等技术,解决以前的跨域等问题
8. CSS3特性:在不牺牲性能和语义结构的前提下,CSS3中提供了更多的风格和更强的效果


### 浏览器兼容参数
1. `-webkit-` chrome浏览器
2. `-moz-` 火狐
3. `-o-` 欧朋
4. `-ms-` IE
5. [兼容性查询网站](http://caniuse.com/)


### H5新增结构标签
```
定义页面或区域的头部 块级元素
<header></header>

定义导航链接的部分 块级元素
<nav></nav>

定义页面中一篇文章 块级元素
<article></article>

定义文档中独立的区域(看成div) 比如章节,页眉,页脚或文档中的其他部分
<section></section>

定义标题标签的组合
<hgroup>
    <h2></h2>
    <h3></h3>
</hgroup>

定义独立的流内容(图像,图表,照片,代码等等),可以对元素进行组合
<figure>
    <figcaption>这是一张图片</figcaption>
    <img src="" alt="">
</figure>

定义侧边栏,广告,nav元素组
<aside></aside>

底部
<footer></footer>

定义带有记号的文本,用于突出显示 行内元素
<mark></mark>

ruby:注释标签,标记定义 注释或音标 rt:拼音 rp:备用 行内元素
<ruby>槑
    <rt>mei 
        <rp>mei
        </rp> 
    </rt>
</ruby>

尺度(电池电量) min max规定范围, low high 规定显示绿色的范围20-90 行内元素
<meter min='0' max='100' value='50' low='20' high='90'></meter>

进度条 配合js使用 显示任务的进度或者进程
<progress min='0' max='100' value='60'></progress>

描述文档的细节部分 可展开二级菜单 行内元素
<details>
    <summary></summary>
    <p></p>
</details>
```
### IE低版本兼容(H5不兼容IE8及以下)
1. 方法1
    - 给元素添加`display:block;`
    - 引入JS
```
<script type='text/Javascript'>
    document.createElement('header')
    document.createElement('nav')
    document.createElement('article')
</script>
```


2. 方法2
    - 给元素添加`display:block;`
    - head中添加条件注释语句
```
<!--[if lt IE 9]> <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script> <![endif]-->
```


## HTML5新增颜色
### HSL
- H:色调 取值0-360
- 0(360):红色;60:黄色;120:绿色;180:青色;240:蓝色;300:洋红;
- S:饱和度 取值 0-100%(灰色-纯色)
- L:明度 取值0-100%(黑色-白色)
```
hsla(360,100%,50%,0.5)
```
### 线性渐变色
- 原理:通过背景图片的方式,所以支持背景图片(background-image:)的样式,它是一张图片而不是颜色
```
位置:从左到右to right;在90度的位置:90deg
linear-gradient(to right,red 200px(40%),blue,orange);
```
### 径向渐变色
```
位置:与线性渐变色相同
-webkit-radial-gradient(center,red,blue)
```
**IE低版本兼容**
```
放在样式中来兼容

filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffff',endColorstr='#ff0000',GradientType='1');
```

## 倒影(chrome)
```
第一个值:倒影的方向 above;below;left;right
第二个值:倒影的间隔 可以为负值
第三个值:倒影的渐变(例如linear-gradient:)
-webkit-box-reflect: below 10px linear-gradient(to right,red,blue)
```
## mask遮罩(chrome)
```
在图片上遮盖上mask里的图片
-webkit-mask-image:url('apple.png');
-webkit-mask-image-repeat: no-repeat;
```

## 过渡
```
可以在不使用flash动画或js的情况下,当元素从一种样式变换为另一种样式时为元素添加效果
允许css属性在一段时间内平滑的过渡
```
### 单样式和复合写法
```
规定为谁添加过渡效果(display不支持过渡)
transition-property:all(默认);

规定过渡所花费的时间(s/ms)
transition-duration:

规定过渡效果延迟的时间(s/ms)
transition-delay:

规定过渡的速度曲线
transition-timing-function:
linear 匀速
ease 慢快慢(默认)
ease-in 匀加速
ease-out 匀减速
ease-in-out 快慢快
cubic-bezier(n,n,n,n) 


复合属性(多个值用逗号隔开)
transition:width 1s 2s,background .1s .2s;
transition: all .5s;
```
[贝赛尔曲线](http://cubic-bezier.com/#.29)

### 过渡的特点
1. 优点
    - 简单易用
2. 缺点
    - 需要事件触发
    - 过渡只会执行一次,每次需要重新触发
    - 只有开始和结束两个状态
    - 一条属性只能定义一个过渡

## 动画
### 单样式和复合写法
```
规定动画的名称
animation-name:move;

规定动画持续时间
animation-duration:

规定动画延迟时间
animation-delay:

运动曲线
animation-timing-function:

规定动画执行的次数
animation-iteration-count:infinite;数字;

规定动画执行的方向
animation-direction:normal(默认);alternate(动画轮流反向播放);

规定动画执行结束后停在什么状态(初始值或者结束值)(不能和执行方向同时存在)
animation-fill-mode:backwards(首帧);forwards(尾帧);both(轮流)

规定动画的状态
animation-play-state:running(默认);paused

绑定动画(可以只有to)
@keyframes move{
    from{width:100px;}
    to{width:200px;}
}
@keyframes move{
    0%{width:200px;}
    100%{width:300px;}
}

复合属性
animation:move 1s 0,2s linear infinite alternate running;

```

##变换
```
允许对元素进行旋转,缩放,移动或倾斜

规定旋转的角度
deg;turn;rad;grad
transform:rotate(120deg)

规定基点(写在元素中)
transform-origin:left top;

规定放大的倍数
transform:scale(1.2);

规定位移(只写一个值代表x方向)
transform:translate(100px,100px);
transform:translateX(200px);
transform:translateY(200px);
transform:translateZ(200px);

规定倾斜
transform:skew(50deg,60deg)
transform:skewX(10deg)
transform:skewY(10deg)

复合属性
transform:rotate(200deg) scale(.5)
```
## 特殊属性
### 允许调整大小 resize
```
水平方向
resize:horizontal;

竖直方向
resize:vertical;

水平和竖直方向
resize:both;

在元素中添加ovf(原因:overflow属性会重新检测盒子中的内容与盒子的大小)
overflow:hidden;
```
### box-sizing
#### content-box
#### border-box
#### 区别
```
.test {
  box-sizing: content-box;
  border: 5px solid #f00;
  padding:5px;
  width: 100px;
  height: 100px;
}
```
- **content-box**的计算公式会把宽高的定义指向 content,border和 padding 另外计算,也就是说`content + padding + border = 120px(盒子实际大小)`
- **border-box**的计算公式是总的大小涵盖这三者, content 会缩小,来让给另外两者`content(80px) + padding(5*2px) + border(5*2px) = 100px`

### 计算
```
calc()
width:calc( 100% - 500px );
```
## 弹性盒模型
弹性盒模型就是让我们的实现响应式布局更加优雅
### 基础概念
- 任何一个容器都可以指定为flex布局
- 行内元素也可以使用flex布局
- 在不同浏览器中需要在前面加上兼容性前缀
- 设为flex布局以后,子元素的float,clear和vertical-align属性将失效
### 容器属性设置(父级)
将以下属性设置在**父级容器**中
- `flex-direction`
- `flex-wrap`
- `flex-flow`
- `justify-content`
- `align-items`
- `align-content`
#### flex-direction属性
定义主轴的方向(即项目的排列方向)
```
.box {
flex-direction: row | row-reverse | column | column-reverse;
}
```
|-|-|
|-|-|
|row(默认值)|主轴为水平方向，起点在左端|
|row-reverse|主轴为水平方向，起点在右端|
|column|主轴为垂直方向，起点在上沿|
|column-reverse|主轴为垂直方向，起点在下沿|


#### flex-wrap属性
默认情况下,项目都排在一条线(又称"轴线")上
flex-wrap属性定义,如果一条轴线排不下,如何换行
```
.box{
  flex-wrap: nowrap | wrap | wrap-reverse;
}
```
- nowrap(默认)不换行

- wrap 换行,第一行在上方

- wrap-reverse 换行,第一行在下方


#### flex-flow属性
flex-flow属性是flex-direction属性和flex-wrap属性的简写形式,默认值为row nowrap

#### justify-content属性
定义了项目在主轴上的对齐方式
```
.box {
  justify-content: flex-start | flex-end | center | space-between | space-around;
}
```
|-|-|
|-|-|
|flex-start(默认值)|主轴方向起点对齐|
|flex-end|主轴方向终点对齐|
|center|主轴方向居中对齐|
|space-between|主轴方向两端对齐,项目之间的间隔都相等|
|space-around|主轴方向平均分布|

#### align-items属性
定义项目在交叉轴上如何对齐
```
.box {
  align-items: flex-start | flex-end | center | baseline | stretch;
}
```

|-|-|
|-|-|
|flex-start(默认值)|交叉轴方向起点对齐|
|flex-end|交叉轴方向终点对齐|
|center|交叉轴方向居中对齐|
|baseline|项目的第一行文字的基线对齐|
|stretch(默认值)|如果项目未设置高度或设置为auto,将占满整个容器的高度|
![Alt text](./1513744202626.png)

#### align-content属性
定义多行项目在交叉轴上如何对齐,`align-items`失效
```
.box {
  align-content: flex-start | flex-end | center | space-between | space-around | stretch;
}
```

|-|-|
|-|-|
|flex-start(默认值)|交叉轴方向起点对齐|
|flex-end|交叉轴方向终点对齐|
|center|交叉轴方向居中对齐|
|space-between|交叉轴方向两端对齐|
|space-around|交叉轴方向平均分布|
|stretch(默认值)|轴线占满交叉轴|


### 项目的属性(子级)
以下属性设置在项目**(子级)**中
- `order`
- `flex-grow`
- `flex-shrink`
- `flex-basis`
- `flex`
- `align-self`

#### order属性
定义项目的排列顺序,数值越小,排列越靠前,默认为0
```
.item {
  order: <integer>;
}
```
#### flex-grow属性
定义项目放大的比例(默认为0,不放大),如果存在剩余空间则参考放大比例进行放大
```
.item {
  flex-grow: <number>; /* default 0 */
}
```

>Ps:如果所有项目的flex-grow属性都为1，则它们将等分剩余空间（如果有的话）。如果一个项目的flex-grow属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。
#### flex-shrink属性
定义项目缩小的比例,默认为1,(为0时不缩小)
```
.item {
  flex-shrink: <number>; /* default 1 */
}
```

- 如果所有项目的flex-shrink属性都为1，当空间不足时，都将等比例缩小。
- 如果一个项目的flex-shrink属性为0，其他项目都为1，则空间不足时，前者不缩小。

#### flex-basis属性
定义了项目的初始宽度,默认为auto(项目原本的大小)
```
.item {
  flex-basis: <length> | auto; /* default auto */
}
```

- 设置为auto时取项目原本的宽度
- 此属性设置项目的初始宽度(覆盖width)

#### flex属性
此属性是`flex-grow`,`flex-shrink`,`flex-basis`的简写,默认值为(0 1 auto)
```
.item {
  flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
}
```

- `flex:auto;`内容撑开之后剩下的空间几个盒子平分 (1 1 auto)
- `flex:none;`内容的宽度撑开 (0 0 auto)

-补充:
    - grow和shrink是一对双胞胎，grow表示伸张因子，shrink表示是收缩因子
    - grow在flex容器下的子元素的宽度和比容器和小的时候起作用
    - grow定义了子元素的宽度增长因子，容器中除去子元素之和剩下的宽度会按照各个子元素的gorw值进行平分加大各个子元素上
    - shrink则是在宽度和比容器宽度大时候，才有用

#### align-self属性
1. 定义单个项目与其他项目不一样的对齐方式,可覆盖`align-items`属性

2. 默认值为auto，表示继承父元素的align-items属性，如果没有父元素，则等同于stretch
```
.item {
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```



## 响应式布局
### 媒体类型
- all 所有媒体
- screen 彩屏设备
- print 用于打印机和打印预览
### 关键词
- and
- not
### 媒体特性
- `(width:600px)` 宽
- `(max-width:800px)` 宽度<=800px
- `(min-width:500px)` 宽度>=500px
- `(orientation:portrait)` 竖屏
- `(orientation:landscape)` 横屏
### 行内样式
`@media screen and (max-width:320px){}`
`@media print and (min-width:300px) and (max-width:400px){}`

### 外部样式
`<link rel='stylesheet' type='text/css' media='screen and (min-width:500px)' href='a.css'>`

### 响应式布局特点
- 优点: 面对不同分辨率设备，灵活性强，能够快捷地解决设备显示适应问题
- 缺点: 兼容各种设备时所需工作量大、效率低下、代码累赘，会隐藏无用的元素，加载时间延长，其实这是一种折中性质的设计解决方案，由于多方面元素影响而达不到最佳效果，在一定程度上改变了网站原有的布局结构，会出现用户混淆的情况


## 移动端视窗viewport
### meta引入
`<meta name='viewport' content='width=device-width,initial-scale=1.0,maxinum-scale=1.0,user-scalable=no' />`

- 参数
    - **width**:控制viewport的大小,可以指定一个正整数(600px)或者特殊的值(device-widths设备的宽度)
    - **height**:设置viewport高度,一般设置了高度,会自动解析出高度,可以不同设置
    - **inital-scale**:初始缩放比例,也即是当前页面第一次load的时候的缩放比例,为一个数字,可以带小数
    - **maximum-scale:**允许用户缩放到的最大比例
    - **minimum-scale:** 允许用户缩放到的最小比例
    - **user-scalable**:用户是否可以手动缩放
### 移动端1px被渲染成2px
1. 局部处理
	1. `initial-scale`设置为1,利用`transform: scale(0.5)`
2. 全局处理
	2. `initial-scale`设置为0.5

### 文档兼容模式声明
`<meta http-equiv="X-UA-Compatible" content="IE=edge">`

## rem适配
```
<script>
    var html = document.querySelector('html');
    changeRem();
    window.addEventListener('resize',changeRem);
    function changeRem() {
        var width = html.getBoundingClientRect().width;
        //console.log( width );
        html.style.fontSize = width/10+ 'px';
    }
</script>
```