<!-- TOC -->

- [overflow](#overflow)
- [float](#float)
  - [文档流](#%e6%96%87%e6%a1%a3%e6%b5%81)
  - [浮动特性](#%e6%b5%ae%e5%8a%a8%e7%89%b9%e6%80%a7)
  - [阻止浮动](#%e9%98%bb%e6%ad%a2%e6%b5%ae%e5%8a%a8)
  - [父元素占据空间](#%e7%88%b6%e5%85%83%e7%b4%a0%e5%8d%a0%e6%8d%ae%e7%a9%ba%e9%97%b4)
- [Position](#position)
  - [static](#static)
  - [relative , absolute , fixed](#relative--absolute--fixed)
    - [relative](#relative)
    - [absolute](#absolute)
    - [fixed](#fixed)
  - [sticky](#sticky)

<!-- /TOC -->

# overflow

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
overflow-y: scroll;

# 自适应设置滚动条
# 宽度溢出则水平设置滚动条
# 高度溢出则垂直设置滚动条
overflow: auto;
```

# float

## 文档流

指得是盒子按照 HTML 标签编写顺序依次从上到下的顺序，块元素独占一行，行内元素在同一行从左到右依次排列，先写的先排，后写的后排，每个盒子有自己的位置

## 浮动特性

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

## 阻止浮动

要想阻止浮动框，需要对该框使用 **clear** 属性

clear 属性的值可以是 left，right，both 或 none，它表示框的哪些边不应该挨着浮动框！

阻止浮动后会换行，可利用此特性制作聊天对话效果！



![](D:\思维导图\markdown\img\10-13_169.png)



```
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            .outer{
                width: 500px;
                height: 200px;
                border: 1px solid black;
                margin: 0 auto;
                padding: 20px;
            }
            .other{
                clear: both;
                float: left;
            }
            .me{
                clear: both;
                float:right;
            }
        </style>
    </head>
    <body>
        <div class="outer">
            <div class="other">在吗</div>
            <div class="me">在</div>
            <div class="other">阿巴阿巴</div>
            <div class="me">嗯嗯</div>
            <div class="other">阿巴阿巴阿巴阿巴</div>
            <div class="me">好的</div>
        </div>
    </body>
</html>
```



## 父元素占据空间

因为浮动元素脱离了文档流，所以包围的图片和文本的 div 不占据空间

此时，当元素浮动起来后，无法撑开父元素的高度，就会出现如下场景：

![img][img@2]

此时，为父元素设置如下属性即可：

```css
父元素{
    overflow: hidden;
}

#或者

父元素:after{
            content: "";
            display: table;
            clear: both;
        }
```

# Position

position 属性用来指定一个元素在网页上的位置，一共有 5 种定位方式，即 position 属性主要有 5 个值

- static
- relative
- fixed
- absolute
- sticky

## static

**static** 是 position 属性的默认值，表示没有定位，或者说不算具有定位属性。如果省略 position 属性，浏览器就认为该元素是 static 定位

这时，浏览器会按照源码的顺序，决定每个元素的位置。每个块级元素占据自己的区块，元素与元素之间不产生重叠，这个位置就是元素的默认位置

static 定位所导致的元素位置，是浏览器自主决定的，所以这时 `top` ， `bottom` ， `left` ， `right` 这四个属性无效

## relative , absolute , fixed

relative , absolute , fixed 这三个属性值有一个共同点，都是相对于某个基点的的定位，不同之处仅仅在于基点不同。

这三种定位都不会对其它元素的位置产生影响，因此元素之间可能产生重叠

### relative

**相对定位**，相对于元素的默认位置进行偏移，定位基点是元素的默认位置

首先按默认方式 (static) 生成一个元素，
然后相对于默认的位置进行偏移，移动的方向和幅度由 `top` ， `bottom` ， `left` ， `right` 属性确定，偏移之后原来位置还在占用，新的位置不占用空间

```css
div{
  position: relative;
  left: 50px;
  top: 50px;
}
```

### absolute

**绝对定位**，相对于**最接近的一个具有定位属性的父元素**进行定位

如果父类元素有定位属性，那么则以父类元素为参照物进行定位

如果父类元素没有定位属性，那么依次向上找，直到 body元素，即相对于浏览器窗口进行定位

```html
<div id="outter">
  <div id="inner">

  </div>
</div>  


#inner{
  position: absolute;
  top: 50px;
}
```

上面的代码中，父元素是 `relative` 定位，子元素是 `absolute` 定位，所以子元素的定位基点是父元素，相对于父元素的顶部向下偏移 50px，如果父元素是 `static` 定位，上面的例子就是相对于网页的顶部向下偏移 20 px

> 注意，absolute 定位的元素是不占空间的，会脱离文档流

### fixed

**固定定位**，相对于浏览器窗口进行偏移，即定位基点是浏览器窗口。这会导致元素的位置不随页面的滚动而变化，好像固定在网页上一样

> 例如： 网页 **回到顶部** 按钮

```css
div{
  position:fixed;
  bottom: 50px;
  right: 30px;
}

```

## sticky

**粘性定位**，跟前面的四个属性值都不一样，它会产生动态效果，很像 `relative` 和 `fixed` 的结合：一些时候是 `relative`定位（定位基点是自身默认位置），另一些时候自动变成 `fixed` 定位（定位基点是浏览器窗口）

因此，它能够形成 "**动态固定**" 的效果。比如，网页的搜索工具栏，初始加载时在自己的默认位置 (`relative`定位)

![img][img@3]

页面向下滚动时，搜索栏变成固定位置，始终停留在页面头部（fixed定位）

![img][img@4]

等到页面重新向上滚动回到原位，工具栏也会回到默认位置

必须指定 `top` ， `bottom` ， `left` ， `right` 其中之一，浏览器把它当作 `sticky` 的生效门槛，否则就等同于 `relative` 定位，不产生 动态固定 的效果。

```css

#item {
  position: sticky; top: 50px; 
}
```

在浏览器顶部与 元素 item 的距离大于 50 px 时，元素为相对定位。之后，元素将固定在与顶部距离 50 px 的位置，直到浏览器窗口回滚到超过阈值



[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_06.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_07.png
[img@3]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-14_08.png
[img@4]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-14_09.png