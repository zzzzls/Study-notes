# 管理器

**Manager** 是一种接口，它赋予了 Django 模型操作数据库的能力。Django 每个模型拥有至少一个 Manager

## 管理器名称

默认情况下，Django 为每个模型添加了一个名为 **objects** 的 **Manager**。不过，若向将 **objects** 用作字段名，或想使用 **objects** 以外的 **Manager** 名字，就要在模型基类中重命名

```python
from django.db import models

class Student(models.Model):
    query = models.Manager()

    ...

```

使用这个实例模型是，**Student.objects** 会产生一个 **AttributeError** 异常，而 **Student.query.all()** 将返回所有 Student 对象的列表

## 自定义管理器

继承基类 Manager ，在模型中实例化自定义 Mandager，你就可以在该模型中使用自定以的 Mandager

自定义 Manager 可以实现以下两种功能：
1. 添加额外的 Manager 方法
2. 修改 Manager 返回的原始 QuerySet

### 添加额外的管理器方法

自定义 Manager 方法能返回任何东西，没必要强制它必须返回一个 QuerySet

例如：如下这个自定义 Manager 提供了一个方法，返回所有 age>18 的 Student 对象姓名列表

```python
from django.db import models

class MyManager(Manager):
    def gt_age_students(self,t_id):
        students = Student.objects.filter(age__gt=18)
        stu_name_list = []
        for stu in students:
            stu_name_list.append(stu.username)
        if stu_name_list:
            return stu_name_list
        else:
            return None

class Student(models.Model):
    username = models.CharField(max_length=32)
    gender = models.IntegerField()
    age = models.IntegerField()
    objects = MyManager()
```

### 修改管理器的初始 QuerySet

Manager 的基础 QuerySet 会返回系统中所有的对象，例如，使用以下模型：

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
```

语句 `Book.objects.all()` 会返回数据库中所有的书

你可以通过重写 `Manger.get_queryset()` 方法来覆盖 Manager 的基础 QuerySet

例如，以下模型有两个 **Manager** ，一个返回所有对象，另一个仅返回 *马云* 写的书

```python
class MaYunBookManager(models.Manager):
    def query_set(self):
        retrun super().query_set().filter(author="mayun")

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    # 默认的 Manager
    objects = models.Mandager()
    # 新增的 Manager
    mayun_objects = models.Manager()
```

使用这个实例模型时，`Book.objects.all()` 会返回数据库中所有的书，而 `Book.mayun_objects.all()` 仅返回 *马云* 写的书

本例同时介绍了另一个有趣的技巧：在一个模型中使用多个管理器。你可以为一个模型添加任意多个 Manager() 

# 参考

[管理器 - Django 文档](https://docs.djangoproject.com/zh-hans/2.2/topics/db/managers/)