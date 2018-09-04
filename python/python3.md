# Django
## 虚拟环境
- `workon`查看虚拟环境
- `mkvirtualenv -p /usr/bin/python3 name`在python3版本下创建虚拟环境
- `workon name`进入虚拟环境
- `deactivate`退出虚拟环境
- `rmvirtualenv name`删除虚拟环境


## 项目初始化
- `django-admin startproject name`在当前目录新建项目
- 目录
    - `manage.py`django的一个命令行工具,管理django项目
    - `__init__.py`空文件,告诉python这个目录是一个python包
    - `setting.py`配置文件,包含数据库信息,调试标志,静态文件等
    - `urls.py`Django项目的URL申明
    - `wsgi.py`部署时用到的

- `django-admin startapp name`创建app

## 基础知识
- path规则
    - `path('test/<xx>/',views.test)`
    - 转换器
        - `str`除了/的非空字符串
        - `int`正整数包含0
        - `slug`字符串包含字母数字横杠和下划线
        - `uuid`
    - 参数`xx`与视图中的形参必须一致
- re_path规则
    - `re_path('^hello/$',views.test5)`
    - `re_path('^hello/(?P<yy>[0-9]+)/',views.test6)`

- path中的参数需要在视图中接收(视图中可以使用`**kwargs`)

- `include`
    - 在主`urls`中设置`path('book/',include('book.urls'))`

- 重定向
    - 在path中设置路由的名称`path('xx', views.test, name='t1')`
    - 在视图中`return redirect(reverse('t1'))`

- 展示html
    1. 在根目录设置`templates`
        - 设置`settings`文件中的`TEMPLATES`的`DIRS`属性

    2. 或者在app目录中设置`templates`
        - 在`settings`中注册`INSTALLED_APPS`
        - 保证`settings`中`TEMPLATES`的`APP_DIRS`为`True`
    3. 在视图中`render(request, 'book/index.html')`

- 在视图中传递数据,并在html中展示
    - 传递数据
        ```
        def test1(request):
            return render(request, 'index_test.html',
                        context={
                            'name': 'Sam',
                        })
        ```
    - 展示数据,
    - 注意:函数默认执行并去返回值.过滤器(常用过滤器和时间过滤器)
        ```
        <h2>字典 {{ dict.name }} 今年 {{ dict.age }} 岁了</h2>
        <h2>字典 {{ dict.items }}</h2>
        <h2>函数 {{ fun }}</h2>
        <h2>列表 {{ list1.1 }}</h2>
        <h2>类的方法 {{ fsay }}</h2>
        <h2>元祖 {{ tp.2 }}</h2>

        <h1>{{ name | upper | title }}</h1>
        <h1>{{ num1 | add:num2 }}</h1>
        <h1>{{ dsadad | default:333 }}</h1>
        <h1>{{ list1 | first }}</h1>
        <h1>{{ name | join:dict.age }}</h1> <!-- 拼接 -->
        <h1>{{ list1 | length_is:1 }}</h1>
        <h1>{{ str | truncatechars:5 }}</h1> <!-- 字符串截断 -->
        <h1>{{ str | truncatewords:2 }}</h1> <!-- 单词截断 -->
        <h1>{{ html | truncatechars_html:4 }}</h1>
        <h1>{{ str | slice:'1:3' }}</h1> <!-- 切片 -->
        <h1>{{ html | striptags }}</h1>
        <h1>{{ html }}</h1>
        {{ html | safe }} <!-- 使字符串中的标签生效 -->
        <h1>{{ float | floatformat:2 }}</h1>
        <a href="/">123</a>
        <h1>{{ time }}</h1>
        <h1 id="a1">{{ time | date:'Y/m/d H:i:s' }}</h1>
        ```