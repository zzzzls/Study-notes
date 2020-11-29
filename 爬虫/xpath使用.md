# Xpath 解析库

​	通过 requests 模块，我们可以很简单地把网页下载到本地，但是此时获取的网页都是未经处理的，冗余的信息太多，无法进行分析和利用。那么怎么从网页中筛选自己需要的信息呢？

​	说到信息筛选我们可能会想到正则表达式，不过由于正则表达式过于复杂而且容错率低，网页有稍微的改动就要重写匹配表达式，对于新手来说十分不友好。

​	那么我们应该使用什么呢？别担心，我们还有很多种解析 HTML页面的方法，例如：**Xpath**



## lxml

`lxml` 是一款高性能的 Python XML 解析库，它天生支持 XPath1.0，XSLT1.0，定制元素类，甚至 Python风格的数据绑定接口。它构建在两个 C 库之上：`libxml2` 和 `libxslt`。它们为执行解析，序列化和转换等核心任务提供了主要动力



### 安装

```python
pip install lxml
```



### 使用

lxml 中大部分的功能都位于 `lxml.etree` 模块中，导入 `lxml.etree` 模块的常见方式如下：

```python
from lxml import etree
```

-   **etree.HTML(string)**

    将 string 解析为 Element 或者 ElementTree，同时修复非法标签

    

-   **etree.parse(\<file_name>)**

    将文件或者是 file_like 对象解析为 ElementTree (not an Element object)

    

-   **etree.tostring(Element, encoding='utf-8')**

    将一个 Element 或者 ElementTree 转换为 string 形式



-   **ElementTree.write(file)**

    这个是 ElementTree 特有的方法，将 ElementTree 写到 file 中



| Element 属性 | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| .tag         | 元素名称                                                     |
| .attrib      | 元素属性的字典                                               |
| .text        | 第一个子元素标签之前的文本。Element的文本均为直接自文本，不包含子元素中的文本 |
| .tail        | Element 的关闭标签之后的文本，并且是在下一个标签之前的部分，没有则为None |



| Element 方法                                    | 描述                                                         |
| :---------------------------------------------- | ------------------------------------------------------------ |
| append(child)                                   | 添加一个子节点到当前 Element                                 |
| insert(index，element)                          | 插入子元素 element 到指定位置                                |
| clear()                                         | 移除 element 所有内容                                        |
| remove(child)                                   | 将子节点从 Element 中移除                                    |
| getchildren()                                   | 返回 Element 子元素的列表                                    |
| iterchildren(tag=etree.Element, reversed=False) | 通过设置 reversed 可以反向顺序迭代子元素                     |
| getiterator(tag=None，*tags)                    | 递归返回 Element 子元素的生成器，可使用 tag 参数过滤返回的元素，深度优先，先根遍历 |
| getroottree()                                   | 返回元素的 Elementree                                        |
| iter(tag=None，*tags)                           | 过滤特定标签，生成迭代器。默认情况下，iter() 迭代所有的节点，包括PI(处理指令) 、Comment(注释) 等。如果只想迭代标签元素，可以使用 Element factory 做参数 `e.iter(tag = etree.Element)` |
| itertext(tag=None, *tags, with_tail=True)       | 迭代 Element 元素的文本内容，with_tail 参数决定是否迭代子元素的 tail 。Element 的tail 不会进行迭代 |
| iterancestors( tag=None )                       | 迭代所有 Element 先辈，可以使用 tag 过滤                     |
| itersiblings( preceding=False )                 | 迭代 Element 之后的兄弟元素，可以通过设置 preceding=True 仅迭代 Element 之前的兄弟元素 |
| items()                                         | 返回 Element 属性的键值所构成的(name，value)元组的列表       |
| keys()                                          | 返回元素属性名的列表                                         |
| get(key，default=None)                          | 返回字符串形式的 属性 key 的值，没有返回 None                |
| set(A，V)                                       | 创建或者改变属性 A 的值为 V                                  |



## 什么是Xpath

Xpath，全称 `XML Path Language`，即  XML路径语言，是一门在 XML文档中查找信息的语言，最初用来搜寻 XML文档，但是它同样适用于 HTML文档的搜索

Xpath中，有七种类型的节点：元素，属性，文本，命名空间，处理指令，注释以及文档节点(根节点)  

Xpath 使用路径表达式选取节点。节点是通过沿着路径或者 step 来选取的



### 节点关系

```html
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```

| 节点关系     | 描述 |
| ------------ | ---- |
| **父（Parent）** |    `book `元素是 `title`，`author` 等元素的父  |
| **子（Children）**             |  `title`，`author` 是 `book` 元素的子    |
|     **同胞（Sibling）**         |    拥有相同的父节点，`title`，`author`，`year `都是同胞  |
| **先辈（Ancestor）** | 某节点的父，父的父等。`title` 元素的先辈是 `book` 和 `bookstore` |
| **后代（Descendant）** | 某节点的子，子的子等。`bookstore` 的后代是 `book` 和 `title` 等 |

### 常用规则

#### 选取节点，常用路径表达式

| 表达式   | 描述                           |
| -------- | ------------------------------ |
| /        | 从根节点选取                   |
| //       | 选取所有节点，不考虑它们的位置 |
| .        | 选取当前节点                   |
| ..       | 选取当前节点的父节点           |
| @        | 选取属性                       |
| nodename | 选取此节点的所有子节点         |
| *        | 匹配任何元素节点               |
| @*       | 匹配任何属性节点               |
| text()   | 取标签当中的值                 |

#### 谓语

谓语的作用就是做过滤的，过滤条件写在 `[]` 中

| 表达式                        | 描述                                                    |
| ----------------------------- | ------------------------------------------------------- |
| /bookstore/book[1]            | 选取属于 bookstore 子元素的第一个 book 元素             |
| /bookstore/book[last()]       | 选取属于 bookstore 子元素的最后一个 book 元素           |
| /bookstore/book[last()]       | 选取属于 bookstore 子元素的倒数第二个 book 元素         |
| /bookstore/book[position()<3] | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素 |
| //book[@lang]                 | 选取所有拥有名为 lang 的属性的 title 元素               |
| //book[@lang='eng']           | 选取所有拥有 lang 属性值为 eng 的 book 元素             |
| //book[price>35]              | 选取所有拥有 price元素且值大于35 的 book 元素           |

#### 运算符

| 运算符 | 描述                      |
| ------ | ------------------------- |
| \|     | 返回两个节点集            |
| +      | 加法。6+4=10              |
| -      | 减法。6-4=2               |
| *      | 乘法。3*2=6               |
| div    | 除法。4 div 2 = 2         |
| mod    | 余数。5 mod 2 = 1         |
| =      | 等于。1=1 返回 true       |
| !=     | 不等于。9 != 9 返回 false |
| <      | 小于                      |
| <=     | 小等于                    |
| >      | 大于                      |
| \>=    | 大等于                    |
| or     | 或                        |
| and    | 与                        |

#### 轴

通过 轴 可以获取 祖先节点，属性值，兄弟节点等

使用方式：`轴::[谓语]`，

-   `child::*` ：所有子节点
-   `child::div` ：所有 div 子节点
-   `child::div[@class='item']`：所有 class=item 的 div 子节点

| 轴                 | 描述                                                     |
| ------------------ | -------------------------------------------------------- |
| ancestor           | 选取当前节点的所有先辈（父、祖父等）。                   |
| ancestor-or-self   | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身。   |
| attribute          | 选取当前节点的所有属性。                                 |
| child              | 选取当前节点的所有子元素。                               |
| descendant         | 选取当前节点的所有后代元素（子、孙等）。                 |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。 |
| following          | 选取文档中当前节点的结束标签之后的所有节点。             |
| following-sibling  | 选取当前节点之后的所有兄弟节点                           |
| preceding          | 选取文档中当前节点的开始标签之前的所有节点。             |
| preceding-sibling  | 选取当前节点之前的所有同级节点。                         |
| namespace          | 选取当前节点的所有命名空间节点。                         |
| parent             | 选取当前节点的父节点。                                   |
| self               | 选取当前节点。                                           |

#### 函数

| 函数                               | 描述                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| position()                         | 返回节点的 index 的位置                                      |
| last()                             | 返回节点的个数                                               |
| contains(string1, string2)         | string1 是否包含 string2                                     |
| text()                             | 返回文本节点                                                 |
| comment()                          | 返回注释节点                                                 |
| normalize-space(string)            | 去除首位空格，中间多个空格用一个空格代替                     |
| substring(string, start, len)      | 返回从 start 位置开始的指定长度的子字符串，第一个字符下标为1 |
| substring-before(string1, string2) | 返回 string1中位于第一个 string2 之前的部分                  |
| substring-after(string1, string2)  | 返回string1中位于第一个string2之后的部分                     |



### 使用示例

```python
# 获取父节点             获取 id=title 的 a 标签 父元素的 class 属性
xpath('//a[id="title"]/../@class')

# 模糊查询              获取 class 以 it 开头的 a 标签
xpath('//a[contains(@class, "it")]')

# 多条件匹配
xpath('//a[@class="title" and @name="t"]')

# 指定位置匹配
# ul 中最后一个 li 标签
xpath('//ul/li[last()]')

# ul 中倒数第二个 li 标签
xpath('//ul/li[last()-1]')

# ul 中前三个 li 标签
xpath('ul/li[position<4]')
```

