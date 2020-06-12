<!-- TOC -->

- [Django 缓存框架](#django-%E7%BC%93%E5%AD%98%E6%A1%86%E6%9E%B6)
- [设置缓存](#%E8%AE%BE%E7%BD%AE%E7%BC%93%E5%AD%98)
    - [文件系统缓存](#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E7%BC%93%E5%AD%98)
    - [数据库缓存](#%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BC%93%E5%AD%98)
    - [局部内存缓存](#%E5%B1%80%E9%83%A8%E5%86%85%E5%AD%98%E7%BC%93%E5%AD%98)
    - [Memcached](#memcached)
- [使用缓存](#%E4%BD%BF%E7%94%A8%E7%BC%93%E5%AD%98)
    - [全站缓存](#%E5%85%A8%E7%AB%99%E7%BC%93%E5%AD%98)
    - [视图缓存](#%E8%A7%86%E5%9B%BE%E7%BC%93%E5%AD%98)
    - [路由缓存](#%E8%B7%AF%E7%94%B1%E7%BC%93%E5%AD%98)
    - [模板缓存](#%E6%A8%A1%E6%9D%BF%E7%BC%93%E5%AD%98)
    - [底层缓存](#%E5%BA%95%E5%B1%82%E7%BC%93%E5%AD%98)
- [参考](#%E5%8F%82%E8%80%83)

<!-- /TOC -->

# Django 缓存框架

动态网站存在一个基本权衡 -- 它们是动态的。

每次用户请求一个页面，web服务器需要提供各种各样的计算:  **数据库查询** --> **模板渲染** --> **业务逻辑** --> **建立页面呈现给用户**

从处理开销的角度来看，这比标准读取文件系统服务安排的开销要高的多！

对于大多 web 应用程序，这种开销并不算什么，但对于中大型网站，必须尽可能减少开销，**这就是缓存的用武之地**

缓存一些经过大量费时的计算结果，这样你下次就不用执行这种计算。下面一些伪代码解释了动态网站生成页面的时候，缓存是怎么工作的

```python
given a URL , try finding that page in cache

if that page is in the cache:
    return the cache page
else:
    generate the page
    save the generated page in the cache (for next time)
    return the generated page
```

Django 带有一个强大的缓存系统，你可以将动态页面保存，这样就不用每次请求页面时都计算。为方便起见，Django 提供了不同级别的缓存粒度：你可以缓存特定视图，或者只缓存那些难以生成的片段，或者缓存整个网站

# 设置缓存

先指明缓存数据所存放的位置，无论是一个**数据库**，还是**文件系统**，或者直接存放在**内存**。这是一个影响缓存性能的重要决定，因为某些缓存类型会比其它缓存类型更快

在项目的配置文件 `settings.py` 中可以通过 **CACHES** 配置缓存

## 文件系统缓存

将每个缓存值序列换并存储在一个单独的文件中，无需安装其它的程序，设置好了就可以使用

```python
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 缓存文件夹
        'LOCATION': os.path.join(BASE_DIR,'cache_file'),
    }
}
```

## 数据库缓存

使用数据库作为缓存，会将缓存的数据保存在指定的表中

```python
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 缓存 表
        'LOCATION': 'my_cache',
    }
}
```

然后执行命令创建该表

`python manage.py createcachetable`

## 局部内存缓存

这种缓存方式会将**缓存保存于每个进程的内存中**，这意味着缓存不可跨进程共享，很显然这样比较浪费内容空间，**不适用于生产环境**，但对于开发环境则比较方便

```python
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # 变量 , 缓存的名称
        'LOCATION': 'unique-mycache',
    }
}
```

LOCATION 被用于标识各个内存存储。如果只有一个 locmem 缓存，你可以忽略 LOCATION 。但是如果你有多个本地内存缓存，那么你至少要为其中一个起个名字，以便将它们区分开

## Memcached

**Memcached** 是一个完全基于内存的缓存服务器，是 Django 原生支持的最快，最高效的缓存类型

Memcached 以一个守护进程的形式运行，并且被分配了指定数量的 RAM，它所做的就是提供一个快速接口用于在缓存中添加，检索和删除数据。所有数据都直接存储在内存中，因此不会产生数据库或文件系统使用的开销

- [官网](https://memcached.org/)
- [Memcached 教程 | 菜鸟教程](https://www.runoob.com/memcached/memcached-tutorial.html)

**(1) 安装 Memcached**

- [Windows 下安装 Memcached](https://www.runoob.com/memcached/window-install-memcached.html)
- [Linux Memcached 安装](https://www.runoob.com/memcached/memcached-install.html)


**(2) 安装 Memcached 模块**

`pip install python-memcached`

**(3) 配置 Memcached**

```python
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # memcached 启动的 ip + port
        'LOCATION': '127.0.0.1:11211',
    }
}
```

# 使用缓存

## 全站缓存

在配置文件 **MIDDLEWARE** 设置中添加 `django.middleware.cache.UpdateCacheMiddleware` 和 `django.middleware.cache.FetchFromCacheMiddleware`

```python
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',

    ...

    'django.middleware.cache.FetchFromCacheMiddleware',
]
```

> `update` 中间件必须放在列表首位，并且 `fetch` 中间件必须在最后一位

## 视图缓存

使用缓存框架的通用办法是对单独的视图结果进行缓存。`django.views.decorators.cache` 定义了一个 cache_page 装饰器，它将自动缓存视图的响应。使用方法很简单：

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index(request,id):
    return render(request,"restful/index.html")
```

cache_page 使用了一个单独的参数：缓存过期时间，以秒为单位。在上面的例子里，视图的结果将缓存 15 分钟。（注意，此处用 60 * 15 这样的方式编写，目的是方便阅读。 60 * 15 将计算为 900，也就是 15分钟乘以每分钟60秒

## 路由缓存

```python
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('index/', cache_page(60 * 15)(index)),
]
```

## 模板缓存

```python
# 导入标签
{% load cache %}
# 第一个参数  缓存时间(以秒为单位)
# 第二个参数  缓存片段的名称
{% cache 500 sidebar %}
    .. sidebar ..
{% endcache %}
```

## 底层缓存

有时，缓存整个渲染页面并不会带来太多好处，事实上，这样会很不方便。

或许，你的站点包含了一个视图，它的结果依赖于许多费时的查询，而且结果会随着时间变化而改变。在这个情况下，使用站点或视图缓存策略提供的全页面缓存并不理想，因为不能缓存所有结果（一些数据经常变动），不过你仍然可以缓存几乎没有变化的结果。

像这样的情况，Django 公开了一个简单的，底层的缓存 API 。你可以使用这个 API 以任意级别粒度在缓存中存储对象。你可以缓存任何可以安全的 pickle 的 Python 对象：模型对象的字符串、字典、列表，或者其他

**基本用法**

|方法|描述|
|:---|:---|
|set|设置单个缓存|
|set_many|设置多个缓存|
|add|键不存在则添加，存在则不执行|
|get|获取对应键的值|
|get_many|返回多个键的值|
|delete|删除键|
|clear|删除缓存中所有键|

```python
from django.core.cache import cache

cache.set(key, value, timeout)

cache.set_many(dict, timeout)

# 如果 key 不存在 返回 None
cache.get(key)
```

# 参考

- [Django 缓存框架 | Django 文档](https://docs.djangoproject.com/zh-hans/2.2/topics/cache)
