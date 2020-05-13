<!-- TOC -->

- [CSS](#css)
  - [CSS 诞生](#css-%e8%af%9e%e7%94%9f)
  - [CSS 语法](#css-%e8%af%ad%e6%b3%95)
  - [HTML 嵌入 CSS 样式](#html-%e5%b5%8c%e5%85%a5-css-%e6%a0%b7%e5%bc%8f)
    - [行内样式](#%e8%a1%8c%e5%86%85%e6%a0%b7%e5%bc%8f)
    - [内嵌式](#%e5%86%85%e5%b5%8c%e5%bc%8f)
    - [链接式](#%e9%93%be%e6%8e%a5%e5%bc%8f)
    - [@import导入](#import%e5%af%bc%e5%85%a5)
  - [CSS 选择器](#css-%e9%80%89%e6%8b%a9%e5%99%a8)
    - [元素选择器](#%e5%85%83%e7%b4%a0%e9%80%89%e6%8b%a9%e5%99%a8)
    - [id 选择器](#id-%e9%80%89%e6%8b%a9%e5%99%a8)
    - [class 选择器](#class-%e9%80%89%e6%8b%a9%e5%99%a8)
    - [属性选择器](#%e5%b1%9e%e6%80%a7%e9%80%89%e6%8b%a9%e5%99%a8)
    - [后代选择器](#%e5%90%8e%e4%bb%a3%e9%80%89%e6%8b%a9%e5%99%a8)
    - [子代选择器](#%e5%ad%90%e4%bb%a3%e9%80%89%e6%8b%a9%e5%99%a8)
    - [兄弟选择器](#%e5%85%84%e5%bc%9f%e9%80%89%e6%8b%a9%e5%99%a8)
    - [伪类/元素 选择器](#%e4%bc%aa%e7%b1%bb%e5%85%83%e7%b4%a0-%e9%80%89%e6%8b%a9%e5%99%a8)
  - [选择器优先级](#%e9%80%89%e6%8b%a9%e5%99%a8%e4%bc%98%e5%85%88%e7%ba%a7)

<!-- /TOC -->

# CSS

CSS 是 "`Cascading Style Sheet`" 的缩写，中文译为 "**层叠样式表**"，用来控制网页的样式，如 字体，颜色，边框，间距，大小，位置，可见性等

如果将 HTML 网页比作 "毛坯房"，那么有了 CSS 就是 "精装修"！

## CSS 诞生 

HTML 标签原本被设计为用于定义文档内容，通过使用 `<h1>`、`<p>`、`<table>` 这样的标签，HTML 的初衷是表达 *这是标题*，*这是段落*，*这是表格* 之类的信息。同时文档布局由浏览器来完成，而不使用任何的格式化标签

此时两种主要的浏览器 ( Netscape 和 Internet Explorer ) 不断地将新的 HTML 标签和属性（比如字体标签和颜色属性）添加到 HTML 规范中，创建文档内容清晰地独立于文档表现层的站点变得越来越困难

为了解决这个问题，万维网联盟（W3C），这个非盈利的标准化联盟，肩负起了 HTML 标准化的使命，并在 HTML 4.0 之外创建出样式 （Style）

所有的主流浏览器均支持层叠样式表

## CSS 语法

CSS 规则由两个主要的部分构成：**选择器** 以及 **一条或多条声明**（ 每条声明由一个属性和一个值组成 ）

- 选择器 通常是需要改变样式的 HTML 元素
- 属性（ property ）是您希望设置的样式属性，每个属性有一个值，属性和值用冒号分开
- 多条声明之间使用 `;` 隔开

![img][img@1]

## HTML 嵌入 CSS 样式

引入方式的优先级： **就近原则**

### 行内样式

行内样式就是把 CSS 样式直接放在代码行内的标签中，一般都是放入标签的 `style` 属性中，最直接的一种方式，但是修改起来较为麻烦

```html
<p style="font-size:30px;">行内样式</p>
```

### 内嵌式

内嵌式通过将 CSS 写在网页源文件的头部，即在 `<head>` 和 `</head>` 之间，通过使用 HTML 标签中的 `<style>` 标签将其包围，解决了行内样式多次书写的弊端

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        p {
            font-size: 32px;
        }
    </style>
</head>
<body>
    <p>内嵌样式</p>
</body>
</html>
```

### 链接式

链接式通过 HTML 的 `<link>` 标签，将外部样式表文件链接到 HTML 文档中，这也是网站使用最多的方式。这种方法将 HTML 和 CSS 完全分离，增强网页结构的扩展性和 CSS样式 的可维护性

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="./my.css">
</head>
<body>
    <p>链接样式</p>
</body>
</html>
```

### @import导入

```css
@import daoru.css;
@import 'daomxss';
@import "daoru.css";
@import url(daoru.css);
@import url('daoru.css');
@import url("daoru.css");
```

## CSS 选择器

### 元素选择器

元素选择器，最常见的 CSS 选择器，匹配文档树中该元素类型的每一个实例

```css
/* 单个元素选择器 */
div {
    background-color: pink;
}

/* 多个元素选择器 */
h1, p {
    color: gray;
}
```

### id 选择器

通过元素的 id 属性定位元素，影响范围最小
选择符 `#`

```css
#item{
    width: 200px;
    height: 200px;
}
```

### class 选择器

通过元素的 class 属性定位元素
选择符 `.`

```css
.box{
    width: 200px;
    height: 200px;
}
```

### 属性选择器

根据元素的属性及属性值来选择元素

```css
/* 对包含 title 属性的元素生效 */
*[title] {color:red;}

/* 对包含 title，href 属性的 a 标签生效  */
a[href][title] {color:red;}
```

### 后代选择器

又称为 包含选择器，对指定元素中的某一元素生效，递归查询符合子元素，全部生效

```css
h1 em {
    color:red;
}
```

查询 h1 标签中的 em 元素，不论嵌套多少层都会生效

### 子代选择器

仅对父元素下一级中符合的子元素生效

```css
h1>em {
    color:red;
}
```

查询 h1 标签中的 em 元素，仅查询一级


### 兄弟选择器

兄弟选择器（Adjacent sibling selector）可选择紧接在另一元素后的元素，且二者有相同父元素

![img][img@2]

### 伪类/元素 选择器

|选择器|描述|
|:---|:---|
|:active |向被激活的元素添加样式|
|:focus|	向拥有键盘输入焦点的元素添加样式|
|:hover|	当鼠标悬浮在元素上方时，向元素添加样式|
|:link	|向未被访问的链接添加样式|
|:visited|	向已被访问的链接添加样式|
|:first-child|	向元素的第一个子元素添加样式|
|:first-letter|	向文本的第一个字母添加特殊样式|
|:first-line|	向文本的首行添加特殊样式|
|:target|选择当前活动元素(点击URL包含锚的名字)|
|:before|	在元素之前添加内容|
|:after|	在元素之后添加内容|
|:focus|向具有焦点的元素设置样式|

```css
/* 当鼠标悬停在 a 标签时生效 */
a:hover {
    color: red;
}
```


## 选择器优先级

例如 同时两个选择器给同一个元素设置相同的属性，那么最终设置为哪个呢？这就要按照优先级来了

- **内连样式** 优先级 1000
- **id 选择器** 优先级 100
- **class 选择器** 优先级 10
- 元素选择器 优先级 1
- 统配选择器 优先级 0
- 继承的样式优先级没有

 以上的优先级先满足高的。

**注意：**
1. 如果是两种相同优先级 为同一个元素 同一个属性设置 的话，是哪个写在代码靠后 最终就按那个的样式
2. 交集选择器的优先级 所有优先级 加起来 运算 然后比较
3. 并集的话 就是各算各的

[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-12_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-12_02.png