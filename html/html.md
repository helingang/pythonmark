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