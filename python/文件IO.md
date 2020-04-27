<!-- TOC -->

- [什么是文件IO?](#%e4%bb%80%e4%b9%88%e6%98%af%e6%96%87%e4%bb%b6io)
- [文件的分类](#%e6%96%87%e4%bb%b6%e7%9a%84%e5%88%86%e7%b1%bb)
- [open() 函数](#open-%e5%87%bd%e6%95%b0)
- [操作文本内容](#%e6%93%8d%e4%bd%9c%e6%96%87%e6%9c%ac%e5%86%85%e5%ae%b9)
  - [读取文本内容](#%e8%af%bb%e5%8f%96%e6%96%87%e6%9c%ac%e5%86%85%e5%ae%b9)
  - [写入字符到文本文件](#%e5%86%99%e5%85%a5%e5%ad%97%e7%ac%a6%e5%88%b0%e6%96%87%e6%9c%ac%e6%96%87%e4%bb%b6)
- [操作二进制文件](#%e6%93%8d%e4%bd%9c%e4%ba%8c%e8%bf%9b%e5%88%b6%e6%96%87%e4%bb%b6)
  - [读取二进制数据](#%e8%af%bb%e5%8f%96%e4%ba%8c%e8%bf%9b%e5%88%b6%e6%95%b0%e6%8d%ae)
  - [写入二进制数据](#%e5%86%99%e5%85%a5%e4%ba%8c%e8%bf%9b%e5%88%b6%e6%95%b0%e6%8d%ae)
- [大文件的复制（二进制文件）](#%e5%a4%a7%e6%96%87%e4%bb%b6%e7%9a%84%e5%a4%8d%e5%88%b6%e4%ba%8c%e8%bf%9b%e5%88%b6%e6%96%87%e4%bb%b6)
- [程序中数据的保存](#%e7%a8%8b%e5%ba%8f%e4%b8%ad%e6%95%b0%e6%8d%ae%e7%9a%84%e4%bf%9d%e5%ad%98)
  - [字符操作方式](#%e5%ad%97%e7%ac%a6%e6%93%8d%e4%bd%9c%e6%96%b9%e5%bc%8f)
  - [字节操作方式](#%e5%ad%97%e8%8a%82%e6%93%8d%e4%bd%9c%e6%96%b9%e5%bc%8f)
  - [小结](#%e5%b0%8f%e7%bb%93)
- [csv模块](#csv%e6%a8%a1%e5%9d%97)
  - [存储数据到csv文件](#%e5%ad%98%e5%82%a8%e6%95%b0%e6%8d%ae%e5%88%b0csv%e6%96%87%e4%bb%b6)
  - [读取csv文件中的数据](#%e8%af%bb%e5%8f%96csv%e6%96%87%e4%bb%b6%e4%b8%ad%e7%9a%84%e6%95%b0%e6%8d%ae)
  - [with 语句](#with-%e8%af%ad%e5%8f%a5)

<!-- /TOC -->

# 什么是文件IO?

文件IO: 通过程序操作计算中文件内容数据的一种技术
> 文件: 泛指计算机硬盘上的文件
> I: input，输入，表示程序中读取文件中的内容
> O：output，输出，表示程序中的数据输出/保存到文件中

# 文件的分类

- 基于文件的用途，文件表象上的宏观分类：
  - 文本文档，视频文件，音频文件，图片文件，word文档

- 基于文件的组成，文件底层的数据组织方式
  - 文本文件：底层是字符数据组成的，使用记事本软件正确打开文件内容
  - 二进制文件：底层是字节数据组成的，使用记事本软件打开出现乱码的文件

# open() 函数

open()函数是 python提供的内建函数，专门用于操作文件内容的一个功能函数
> 参数 **file**：第一个参数，描述的要打开的文件，可以是绝对路径，也可以是相对路径  
> 参数 **mode**：第二个参数，描述打开文件的方式，也称为操作文件的权限  
> 参数 **encoding**：描述操作文本文件的编码方式  

mode参数指定的权限（`r，w，x，a，b，t，+`）
> rt ：文件的默认打开方式，读取文本文件内容，可以省略  
> wt ：覆盖写入文本文件，可以省略 t  
> at ：追加写入文本文件，可以省略 t  
> rb : 读取二进制文件内容  
> wb ：覆盖写入二进制文件  
> ab ： 追加写入二进制文件  

# 操作文本内容

## 读取文本内容

```python
# 打开文件
file = open("cs.txt", "r", encoding="utf-8")
# 读取内容，打印
content = file.read()
print(content)
# 关闭文件
file.close()
```

## 写入字符到文本文件

```python
# 打开文件
file = open("cs.txt", "r", encoding="utf-8")
# 写入字符数据
file.write("你好，世界！")
# 关闭文件
file.close()
```

# 操作二进制文件

## 读取二进制数据

```python
# 1. 打开文件，以二进制的方式读取（二进制文件不需要设置字符编码）
file = open("mm.jpg", "rb")
# 读取数据
content = file.read()
print(content)
# 关闭文件
file.close()
```

## 写入二进制数据

```python
# 字符数据
msg = "你好，世界！"
# 以二进制方式打开文件
file = open("text.dat", "wb")
# 写入字节数据（可以通过编码方式将字符数据转换为字节数据）
file.write(msg.encoding("UTF-8"))
file.close()
```

# 大文件的复制（二进制文件）

文件内容较多，体积较大的文件的复制操作，涉及到文件内容的读取和写入操作。

> 二进制文件执行read()方法时 ：一次性将所有数据读取到内存中（文件体积较大，读取文件相当耗费内存！）

`read([size])` 此时可以指定每次读取的数据大小，单位字节；如每次读取 **1024字节-->1K** 数据。

如果进行大文件的复制，需要循环读取文件内容数据，最终完成文件的所有内容复制粘贴！

```python
"""大文件的复制操作"""
def file_copy(old_path, new_path):
    # 以读取方式打开 原路径
    old_file = open(old_path, "rb")
    # 以写入方式打开 新路径
    new_file = open(new_path, "wb")
    # 设置每次读取的数据大小 设置为 10M
    buffer = 1024 * 1024 * 10

    while True:
        # 循环读取，每次读取 10M 大小数据
        content = old_file.read(buffer)
        # 如果读取到的内容为空，则说明已经读取完
        if content == b"":
            print("读取完毕！")
            break
        # 写入新文件
        # 虽然上边使用 wb 覆盖写入的方式,由于此处 new_file 文件对象未关闭,所以仍是追加写入!
        new_file.write(content)
    print("复制完成！")
    old_file.close()
    new_file.close()

file_copy(原文件，拷贝到的位置)
```


# 程序中数据的保存

计算机中的文件存储的时**字符数据或者字节数据**，对应了程序代码中的字符数据和字节数据，但是程序中还有其它类型的数据，如列表，字典等等，这些数据存储到文件中时，应该怎么处理?

**解决方法：**将程序中其它类型的数据，转换成字符数据或者字节数据进行操作

## 字符操作方式

Python语法中提供了 json模块，可以将程序中的各种类型的数据转换成类似字典格式的字符串数据，称为**json数据**

- **json.dump(obj,fp)** 将程序中的一个对象数据（列表，字典等等）写入到一个打开的文件中
- **json.load(fp**) 将文件中的内容，转换成 python中的对应的对象数据

**1. 将数据保存到文本文件中**

```python
import json

dct1 = {
    "name": "zong",
    "pwd": "zong"
}

dct2 = {
    "name": "admin",
    "pwd": "admin"
}

lst = [dct1, dct2]
file = open("./cs.txt","w",encoding="utf-8")
json.dump(lst, file)
file.close()
```

**2. 将文本文件中的数据读取到程序中**

```python
import json

file = open("./cs.txt", "r", encoding="utf-8")
lst = json.load(file)
print(lst)
file.close()
```




## 字节操作方式

Python语法中提供了 **pickle 模块**，用于程序中的数据有组织的保存到二进制文件中

- dump(obj,fp) 将程序中的一个对象数据（列表，字典等等），写入到一个二进制文件中
- load(fp) 将文件中的字节数据，转换成python中对应的对象数据

**1. 保存数据到文件中**

```python
import pickle

dct1 = {
    "name": "zong",
    "pwd": "zong"
}

dct2 = {
    "name": "admin",
    "pwd": "admin"
}

lst = [dct1,dct2]

file = open("cs.dat","wb")
pickle.dump(lst,file)
file.close()
```

**2. 从文件中读取数据**

```python
import pickle

file = open("./cs.zong","rb")
lst = pickle.load(file)
print(lst)
file.close()
```

## 小结

上述 json模块 和 pickle模块，都只能在一个文件中操作一个对象数据，当然我们也可以将多个对象数据包含在一个列表容器中，解决存储多个数据的问题。  

Python中同样提供了其它的操作模块可以非常友好的完成数据的交互，如 **marshal模块**可以序列化多个数据，**shelve模块**可以按照字典的方式组织序列化数据等等

# csv模块

**csv文件**时按照行列式 存储数据的一种方式，是一个文本文件，可以使用 excel软件直接打开希纳是为表格格式，Python中提供了一个 csv模块用于专门操作 csv文件

```python
import csv
dir(csv)
['excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']
```

## 存储数据到csv文件

```python
import csv

file = open("text.csv", "w", newline="", encoding="UTF-8-sig")
# 获取csv的writer对象
writer = csv.writer(file)
# 写入标题
writer.writerow(["姓名", "年龄", "性别", "邮箱"])

# 写入多行数据
writer.writerows([
    ["tom", "18", "男", "tom@qq.com"],
    ["jimi", "21", "男", "jimi@qq.com"],
])

file.close()
```

## 读取csv文件中的数据

```python
import csv

file = open("text.csv", "r", encoding="UTF-8-sig")
reader = csv.reader(file)
for row in reader:
    print(row)

file.close()
```

# with 语句

当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候在慢慢写入。只有在调用 close() 方法时，操作系统才保证**把没有写入的数据全部写入磁盘，同时释放资源**。忘记调用 close 的后果时数据可能只写了一部分到磁盘，剩下的丢失了。

有时，我们使用 open() 函数打开文件，如果出现异常，如读取过程中文件不存在，此时程序中断，尚未执行到 close() 方法，文件对象同样无法关闭！

此时，我们可以考虑使用 with语句来打开文件，具体语法格式如下：

```python
with open("cs.txt","w",encoding="utf-8") as f:
    content = f.read()

print(content)
```

使用 with 语句的好处，就是到达语句末尾时，即便出现异常，也会自动关闭文件，可以确保文件一定会被关闭！

