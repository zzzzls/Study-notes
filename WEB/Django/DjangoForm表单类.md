<!-- TOC -->

- [Form 表单类](#form-%E8%A1%A8%E5%8D%95%E7%B1%BB)
    - [创建表单页](#%E5%88%9B%E5%BB%BA%E8%A1%A8%E5%8D%95%E9%A1%B5)
    - [前端校验](#%E5%89%8D%E7%AB%AF%E6%A0%A1%E9%AA%8C)
    - [后端校验](#%E5%90%8E%E7%AB%AF%E6%A0%A1%E9%AA%8C)
        - [内置校验器](#%E5%86%85%E7%BD%AE%E6%A0%A1%E9%AA%8C%E5%99%A8)
        - [界面展示错误信息](#%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA%E9%94%99%E8%AF%AF%E4%BF%A1%E6%81%AF)
        - [自定义校验](#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%A0%A1%E9%AA%8C)
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

# 参考

[使用表单 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/2.2/topics/forms/)

[Django: 使用表单 | MDN](https://developer.mozilla.org/zh-CN/docs/learn/Server-side/Django/Forms)

[Django：forms组件](https://www.cnblogs.com/ZJiQi/p/9895728.html)
