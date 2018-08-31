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