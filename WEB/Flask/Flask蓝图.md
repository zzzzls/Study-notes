# 蓝图

为了在一个或多个应用中，使应用模块化并且支持常用方案，Flask引入了 蓝图 的概念。蓝图可以极大地简化大型应用并为扩展提供集中的注册入口

# 为什么使用蓝图

Flask 中蓝图有以下用途：

- 把一个应用分解为一套蓝图。这是针对大型应用的理想方案：一个项目可以实例化一个应用，初始化多个扩展，并注册许多蓝图
- 在一个应用的 URL 前缀和（或）子域上注册一个蓝图。 URL 前缀和（或）子域的 参数成为蓝图中所有视图的通用视图参数（缺省情况下）
- 使用不同的 URL 规则在应用中多次注册蓝图
- 通过蓝图提供模板过滤器、静态文件、模板和其他工具。蓝图不必执行应用或视图 函数
- 当初始化一个 Flask 扩展时，为以上任意一种用途注册一个蓝图

# 基本用法

```python
# flask_project/views/bl.py

# 1. 导入蓝图的模块
from flask import Blueprint

# 2. 实例化蓝图对象
bl = Blueprint("bl",__name__)

# 3.使用蓝图编写路由
@bl.route("/")
def view():
    return "首页"

@bl.route("/index/")
def index():
    return "index"
```

要创建一个蓝图对象，你需要 `import Blueprint()` 类并用参数 `name` 和 `import_name` 初始化。通常使用 `__name__`，一个表示当前模块的特殊的 Python 变量，作为 `import_name` 的取值

假如采用分区式架构，你要告诉 Flask 某个蓝图是有着自己的模板和静态文件夹的。下面是这种情况下我们的定义大概的样子：

```python
bl = Blueprint("bl",__name__,
                templates_folder="temolates",
                static_folder="static")
```

现在我们定义好了蓝图，是时候向 Flask app 注册它了

```python
#flask_project/main.py

from flask import Flask
from views.bl import bl

app = Flask(__name__)
# 4. 注册蓝图
app.register_blueprint(bl)
```

现在 `bl.py` 中定义的路由会被注册到应用中，就像是通过 `@app.route()` 定义的

# URL 前缀

蓝图允许我们定义静态的或动态的前缀。举个例子，我们可以告诉 Flask 蓝图中所有的路由应该以 `/bl` 作为前缀，这样是一个静态前缀；

**静态前缀设置**

```python
# 在实例化的时候设置 URL 前缀
profile = Blueprint('profile', __name__, url_prefix='/bl')

# 在注册的时候设置 URL 前缀
app.register_blueprint(profile, url_prefix='/bl')
```

尽管两种方式在技术上没有区别，最好还是在注册的同时定义前缀。这样使得前缀的定义可以集中到顶级目录中

**动态前缀设置**

详见 [在Flask蓝图中使用动态URL前缀](https://segmentfault.com/a/1190000002480266)

# 使用蓝图进行项目目录结构优化

## 功能式架构

在功能式架构中，按照每部分代码的功能来组织你的应用。所有模板放到同一个文件夹中，静态文件放在另一个文件夹中，而视图文件放在第三个文件夹中

```
yourapp/
    __init__.py
    static/
    templates/
        home/
        control_panel/
        admin/
    views/
        __init__.py
        home.py
        control_panel.py
        admin.py
    models.py
```
除了 `yourapp/views/__init__.py` ，在 `yourapp/views/` 文件夹中的每一个 `.py` 文件都是一个蓝图。在 `yourapp/__init__.py` 中，我们将加载这些蓝图并在我们的 Flask()对象中注册它们

## 分区式架构

在分区式架构中，按照每一部分所属的蓝图来组织你的应用，管理面板的所有的模板，视图和静态文件放在一个文件夹中，用户控制面板的则放在另一个文件夹中

```
yourapp/
    __init__.py
    admin/
        __init__.py
        views.py
        static/
        templates/
    home/
        __init__.py
        views.py
        static/
        templates/
    control_panel/
        __init__.py
        views.py
        static/
        templates/
    models.py
```

在上面的分区时结构，每一个 yourapp/ 之下的文件夹都是一个独立的蓝图。所有的蓝图通过顶级的 `__init__.py` 注册到 Flask() 中

## 哪种更胜一筹

选择使用哪种架构实际上是一个个人问题。两者键的唯一区别式表达层次性的方式不同，你可以使用任意一张方式架构 Flask 应用

- 如果你的应用式由独立的，仅仅共享模型和配置的各组件组成，分区式将是一个好选择

- 如果你的应用的组件之间的联系较为紧密，使用功能式架构会更好