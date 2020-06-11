<!-- TOC -->

- [Django REST framework 框架](#django-rest-framework-框架)
  - [安装与配置](#安装与配置)
  - [序列化 Serializer](#序列化-serializer)
  - [视图](#视图)
    - [继承 APIView 类](#继承-apiview-类)
    - [mixins 类](#mixins-类)
    - [通用视图类](#通用视图类)
    - [viewset](#viewset)
  - [分页](#分页)
- [参考](#参考)

<!-- /TOC -->

# Django REST framework 框架

编写一个只返回数据的接口很容易，但是如果让这个接口符合 rest 风格很繁琐

**Django REST framework** 框架是一个用于构建 Web API 的强大而又灵活的工具。通常简称为 **DRF 框架**

DRF框架 是建立在 Django 框架基础之上二次开发的开源项目

官网：[https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

**特点：**

1. 提供了序列化器 Serializer 的方法，可以快速根据 Django ORM 或者其它库自动序列化/反序列化
2. 提供了丰富的类视图，Mixin扩展类，简化视图的编写
3. 丰富的定制层级：函数视图，类视图，视图集合到自动生成 API
4. 多种身份认证和权限认证方式的支持
5. 内置了限流系统
6. 直观的 API Web 界面
7. 可扩展性，插件丰富

## 安装与配置

(1) 安装 Django REST framework

`pip install djangorestframework`

(2) 注册 app

> Django 中的功能组件大部分以 app 的形式存在

在 Django 配置文件 `settings.py` 的 `INSTALLED_APPS` 中添加 `rest_framework`

```python
INSTALLED_APPS = [ ... ,'rest_framework']
```

## 序列化 Serializer

序列化 是 DRF 的核心概念，提供了数据的验证和渲染功能

(1) 在 app 中创建 `serializer.py` 文件

(2) 编写序列化的内容

```python
# 导入序列化类
from rest_framework import serializers
# 导入定义的 ORM 模型
from .models import Teacher

class MoreListSerializer(serializers.ModelSerializer):
    # Teacher 的序列化类
    class Meta:
        # 对应的模型
        model = Teacher
        # 模型中所有的属性
        fields = "__all__"
        # fields = ["id","name","age"]
```

## 视图

### 继承 APIView 类

```python
# 视图

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MoreListSerializer

class MoreListView(APIView):
    def get(self,format=None):
        t_id = self.request.GET.get("t_id")
        teacher = Teacher.objects.get(id=int(t_id))
        # many 判断 序列化单个对象 还是 列表
        serializer = MoreListSerializer(teacher,many=False)
        res = serializer.data
        return Response(res)

# 路由
path('morelistview/',MoreListView.as_view())
```

### mixins 类

使用 REST 的 mixins 类，提高代码的重用率

```python
# 视图

from rest_framework import generics,mixins
from .serializer import MoreListSerializer

class MixinsView(mixins.ListModelMixin,generics.GenericAPIView):
    def get_queryset(self):
        t_id = self.request.GET.get("t_id")
        students = Student.objects.filter(s_teacher_id=int(t_id)).all()[:10]
        return students

    serializer_class = MoreListSerializer

    def get(self,*args, **kwargs):
        return self.list(*args, **kwargs)

# 路由
path('mixinsview/',MixinsView.as_view())
```

若 ORM 模型中存在 ImageField 字段，那么返回的图片数据，默认添加了根路径，如果只需要返回数据库中存储的文件路径，办法如下：

```python
class MixinsView(mixins.ListModelMixin,generics.GenericAPIView):
    def get_queryset(self):
        t_id = self.request.GET.get("t_id")
        students = Student.objects.filter(s_teacher_id=int(t_id)).all()[:10]
        return students

    serializer_class = MoreListSerializer

    def get(self,*args, **kwargs):
        return self.list(*args, **kwargs)

    def get_serializer_context(self):
        # 返回一个数据本身，否则 DRF 框架会自动给图片增加根路径
        return {
            "view":self
        }
```

### 通用视图类

使用了 mixins 之后，我们重写了视图，代码量变少了，但是可以更进一步，REST 框架提供了一组已经封装好的通用视图类，可以更进异步减少 views.py 模块的工作量

```python
# 视图

from rest_framework import generics
from .serializer import MoreListSerializer
class Generics(generics.ListAPIView):
    def get_queryset(self):
        t_id = self.request.GET.get("t_id")
        students = Student.objects.filter(s_teacher_id=int(t_id)).all()[:10]
        return students

    serializer_class = MoreListSerializer
    
    def get_serializer_context(self):
        return {
            "view":self
        }

# 路由

path('generics/',Generics.as_view())
```

### viewset

viewset 对通用的视图类进行进一步的封装

```python
# 视图

from rest_framework import viewsets
from .serializer import MoreListSerializer

class Viewset(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        t_id = self.request.GET.get("t_id")
        students = Student.objects.filter(s_teacher_id=int(t_id)).all()[:10]
        return students

    serializer_class = MoreListSerializer

    def get_serializer_context(self):
        return {
            "view":self
        }

# 路由

path('viewset/',Viewset.as_view({"get":"list"}))
```

使用 DRF 路由 代替 Django 路由

修改 `urls.py`

```python
from django.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("viewset",Viewset,basename="")


urlpatterns = [

    ...

    path("",include(router.urls))
]
```

## 分页

DRF 提供了分页的功能
`settings.py` 中增加如下配置

```python
REST_FRAMEWORK = {
    # 分页器
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # 每页返回的条数
    "PAGE_SIZE":10
}
```

此时访问接口

```json
{
    // 总页数
    "count": 96,
    // 下一页链接
    "next": "http://127.0.0.1:8000/viewset/?format=json&page=2&t_id=2",
    // 上一页链接
    "previous": null,
    "results": [
        {
            "id": 9,
            "username": "韩丝瓜",
            "gender": 1,
            "age": 35,
            "s_teacher": 2
        },
        {
            "id": 10,
            "username": "杨西葫芦",
            "gender": 0,
            "age": 18,
            "s_teacher": 2
        },

        ...
}
```

# 参考

- [Django REST framework的使用总结](https://juejin.im/post/5d064f856fb9a07f0420478a)
- [Django-REST-framework 学习笔记](https://blog.windrunner.me/python/web/django-rest-framework.html)