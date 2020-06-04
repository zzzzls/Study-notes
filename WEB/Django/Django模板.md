<!-- TOC -->

- [Django 模板](#django-%E6%A8%A1%E6%9D%BF)
    - [创建模板文件夹](#%E5%88%9B%E5%BB%BA%E6%A8%A1%E6%9D%BF%E6%96%87%E4%BB%B6%E5%A4%B9)
    - [视图返回界面](#%E8%A7%86%E5%9B%BE%E8%BF%94%E5%9B%9E%E7%95%8C%E9%9D%A2)
    - [返回数据到模板](#%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE%E5%88%B0%E6%A8%A1%E6%9D%BF)
    - [模板语法](#%E6%A8%A1%E6%9D%BF%E8%AF%AD%E6%B3%95)
        - [展示变量](#%E5%B1%95%E7%A4%BA%E5%8F%98%E9%87%8F)
        - [控制语句](#%E6%8E%A7%E5%88%B6%E8%AF%AD%E5%8F%A5)
        - [过滤器](#%E8%BF%87%E6%BB%A4%E5%99%A8)
        - [静态文件](#%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6)
        - [模板继承 & 加载](#%E6%A8%A1%E6%9D%BF%E7%BB%A7%E6%89%BF--%E5%8A%A0%E8%BD%BD)

<!-- /TOC -->

# Django 模板

模板是一个文本，用于分离文档的表现形式和内容

## 创建模板文件夹

1. 在 项目中创建 `templates` 文件夹，并建立 `index.html` 文件

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    templates/
        index.html
```

2. 在 `settings.py` 中配置

![img](http://img.zzzzls.top/06-02_56472.png&git)

## 视图返回界面

```python
from django.shortcuts import render_to_response
def index(request):
    return render_to_response("index.html")
```

## 返回数据到模板

```python
from django.shortcuts import render_to_response
def index(request):
    dct = {
        "name": "tom",
        "age": 18
    }
    return render_to_response("index.html", locals())
```

## 模板语法

### 展示变量

```html

<!-- 展示字典值 -->
<p>{{ dct.name }}</p>
<p>{{ dct.age }}</p>

<!-- 列表 -->
<p>{{ hobby.1 }}</p>
```

### 控制语句

```html
<!-- if 语句 -->
{% if age > 18 %}
    大于18
{% elif age == 18 %}
    等于18
{% else %}
    小于18
{% endif %}

{% ifequal age 18 %}
    <p>等于18...</p>
{% endifequal %}

<!-- for语句 -->
{% for one in hobby %}
    <p>{{ one }}</p>
{% endfor %}

{% for k,v in dct.items %}
    <p>{{ k }}: {{ v }}</p>
{% endfor %}
```

`forloop` 类似于 jinja2 中的 loop，是一个 Django 模板中的变量，用于记录循环的状态

|属性|描述|
|:---|:---|
|counter0|循环计数器（从0开始）|
|counter|循环计数器（从1开始）|
|revcounter0|倒序循环计数器（从0开始）|
|revcounter|倒序循环计数器（从1开始）|
|first|是否为第一次循环|
|last|是否为最后一次循环|

### 过滤器

**(1) 内置过滤器**

```html
<p>{{ dct.name | upper | lower }}</p>
<p>{{ dct.html | safe }}</p>
<!-- 当前数值增加 10 -->
<p>{{ dct.age | add:10 }}</p>
```

(2) 自定义过滤器

...


### 静态文件

**(1) 创建静态文件目录**

在项目目录中创建 static 目录

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    templates/
        index.html
    static/
        nb.png
```

**(2) 在 settings.py 中配置**

在文件末尾添加配置项：

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static")
]
```

**(3) 模板文件中使用静态文件**

```html
<img src="/static/nb.png">

<!-- 方法2 -->
{% load static %}
<img src="{% static 'nb.png' %}" alt="">
```

### 模板继承 & 加载

```html
<!-- 继承父模板 -->
{% extends "base.html" %}

<!-- 覆盖父模板 title 块的内容 -->
{% block title %}Index{% endblock %}


<!-- 导入 cs.html 的内容 -->
{% include "cs.html" %}
```

