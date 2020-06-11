# 子路由

在网页较为简单的情况下 Django 可以只使用单个 app 和项目自带的 urls 文件进行路由，但是在网页较为复杂或项目内有多个 app 的情况下就不太合适了，这时候就需要在 app 中单独设置路由

项目有个 主路由 ，各 app 下分别有自己的一个 路由文件 ，既集中又分治，是一种解耦的模式

**实现方式**

(1) 在每个 app 中创建 `urls.py` 文件
(2) 在每个 app 中编写各自的路由
(3) 在 项目的主路由中包含每个子路由

```python
from django.urls import path,include

urlpatterns = [
    path("restful/", include("restful.urls")),
    path("test/", include("test.urls"))
]
```

# 子模板

每一个 app 对自己的模板进行管理维护

(1) 在 app 中创建 `templates/appname` 目录
(2) settings 中进行修改

![img][img@1]

(3) 视图中返回页面

```python
def index(request):
    return render(request,"appname/index.html")
```

# 子静态

在子应用创建 `static/appname` , 每个 app 中存放各自的静态文件

每个 app 中的 static 静态文件，只是单纯的为了方便管理，项目中使用的静态文件不是各自app下的 static 目录中的文件

**静态文件的收集：**

(1) settings 中修改配置

![img][img@2]

(2) 执行命令收集文件

`python manage.py collectstatic`

(3) settings 文件还原配置

<br/>

> APP 下面创建了 static/appname 静态文件目录，该目录只是为了方便管理，同时收集静态文件，收集文件之后，该目录可以删除，但是不建议删除，为了方便之后的管理和下一次静态文件的收集使用

> 项目主目录的 static/appname 项目中使用的静态文件





[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/Django/06-11_52748.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/Django/06-11_3824.png
