<!-- TOC -->

- [ORM 技术](#orm-技术)
- [SQLAlchemy 框架](#sqlalchemy-框架)
- [Flask-SQLAlchemy](#flask-sqlalchemy)
    - [安装](#安装)
    - [配置](#配置)
    - [定义数据表模型](#定义数据表模型)
    - [创建数据表](#创建数据表)

<!-- /TOC -->

# ORM 技术
ORM（**Object Ralational Mapping，对象关系映射**）用来把对象模型表示的对象映射到基于 SQL 的关系模型数据库结构中去。这样，我们在具体的操作实体对象的时候，就不需要再去和复杂的 SQL 语句打交道，只需简单的操作实体对象的属性和方法。ORM 技术是在对象和关系之间提供了一条桥梁，前台的对象型数据和数据库中的关系型的数据通过这个桥梁来相互转化。

| 数据库                 | Python                   |
| :--------------------- | :----------------------- |
| 数据库中的表 ( table ) | 类 ( class )             |
| 记录 ( recor，行数据)  | 对象 ( object )          |
| 字段 ( field )         | 对象的属性 ( arrtibute ) |

![img][img@1]

# SQLAlchemy 框架

上述就是 ORM技术 ，把关系数据库的表结构映射到对象上。但是由谁来做这个转换呢？所以 ORM框架 应运而生。在 Python 中，最有名的 ORM框架 是 SQLAlchemy。其工作单元使得有必要限制所有的数据库操作代码到一个特定的数据库 session，在该 session 中控制每个对象的生命周期 。

优点

 1. 企业级 API，使得代码有健壮性和适应性
 2. 灵活的设计，使得能轻松写复杂查询
 
缺点

 1. 工作单元概念不常见
 2. 重量级 API，导致长学习曲线

# Flask-SQLAlchemy

[Flask-SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/) 在 SQLAlchemy 的基础上进行二次开发，是一个为您的 Flask 应用增加 SQLAlchemy 支持的扩展。它致力于**简化在 Flask 中 SQLAlchemy 的使用，提供了有用的默认值和额外的助手来更简单地完成常见任务**。

### 安装

在python中，我们直接使用 pip 即可进行安装

```python
pip install flask-sqlalchemy
```

> 需要注意的是，
> 使用 pip 安装的时候模块名为 `flask-sqlalchemy`，
> 但是在代码中导入模块时，我们导入的是
> `from flask_sqlalchemy import SQLAlchemy`
> 注意模块名中 `-` 与 `_` 的区别！

### 配置

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库对象发生修改时是否跟踪修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 配置数据库文件位置
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////my.db"
# 实例化 flask_sqlalchemy
db = SQLAlchemy(app)

@app.route("/")
def view():
    return "hello world"

app.run()
```

### 定义数据表模型

```python
# 自定义类型继承 db.Model
class User(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
```

db.Column(字段类型，可选参数)
| 字段类型      | 说明                              |
| :------------ | :-------------------------------- |
| Integer       | 整数                              |
| String (size) | 有最大长度的字符串                |
| Text          | 长 unicode 文本                   |
| DateTime      | 表示为 datetime 对象 的时间和日期 |
| Float         | 存储浮点值                        |
| Boolean       | 存储布尔值                        |
| PickleType    | 存储一个持久化 Python 对象        |
| LargeBinary   | 存储任意大的二进制数据            |

| 可选参数      | 说明                                    |
| :------------ | :-------------------------------------- |
| primary_key   | 表的主键                                |
| autoincrement | 自增                                    |
| unique        | 不允许出现重复值                        |
| index         | 为列创建索引，提升查询效率              |
| nullable      | True 允许使用空值  false 不允许使用空值 |
| default       | 设置默认值                              |

> Flask-SQLAlchemy 要求每个模型都要定义主键，这一列经常命名为 id

### 创建数据表

创建完模型后，只是创建了python对象，但是并没有创建数据库，还需要通过 `db.create_all()` 创建数据表。

可以通过 flask shell 创建，也可以直接写在python文件中创建。

```python
# flask shell
from app import db
db.create_all()
```

> 如果写在python文件中创建，创建完毕后，需要注释该行创建语句
