<!-- TOC -->

- [Django 请求](#django-请求)
  - [请求对象](#请求对象)
  - [文件处理](#文件处理)
  - [form表单](#form表单)
  - [重定向](#重定向)

<!-- /TOC -->

# Django 请求

## 请求对象

Flask 导入 request，获取了请求的信息

Django 中是从形参 request 中获取

```python
# rquest 包含请求信息的请求对象
def view(request):
    pass
```

request 常用属性

|属性名|描述|
|:---|:---|
|method|	请求方式|
|GET|	获取 get 请求传递的参数|
|POST|	获取 post 请求传递的参数|
|body| 获取**非表单数据(如 json)**，返回值为 bytes对象|
|COOKIES|	获取 cookies|
|session| 获取 session|
|FILES|	获取上传的文件|
|headers|获取请求头|

|META|	获取更多的请求信息|

## 文件处理

表单上传的文件对象存储在类字典对象 `request.FILES` 中，表单格式需为 `multipart/form-data`

```python
# 获取文件对象
file = request.FILES.get("file")

# 获取文件名
file.name

# 获取文件大小
file.size

# 获取文件类型
file.content_type

# 返回一个生成器对象，可用于存储图片
file.chunks(chunk_size=None)

# 存储图片
file = request.FILES.get("file")
with open('./cs.png', 'wb+') as f:
    for chunk in file.chunks():
        f.write(chunk)
```

## form表单

```html
<form action="/login/" method="POST">
    <!-- Django 默认开启了csrf 验证，需要设置 csrf_token -->
    {% csrf_token %}
    <p>账号: <input type="text" name="username"></p>
    <p>密码: <input type="password" name="password"></p>
    <input type="submit" value="提交">
</form>
```

```python
def login(request):
    print(request.POST)
    return render(request, "index.html")
```

## 重定向

```python
from django.http import HttpResponseRedirect

def login(request):
    return HttpResponseRedirect("/index/")
```

