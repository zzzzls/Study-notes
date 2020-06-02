Flask 会根据 HTTP 请求的 URL 在路由表中和定义好的路由进行匹配，然后找到对应的函数处理这个请求。

这个过程中需要保存一个 URL 到函数的映射关系，我们把这个映射关系及处理请求的函数之间的关系称为 **路由**

# 路由绑定

(1) **使用 route() 装饰器来把函数绑定到 URL**

```python
@app.route("/hello/")
def hello():
    return "hello bro!"
```

在这里，URL /hello/ 绑定到 hello() 函数。因此，如果用户访问 `http://127.0.0.1:5000/hello/` URL，hello() 函数的输出将在浏览器中呈现

(2) **使用 add_url_rule() 函数绑定**

```python
def hello():
    return "hello"

app.add_url_rule("/hello/", view_func=hello)
```

(3) **多个路由绑定同一个视图函数**

```python
@app.route("/index/")
@app.route("/hello/")
def hello():
    return "hello bro!"
```

# 动态路由

通过把 URL 的一部分标记为 `<variable_name>` 就可以在 URL 中添加变量。标记的部分会作为关键字参数传递给函数。通过使用 `<converter:variable_name>` 可以选择性的加上一个转换器，为变量指定规则

```python
# 动态路由
@app.route("/user/<username>/")
def view(username):
    return username

# 为变量指定规则
# /path/https://www.baidu.com/
@app.route("/path/<path:url_path>/1")
def show_path(url_path):
    return url_path
```

|转换器类型|描述|
|:---|:---|
|string|接受任何不包含斜杠的文本|
|int|接收正整数|
|float|接收正浮点数|
|path|类似string，但是可以包含斜杠|
|uuid|接受 UUID 字符串|