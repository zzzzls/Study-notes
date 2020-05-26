<!-- TOC -->

- [封装](#%E5%B0%81%E8%A3%85)
- [flask-sqlalchemy 关系](#flask-sqlalchemy-%E5%85%B3%E7%B3%BB)
    - [一对多](#%E4%B8%80%E5%AF%B9%E5%A4%9A)
        - [创建模型](#%E5%88%9B%E5%BB%BA%E6%A8%A1%E5%9E%8B)
        - [正向 & 反向](#%E6%AD%A3%E5%90%91--%E5%8F%8D%E5%90%91)
        - [增加数据](#%E5%A2%9E%E5%8A%A0%E6%95%B0%E6%8D%AE)
        - [查询数据](#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE)
    - [多对多](#%E5%A4%9A%E5%AF%B9%E5%A4%9A)
        - [创建模型](#%E5%88%9B%E5%BB%BA%E6%A8%A1%E5%9E%8B)
        - [增加数据](#%E5%A2%9E%E5%8A%A0%E6%95%B0%E6%8D%AE)
        - [查询数据](#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE)
    - [一对一](#%E4%B8%80%E5%AF%B9%E4%B8%80)
    - [参考](#%E5%8F%82%E8%80%83)

<!-- /TOC -->

# 封装

```python
# 抽取公共内容到 Base 类中
class Base(db.Model):
    # 将父类置为 抽象类, 不能实例化, 只能被继承
    # 置为 抽象类后, Base类 不会生成表
    __abstract__ = True
 
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    # 封装 添加方法
    def save(self):
        db.session.add(self)
        db.session.commit()

    # 封装 删除方法
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Users(Base):
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    score = db.Column(db.Integer)
```

# flask-sqlalchemy 关系

## 一对多

OA 项目中，用户表和职位表就是 一对多 的关系，一个用户一个职位，一个职位中有多个用户

一对多 通过 `db.ForeignKey` 和 `db.relationship` 来声明两个模型之间的关系

### 创建模型

```python
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    score = db.Column(db.Integer)

    # db.ForeignKey 声明一个外键，关联 position表中的id属性
    # 外键 通常定义在 多 的以一方
    p_id = db.Column(db.Integer, db.ForeignKey("position.id"))

class position(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))

    # db.relationship 构建表之间的关联关系
    # 通常定义在 一 的一方
    # 第一个参数 是关联类的名字
    # 第二个参数 backref 是一个反向身份的代理
    #   会在 关联类中新增一个属性，供反向引用时调用，使用 user.pos 方法就能返回 user 对应的 position 对象
    # 返回值为 当前对象 的所有关联对象
    p_user = db.relationship(
        "Users",
        backref="pos"
    )
```

### 正向 & 反向

- 正向: 从 `relationship` 到另一个模型叫 正向操作
- 反向: 从 另一个模型到 `relationship` 叫 反向操作

### 增加数据

```python
# 增加 职位表 数据
po1 = Position(name="程序猿")
po2 = Position(name="工程师")

# 增加 用户表 数据

## (1) 使用外键增加数据

###    增加用户 张三，职位为 程序猿
u1 = Users(name="张三",age=18,score=70, p_id=1)

###    增加用户 李四，职位为 工程师
p_id = Position.query.filter(Position.name == "工程师").first().id
u2 = Users(name="李四",age=28,score=75, p_id=p_id)

## (2) 正向操作 增加数据

###    增加用户 王五，职位为 程序猿
u3 = Users(name="王五",age=21,score=62)
# 获取职位为 程序猿的数据对象
po1 = Position.query.filter(Position.name == "程序猿").first()

# 获取 该职位中的所有用户
print(po1.p_user)
# 追加 王五 用户 到该职位中
po1.p_user.append(u3)

# (3) 反向操作 增加数据

###    增加用户 赵六，职位为 工程师
u4 = Users(name="赵六",age=34,score=80)
u4.pos = Position.query.filter(Position.name == "工程师").first()
```

### 查询数据

```python

## (1) 使用外键查询

###     查询用户 王五 的职位
user = Users.query.filter(Users.name == "王五").first()
# 获取用户外键
p_id = user.p_id
# 根据用户外键 在职位表查询相关职位
pos = Position.query.filter(Position.id == p_id).first().name

## (2) 正向查询

###    获取程序猿职位 的所有用户
pos = Position.query.filter(Position.name == "程序猿").first()
print(pos.p_user)

## (3) 反向查询

###    查询用户 王五 的职位

user = Users.query.filter(Users.name == "王五").first()
pos = user.pos.name
```

## 多对多

多对多关系 : 需要额外一张关系表进行维护

例如: OA 项目中的职位和权限表，是一个多对多的关系
一个职位用户多个权限
一个权限属于多个职位

### 创建模型

```python
# 权限表
class Authority(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))

# 关系表
# 对于这个关系表，强烈建议不使用模型，而是使用 db.Table 创建一个实际的表
# 我们不需要关心这张表，这张表会由 SQLAlchemy 接管，它唯一的作用是为其它两张表建立关系
pos_auth = db.Table(
    # 表名
    "pos_auth",
    db.Column("pos_id",db.Integer, db.ForeignKey("position.id")),
    db.Column("auth_id", db.Integer, db.ForeignKey("authority.id"))
)

# 职位表
class Position(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))

    p_auth = db.relationship(
        "Authority",
        backref="pos",
        # secondary 指定上边定义的 关系表
        secondary="pos_auth"
    )
```

两表内容如下：

- **position** 表
    |id|name|
    |:---|:---|
    |1|程序猿|
    |2|工程师|

- **authority** 表
    |id|name|
    |:---|:---|
    |1|	查看|
    |2|	修改|
    |3|	删除|
    |4|	执行|


### 增加数据

```python
# (1) 正向操作 

###    给 程序猿 修改 权限

pos = Position.query.filter(Position.name =="程序猿").first()
add_auth = Authority.query.filter(Authority.name == "修改").first()
pos.p_auth.append(add_auth)

# (2) 反向操作

###    将 执行 权限 给 程序猿 和 工程师

run_auth = Authority.query.filter(Authority.name == "执行").first()
pos1 = Position.query.filter(Position.name == "程序猿").first()
pos2 = Position.query.filter(Position.name == "工程师").first()
run_auth.pos.append(pos1)
run_auth.pos.append(pos2)
```

### 查询数据

```python
# (1) 正向操作

###    查找 程序猿 的所有权限
pos = Position.query.filter(Position.name == "程序猿").first()
print(pos.p_auth)

# (2) 反向操作

###    查找拥有 执行 权限的所有职位
run_auth = Authority.query.filter(Authority.name =="执行").first()
print(run_auth.pos)
```

## 一对一

一对一是在一对多的模型中增加属性即可，`uselist = False`

```python
db.relationship(
    "Users",
    backref="pos",
    uselist = False
)
```

## 参考

[http://www.pythondoc.com/flask-sqlalchemy/models.html#one-to-many](http://www.pythondoc.com/flask-sqlalchemy/models.html#one-to-many)