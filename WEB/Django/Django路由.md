# Django 路由

路由简单的说就是根据用户请求的 URL 链接来判断对应的处理程序，并返回处理结果，也就是 URL 与 Django 的视图建立映射关系

Django 的路由在 `urls.py` 配置，`urls.py` 中的每一条配置对应相应的处理方法

Django 不同版本 `urls.py` 配置不同

## Django 1.1.x 版本

**url()方法**: 普通路径和正则路径均可使用，需要自己手动添加正则首位限制符号

```python
from django.conf.urls import url # 用 url 需要引入

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^index/$', views.index), # 普通路径
    url(r'^articles/([0-9]{4})/$', views.articles), # 正则路径
]
```

## Django 2.2.x 之后版本

**path()**: 用于普通路径，不需要自己手动添加正则首位限制符号，底层已经添加
**re_path()**: 用于正则路径，需要自己手动添加正则首位限制符号

```python
from django.urls import path
from django.urls import re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # 普通路径
    re_path(r'^articles/([0-9]{4})/$', views.articles), # 正则路径
]
```

`path("匹配的内容",视图函数名)`
`re_path("正则匹配",视图函数名)`

## path() 函数

`path(route, view[, kwargs=None, name=None])`

**route**

一个匹配 URL 的准则，当 Django 响应一个请求时，会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项

**view**

当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 `HttpResponse` 对象作为第一个参数

**kwargs**

任意个关键字参数可以作为一个字典传递给目标视图函数

**name**

用来反向获取 URL

## 路由中使用正则

在路由中使用组匹配并且设置组名，**组名和视图函数的参数一致**

```python
def view(request, year, month):
    return ""

urlpatterns = [
    re_path(r'(?P<year>\d+)/(?P<month>\d+)', view)
]
```

