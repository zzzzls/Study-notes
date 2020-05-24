<!-- TOC -->

- [渲染模板](#%e6%b8%b2%e6%9f%93%e6%a8%a1%e6%9d%bf)
- [传递参数到模板中](#%e4%bc%a0%e9%80%92%e5%8f%82%e6%95%b0%e5%88%b0%e6%a8%a1%e6%9d%bf%e4%b8%ad)
- [过滤器](#%e8%bf%87%e6%bb%a4%e5%99%a8)
- [模板语法](#%e6%a8%a1%e6%9d%bf%e8%af%ad%e6%b3%95)
  - [变量](#%e5%8f%98%e9%87%8f)
  - [注释](#%e6%b3%a8%e9%87%8a)
  - [控制结构](#%e6%8e%a7%e5%88%b6%e7%bb%93%e6%9e%84)
    - [for](#for)
    - [if](#if)
- [模板继承](#%e6%a8%a1%e6%9d%bf%e7%bb%a7%e6%89%bf)
- [包含](#%e5%8c%85%e5%90%ab)
- [参考资料](#%e5%8f%82%e8%80%83%e8%b5%84%e6%96%99)

<!-- /TOC -->

## 渲染模板

在 Python 内部生成 HTML 不好玩，且相当笨拙。因为你必须自己负责 HTML 转义，来确保应用的安全。因此，Flask 自动为您配置 Jinja2 模板引擎

使用 `render_template()` 方法可以渲染模板，你只需要提供模板名称和需要作为参数传递给模板的变量就可以了

下面是一个简单的模板渲染的例子：

```python
from flask improt render_template

@app.route("/hello/")
def view():
    return render_template("index.html")
```

flask 将尝试在 `templates` 文件夹中寻找 HTML 文件。因此，如果你的应用是一个模块，那么模板文件夹应该在模块同级目录下

```
/run.py
/templates
    /index.html
```

## 传递参数到模板中

(1) **变量传值**

```python
return render_template("index.html", name="zong", age=18, hobby=["唱歌","游泳"])
```

```html
<body>
<p>姓名: {{ name }}</p>
<p>年龄: {{ age }}</p>
<p>爱好: {{ hobby }}</p>
</body>
```

(2) **字典传值**

```python
dct = {
    "name": "zong",
    "age": 18,
    "hobby": ["唱歌","游泳"]
}
return render_template("index.html", dct=dct)
```

```html
<body>
<p>姓名: {{ dct.name }}</p>
<p>年龄: {{ dct.age }}</p>
<p>爱好: {{ dct.hobby }}</p>
</body>
```

## 过滤器

变量可以通过过滤器修改，过滤器和变量用管道符号 `|` 分割，并且也可以用圆括号传递可选参数。多个过滤器可以链式调用，前一个多滤器的输出会被作为后一个过滤器的输入

例如 `{{ name|striptags|title }}` 会移除 name 中所有 HTML 标签并且改写为标题样式的大小写格式

过滤器接受带圆括号的参数，如同函数调用，如 把一个列表用逗号链接起来

`{{ list|join(',') }}`


**常用过滤器:**

|过滤器|示例|描述|
|:---|:---|:---|
|`striptags`|`bq|striptags`|去除标签|
|`reverse`|`test|reverse`|字符串反转|
|`default`|`url|default("***")`|默认值|
|`safe`|`bq|safe`|将值标记为安全，不再自动转义|
|`length`|`[1,2,3]|length`|列表长度|
|`sum`|`[1,2,3]|sum`|列表求和|
|`sort`|`[1,2,3]|sort`|列表排序|

**自定义过滤器:**

过滤器的本质是函数，当模板内置的过滤器不能满足要求，可以自定义过滤器。自定义过滤器有两种实现方式：

(1) `add_temp_filter()`

```python
def my_filter(test):
    return "***"

app.add_temp_filter(my_filter,"my_filter")
```

> 可以给过滤器指定一个名字，如果不指定，默认为函数名

(2) `@app.template_filter`

```python
@app.template_filter("mf")
def my_filter(args):
    return "***"
```

> 自定义的过滤器名称如果和内置的过滤器重名，会覆盖内置的过滤器

## 模板语法

模板仅仅是文本文件，可以生成任何基于文本的格式（HTML,XML,CSV等）。它并没有特定的扩展名，`.html` 和 `.xml` 都是可以的

模板包含 **变量** 和 **表达式**，这两者在模板求值的时候会被替换为值。模板中还有标签，控制模板的逻辑。Jinja2 模板语法的大量灵感来自 Django 和 Python

下面是一个最小的模板:

```html
<!DOCTYPE html">
<html">
<head>
    <title>test</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}
</body>
</html>
```

这里有两种分隔符 `{% ... %}` 和 `{{ ... }}`，前者用于执行诸如 for 循环 或 赋值的语句，后者把表达式的结果打印到模板上

### 变量

将变量传到到模板后，可以使用 `.` 来访问变量的属性，作为替代，也可以使用下标语法 `[]`，下面几行效果是一样的

```python
{{ foo.bar }}
{{ foo['bar'] }}
```

### 注释

要把模板中一行的部分注释掉，默认使用 `{# ... #}` 注释语法

### 控制结构

控制结构指的是所有的可以控制程序流的东西 --条件(if/elif/else)、for循环等，控制结构在默认语法中以 `{% ... %}` 块的形式出现

#### for

遍历序列中的每项

```python
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
```

在一个 for 循环块中你可以访问这些特殊的变量

|变量|描述|
|:---|:---|
|`loop.index`|当前循环迭代的次数 (从 1 开始)|
|`loop.index0`|当前循环迭代的次数 (从 0 开始)|
|`loop.revindex`|	到循环结束需要迭代的次数（从 1 开始）|
|`loop.revindex0`|	到循环结束需要迭代的次数（从 0 开始）|
|`loop.first`|	如果是第一次迭代，为 True|
|`loop.last`|	如果是最后一次迭代，为 True|
|`loop.length`|	序列中的项目数|
|`loop.cycle`|	在一串序列间期取值的辅助函数。见下面的解释|

在 for 循环中，可以使用特殊的 `loop.cycle` 辅助函数，伴随循环在一个字符串 / 变量列表中周期取值

```python
{% for row in rows %}
    <li class="{{ loop.cycle('odd', 'even') }}">{{ row }}</li>
{% endfor %}
```

> 与 python 中不同，模板中的循环不能 break 或 continue

#### if

```python
{% if a == 1 %}
    a == 1
{% elif a == 2 %}
    a == 2
{% else %}
    a != 1 && a != 2
{% endif %}
```

## 模板继承

Jinja 中最强大的部分就是模板继承，可以**把一写公共的代码放在父模块中，避免每个模块写同样的代码**。同时父模板中提前在可能更改的地方定义好接口，方便子模板进行修改！

**基本的父模板**

这个模板，我们习惯性叫做 `base.html`，定义了一个简单的 HTML 骨架文档

```html
<!DOCTYPE html>
<html>
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>
        {% block title %}{% endblock %} - My Webpage
    </title>
    {% endblock %}
</head>
<body>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
    
    <div id="footer">
        {% block footer %}{% endblock %}
    </div>
</body>
</html>
```

所有的 block 标签告诉模板引擎子模板可以覆盖模板中的这些部分

```python
{% block 接口名 %}

{% endblock %}
```

**子模板**

```python
# 继承父模板
{% extends "base.html" %}

# 覆盖父模板 title 块的内容
{% block title %}Index{% endblock %}

{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}

{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome on my awesome homepage.
    </p>
{% endblock %}
```

## 包含

include 语句用于包含一个模板，并在当前命名空间中返回那个文件的内容渲染结果

```html
<!-- cs.html -->
<ul>
    <li>Python</li>
    <li>Java</li>
    <li>PHP</li>
    <li>GO</li>
    <li>C++</li>
</ul>
```

```html
<!-- index.html -->

<!-- 导入 cs.html 的内容 -->
{% include "cs.html" %}

<!-- 导入 cs.html 的内容，如果 该文件不存在，模板忽略该语句 -->
{% include "cs.html" ignore missing %}
```

> 一个模板中可以多次使用 include 语句
> include 可以和 模板继承同时使用

## 参考资料

[Jinja2 中文手册](https://docs.pythontab.com/jinja/jinja2/templates.html)




