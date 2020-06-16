<!-- TOC -->

- [SQLALchemy](#sqlalchemy)
  - [安装](#安装)
  - [连接数据库](#连接数据库)
  - [编写模型](#编写模型)
  - [CRUD](#crud)
    - [增加数据](#增加数据)
    - [查询数据](#查询数据)
    - [修改数据](#修改数据)
    - [删除数据](#删除数据)

<!-- /TOC -->

# SQLALchemy

详细介绍可参考: [Flask-SQLAlchemy](https://github.com/zzzzls/Study-notes/blob/master/WEB/Flask/FlaskSQLAlchemy%E4%B8%8A.md)  

官网: [SQLAlchemy - The Database Toolkit for Python](https://www.sqlalchemy.org/)  
中文文档: [SQLAlchemy 1.4 Documentation](https://www.osgeo.cn/sqlalchemy/)

## 安装

```python
pip install pymsql
pip install sqlalchemy
```

## 连接数据库

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# 连接 mysql 数据库
# mysql://用户名:密码@主机/数据库名
db_path = "mysql+pymysql://root:root@127.0.0.1/tortest"

# 连接 sqlite 数据库
# base_dir = os.path.abspath(os.path.dirname(__name__))
# db_path = "sqlite:///" + os.path.join(base_dir, "db.sqlite")

# 创建连接引擎
engine = create_engine(
    db_path,
    encoding="utf-8",  # 编码
    echo=True          # 输出 ORM 语句转换后的 sql 语句
)
```

> 此处使用 pymysql驱动 连接 mysql 数据库时,  
> 可能会触发 `Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 485")`  
> 此处直接忽略即可 ,  或者改用 mysql-connector-python 驱动  
> `pip install mysql-connector-python`  
> `db_path = "mysql+mysqlconnector://root:root@127.0.0.1/tortest"`  

## 编写模型

```python
# 编写模型
from sqlalchemy import Column, Integer, String, Float

# 模型继承的父类
Base = declarative_base(bind=engine)

class Car(Base):
    # 设置表名
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    price = Column(Float)
    num = Column(Integer)

# 创建表结构
Base.metadata.create_all()
```

## CRUD

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

### 增加数据

```python
# 增加单条数据
car = Car(name="宝马",price=20.0,num=15)
session.add(car)
session.commit()

# 增加多条数据
session.add_all([car1, car2, car3])
session.commit()
```

### 查询数据

```python
# 查询所有数据
car_list = session.query(Car).all()

# 查询第一条数据
car = session.query(Car).first()

# 筛选数据
car_list = session.query(Car).filter(Car.name=="奥迪").first()

# 查询部分列
car_list = session.query(Car.name,Car.price).first()
```

更多可参阅: [Flask-sqlalchemy](https://github.com/zzzzls/Study-notes/blob/master/WEB/Flask/FlaskSQLAlchemyCRUD.md)

### 修改数据

```python
# 查询取得数据
car = session.query(Car).first()
# 修改数据
car.price = random.randint(10,50)
# 提交修改
session.commit()
```

### 删除数据

```python
car = session.query(Car).first()
session.delete(car)
session.commit()
```
