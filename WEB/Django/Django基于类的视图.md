# 基于类的视图

视图是可调用的，能接受用户的请求并返回响应。视图远不只是个函数，Django提供了一些视图类的实例，允许你通过继承和复用构建自己的视图



## 基础示例

Django 提供了适用于很多应用的基本视图类。所有视图继承自 `View` 类，它处理视图 **链接到URLs**，**HTTP方法调度** 和 **其它简单的功能**

>   RedirectView 用于 HTTP 重定向，**TemplateView** 扩展基类来使他能渲染模板



使用通用视图最直接的方式是在 URLconf 中直接创建它们。如果你只在基于类的视图上改变一些属性，那么你可以把它们传递到 `as_view()` 方法中调用：

```python
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about', TemplateView.as_view(template_name='about.html'))
]
```

-   `TemplateView` 只是一个类，而不是一个函数，因此我们将 URL 指向 `as_view()` ，**它为基于类的视图提供一个类似函数的入口**

-   任何传递到 `as_view()` 的参数将覆盖在类上设置的属性



## 子类化通用视图

使用通过视图更有力的方式是继承已存在的视图并覆盖子类里的属性 （比如 **template_name**）来提供新的值或方法。例如，考虑只显示一个 **about.html** 模板的视图。Django 的 `TemplateView` 可以完成这个工作，因此我们可以将其子类化并重写模板名称：



```python
# ==== views.py

from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'about.html'
    
    
# ==== urls.py

urlpatterns = [
	path('about', AboutView.as_view())
]
```



## 支持其他的 HTTP 方法



TODO