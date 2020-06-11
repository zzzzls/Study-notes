# 关闭 CSRF

由于 Django 默认开启了 CSRF 防护，当我们使用 postman 等第三方工具进行接口测试时，没有办法获取到最新的 csrf_token，因此我们需要暂时关闭 CSRF 验证

**(1) 视图关闭 CSRF**

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def views(request):
    return HttpResponse("测试视图.")
```

**(2) 路由关闭 CSRF**

```python
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("views/",csrf_exempt(views))
]
```

**(3) 类视图中关闭 CSRF**

方案一：

```python
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,"dispatch")
class Cbv(View):
    def get(self,request):
        return JsonResponse({"method": "GET 请求"})
```

方案二：

```python
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("cbv/",csrf_exempt(Cbv.as_view()))
]
```

# FBV & CBV

**(1) FBV**

函数视图: 基于函数的视图，需要接收一个参数 request 包含请求信息的请求对象

```python
@csrf_exempt
def fbv(request):
    if request.method == "GET":
        return JsonResponse({"method": "GET 请求"})
    if request.method == "POST":
        return JsonResponse({"method": "POST 请求"})
    if request.method == "PUT":
        return JsonResponse({"method": "PUT 请求"})
    if request.method == "DELETE":
        return JsonResponse({"method": "DELETE 请求"})
```

**(2) CBV**

类视图: 基于类的视图

```python
from django.views import View

class Cbv(View):
    def get(self,request):
        return JsonResponse({"method": "GET 请求"})

    def post(self, request):
        return JsonResponse({"method": "POST 请求"})

    def put(self,request):
        return JsonResponse({"method": "PUT 请求"})

    def delete(self,request):
        return JsonResponse({"method": "DELETE 请求"})
```

路由

```python
path("cbv/",Cbv.as_view())
```

> `as_view()`: 根据请求方式的不同做出不同相应的处理，实际上调用了 dispatch 方法进行处理  
> dispatch 会根据不同的请求方式，找到对应的方法进行处理，并将该方法处理结果返回