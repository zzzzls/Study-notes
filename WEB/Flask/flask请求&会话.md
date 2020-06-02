# 常见的请求方式

- **GET** : 页面的默认请求方式，请求的数据是以明文的形式放在路由上面，以 `?` 开头的键值对，中间以 `&` 连接多个参数
- **POST** : 请求的数据隐藏发送的，安全系数高，通常用来向服务器提交数据

# 请求对象

Flask 中由全局对象 `request` 处理请求，需要使用 `from flask import request` 导入模块

**request 常用属性**

|属性名|描述|
|:---|:---|
|`args`|获取 get 请求的参数|
|`form`|获取 post 请求的参数|
|`method`|获取请求的方式 GET or POST|
|`files`|获取上传的文件|
|`cookirs`|获取 cookie 信息|
|`headers`|获取请求头|
|`path`|获取 /|
|`host`|获取 ip:host|
|`host_url`|获取 http://127.0.0.1:5000/|
|`referrer`|请求的来源|

# 配置请求

```python
# 配置路由 支持 POST 及 GET 请求 (默认仅支持 GET 请求)
@app.route("/",methods=["POST","GET"])
def view():
    # 如果请求方式为 POST
    if request.method == "POST":
        # 获取 POST 方式提交的参数
        data = request.form
    # 如果请求方式为 GET
    elif request.method == "GET":
        # 获取 GET 方式提交的参数
        data = request.args
```

# 文件上传

**HTML 表单**

```html
<form action="/file_upload/" method="POST" enctype="multipart/form-data">
    <input type="file" name="img">
    <input type="submit" value="上传">
</form>
```

**Flask**

```python
@app.route("/file_upload/",methods=["POST"])
def file_upload():
    # 获取文件对象
    file = request.files.get("img")
    # 获取文件名
    file_name = file.filename
    # 保存文件
    file.save(f"./{file_name}")
```

# 会话

由于 HTTP 协议都是无状态的，即当前请求和上一次请求没有任何的联系，请求者的身份都是匿名的，这样的访问缺乏连续性，导致在一个 WEB 项目中没有办法表示用户的身份，对于 WEB 有很大的制约，基于此出现了会话机制，即 Cookie 和 Session

## Cookie

Cookie 是浏览器在请求的时候，由服务器下发，保存在用户的客户端（本地）的一段用于标识身份的小文本

Cookie的出现让浏览器的访问有了连续性，可以有身份的访问，但是也带来了很大的安全隐患，Cookie 很容易被盗用和篡改

**(1) 设置 Cookie**

在 Flask 中，cookie 设置在响应对象上，使用 `make_response()` 函数从视图函数的返回值中获取响应对象。之后，使用响应对象的 `set_cookie()` 函数老存储 cookie

`set_cookie(key, value[, max_age, expires, path, domain, secure, httponly])`

|参数|描述|
|:---|:---|
|**key**|设置的 cookie 中的 key|
|**value**|设置的 cookie 中的 value|
|**max_age**|cookie的过期时间，值为秒数|
|**expires**|cookie的过期时间，值为 datetime对象 或 unix时间戳|
|path|将 cookie 限制为给定路径生效，默认为所有路径|
|domain|cookie 生效的域名|
|secure|如果为 True，则 cookie 仅可通过 https 使用|
|httponly|如果为 True，则禁止 JavaScript 访问 cookie|

```python
from flask import make_response

@app.route("/")
def view():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("username","zong")
    return resp
```

**(2) 获取 Cookie**

`request.cookies.get("key")`

**(3) 删除 Cookie**

```python
@app.route("/del_cookie/")
def del_cookie():
    rep = make_response("删除 cookie")
    rep.delete_cookie("username")
    return rep
```

通过观察 Reponse Headers 可以发现，删除 cookie 就是将 cookie 值 置为空，并将过期时间设置为 过去

```
Set-Cookie: username=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/
```

## Session

与 Cookie 不同，session 数据存储在服务器上，安全性有了提高。

session 为每个客户端的会话分配 会话ID，会话数据存储在 cookie 的顶部，服务器以加密方式对其进行签名。对于此加密，Flask程序需要定义一个 SECRET_KEY

**特点：**

1. session 依赖 cookie 技术
2. session本身存储在服务器上边，多数情况下存储在数据库中，频繁校验数据会导致服务器，数据库的压力变大


**(1) 设置 Session**

```python
from flask import session

# 设置 session SECRET_KEY
app.config["SECRET_KEY"] = "test@0527"

# 添加 session
session['xxx'] = "xxx"
```

**(2) 获取 Session**

```python
session['xxx']
session.get('xxx')
```

**(3) 删除 Session**

```python
# 删除指定 session
session.pop("xx")

# 清空 session
session.clear()
```

**(4) 设置 session 过期时间**

```python
# 如果不设置过期时间，session默认为 浏览器关闭后过期

# 默认过期时间为 31 天
session.permanent = True

# 配置 app.config 修改默认过期时间
from datetime import timedelta
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
session.permanent = True
```


