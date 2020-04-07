<!-- TOC -->

- [软件的运行过程](#%e8%bd%af%e4%bb%b6%e7%9a%84%e8%bf%90%e8%a1%8c%e8%bf%87%e7%a8%8b)
- [Python解释器内存划分](#python%e8%a7%a3%e9%87%8a%e5%99%a8%e5%86%85%e5%ad%98%e5%88%92%e5%88%86)
  - [不可变类型 -- 内存模型](#%e4%b8%8d%e5%8f%af%e5%8f%98%e7%b1%bb%e5%9e%8b----%e5%86%85%e5%ad%98%e6%a8%a1%e5%9e%8b)
    - [字符串操作](#%e5%ad%97%e7%ac%a6%e4%b8%b2%e6%93%8d%e4%bd%9c)
    - [整数操作](#%e6%95%b4%e6%95%b0%e6%93%8d%e4%bd%9c)
  - [可变类型 -- 内存模型](#%e5%8f%af%e5%8f%98%e7%b1%bb%e5%9e%8b----%e5%86%85%e5%ad%98%e6%a8%a1%e5%9e%8b)

<!-- /TOC -->

# 软件的运行过程

软件是在计算机上运行，安装在计算机硬盘中的，计算机的基本组成如下图:  

![img][img@1]

软件在计算机中运行时，是运行在系统的内存中的，平时使用电脑的时候打开软件较多的话，电脑会卡顿（**内存空间不足！**）  

编程语言编写的代码，就是在编写软件，所以代码的运行就是运行在内存中的。  

# Python解释器内存划分

Python代码在运行是，Python解释器会向操作系统申请运行内存，将代码加载到内存中运行，如图所示：

![img][img@2]

Python 解释器为了利用好有限的内存空间，将内存进行了如图的划分：  

![img][img@3]

## 不可变类型 -- 内存模型

**不可变类型**：数据在内存中一旦创建，就不能修改了。  
Python 为了优化程序执行速度，将字符串、整数定义成了不可变类型，一旦声明出来，数据就不能修改了。  

### 字符串操作

字符串是内存中使用特别的多的数据，所以 Python对字符串进行了优化，字符串是不可变数据类型，所以不能直接修改字符串内部的数据。  

当我们通过变量修改数据时，内存中将变量指向了一个新的内存地址。原来的字符串数据依然存在，并没有修改。  

![img][img@4]

### 整数操作

整数和字符串一样，在程序中也是一个经常操作的数据。所以也对整数进行了优化，Python 解释器在加载的时候，将 `-5~256` 的整数直接在内存中创建好了开发人员要使用的时候直接使用即可，不需要创建对象。  
整数也是不可变数据，如果需要修改变量中的整数数据时，就是将变量指向了一个新的内存地址，原来在内存中的数据不会收到影响。

![img][img@5]

## 可变类型 -- 内存模型

可变类型就是可以修改数据内部的数据，如列表  
Python 中的列表可以存储多个数据，存储的多个数据可能要参与业务处理需要经常变化，所以列表中的数据在语法上被定义成了可以修改的数据。如图所示：  

![img][img@6]


[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E5%88%86%E6%9E%90/04-07_1.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E5%88%86%E6%9E%90/04-07_2.png
[img@3]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E5%88%86%E6%9E%90/04-07_3.png
[img@4]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E5%88%86%E6%9E%90/04-07_4.png
[img@5]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E5%88%86%E6%9E%90/04-07_5.png
[img@6]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E5%88%86%E6%9E%90/04-07_6.png

