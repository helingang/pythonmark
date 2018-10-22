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


## csrf问题
- 在form表单处添加`{% csrf_token %}`
- 屏蔽中间件`'django.middleware.csrf.CsrfViewMiddleware'`,以不验证csrf
- 添加装饰器
    ```
    from django.views.decorators.csrf import csrf_exempt, csrf_protect
    # csrf_exempt : 不验证csrf
    # csrf_protect : 验证csrf
    from django.utils.decorators import method_decorator


    # @csrf_exempt
    # def login(request):
    #     return render(request, 'account/login.html')
    #
    #
    # def register(request):
    #     return render(request, 'account/register.html')



    # 类视图
    from django.views import View

    # django 推荐使用类视图
    @method_decorator([csrf_exempt], name='dispatch') # 此视图不验证csrf
    class LoginView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'account/login.html')

        def post(self, request, *args, **kwargs):
            form = LoginForm(request.POST)
            if form.is_valid():
                telephone = form.cleaned_data.get('telephone', None)
                password = form.cleaned_data.get('password', None)
                print(telephone, password)
                return HttpResponse('通过')
            else:
                return HttpResponse('不通过')


    class registerView(View):
        def get(self, request):
            return render(request, 'account/register.html')

        def post(self):
            pass

    ```

## 登录验证
- js
    ```
    $(function () {
        let $loginBtn = $('.login-btn');
        let $telephone = $('input[name=telephone]');
        let $password = $('input[name=password]');
        let $remember = $('input[name=remember]');

        function loginFn() {
            // 前端做验证
            telVal = $telephone.val();
            pwdVal = $password.val();
            if (telVal && pwdVal) {
                $.ajax({
                    url: '/account/login/',
                    method: 'post',
                    data: {
                        'telephone': telVal,
                        'password': pwdVal
                    },
                    dataType: 'json',
                    success: res => {
                        console.log('success', res);
                        if (res['code'] === 1) {
                            message.showSuccess(res['msg'])
                        } else {
                            message.showError(res['msg'])
                        }
                    },
                    error: err => {
                        console.log('error', err);
                    }
                })
            } else {
                window.message.showError('电话或密码不能为空')
            }
        }

        $loginBtn.click(loginFn);

        $(document).ready(
            function () {
                $(document).keydown(function (event) {
                    if (event.keyCode === 13) {
                        loginFn()
                    }
                })
            }
        );


    });

    ```

- views
    ```
    # 类视图
    from django.views import View

    # django 推荐使用类视图
    @method_decorator([csrf_exempt], name='dispatch') # 此视图不验证csrf
    class LoginView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'account/login.html')

        def post(self, request, *args, **kwargs):
            form = LoginForm(request.POST)
            if form.is_valid():
                telephone = form.cleaned_data.get('telephone', None)
                password = form.cleaned_data.get('password', None)
                print(telephone, password)
                user = authenticate(username=telephone, password=password)
                if user:
                    login(request, user)
                    return JsonResponse({
                        'code': 1,
                        'msg': '登录成功'
                    })
                else:
                    return JsonResponse({
                        'code': 0,
                        'msg': '手机号或密码错误'
                    })
            else:
                print(form.errors)
                return JsonResponse({
                    'code': 0,
                    'msg': '手机号或密码校验失败'
                })

    ```