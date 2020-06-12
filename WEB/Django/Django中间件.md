# 中间件

中间件是 Django 请求/相应处理的钩子框架。它是一个轻量级的、低级的 "插件" 系统，用于全局改变 Django 的输入或输出

在 `settings.py` 中可以查看 Django 中默认加载的中间件

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

中间件提供了如下 4 种方法

|方法|描述|
|:---|:---|
|process_request|请求开始，到达视图之前|
|process_view|请求开始，路由匹配之后|
|proccess_exception|视图中出现异常|
|process_response|视图处理完毕，返回响应的结果|

执行循序如下选图所示：

![img][img@1]

# 中间件的使用

(1) 在 app 中创建 `middleware.py` 文件
(2) 编写中间件

```python
from django.utils.deprecation import MiddlewareMixin

class MiddleWareDemo(MiddlewareMixin):
    def process_request(self):
        pass
    def process_view(self):
        pass
    def process_exceotion(self):
        pass
    def process_response(self):
        pass
```

(3) `settings.py` 中注册使用

```python
MIDDLEWARE = [

    ...

    'appname.middleware.MiddleWareDemo',
]
```

# 中间件的使用

**(1) process_request**

```python
def process_request(self,request):
    """
    请求进来第一个被触发的方法

    :param request:  包含请求信息的请求对象
    :return:
        当返回 None 的时候 , 继续向下执行
        如果返回不是 None , 则该请求直接在这个方法中返回响应
    """

    # example: 判断请求者 ip 是否在黑名单中
    ip_list = ["192.168.0.101","192.168.0.102","192.168.0.103"]

    # 获取访问者 ip
    user_ip = request.META.get("REMOTE_ADDR")

    if user_ip in ip_list:
        from django.http import HttpResponse
        return HttpResponse("您没有访问权限!")
    else:
        return None
```

**(2) process_view**

```python
def process_view(self,request,view_func,view_args,view_kwargs):
    """
    方法在通过 process_request 之后 , 到达视图之前被触发

    :param request: 包含请求信息的请求对象
    :param view_func: 要处理业务的视图
    :param view_args: 传递给视图的位置参数列表
    :param view_kwargs: 传递给视图的关键字参数字典
    :return:
        当返回 None 的时候 , 继续向下执行
        如果返回不是 None , 则该请求直接在这个方法中返回响应
    """

    pass
```

**(3) process_exception**

```python
def process_exception(self,request,exception):
    """
    当视图中出现异常时触发

    :param request:
    :param exception: 异常信息
    :return:
        当返回 None 的时候 , 继续向下执行
        如果返回不是 None , 则该请求直接在这个方法中返回响应
    """

    # example: 记录异常信息 log
    import os
    import time
    file_path = os.path.dirname(os.path.abspath(__file__))

    err_log_path = os.path.join(file_path,"errlog.txt")
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    err_msg = f"[{now_time}] {exception}\n"

    with open(err_log_path,"a",encoding="utf-8") as f:
        f.write(err_msg)

    return HttpResponse("500 error")
```

**(4) process_response**

```python
def process_response(self,request,response):
    """
    视图处理完成之后 最终返回的时候触发的方法

    :param request: 请求对象
    :param response: 响应对象
    :return:
    """

    # example: 给所有返回内容设置 cookie

    response.set_cookie("ver","v1")
    return response
```

# 参考

-[中间件 | Django 文档](https://docs.djangoproject.com/zh-hans/3.0/topics/http/middleware/#writing-your-own-middleware)

[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/Django/06-12_01.png