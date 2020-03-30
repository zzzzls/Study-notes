- [Python概述](#Python概述)
  * [发展历程](#发展历程)
  * [Python语言的优势](#Python语言的优势)
  * [The Zen of Python](#the-zen-of-python)
- [环境搭建](#环境搭建)
  * [基本环境搭建](#基本环境搭建)
  * [集成环境搭建](#集成环境搭建)
- [开发工具](#开发工具)
  * [记事本](#记事本)
  * [超级记事本](#超级记事本)
  * [IDE工具](#IDE工具)


# Python概述

## 发展历程

1989 年圣诞节，荷兰人 [Guido van Rossum][龟叔]（吉多·范罗苏姆） 为了打发圣诞节的无趣而开发了一个脚本解释程序 —— `Python`，取自英国20世纪70年代首播的电视喜剧`《蒙提.派森的飞行马戏团》（Monty Python's Flying Circus）`

诞生之初，并没有引发轰动性的效应，主要负责编写软件的维护脚本。

2010年，Python语言入选十大流行语言之一，开始进入大部分开发人员的眼睛。

2016年，人工智能的元年，Google公司开源了使用Python语言开发的深度学习库，人工智能出现了突飞猛进的发展，Python开始进入大家的视野。

**[Life is short ，you need Python][Python]**

## Python语言的优势

- 入门简单，语法简介，规则规范
- 可移植性性强，可以和其它语言混合开发
- 同时支持函数式编程和面向对象编程
- 丰富的第三方库
- 非常火爆活跃的社区
- 支持各种业务应用软件的开发

## The Zen of Python

在 Python shell 中输入 `import this`，就会展示 Tim Peters 的 The Zen of Python:

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

# 译文如下：

Python 之禅， by Tim Peters

优美胜于丑陋（Python 以编写优美的代码为目标）
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
可读性很重要（优美的代码是可读的）
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写except:pass风格的代码）
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido）
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```

# 环境搭建

- [Python官网][官网]  
   Python 最新源码，二进制文档，新闻资讯等

- [Python在线文档][文档]  
  HTML、PDF、PostScript 等格式的文档。

- [Python Releases for Windows][windows版下载地址]  
  Python Windows 版本下载地址

## 基本环境搭建

1. 以 Python 3.7.7 为例，下载安装，选择 `Customize installation`，进行自定义安装

   ![img][注意事项]

2. 验证是否安装成功
   - 打开系统命令行程序，如 **CMD**
   - 输入 `Python -V`
   - 打印出Python版本信息即为安装成功！
  
        ```python
        Python 3.7.7
        ```

    - 如果出现如下错误：

        ```diff
        - 'python' 不是内部或外部命令，也不是可运行的程序或批处理文件。
        ```

        这是因为系统会根据环境变量中的 `Path` 设定的路径去查找 python.exe，如果没找到，就会报错。如果在安装时没有勾选 `"Add Python 3.7 to PATH"`，那就要手动把 python.exe 所在的路径`（例如 C:\Program Files\Python）`添加到 Path 中。

## 集成环境搭建

1. **为什么需要集成环境**

   - **省时省心**
   - **分析利器**

2. **安装集成环境**

    经典的集成环境：**[Anaconda][Anaconda]**、Miniconda，安装好之后就默认内置了很多程序需要的功能，在后期学习数据分析时，就不需要手工安装大量的程序了。

    由于 Anaconda官网只提供了最新版本的下载，技术行业，最先进的不一定是最流行的！我们可以前往 <https://repo.continuum.io/archive> 下载指定版本安装。

    ![img][Anaconda版本]

    安装过程中没有需要注意的事项，直接类似普通软件安装即可！

3. **验证是否安装成功**

    打开系统命令行，执行命令

    ```python
    # 查看安装的集成环境的版本
    conda -V 
    ```

# 开发工具

编程语言，都是文本代码，所以可以使用记事本`（notepad.exe）` 直接编写，但是使用不同的工具编写代码的效率和开发体验是不一样的！

## 记事本

最原始的写代码的工具

- 优点
   - 任何操作系统都内置了记事本，不需要在安装
   - 打开速度快，修改少量代码方便

- 缺陷
  - 不能正确识别和区分代码
  - 代码无颜色提示
  - 代码无错误提示
  - 无代码提示，自动补全
  
## 超级记事本
类似 [VSCode][VSCode]，sublime，Editplus 这样的记事本，就是在记事本的基础上，进行了功能的升级！

- 优点
  - 打开速度快，消耗内存少
  - 支持代码高亮，错误提示，自动补全
  - 可根据需求安装插件

- 缺点
  - 对于中大型项目开发能力有限

## IDE工具

针对特定的编程语言，开发的比较有针对性的功能异常强大的软件。

- **Python常见IDE**
  - eclipse + python插件
  - [Pycharm][Pycharm]

- 优点
  - 颜色高亮，错误提示
  - 智能提示，自动补全
  - 版本管理，调试运行
  - more and more
  







[龟叔]:https://gvanrossum.github.io/
[Python]:https://sebsauvage.net/python/
[官网]:https://www.python.org/
[文档]:https://docs.python.org/zh-cn/3/
[windows版下载地址]:https://www.python.org/downloads/windows/
[注意事项]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/03-30_1.png

[Anaconda]:https://www.anaconda.com

[Anaconda版本]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/03-30_2.png

[VSCode]:https://code.visualstudio.com/

[Pycharm]:https://www.jetbrains.com/pycharm/
