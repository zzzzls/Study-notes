# Django中的 APP

App( Application ) 是应用，当项目足够大的时候，我们将功能进行划分，单独的分成几个 app( 子应用 ) 进行管理

在 Django 中，每个应用都是一个 Python 包，并且遵循相同的约定。Django自带一个工具，可以帮你生成应用的基础目录结构

## 创建 app

(1) 进入项目中的 `manage.py` 同级目录

(2) 执行命令创建子应用 `python manage.py startapp appname`

(3) app 目录结构

```
test_app/
    migrations/   数据库迁移文件
    __init__.py   app 子应用 初始化文件
    admin.py      站点管理
    apps.py       app 的配置信息
    models.py     模型
    tests.py      测试文件，单元测试..
    views.py      视图文件
```

## 配置 app

在 `settings.py` 中配置 app ( 安装 app )


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 添加创建的 app 目录名字
    'test_app',
    # 或者
    'test_app.apps.TestAppConfig'
]
```

## 使用 app

```python
# app/views.py
from django.shortcuts import render

def hello(request):
    return render(request, "index.html")



# urls.py
from test_app.views import hello

urlpatterns = [
    path('hello/', hello)
]
```
