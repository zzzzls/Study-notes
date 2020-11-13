# 内置的基于类的视图

-   基础视图
    -   View
    -   TemplateView
    -   RedirectView

-   ...



## View

类 `django.views.generic.base.View`

基于主类的基本视图。所有其他基于类的视图都从该基类继承



####  方法流程图

-   `setup()`
-   `dispatch()`
-   `http_method_not_allowed()`
-   `options()`



#### 使用示例

```python
####### views.py
from django.http import HttpResponse
from django.views import View


class MyView(View):

    # 匹配 get 请求
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')



####### urls.py
urlpatterns = [
    path('mine/', MyView.as_view())
]
```



#### 属性

```python
http_method_names ：
	该视图将接受的 HTTP 请求类型的列表
    
    默认值: ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
```



#### 方法

-   `as_view()`

    返回一个接受请求并返回响应的可调用视图，它为基于类的视图提供一个类似函数的入口



-   `setup(request, *args, **kwargs)`

    在视图之前初始化 `dispatch()`  

    如果重写此方法，必须调用 `super()`  



-   `dispatch(request, *args, **kwargs)`

    **view** 视图的一部分，接受 **request** 参数并返回 HTTP响应的方法

    默认实现将检查 HTTP 方法，并尝试委托给与 HTTP 方法匹配的方法；GET 将委托给 `get()` ，POST 将委托给 `post()`，以此类推。

​		默认情况下，将 HEAD请求委托给 `get()` ，如果需要以不同的方式处理 HEAD请求，则可以重写 `head()` 方法



-   `http_method_not_allowed(request, *args, **kwargs)`

    如果使用不支持的 HTTP方法调用该视图，则改为调用本方法



-   `options(request, *args, **kwargs)`

    处理 OPTION 请求。返回带有 **Allow** 的响应头，响应头中包含视图允许的 HTTP请求方式



## TemplateView

类 `django.views.generic.base.TemplateView`

呈现给定的模板，其上下文包含 URL 中捕获的参数



#### 父类

该视图类从以下视图继承方法和属性：

-   `django.views.generic.base.TemplateResponseMixin`
-   `django.views.generic.base.ContextMixin`
-   `django.views.generic.base.View`



#### 方法流程图

-   `setup()`
-   `dispatch()`
-   `http_method_not_allowed()`
-   `get_context_data()`



#### 使用示例

```python
######  views.py
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    # 指定返回的模板
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # 获取原上下文变量的值
        context = super().get_context_data(**kwargs)
        # 增加值
        context['data'] = 'ahahah'
        return context
    
    
###### urls.py
urlpatterns = [
	path('mine/', HomePageView.as_view())
]
```



#### 方法

-   `get_context_data(**kwargs)`

    返回用于显示对象的上下文数据

    >   小心覆盖问题，详见上例





## 参考



-   [全部视图类](https://docs.djangoproject.com/zh-hans/3.1/ref/class-based-views/)
-   [视图类字段、方法](https://docs.djangoproject.com/zh-hans/3.1/ref/class-based-views/mixins-single-object/)
