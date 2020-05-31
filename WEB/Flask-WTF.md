# Flask WTF

`Flask-WTF` 是简化了 `WTForms` 操作的一个第三方库，`WTForms` 表单的两个主要功能是验证用户提交数据的合法性以及渲染模板。当然还包括一些其它的功能：**CSRF保护**，文件上传等。

安装 Flask-WTF 默认也会安装 WTForms，因此使用以下命令来安装 Flask-WTF

`pip install flask-wtf`

# 渲染表单

**`forms.py`**

```python
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField

class Login_form(FLaskForm):
    username = StringField("账号")
    password = PasswordField("密码")
```

**`views.py`**

```python
from form import Login_form

@app.route("/login/")
def login():
    login_form = Login_form()
    return render_template("login.html",form=login_form)
```

**`login.html`**

```html
<form action="" method="POST">
    <p>
        {{ form.username.label }}: {{ form.username }}
    </p>
    <p>
        {{ form.password.label }}: {{ form.password }}
    </p>
    <input type="submit">
</form>
```

此时当我们尝试运行时，你会发现报错：

`RuntimeError: A secret key is required to use CSRF.`

WTF 在处理表单时有一个机制是为了方式 CSRF 攻击的，详细说明请看：[浅谈CSRF攻击方式](https://www.cnblogs.com/hyddd/archive/2009/04/09/1432744.html)

这个机制其实就是在表单提交的过程中加一个随机字符串，只有当客户端和服务端的随机字符串一致，后端才执行，看似简单的一个机制却有效防止了 CSRF 攻击

所以，我们需要在配置中定义一个 随机字符串

```python
app.config['SRCRET_KEY'] = "hard to guess string"
```

此时再访问路由，就可以看到我们的界面了！

**表单常用参数**

|标准表单字段|描述|
|:---|:---|
|TextField |表示 `<input type ='text'>` HTML表单元素|
|PasswordField| 表示 `<input type ='password'>` HTML表单元素|
|SubmitField| 表示 `<input type ='submit'>` 表单元素|

# 后端校验

以下列表展示了部分验证器

|验证器类|描述|
|:---|:---|
|Email| 验证上传的数据是否为邮箱|
|Length |长度限制，有min和max两个值进行限制|
|EqualTo| 验证上传的数据是否和另外一个字段相等，常用的就是密码和确认密码|
|Regexp|自定义正则表达式|

**`forms.py`**

```python
class Login_form(FlaskForm):
    username = StringField(
        "账号",
        # 校验规则
        validators=[
            # message 校验未通过时的提示信息
            validators.Email(message="请输入邮箱")
        ])
    password = PasswordField(
        "密码",
        validators=[
            validators.Length(max=8,min=6,message="填写6到8位的内容"),
            validators.EqualTo("repassword",message="两次密码不一致")
        ])
    repassword = PasswordField("重复密码")
```

**`views.py`**

```python
@app.route("/login/",methods=["POST","GET"])
def login():
    form = Login_form()
    if request.method == "POST":
        # 校验提交的数据
        if form.validate():
            message = "ok"
            print(form.data)
        else:
            print(form.errors)
            message = form.errors
    return render_template("login.html",**locals())
```

**`login.html`**

```python
<form action="" method="POST">
    # 如果不添加，会导致 error csrf_token: The CSRF token is missing
    {{ form.csrf_token }}
    <p>
        <input type="text" name="username">
    </p>
    <p>
        <input type="password" name="password">
    </p>
    <p>
        <input type="password" name="repassword">
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
</form>
<p style="color:red">{{ message }}</p>
```

这样一个简单的后端校验就完成了，但是 内置的验证器 并不能很好的完成我们的验证需求，因此我们还可以使用 自定义验证器

**自定义验证器**

**(1) 在表单类中创建验证函数**

```python
from wtforms import ValidationError

# 自定义校验规则
class Login_form(FlaskForm):

    def validate_username(self,field):
        # 敏感字符列表
        data_list = ["admin","x"]
        # field.data 当前标签的数据
        for i in data_list:
            if i in filed.data:
                raise ValidationError("用户名包含敏感字符")

    username = StringField(
        "账号",
        # 校验规则
        validators=[
            # message 校验未通过时的提示信息
            validators.Email(message="请输入邮箱"),
            # 使用自定义规则
            validate_username
        ])
```

**(2) 自定义类创建验证函数**

```python
class My_valid():
    def __init__(self,message=None):
        self.message = message
    def __call__(self,form,filed):
        # 敏感字符列表
        data_list = ["admin","x"]
        # field.data 当前标签的数据
        for i in data_list:
            if i in filed.data:
                raise ValidationError(self.message)

# 使用验证器
My_valid(message="用户名包含敏感字符")
```

# CSRF

**开启保护**

(1) 导入模块

```python
from flask_wtf import CSRFProtect
csrf = CSRFProtect()
# 惰性加载
csrf.init_app(app)
```

(2) 设置一个应用令牌

```python
app.config['SECRET_KEY'] = 'a string'
# 或csrf专用令牌
app.config['WTF_CSRF_SECRET_KEY'] = 'a string'
```

(3) 表单中添加 token

```python
{{ form.csrf_token }}
# 或者
{{ form.hidden_tag() }}
# 或者
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

**关闭保护**

自然，有的表单中我们不需要保护。那么，有如下三种方法去除保护：

1. 全局禁用: `app.config` 中设置 `WTF_CSRF_ENABLED = False`
2. 单个表单中禁用: 生成表单时加入参数 `form = Form(csrf_enabled=False)`
3. 单个视图中禁用: 使用 `@csrf.exempt` 装饰不需要验证的视图

# more

[http://www.pythondoc.com/flask-wtf/index.html](http://www.pythondoc.com/flask-wtf/index.html)









