<!-- TOC -->

- [什么是 HTML](#%e4%bb%80%e4%b9%88%e6%98%af-html)
- [HTML 标签](#html-%e6%a0%87%e7%ad%be)
- [HTML 属性](#html-%e5%b1%9e%e6%80%a7)
- [HTML 基本结构](#html-%e5%9f%ba%e6%9c%ac%e7%bb%93%e6%9e%84)
- [常见的 HTML 标签](#%e5%b8%b8%e8%a7%81%e7%9a%84-html-%e6%a0%87%e7%ad%be)
  - [h1-h6](#h1-h6)
  - [p](#p)
  - [br、hr](#brhr)
  - [i、b、del、u](#ibdelu)
  - [div、span](#divspan)
  - [img](#img)
  - [a](#a)
  - [ul、ol、dl](#uloldl)
  - [table](#table)
  - [form表单](#form%e8%a1%a8%e5%8d%95)
  - [表单元素](#%e8%a1%a8%e5%8d%95%e5%85%83%e7%b4%a0)
    - [input](#input)
    - [select](#select)
    - [textarea](#textarea)

<!-- /TOC -->

# 什么是 HTML

HTML 是用来描述网页的一种语言

- HTML 指的是超文本标记语言（Hyper Text Markup Language）
- HTML 不是一种编程语言，而是一种**标记语言**（markup language）
- 标记语言是一套标记标签（markup tag）
- HTML 使用**标记标签**来描述网页
- HTML 对大小写不敏感，建议使用小写

# HTML 标签

HTML 标记标签通常被称为 HTML 标签（HTML tag）

- HTML 标签是由**尖括号包围**的关键词，如 `<html>`
- HTML 标签通常是**成对出现**的，如 `<b> <\b>`
- 标签队中的第一个标签是**开始标签**，第二个标签是**结束标签**
- 开始和结束标签也被称为**开放标签**和**闭合标签**

# HTML 属性

属性是 HTML 元素提供的附加信息

- HTML 元素可以设置属性
- 属性可以在元素中添加附加信息
- 属性一般描述与开始标签
- 属性总是以名称/值对的形式出现，如 name="value"

常见属性：
|属性名|描述|
|:---|:---|
|class|为 html 元素定义一个或多个类名|
|id|定义元素的唯一id|
|style|规定元素的行内 CSS 样式|
|title|规定有关元素的额外信息|
|accesskey|规定激活元素的快捷键|
|hidden|元素是否显示|
|data-*|用于存储页面或应用程序的私有定制数据|

# HTML 基本结构

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Document</title>
    </head>
    <body>
        hello Python!
    </body>
</html>
```


上述代码是 HTML 的基本结构，我们分别来看一下：

- `<!DOCTYPE>`: 是 `Document Type Declaration`，用来声明文档，也就是告知 web 浏览器当前页面使用了哪种 HTML 版本编写代码，此处使用的是 HTML5 版本，声明文档必不可少，而且必须位于 HTML 文档第一行
- `<html>`: 表示页面编写的代码都是 HTML 代码。它是成对出现的标签，所有代码都必须写在 `<html><\html>`之间
- `<head>`: 表示页面的头部
- `<title>`: 表示页面的标题
- `<body>`: 表示页面的身体

# 常见的 HTML 标签

## h1-h6

六个不同的 HTML 标题

|标签|描述|示例|
|:---|:---|:---:|
|`<h1></h1>`|一级标题|<h1>一级标题</h1>|
|...|||
|`<h6></h6>`|六级标题|<h6>六级标题</h6>|

## p

|标签|描述|示例|
|:---|:---|:---:|
|`<p></p>`|段落标签|\|

## br、hr

|标签|描述|示例|
|:---|:---|:---:|
|`<br/>`|换行标签|\|
|`<hr/>`|水平分割线|\|

## i、b、del、u

|标签|描述|示例|
|:---|:---|:---:|
|`<i></i>`|倾斜|<i>倾斜</i>|
|`<b></b>`|加粗|<b>加粗</b>|
|`<del></del>`|删除线|<del>删除线</del>|
|`<u></u>`|下划线|<u>下划线</u>|

## div、span

|标签|描述|示例|
|:---|:---|:---:|
|`<div></div>`|定义文档中的分区或节|\|
|`<span></span>`|组合文档中的行内元素|\|

## img

定义图像

```html
<img src="" alt="" title="" width="" height="" \>
```

常用属性：

- src : 图片地址，可以是 网络地址 或者 本地地址
- alt : 图片加载失败时，显示的提示文本
- title : 鼠标悬浮在图片上时，显示的文本信息
- width : 设置图片的宽度
- height : 设置图片高度

> 单独设置图片的宽或高，图片会自适应变化

## a

超链接 跳转网络地址 | 跳转本地界面 | 锚点

```html
<a href=""></a>
```

常用属性：

- href : 链接指向的页面的URL
- target : 规定在何处打开链接 _blank 在新窗口打开链接
- download : 点击链接下载文件

## ul、ol、dl

**ul 无序列表**

```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

**ol 有序列表**

```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

**dl 自定义列表**

```html
<dl>
   <dt>计算机</dt>
   <dd>用来计算的仪器 ... ...</dd>
   <dt>显示器</dt>
   <dd>以视觉方式显示信息的装置 ... ...</dd>
</dl>
```

## table

```html
<table border="1">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>
```

`<table>` 标签定义 HTML 表格。

简单的 HTML 表格由 table 元素以及一个或多个 tr、th 或 td 元素组成。

tr 元素定义表格行，th 元素定义表头，td 元素定义表格单元。

rowspan 跨行，colspan 跨列

## form表单

form表单用于收集用户输入

```html
<form action="">
...
</form>
```

表单常用属性:

- action : 规定当提交表单时向何处发送表单数据
- method : 规定用于发送表单数据的 HTTP 方法，get | post

## 表单元素

表单是一个包含表单元素的区域  
表单元素是允许用户在表单中输入内容，比如：文本域，下拉列表，单选框，复选框等

### input

input 标签规定了用户可以在其中输入数据的输入字段
输入字段可以通过多种方式改变，取决于 type 属性

```html
<input type="value">
```

属性值：

|值|描述|
|:---|:---|
|text|单行输入框|
|password|单行密码输入框|
|radio|单选按钮|
|checkbox|复选框|
|submit|提交按钮|
|number|数字输入框|
|range|滑动条|
|date|日期选择器|
|search|搜索框|
|reset|重置按钮|
|image|图像形式提交按钮|
|file|文件上传按钮|
|hidden|隐藏域|

### select

```html
<select name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
</select>
```

### textarea

```html
<textarea name="message" rows="10" cols="30">
  The cat was playing in the garden.
</textarea>
```

