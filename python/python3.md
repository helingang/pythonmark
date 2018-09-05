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

- 常用标签
    - `if`标签
        - 语句`if/elif/else/endif/ifequal/ifnotequal`,可以使用`and/or/not/in/<`等运算符
        - 例子
            ```
            {% if name == 'py1' and l2.0 == 11 %}
                py1
            {% elif name == 'py12' or l2.0 == 10 %}
                py
            {% endif %}

            {% ifequal name 'py1' %}
                <br>
                满足ifequal
            {% endifequal %}

            {% ifnotequal name 'py2' %}
                <br>
                满足ifnotequal
            {% endifnotequal %}
            ```
    - `for`标签
        - 语句`for in`
        - `forloop.counter0`当前迭代的次数,下标从0开始(相反于revcounter0)
        - `forloop.counter`当前迭代的次数,下标从1开始(相反于revcounter)
        - `forloop.first`返回布尔值,第一次迭代返回True
        - `forloop.last`
        - `forloop.parentloop`表示上一层循环
        - 例子
            ```
            {% for i in l2 %}
                {% if forloop.counter0 > 0 %} <!-- 下标>0 -->
                    <br>
                    <a href="">{{ i }}</a>
                {% else %}
                    <br>
                    {{ i | add:5 }}
                {% endif %}
            {% endfor %}
            <br><br>
            {% for i in l2 %}
                {% if forloop.last %} <!-- 最后一次迭代 -->
                    <br>
                    <a href="">{{ i }}</a>
                {% else %}
                    <br>
                    {{ i | add:5 }}
                {% endif %}
            {% endfor %}

            {% for i in l2 %}
                {% for j in name %}
                    {% for k in test %}
                        <br>
                        外层i的值是: {{ forloop.parentloop.parentloop.counter0 }}
                        中层j的值是: {{ forloop.parentloop.counter0 }}
                        内层k的值是: {{ forloop.counter0 }}
                    {% endfor %}
                {% endfor %}
            {% endfor %}
            ```
    - `for in empty`
        - 例子
            ```
            {% for i in l1 %}
                    {{ i }}
                {% empty %}
                    empty
            {% endfor %}

            ```

    - `url`命令路径
        - 在`urls`中设置路由的名称`path('test5/<p1>', views.test5, name='path_test5')`
        - 在html文件中设置路径`<a href="{% url 'path_test5' name %}">进入test5视图</a>`

    - 在html中使用`with`缓存变量
        - 例子
            ```
            {% with name as n %}
                1111{{ n }}
                2222{{ name }}
            {% endwith %}
                3333{{ n }}
                4444{{ name }}
            ```
    
    - 关闭自动转义
        ```
        {{ html }}
        {{ html | safe }}
        {% autoescape off %}
            {{ html }}
        {% endautoescape %}
        ```

    - 注释(如果使用`<!-- -->`则查看源代码可以看到)
        ```
        {# 2 #}
        {% comment %}
            123
        {% endcomment %}
        ```

    - 继承与引用
        - 创建`base`页面
            ```
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{% block title %}base页面{% endblock %}</title>
            </head>
            <body>
                {% block content %}
                <h1>我是base页面</h1>
                {% endblock %}

                {% block content1 %}
                {% endblock %}
            </body>
            </html>
            ```
        - 创建继承和引用的页面
            - 注意
                1. 模板继承使用extends标签实现。通过使用block来给子模板开放接口
                2. extends必须是模板中的第一个出现的标签
                3. 子模板中的所有内容，必须出现在父模板定义好的block中，否则django将不会渲染
                4. 如果出现重复代码，就应该考虑使用模板
                5. 尽可能多的定义block，方便子模板实现更细的需求
                6. 如果在某个block中，要使用父模板的内容，使用block.super获取
            
            - 例子
                ```
                {% extends 'test_parent.html' %}

                {% block title %}
                    自定义的title内容
                {% endblock %}

                {% block content %}
                    通过super继承父类的内容: {{ block.super }}
                    <br>
                    自己创建的内容
                {% endblock %}


                {% block content1 %}
                    {% include 'test_incloud.html' %} {# 引用目标文件body中的内容 #}
                {% endblock %}
                ```
        - 设置静态文件
            - 创建静态文件
                - 在app中创建static文件夹
                - 或者在根目录创建static文件夹
            - 在`settings`中设置路径和注册
                ```
                STATIC_URL = '/static/'

                STATICFILES_DIRS = [
                    os.path.join(BASE_DIR, 'static')
                ]

                INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'book',
                ]
                ```
            - 在html文件中引用静态文件
                ```
                {% load static %}
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Title</title>
                    <link rel="stylesheet" href="{% static 'css/index2.css' %}">
                </head>
                <body>
                <img src="{% static 'images/14.png' %}" alt="123" width="" height="" title="321">
                </body>
                    <script src="{% static 'js/index.js' %}"></script>
                </html>
                ```