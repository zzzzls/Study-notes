<!-- TOC -->

- [程序结构概述](#%e7%a8%8b%e5%ba%8f%e7%bb%93%e6%9e%84%e6%a6%82%e8%bf%b0)
- [顺序结构](#%e9%a1%ba%e5%ba%8f%e7%bb%93%e6%9e%84)
- [选择结构](#%e9%80%89%e6%8b%a9%e7%bb%93%e6%9e%84)
  - [if语句](#if%e8%af%ad%e5%8f%a5)
  - [if...else语句](#ifelse%e8%af%ad%e5%8f%a5)
  - [if…elif…else语句](#ifelifelse%e8%af%ad%e5%8f%a5)
  - [嵌套if](#%e5%b5%8c%e5%a5%97if)
  - [三元语法](#%e4%b8%89%e5%85%83%e8%af%ad%e6%b3%95)
- [循环结构](#%e5%be%aa%e7%8e%af%e7%bb%93%e6%9e%84)
  - [while循环](#while%e5%be%aa%e7%8e%af)
  - [for循环](#for%e5%be%aa%e7%8e%af)
  - [break关键字](#break%e5%85%b3%e9%94%ae%e5%ad%97)
  - [continue关键字](#continue%e5%85%b3%e9%94%ae%e5%ad%97)
  - [else关键字](#else%e5%85%b3%e9%94%ae%e5%ad%97)

<!-- /TOC -->

# 程序结构概述

程序结构，就是程序的流程控制结构  
就是控制代码的运行过程的固定语法，常见的流程语法：

# 顺序结构

代码按照从上到下的顺序，依次执行的过程，如图：

![img][img@1]

# 选择结构

程序执行过程中，根据不同的情况，选择执行不同的操作，如图：

![img][img@2]

## if语句

**语法格式：**  

```python
if <判断条件>：
    <执行语句 ... >

# ================================

price = 200
if price < 500:
    print("价格大于500")
print("end")

# 价格大于500
# end
```

当 条件 成立时，才执行语句；反之，则不执行  
执行语句可以为多行，以缩进来区分表示同一范围。  
**注意：** 在 Python中，非零值标识 True; None 和 0 表示 False

![img][img@3]


## if...else语句

**语法格式**

```python
if <判断条件>:
    <执行语句1……>
else:
    <执行语句2……>

# ================================

price = 1000
if price < 500:
    print("价格小于500")
else：
    print("价格大于500")
print(end)

# 价格大于500
# end
```

当条件为 True时，执行语句1，否则，则执行语句2

![img][img@4]

## if…elif…else语句

**语法格式**

```python
if <判断条件1>：
    <执行语句1...>
elif <判断条件2>
    <执行语句2...>
elif <判断条件3>
    <执行语句3...>
else：
    <执行语句4...>

# ================================

price = 500
if price > 1000:
    print("价格大于1000")
elif price > 800:
    print("价格大于800")
elif price > 600:
    print("价格大于500")
else：
    print("价格在600以下")
print("end")

# 价格在600以下
# end
```

elif 是 else if 的缩写，允许我们检查多个表达式  
如果 if 的条件为 False，则检查下一个 elif 的状态，依次进行 ... 如果所有的条件都为 False ，则执行 else里边的语句  
**注意：** if 和 else 只能有一个，但 elif 可以有多个，if ... elif ... else 中只有一个语句块可以根据条件来执行，

## 嵌套if

可以将一个 if 语句加入至另一个 if 语句中，这被称为嵌套。  
任何数量的这些语句都可以嵌套在一起，要找出嵌套级别，缩进是唯一的方法。

```python
price = 200
time = 3

if price < 300:
    print("价格低于300")
    if time < 5:
        print("快递时间少于5天")
else:
    print("价格低于300")
print("end")

# 价格低于300
# 快递时间少于5天
# end
```

## 三元语法

**语法格式**

```python
<条件为True> if <条件> else <条件为False>

price = 500
b = "价格大于300" if price > 300 else "价格低于300"
print(b)

# 价格大于300

```

# 循环结构

如果满足一定的条件，重复执行一件事情，如图：

![img][img@5]

## while循环

while 循环用于遍历代码块，只要判断条件为True，就会一直地循环执行。

**语法格式**

```python
while <判断条件>:
    <循环体>
```

![img][img@6]

进入 while 循环，首先检测判断条件，只有当其为 True 时，才会进入循环体，迭代一次后，再次检测判断条件，一直持续到 **判断条件为False**

和 if 语句类似，while循环也通过缩进来区分循环体

```python
i = 0
while i<3:
    print(i)
    i += 1

# 0
# 1
# 2
```

只要 i 小于 3 ，判断条件为 True  
**注意**：要在循环体中改变 i 的值，否则将导致无限循环  

## for循环

for循环用于迭代序列（例如：列表，元组）或者其它可迭代对象，俗称遍历  

**语法格式**

```python
for <val> in <序列>:
    <循环体>
```

![img][img@7]

val 是一个变量，在每次迭代中，用于接收序列中元素的值  
循环会一直继续，知道序列的最后一项  
循环体与其他代码使用缩进分割  

```python
for i in "Python":
    print(i)

# P
# y
# t
# h
# o
# n

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4
```

## break关键字

`break` 用于终止循环语句，即使循环条件不是 False或者循环序列还没有完全递归完，也会强行终止！  
**注意**：如果 break语句在嵌套循环中，break将终止最内层循环！

```python
# while 循环中的 break
i = 4
while i<1:
    if i == 2:
        print("退出循环！")
        break
    print(i)

# 4
# 3
# 退出循环！

# =================================

# for 循环中的 break
for i in "Python":
    if i == "h":
        print("退出循环！")
        break
    print(i)

# P
# y
# t
# 退出循环！
```

## continue关键字

`continue` 用于跳过本次循环中剩余的代码，继续下一次循环  

```python
songs = ['安静', '蜗牛', '稻香']

# 通过索引遍历列表
for i in range(len(songs)):
    if i == 1:
        print('不想听', songs[i])
        print('快进，下一曲')
        continue
    print("正在播放：", songs[i])

# 正在播放： 安静
# 不想听 蜗牛
# 快进，下一曲
# 正在播放： 稻香

```

**break 与 continue 的区别**：`break` 用于终止整个循环；`continue` 用于跳出本次循环，还会继续下一次循环。

## else关键字

循环中有一个可选的 else 块，如果循环正常执行完（即：不是通过 break 跳出而中断的），则执行else部分  

**注意**： 如果循环中使用 break 语句跳出了，else 部分不会执行

```python
songs = ['安静', '蜗牛', '稻香']
for song in songs:
    print('正在播放：', song)
else:
    print('播放结束')

# 正在播放： 安静
# 正在播放： 蜗牛
# 正在播放： 稻香
# 播放结束
```

[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_1.png

[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_2.png

[img@3]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_3.png

[img@4]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_4.png

[img@5]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_5.png

[img@6]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_6.png

[img@7]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/python%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/04-01_7.png