应用总是需要一定的配置的。根据应用环境不同，会需要不同的配置。比如开关调试 模式、设置密钥以及其他依赖于环境的东西。

Flask 的设计思路是在应用开始时载入配置。你可以在代码中直接硬编码写入配置， 对于许多小应用来说这不一定是一件坏事，但是还有更好的方法。

不论使用何种方式载入配置，都可以**使用 Flask 对象的 config 属性来操作配置的值**

Flask 常用配置项的内容可以在这里查看：[常用配置项](https://dormousehole.readthedocs.io/en/latest/config.html#id4)

# 设置配置项

## 直接配置

```python
# 每次配置一条内容
app.config['DEBUG'] = True
app.config['ENV'] = development

# 一次配置多条内容
app.config.update(
    DEBUG=True,
    ENV="development"
)
```

## 配置文件

```python
app.config.from_pyfile("config.py")

# config.py
DEBUG=True
ENV="development"
```

## 配置类

```python
from config import Config
app.config.from_object(Config)

# config.py
class Config:
    DEBUG=True
    ENV="development"

```