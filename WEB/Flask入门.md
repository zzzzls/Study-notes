![flask](http://img.zzzzls.top/flask-logo.png&git)

Flask 是一个使用 Python编写的**轻量级 Web 应用框架**，只提供了 **Web 框架的核心功能**，相较于其它的框架来说更加**灵活**，**自由**，更加适合开发**高度定制化**的项目。

其 WSGI 工具箱采用 Werkzeug，模板引擎则使用 Jinja2，Flask 使用 BSD 授权

中文文档: https://dormousehole.readthedocs.io/en/latest/

**安装 Flask**

```python
pip install flask
```

# 第一个 Flask 应用

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def view():
    return "hello Flask"

app.run()
```

(1) 导入了 Flask 类
(2) 接着创建一个类的实例，第一个参数是应用模块或者包的名字。这个参数是必需的，这样 Flask 才能知道在哪里可以找到模板和静态文件等东西
(3) 然后使用 `route()` 装饰器来告诉 Flask触发视图函数的 URL
(4) 在上面的示例中，`/` 与 `view()` 视图函数绑定。因此当用户在浏览器中访问 Web服务器主页时，将呈现该函数的返回值


## run()

Flask 的 `run()` 方法将在本地开发服务器上运行应用程序，默认地址为： `http://127.0.0.1:5000`

我们可以通过设置 `run() `方法的参数来配置主机名，端口号，debug 模式

```python
app.run(host, port, debug)

# host
# 要监听的主机名，默认为 127.0.0.1(localhost)
# 设置为 0.0.0.0 以使服务器在外部可用

# port
# 监听的端口号，默认为 5000

# debug
# debug模式，默认为 False，即关闭 debug 模式
# 可通过设置为 True 开启 debug 模式
# 如果打开调试模式，那么服务器会在每次修改代码之后自动重启，并且当应用出错时还会提供了一个有用的调试器
```

## 访问 URL

启动我们的 flask 程序，此时可能在控制台看到一句 WARNING 警告

```
WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
```

提示我们当前为开发服务器，不要在生产部署中使用它

当我们在本地环境测试时，忽略即可，如果不想看到这一条警告，可以通过如下配置隐藏

```python
app.config['ENV'] = "development"
```

此时，打开浏览器，输入 `http://127.0.0.1:5000` ，应该就可以看到 **hello Flask** 字样了，我们的第一个 flask 程序也就执行成功了！

