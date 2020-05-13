<!-- TOC -->

- [overflow](#overflow)
- [float](#float)
  - [文档流](#%e6%96%87%e6%a1%a3%e6%b5%81)
  - [浮动特性](#%e6%b5%ae%e5%8a%a8%e7%89%b9%e6%80%a7)
  - [阻止浮动](#%e9%98%bb%e6%ad%a2%e6%b5%ae%e5%8a%a8)
  - [父元素占据空间](#%e7%88%b6%e5%85%83%e7%b4%a0%e5%8d%a0%e6%8d%ae%e7%a9%ba%e9%97%b4)
- [定位](#%e5%ae%9a%e4%bd%8d)

<!-- /TOC -->

## overflow

overflow 属性用于控制内容溢出元素框时显示的方式

|属性值|描述|
|:---|:---|
|visible|	默认值。内容不会被修剪，会呈现在元素框之外|
|hidden|	内容会被修剪，并且其余内容是不可见的|
|scroll|	内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容|
|auto|	如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容|

```css
# 内容会被修剪，浏览器会显示滚动条以便查看其余内容
overflow: scroll;

# 设置 水平 垂直 滚动条状态
overflow: scroll hidden;

# 设置 水平滚动条
overflow-x: scroll;

# 设置 垂直滚动条
overflow-y: hidden;
```

## float

### 文档流

指得是盒子按照 HTML 标签编写顺序依次从上到下的顺序，块元素独占一行，行内元素在同一行从左到右依次排列，先写的先排，后写的后排，每个盒子有自己的位置

### 浮动特性

浮动: 指的是标签浮动到指定的位置上，浮动之后不会和之前的元素保持同一层

- 浮动会脱离文档流，不再占用位置，会覆盖后面的没有浮动的元素
- 浮动只有两个方向，即 左浮动(left) 和 右浮动(right)
- 浮动会造成文字环绕效果
- 停止浮动
  - 当浮动遇到父元素的边界停止浮动
  - 如果前面有浮动的元素，碰到前面的浮动元素并列一排显示
  - 如果前面有未浮动的元素，换行浮动
  - 当浮动的元素的宽度，超过父类元素的边界时，自动换行

![img][img@1]

### 阻止浮动

要想阻止浮动框，需要对该框使用 **clear** 属性

clear 属性的值可以是 left，right，both 或 none，它表示框的哪些边不应该挨着浮动框！

### 父元素占据空间

因为浮动元素脱离了文档流，所以包围的图片和文本的 div 不占据空间

此时，当元素浮动起来后，无法撑开父元素的高度，就会出现如下场景：

![img][img@2]

此时，为父元素设置如下属性即可：

```css
父元素:after{
            content: "";
            display: table;
            clear: both;
        }
```

## 定位

...






[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_06.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_07.png