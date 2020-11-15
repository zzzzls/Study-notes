<!-- TOC -->

- [Form 表单类](#form-%E8%A1%A8%E5%8D%95%E7%B1%BB)
    - [创建表单页](#%E5%88%9B%E5%BB%BA%E8%A1%A8%E5%8D%95%E9%A1%B5)
    - [前端校验](#%E5%89%8D%E7%AB%AF%E6%A0%A1%E9%AA%8C)
    - [后端校验](#%E5%90%8E%E7%AB%AF%E6%A0%A1%E9%AA%8C)
        - [内置校验器](#%E5%86%85%E7%BD%AE%E6%A0%A1%E9%AA%8C%E5%99%A8)
        - [界面展示错误信息](#%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA%E9%94%99%E8%AF%AF%E4%BF%A1%E6%81%AF)
        - [自定义校验](#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%A0%A1%E9%AA%8C)
        - [自定义 Field]
- [参考](#%E5%8F%82%E8%80%83)

<!-- /TOC -->

# Form 表单类

Django 自带的 form 表单类，可以创建表单页，完成 前端校验 和 后端校验，类似 flask 中的 wtf 插件

## 创建表单页

(1) 创建 forms.py 
(2) 编写 form 表单

```python
from django import forms

class Myform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
```

(3) 视图中返回

```python
def form(request):
    from .forms import Myform
    myform = Myform()
    return render(request,"index.html",{"myform":myform})
```

(4) HTML 展示

```html
<form action="/login/" method="POST">
    {% csrf_token %}
    {{ myform.as_p }}
    <input type="submit" value="提交">
</form>
```

## 前端校验

```python
class Myform(forms.Form):
    username = forms.CharField(required=True,max_length=10, min_length=8)
```

## 后端校验

在验证某个字段的时候，可以传递一个 `validators` 用来指定校验器，完成对数据的校验，当然也可以通过 field 一些参数完成

如：验证数据的长度，可以通过属性 `max_length` 进行校验，也可以通过 `validators` 校验器完成

**`forms.py`**

```python
# 导入正则校验器
from django.core.validators improt RegexValidator
from django import forms

class Myform(forms.Form):
    password = CharField(
        # 校验密码最大长度
        max_length = 8,
        # 校验密码最小长度
        min_length = 6,
        # 指定 上边两个属性的错误信息
        error_msg = {
            "max_length":"长度不能超过8",
            "min_length":"长度不能低于6"
        },
        validators = [
            # 正则校验器，内部必须为数据，否则错误信息为 密码类型错误
            RegexValidator(r"^\d+$", "密码类型错误")
        ]
    )
```

**`views.py`**

```python
def login(request):
    # 如果为 get 请求，返回页面
    if request.method == "GET":
        return render(request, "index.html")
    # 如果为 post 请求，验证数据
    elif request.method == "POST":
        # 将 post 请求的数据 传递给 form类验证
        myform = Myform(request.POST)
        # 验证数据
        if myform.is_valid():
            # 通过
            print("valid success")
            # 校验之后的数据
            print(myform.cleaned_data)
        else:
            # 未通过
            print("valid error")
            # 校验失败的报错信息
            print(myform.errors.as_json())
    return HttpResponseRedirect("/index/")
```

### 内置校验器

|校验器|描述|
|:---|:---|
|RegexValidator|	正则表达式的验证|
|EmailValidator|	邮箱格式的校验器|
|MaxValueValidator|	最大值|
|MinValueValidator|	最小值|
|MinLengthValidator|	最小长度|
|MaxLengthValidator|	最大长度|

### 界面展示错误信息

```html
<form action="/login/" method="POST">
    {% csrf_token %}
    <p>账号: <input type="text" name="username"></p>
    <p>密码: <input type="password" name="password"></p>
    <span style="color:red;">{{ myform.password.errors }}</span>
    <input type="submit" value="提交">
</form>
```

### 自定义校验

example : 校验不能出现 敏感字

(1) 自定义校验类

```python
from django.core.exceptions import ValidationError

class Myvalid:
    def __call__(self, value):
        # value 为 form 表单传递的值
        if "sb" in value:
            raise ValidationError("不能包含敏感字")

# 使用
password = forms.CharField(
    validators = [
        Myvalid()
    ]
)
```

(2) 自定义校验函数

```python
def myvalid(value):
    if "root" in value:
        raise ValidationError("不能包含敏感字")

# 使用
password = forms.CharField(
    validators = [
        myvalid
    ]
)
```

### 自定义Field

表单的验证分为如下几个步骤，这些步骤通常在调用表单的 `is_valid()` 方法时执行



一般来说， 如果这些步骤中处理的数据存在问题，可以直接抛出 `ValidationError`，你可以自定义或者重写如下几个步骤

-   **to_python**

    Field 上的 `to_python()` 方法时每次校验的第一步。接收来自表单的原始值，强制将该值转换为指定的数据类型并返回

    

-   **validate**

    用于自定义校验规则，接收上一步中转换后的值，并在校验失败时返回 `ValidationError`，这个方法不返回任何东西，也不应该改变值



-   **clean**

    该方法返回校验过后干净的数据，并将其插入到 Form 的 `cleaned_data` 字典中

    由于在调用 `clean()` 的时候，字段的验证方法已经运行，所有你也可以访问 Form 的错误属性，它包含了所有通过校验各个字段而产生的错误

    >   任何由 `Form.clean()` 覆盖引发的错误都不会与任何特定的字段相关联，它们会进入一个特殊的字段 `__all__`，可以通过 `non_field_errors()` 方法来访问。如果你想将错误附加到 Form 的某个字段，你需要调用 `add_error()`



-   **clear_\<fieldname>**

    该方法会对指定属性进行特定的清理，与字段类型无关，其中 `<fieldname>` 应被替换为表单字段属性的名称。本方法不传递任何参数，你需要在 `self.cleaner_data` 中查找字段的值，并且记住，此时它将是一个 Python对象，而不是表单中提交的原始字符串，它已经经过了上面的校验

    这个方法的返回值会替换 `cleaned_data` 中的值，所以它必须是 `cleaned_data` 中字段的值



#### 示例

-   `to_python` & `validate`

    ```python
    # 创建一个自定义 Form Field , 验证输入是否包含逗号分隔的电子邮件地址的字符串
    from django import forms
    from django.core.exceptions import ValidationError

    class MultiEmailField(forms.Field):
        def to_python(self, value):
            """去除数据两侧的空白字符"""
            if not value:
                raise ValidationError('请输入邮箱地址')
            return value.strip()

        def validate(self, value):
            super().validate(value)
            if not '@' in value:
                raise ValidationError('错误的邮箱地址')
                
    class LoginForm(forms.Form):
        email = MultiEmailField()
    ```



-   `clean_<fieldname>` & `clean`

    ```python
    class LoginForm(forms.Form):
        username = forms.CharField(max_length=8)
        password = forms.CharField(max_length=8)
        r_password = forms.CharField(max_length=8)
        email = MultiEmailField()
        code = forms.CharField(max_length=6)
    
        # 局部钩子
        def clean_code(self):
            """校验验证码"""
            email = self.cleaned_data.get('email')
            # 获取用户输入的验证码
            user_verifyCode = self.cleaned_data.get('code')
            # 通过 邮箱 获取 redis 中存储的验证码
            verifyCode = cache.get(email)
            
            if verifyCode != user_verifyCode:
                raise ValidationError('验证码错误')
            else:
                return verifyCode
            
        # 全局钩子
        def clean(self):
            """校验两次输入的密码是否一致"""
        	password = self.cleaned_data.get("password")
            r_password = self.cleaned_data.get("r_password")
    
    
            if password == r_password:
                return self.cleaned_data
            else:
                raise ValidationError("请确认密码是否一致")
    ```

# 参考

[表单和字段验证 | Django 文档](https://docs.djangoproject.com/zh-hans/3.1/ref/forms/validation/)

[Django Form 组件|菜鸟教程](https://www.runoob.com/django/django-form-component.html)

[Django: 使用表单 | MDN](https://developer.mozilla.org/zh-CN/docs/learn/Server-side/Django/Forms)

[Django：forms组件](https://www.cnblogs.com/ZJiQi/p/9895728.html)
