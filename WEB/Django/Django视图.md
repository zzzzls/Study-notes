# Django 视图函数

一个视图函数，简称视图，是一个简单的 Python 函数，它接受 Web 请求并返回 Web 响应

响应可以是一个 HTML 页面，一个 404 错误页面，重定向页面，XML 文档，或者一张图片 ...

无论视图本身包含什么逻辑，都要返回响应。视图一般放在项目的 `views.py` 文件中

每个视图函数都负责返回一个 `HttpResponse` 对象，对象中包含生成的响应

视图层中有两个重要的对象: **请求对象(request)** 与 **响应对象(HttpResponse)**

## 第一个视图函数

```python
# 导入 HttpResponse
from django.http import HttpResponse

# 定义视图函数
# 视图函数至少有一个参数，第一个参数必须是 request，它携带了浏览器的请求信息
def hello(request):
    # 必须返回 HttpResponse 对象的响应内容
    return HttpResponse("<h1>hello Django</h1>")
```

## 视图函数执行过程

- Django 收到浏览器请求
- 创建带有请求信息的 HttpResponse 对象 request
- 将 request 作为第一个参数传递给视图函数
- 视图函数接收到参数后继续向下执行
- 最终返回 HttpResponse 对象给浏览器