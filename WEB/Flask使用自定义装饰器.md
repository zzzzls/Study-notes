# 问题描述

Flask Web 项目，遇到一个需求：

> 部分视图，只有已经登录的用户才能访问，如果用户访问时没有登录，则会重定向到登录页面。

手动为每个视图函数添加判读语句太过繁琐，遂决定使用装饰器实现这个功能，代码大概如下所示：

```python
from flask import Flask,request,redirect

app = Flask(__name__)

def check_login_status(func):
    def wrapper(*args, **kwargs):
        if request.cookies:
            return func(*args, **kwargs)
        else:
            # 否则重定向到登录页面
            return redirect("/login/")
    return wrapper

@app.route("/",endpoint="index")
@check_login_status
def index():
    return "首页"

print(index.__name__)

@app.route("/news/",endpoint="news")
@check_login_status
def news():
    return "新闻界面"
```

但是执行时，却发生了如下错误：

> AssertionError: View function mapping is overwriting an existing endpoint function: wrapper

# 问题思考

这是一个新手经常会遇到的错误，如果不小心把视图函数写重名，就会出现这个错误，如下所示：

![img](http://img.zzzzls.top/05-27_1094.png&git)

但是这里视图函数名并没有问题，为什么也出现了这个问题？

一顿查阅资料后得知，是 **装饰器** 出现了问题！

经过 装饰器 装饰之后的函数，它们的 `__name__` 已经从原来的函数名变成 `wrapper`，也就是变成了装饰器内部的函数名称

我们可以通过打印函数的 `__name__` 看到这一结果：

```python
>>> @app.route("/")
>>> @check_login_status
>>> def index():
...    return "首页"

>>> print(index.__name__)

wrapper
```

# 解决方案

知道了出错的原因，我们就可以对症下药了，具体的解决办法有如下几种：

**(1) 把每个 `wrapper.__name__` 设置成唯一的**

```python
def check_login_status(func):
    def wrapper(*args, **kwargs):
        if request.cookies:
            return func(*args, **kwargs)
        else:
            # 否则重定向到登录页面
            return redirect("/login/")
    wrapper.__name__ = func.__name__
    return wrapper
```

**(2) 使用 `functools.wraps` 装饰下 `wrapper` 函数**

其实这个办法做的事情和上一个办法是差不多的，只不过除了 `__name__` 之外，它还把 `__module__`、`__doc__` 和 `__dict__` 都复制到 `wrapper` 上去了

```python
from functools import wraps
def check_login_status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 如果获取到 session , 即判定为 已登录
        if request.cookies:
            return func(*args, **kwargs)
        else:
            # 否则重定向到登录页面
            return redirect("/login/")
    return wrapper
```

**(3) 显式设置每个视图函数的 endpoint 名称**

```python
@app.route("/",endpoint="index")
@check_login_status
def index():
    return "首页"

@app.route("/news/",endpoint="news")
@check_login_status
def news():
    return "新闻界面"
```

# 参考文档

- [视图装饰器 — Flask 中文文档](https://dormousehole.readthedocs.io/en/latest/patterns/viewdecorators.html)

- [实现Flask中view函数的装饰器](https://cuyu.github.io/python/2017/08/11/%E5%AE%9E%E7%8E%B0Flask%E4%B8%ADview%E5%87%BD%E6%95%B0%E7%9A%84%E8%A3%85%E9%A5%B0%E5%99%A8)

- [装饰器 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584)
