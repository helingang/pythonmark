# 项目1
## 环境
- `virtualenv --no-site-packages venv`
- `source venv/bin/activate`
- `deactivate`退出

## 初始化项目
- 注册`INSTALLED_APPS`
- `TEMPLATES`目录配置`DIRS`文件路径
- `DATABASES`配置数据库信息
- 设置语言和时区
- 配置静态文件地址`STATICFILES_DIRS`
- 设置`templates`模板的`extend`继承


## account的模型
```
class UserManager(BaseUserManager):

    # 创建用户
    def _create_user(self, username, telephone, password, **extra_fields):
        user = self.model(username=username, telephone=telephone, **extra_fields)
        # 也可以在参数中添加password: password=make_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, telephone=None, password=None, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False

        return self._create_user(username, telephone, password, **extra_fields)

    def create_superuser(self, username, telephone, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        print(extra_fields)

        return self._create_user(username, telephone, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    '''
    User
    '''
    telephone = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    # password = set_password()
    is_active = models.BooleanField(default=True) # 账户是否可用
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone' # 1
    REQUIRED_FIELDS = ['username', 'email'] # 2, 3
    # 4 password
    # createsuperuser的时候字段输入的顺序是 telephone, username, email, password
```

## 提示插件
- `sweetalert`
- `message.js`
