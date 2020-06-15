<!-- TOC -->

- [Tornado](#tornado)
  - [第一个 Tornado 程序](#第一个-tornado-程序)
  - [路由](#路由)
  - [模板](#模板)
    - [模板调用](#模板调用)
    - [模板语法](#模板语法)
    - [过滤器？](#过滤器)
    - [模板继承和加载](#模板继承和加载)
  - [响应](#响应)

<!-- /TOC -->

# Tornado

Tornado 是一个Python web框架和异步网络库，通过使用非阻塞网络I/O, Tornado 可以支持上万级的连接，处理 长连接, WebSockets, 和其他 需要与每个用户保持长久连接的应用

Tornadi 大体上可以分为 4 个主要的部分

1. web 框架（ 包括创建 web 应用的 `RequestHandler` 类等）
2. HTTP 的客户端和服务端实现（ `HTTPServer` 和 `AsyncHTTPClient` ）
3. 异步网络库（`IOLoop` 和 `IOStream`），为 HTTP 组件提供构建模块，也可以用来实现其它协议
4. 协程库 ( `tornado.gen` ) 允许异步代码写的更直接而不用链式回调的方式

安装：

`pip install tornado`

## 第一个 Tornado 程序

```python
"""
Tornado 入门案例
"""

# 负责 tornado 操作 io 的类
import tornado.ioloop
# tornado web 开发的基础类
import tornado.web


# tornado.web.RequestHandler 负责请求处理的基础类
class MyHandler(tornado.web.RequestHandler):
    # 重写 get 方法 , 处理 get 请求
    def get(self):
        self.write("hello world")


if __name__ == "__main__":
    # 应用相关的基础类 , 指出路由设置表 , 接收一个列表参数
    app = tornado.web.Application([
            # 路由
            (r"/",MyHandler)
        ])
    # 负责监听的端口
    app.listen(8000)
    # 负责 io 监听
    tornado.ioloop.IOLoop.current().start()
```

## 路由

Tornado 中依然可以使用路由传参

1. 路由可以使用 **字符串** 进行匹配
2. 路由可以使用 **正则** 进行匹配
3. 路由中可以使用 **正则组** 匹配，同时将匹配到的内容作为参数传递
4. 路由中可以使用 **正则组+别名** 的形式匹配，将匹配的内容作为参数传递，但是参数的名字需要和别名一致

```python
class StrRoute(tornado.web.RequestHandler):
    def get(self):
        self.write("字符串路由")


class ReRoute(tornado.web.RequestHandler):
    def get(self):
        self.write("正则路由")


class ReGroupRoute(tornado.web.RequestHandler):
    def get(self, id):
        self.write(f"正则组路由, {id}")


class ReGroupAsRoute(tornado.web.RequestHandler):
    def get(self, id):
        self.write(f"正则组 + 别名路由, {id}")

if __name__ == "__main__":
    app = tornado.web.Application([
            # 路由
            (r"/str/",StrRoute),
            (r"/re/\d+/", ReRoute),
            (r"/regroup/(\d+)/", ReGroupRoute),
            (r"/regroupas/(?P<id>\d+)/", ReGroupAsRoute),
        ])
```

> 备注：  
> 路由若为 `/str/`，则请求地址必须为 `127.0.0.1:8000/str/`  
> 路由若为 `/str`，则请求地址必须为 `127.0.0.1:8000/str`

## 模板

### 模板调用

Tornado 默认调用启动文件同级的模板文件

```
/Tornado_demo/
    app.py
    index.html
```

```python
# app.py

class TemplatesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
```

项目的开发中，由于有大量的模板文件等，会导致目录混乱。基于此，tornado 可以修改静态文件和模板文件的路径

**Application** 类接收参数，修改静态文件和模板的路径

|配置|说明|
|:---|:---|
|template_path|模板文件目录|
|static_path|静态文件目录|
|static_url_prefix|静态文件路由|

```python
app = tornado.web.Application(
    [
        # 路由
        (r"/",templateHandler),
    ],
    # 配置 静态文件 模板 静态文件路由
    template_path = "templates",
    static_path = "static",
    static_url_prefix = "/static/"
)
```

### 模板语法

**(1) 传递变量**

```python
# example 1
name = "zong"
age = 18
self.render("index.html",name=name,age=age)
```

```python
# example 2
name = "zong"
age = 18
dct = {
   "name" : name,
    "age" : age
}
self.render("index.html",dct=dct)
```

```python
# example 3
name = "zong"
age = 18

kwargs = locals()
kwargs.pop("self")
# 如果使用 **locals() 传递参数，需要先干掉 locals() 中的 self 参数
self.render("index.html",**kwargs)
```



**(2) 变量的使用**

```python
# domo.html

# 展示变量
{{ name }}

# 展示列表
{{ lst }}
{{ lst[1] }}

# 展示字典
{{ dct }}
{{ dct["key"] }}
{{ dct.get("key") }}
```

(3) 标签语法

Tornado 标签语法和 flask 以及 django 中的语法大致相同，不同的是结束的时候所有的标签均为 end

```python
# if

{% if age > 18 %}
    已经成年了
{% elif age == 18 %}
    刚刚成年
{% else %}
    还未成年
{% end %}
```

```python
# for

{% for one in ["唱歌","跳舞","扣腚"] %}
    <p>{{ one }}</p>
{% end %}

{% for one in range(5) %}
    <p>{{ one }}</p>
{% end %}

{% for k,v in dct.items() %}
    {{ k }} : {{ v }}
{% end %}
```


### 过滤器？

**Torando 模板中没有过滤器**

### 模板继承和加载

使用方式和 Django ，flask 中模板继承的方式基本一致，仅结束标签为 end

## 响应

|方法|描述|
|:---|:---|
|write|返回数据|
|render|加载页面|
|redirect|重定向|
|set_header|设置响应头|

```python
# Example: 返回 JSON 数据
def get(self):
    import json
    dct = {
        "code": "200",
        "msg": "success"
    }
    self.set_header("Content-Type","application/json;charset=UTF-8")
    self.write(json.dumps(dct))
```

