<!-- TOC -->

- [插入数据](#%E6%8F%92%E5%85%A5%E6%95%B0%E6%8D%AE)
- [删除数据](#%E5%88%A0%E9%99%A4%E6%95%B0%E6%8D%AE)
- [修改数据](#%E4%BF%AE%E6%94%B9%E6%95%B0%E6%8D%AE)
- [查询数据](#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE)
    - [获取查询到的所有记录](#%E8%8E%B7%E5%8F%96%E6%9F%A5%E8%AF%A2%E5%88%B0%E7%9A%84%E6%89%80%E6%9C%89%E8%AE%B0%E5%BD%95)
    - [获取查询到的第一条记录](#%E8%8E%B7%E5%8F%96%E6%9F%A5%E8%AF%A2%E5%88%B0%E7%9A%84%E7%AC%AC%E4%B8%80%E6%9D%A1%E8%AE%B0%E5%BD%95)
    - [根据 ID 查询](#%E6%A0%B9%E6%8D%AE-id-%E6%9F%A5%E8%AF%A2)
    - [查询部分列](#%E6%9F%A5%E8%AF%A2%E9%83%A8%E5%88%86%E5%88%97)
    - [过滤筛选](#%E8%BF%87%E6%BB%A4%E7%AD%9B%E9%80%89)
    - [模糊查询](#%E6%A8%A1%E7%B3%8A%E6%9F%A5%E8%AF%A2)
    - [排序](#%E6%8E%92%E5%BA%8F)
    - [分页](#%E5%88%86%E9%A1%B5)
    - [聚合函数](#%E8%81%9A%E5%90%88%E5%87%BD%E6%95%B0)
    - [分组](#%E5%88%86%E7%BB%84)
    - [逻辑关系](#%E9%80%BB%E8%BE%91%E5%85%B3%E7%B3%BB)
- [参考](#%E5%8F%82%E8%80%83)

<!-- /TOC -->

## 插入数据

向数据库插入数据分为三个步骤

1. 创建 Python 对象
2. 把它添加到会话
3. 提交会话

通过实例化模型类即可创建一个新的对象，这个对象就对应着数据库中的一条记录  
这里的会话是 Flask-SQLAlchemy 的会话，它本质上是一个数据库事务的加强版本
add()    ==> 执行 INSERT 语句
commit() ==> 提交事务

```python
# 实例化对象
user1 = User(username="admin",password="admin")
user2 = User(username="guest",password="guest")

# 一次插入一条数据
db.session.add(user1)
db.session.add(user2)

# 一次插入多条
db.session.add_all([user1, user2])

# 提交到数据库
db.session.commit()
```

## 删除数据

删除记录与插入记录十分类似，使用 `delete()` 代替 `add()`

```python
db.session.delete(obj)
db.session.commit()
```

## 修改数据

```python
# 获取一条数据
user = User.query.get(1)
# 修改内容
user.name = "***"
# 插入并提交
db.session.add(user)
db.session.commit()
```

## 查询数据

Flask-SQLAlchemy 在 Model 类上提供了 query 属性。当访问它时，会得到一个新的所有记录的查询对象

`Users.query`  ==>  `select * from users`

假设 数据库 有如下条目：

| id   | name   | age  | score |
| :--- | :----- | :--- |:---|
| 1    | 张三   | 18   | 65    |
| 2    | 李四   | 16   | 72    |
| 3    | 王五   | 24   | 89    |
| 4    | 张三丰 | 29   | 91    |
| 5    | 李捕头 | 35   | 89    |

### 获取查询到的所有记录

`all()`

`return 对象列表`

```python
>>> data = Users.query.all()
>>> print(data)

[<Users 1>, <Users 2>, <Users 3>, <Users 4>, <Users 5>]
```

### 获取查询到的第一条记录

`first()`

`retutn 对象`

```python
>>> data = User.query.first()
>>> print(data)

<Users 1>
```

### 根据 ID 查询 

`get()`

```python
# 查询 ID 为 5 的用户
# select * from user where id = 5
>>> data = User.query.get("5")
>>> print(data)

<Users 5>
```

### 查询部分列

`db.session.query()`

```python
>>> data = db.session.query(Users.name,Users.age,).all()
[("张三",18),("李四",16),("王五",24),("张三丰",29),("李捕头",35)]
```

### 过滤筛选

`filter()`

```python
# 查询分数为 89 的用户
# 等效于 select * from user where score = "89"
>>> data = User.query.filter(User.score == "89").all()
```

### 模糊查询

_ 匹配一个字符
% 匹配 0 个 或者 多个

```python
# 查询姓名以 张 开头用户
# 等效于 select * from user where name like "张%"
>>> data = User.query.filter(User.name.like("张%")).all()
```

### 排序

```python
# 按照用户分数排序 默认升序
# 等效于 select * from user order by score
data = User.query.order_by(User.score).all()

# 降序排列
data = User.query.order_by(User.score.desc()).all()
```

### 分页

**limit** 返回数据的条数
**offset** 偏移，查询的起始位置，以下标进行偏移

```python
# 获取三条数据
data = User.query.limit(3).all()

# 从指定的下标 [从0开始] 开始向后获取数据
data = User.query.offset(2).all()

# 从指定下标开始向后获取 n 条数据
data = User.query.offset(2).limit(3).all()
```

**paginate**

```python
# 分页查询, 每页3个, 查询第2页的数据
pn = User.query.paginate(2, 3)

# 获取该页的数据
pn.items

# 获取当前的页码 
pn.page

# 获取总页数
pn.pages  
```

### 聚合函数

```python
# 导入聚合函数
from sqlclchemy import func

# 常用聚合方法： sum  max  min  count  avg

# 查询 18 岁以上的用户中的最高分数
data = db.session.query(func.max(User.score).filter(User.age > 18).all()
```

### 分组

```python
data = db.session.query(func.count(User.id),User.gender).group_by(User.gender).all()
```

### 逻辑关系

`and`
`or` 
`not`

```python
from sqlalchemy import and_,or_,not_

# and
# 获取 年龄大于16 并且 分数大于60 的用户
Users.query.filter(Users.age > 16,Users.score > 60).all()
Users.query.filter(and_(Users.age > 16,Users.score > 60)).all()

# or
# 获取 年龄大于16 或者 分数大于60 的用户
Users.query.fitler(or_(Users.age > 16,Users.score > 60)).all()

# not
# 获取 年龄不等于 18 的用户
Users.query.filter(Users.age != 18).all()
Users.query.filter(not_(Users.age == 18)).all()
```

## 参考

- [https://juejin.im/post/5bf741886fb9a049fa0f671e](https://juejin.im/post/5bf741886fb9a049fa0f671e)

- [https://blog.csdn.net/qq_35430000/article/details/86361721](https://blog.csdn.net/qq_35430000/article/details/86361721)

- [https://www.jianshu.com/p/8d085e2f2657](https://www.jianshu.com/p/8d085e2f2657)