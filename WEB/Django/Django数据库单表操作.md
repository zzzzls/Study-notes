<!-- TOC -->

- [Django 单表操作](#django-单表操作)
  - [增加数据](#增加数据)
  - [查询数据](#查询数据)
    - [all()](#all)
    - [get()](#get)
    - [first() & last()](#first--last)
    - [values()](#values)
    - [exists()](#exists)
    - [filter()](#filter)
    - [order_by()](#order_by)
    - [双下划线](#双下划线)
    - [聚合查询](#聚合查询)
    - [分组查询](#分组查询)
    - [F 查询](#f-查询)
    - [Q查询](#q查询)
    - [分页](#分页)
  - [修改数据](#修改数据)
  - [删除数据](#删除数据)

<!-- /TOC -->

# Django 单表操作

## 增加数据

```python
# (1) save 方法
per = Person(username="tom", age=18, address="北京市")
per.save()

# (2) create 方法
#     create 方法有返回值，返回当前对象
per = Person.objects.create(username="Q",age=35,address="唐人街")
print(per.username)
```

## 查询数据

### all()

返回符合条件的所有数据，类型为 **queryset 列表**

```python
users = Person.objects.all()
print(users)

# <QuerySet [<Person: Person object (1)>, <Person: Person object (2)>]>
```

### get()

- 返回符合条件的数据，类型为对象
- `get()` 仅返回一条数据，如果数据超过一条或者没有 则报错

```python
# 获取 id=1 的用户
user = Person.objects.get(id=1)

# 获取 age=18 的用户
# 若 age=18 的用户超过1人或者没有，则报错
# 仅当 age=18 的用户为1人时，返回对应对象
user = Person.objects.get(age=18)
```

### first() & last()

- `first()` 返回符合条件的第一条数据，类型为对象
- `last()` 返回符合条件的最后一条数据，类型为对象

```python
user = Person.objects.first()
user = Person.objects.last()
```

### values()

查询表中指定字段

```python
# 等效于 select username,age from person
user = Person.objects.values("username","age")

# <QuerySet [{'username': 'tom', 'age': 18}, {'username': 'Q', 'age': 35}]>
```

### exists()

判断查询结果 是否有数据存在，返回值为 bool

```python
flag = Person.objects.filter(age=19).exists()

# false
```

### filter()

过滤筛选，返回值为 **queryset 列表**

```python
# 查询 age=18 的所有用户
usres = Perosn.objects.filter(age=18)

# and 关系
users = Person.objects.filter(age=18, username="tom")
```

### order_by()

排序

```python
# 升序
users = Person.objects.order_by("age")

# 降序
users = Person.objects.order_by("-age")

# 多重排序
# 按照 age 排序，若 age 相同则按照 username 排序
users = Person.objects.order_by("age").order_by("username")
```

### 双下划线

```python
# 寻找 age 大于 18 的所有用户
users = Person.objects.filter(age__gt=18)

# 模糊查询 username中包含 j 的用户
# 等效于 select * from person where username like "%j%"
users = Perosn.objects.filter(username__contain="j")
```

|方法|	说明|
|:---|:---|
|`__gt`|	大于|
|`__gte`|	大于等于|
|`__lt`|	小于|
|`__lte`|	小于等于|
|`__contain`|模糊查询（包含），区分大小写|
|`__icontains`|模糊查询（包含），不区分大小写|
|`__in`|	范围查询|
|`__startswith`|	判断开头|
|`__endswith`|	判断结尾|
|`__range`|	范围查询|

### 聚合查询

```python
from django.db.models import Sum,Max,Min,Count,Avg

# 等效于 select count(id) from test_app_person where age=18
data = Person.objects.filter(age=18).aggregate(Count("id"))

# 修改返回值中的 key
data = Person.objects.filter(age=18).aggregate(Count("id"))
```

### 分组查询

```python
# 根据年龄进行分组查询
# 等效于 select age,count(id) from test_app_person group by age
users = Person.objects.all().values("age").annotate(Count("age"))
```

### F 查询

F 查询用于同一张表的其它字段

```python
from django.db.models import F

# 查询 age 等于 id+10 的用户
# 等效于 select username from test_app_person where age = (id+10);
users = Person.objects.filter(age=F("id")+10).all().values("username")

# 给表中所有人的 age 加 1
Person.objects.all().update(age=F("age")+1)
```

### Q查询

逻辑关系查询

- `&` : and 关系
- `|` : or 关系
- `~` : not 关系

```python
from django.db.models import Q
# 查询年龄 大于 10 并且 性别为 女 的用户
users = Person.objects.filter(Q(age__gt=10) & Q(gender="女")).all()

# 查询年龄 大于 10 或者 性别为 女 的用户
users = Person.objects.filter(Q(age__gt=10) | Q(gender="女")).all()

# 查询非 女性 的用户
usess = Perosn.objects.filter(~Q(gender="女")).all()
```

### 分页

```python
users = Person.objects.all()[1:2]
```

## 修改数据

```python
# (1) save() 修改数据
user = Person.objects.get(id=3)
user.age = 19
user.save()

# (2) update() 修改数据
# update() 属于 queryset 的方法

# 修改单条数据
Person.objects.filter(id=4).update(age=20)

# 修改多条数据
Person.objects.filter(age=18).update(age=21)
```

## 删除数据

```python
# delete() 删除数据
# delete() 在 对象 或者 queryset 后边都可以使用

# 删除 id 为 6 的用户
Person.objects.get(id=6).delete()

# 删除 age > 35 的用户
Person.objects.filter(age__gt=35).delete()
```