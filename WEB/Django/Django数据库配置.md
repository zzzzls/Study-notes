<!-- TOC -->

- [数据库配置](#%E6%95%B0%E6%8D%AE%E5%BA%93%E9%85%8D%E7%BD%AE)
    - [SQLite](#sqlite)
    - [Mysql](#mysql)
        - [使用 Mysql 数据库常见错误](#%E4%BD%BF%E7%94%A8-mysql-%E6%95%B0%E6%8D%AE%E5%BA%93%E5%B8%B8%E8%A7%81%E9%94%99%E8%AF%AF)
- [建模](#%E5%BB%BA%E6%A8%A1)
    - [常用字段](#%E5%B8%B8%E7%94%A8%E5%AD%97%E6%AE%B5)
    - [常用属性](#%E5%B8%B8%E7%94%A8%E5%B1%9E%E6%80%A7)
    - [ImageField 保存图片](#imagefield-%E4%BF%9D%E5%AD%98%E5%9B%BE%E7%89%87)
- [数据迁移同步](#%E6%95%B0%E6%8D%AE%E8%BF%81%E7%A7%BB%E5%90%8C%E6%AD%A5)

<!-- /TOC -->

# 数据库配置

## SQLite

打开 `settings.py` 找到如下配置项：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

通常，这个文件使用 SQLite 作为默认数据库，所以无需额外操作

**ENGINE**

可选值有：`'django.db.backends.sqlite3'`，`'django.db.backends.postgresql'`，`'django.db.backends.mysql'`，或 `'django.db.backends.oracle'`等

**NAME**

数据库的名字，使用使用的是 SQLite，数据库将是电脑上的一个文件，在这种情况下，**NAME** 应该是此文件的绝对路径，包括文件名。默认值 `os.path.join(BASE_DIR, 'db.sqlite3')` 将会把数据库文件储存在项目的根目录

>如果你不使用 SQLite，则必须添加一些额外设置，比如 USER 、 PASSWORD 、 HOST 等等

## Mysql

(1) 在 Mysql 中创建一个数据库

`CREATE DATABASE test DEFAULT CHARSET=UTF8`

(2) `settings.py` 文件中修改配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': test,         # 数据库名字
        'USER': 'root',       # 数据库用户名
        'PASSWORD': 'root',   # 数据库密码
        'HOST': '127.0.0.1',  # mysql 主机ip
        'PORT': '3306'        # mysql 端口
    }
}
```

### 使用 Mysql 数据库常见错误

**(1) `django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module`**

**原因**：Django 连接 MySQL 时默认使用 MySQLdb 驱动，但是 MySQLdb 并不支持 Python3，所以我们需要在项目根目录下的 `__init__.py` 手动进行配置使用 pymysql 驱动

![img](http://img.zzzzls.top/06-03_37933.png&git)

**解决办法**：在项目的初始化文件 `__init__.py` 中，写入如下代码

![img](http://img.zzzzls.top/06-03_12558.png&git)

(2) **`ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3`**

**原因**：上一个问题解决后，大概率遇到这个问题。没关系，仔细看下倒数第三行，已经告诉你是在 `base.py` 第 36 行报的错

![img](http://img.zzzzls.top/06-03_367578.png&git)

**解决办法**：根据报错提示的路径打开 `base.py` ，将 35，36 行代码注释即可

![img](http://img.zzzzls.top/06-03_26133.png&git)

**(3) `'str' object has no attribute 'decode'`**

**原因**：如果前边两个问题你遇到了，那你多半还会遇到这个问题。在 Python3 中，str 只有 `encode()` 方法，bytes 之后 `decode()` 方法，这个估计是 Django 的 BUG 了

![img](http://img.zzzzls.top/06-03_22677.png&git)

**解决办法**：根据错误提示打开报错文件 `operations.py` ，找到第 146 行，将 decode 修改为 encode 即可

![img](http://img.zzzzls.top/06-03_8365.png&git)


# 建模

```python
# app/models.py

from django.db import models
class Person(models.Model):
    # django 中的模型，会自动创建 自增主键 id
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    address = models.TextField()

    # 设置 表名
    # 若不设置 ,默认表名为  appname_类名(小写)
    class Meta:
        db_table = "person"
```

## 常用字段

| 字段          | 描述                                                    |
| :------------ | :------------------------------------------------------ |
| CharField     | 字符串类型，对应数据库中的varchar，需要指定长度         |
| IntegerField  | 整形                                                    |
| FloatField    | 浮点型                                                  |
| TextField     | 文本型                                                  |
| DateField     | 日期类型                                                |
| DateTimeField | 日期类型                                                |
| EmailField    | 邮箱类型                                                |
| FileField     | 文件类型                                                |
| ImageField    | 图片类型，需要依赖pillow模块，同时需要指定upload_to属性 |


## 常用属性

|属性|	说明|
|:---|:---|
|max_length|	字符串类型中，指定最大长度|
|verbose_name|	能够起到注释的作用，主要是在admin站点管理中以中文的形式显示|
|default|	默认值|
|blank|	可以为空，常用于字符串，表单为空|
|null|	可以为null，常用于数字和时间，数据库内容为null|
|unique|	不能重复|
|upload_to|	指定上传的路径|
|auto_now|	默认使用当前时间|

## ImageField 保存图片

(1) 安装 pillow 模块

`pip install pillow`

(2) settings 中增加配置
```
MEDIA_ROOT = os.path.join(BASE_DIR,"static")
```

(3) 定义模型，指定图片上传路径

```python
class Person(models.Model):

    ...

    picture = models.ImageField(upload_to="images",verbose_name="头像")

    ...
```

(4) 视图保存图片

```python
def user(request):
    picture = request.FILES.get("picture")
    user = Person.objects.get(id=1)
    user.picture = picture
    user.save()
```

图片就会自动保存在 `/static/images/` 文件夹下了，数据库中存储的则是 `images/filename`

# 数据迁移同步

- 检测环境，配置是否正确
`python manage.py check`

<br>

- 生成迁移文件
  `python manage.py makemigrations`

<br>

- 执行迁移文件，完成表格同步
  `python manage.py migrate`

