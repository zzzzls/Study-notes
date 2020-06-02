# Flask-script

Flask-Script 插件为在 Flask 里编写额外的脚本提供了支持。

包括运行一个开发服务器，一个定制的 Python命令行，用于执行初始化数据库，定时任务和其它属于 web应用之外的命令行任务的脚本

**(1) 安装**

`pip install flask-script`

**(2) 基本使用**

```python
# 1. 导入模块
from flask_script import Manager,Command
from flask import Flask

app = Flask(__name__)
# 2. 实例化对象
manager = Manager(app)

# 自定义命令
class Runserver(Command):
    def run(self):
        app.run(port=8000)

class SayHello(Command):
    def run(self):
        print("hello world")

# 绑定命令
manager.add_command("runserver8000",Runserver)   # python main.py runserver8000
manager.add_command("say",SayHello)   # python main.py hello

if __name__ == "__main__":
    manager.run()
```

**more** : [使用 Flask-Script 启动应用](https://wizardforcel.gitbooks.io/the-way-to-flask/chapter009.html)

# Flask-Migrate

从名字就 migrate 就可以理解，主要是数据迁移方面的作用

在 Flask 数据库操作一般引用 SQLAlchemy，表初始化的方式一般采用的是 `db.create_all` ，但是当需要对表修改的时候就需要先去数据库删除该表然后才能重新生成新的表，这样明显是不符合我们的需求的，使用 `flask_migrate` 就可以解决这个问题

**(1) 安装**

`pip install flask-migrate`

**(2) 示例代码**

```python
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from flask_script import Manager

manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command("db",MigrateCommand)
```

**(3) 表的初始化和变更**

第一次数据初始化过程需要三个步骤 **建立模型** -> **创建迁移文件** -> **创建表**，分别对应三个命令 `init`，`migrate`，`upgrade`，以后表的 增删改 只需要执行后两个步骤即可。

具体执行代码如下：

```python
# 建立模型（只需要执行一次）
python main.py db init

# 迁移文件
python main.py db migrate

# 创建表
python main.py db upgrade
```