<!-- TOC -->

- [CSS 盒子模型(Box Model)](#css-%e7%9b%92%e5%ad%90%e6%a8%a1%e5%9e%8bbox-model)
- [元素的宽度和高度](#%e5%85%83%e7%b4%a0%e7%9a%84%e5%ae%bd%e5%ba%a6%e5%92%8c%e9%ab%98%e5%ba%a6)
- [内边距](#%e5%86%85%e8%be%b9%e8%b7%9d)
- [外边距](#%e5%a4%96%e8%be%b9%e8%b7%9d)
- [外边距自动合并](#%e5%a4%96%e8%be%b9%e8%b7%9d%e8%87%aa%e5%8a%a8%e5%90%88%e5%b9%b6)

<!-- /TOC -->

# CSS 盒子模型(Box Model)

所有的 HTML 元素可以看作盒子

CSS 盒模型本质上是一个盒子，封装周围的 HTML 元素，包括：边距，边框 和 实际内容

下面的图片说明了盒子模型：

![img][img@1]

- **Margin(外边距)**: 边框外的区域
- **Border(边框)**: 围绕在内边距和内容外的边框
- **Padding(内边距)**: 内容周围的区域
- **Content(内容)**: 盒子的内容

# 元素的宽度和高度

当你指定一个 CSS 元素的宽度和高度属性时，你只是设置内容区域的宽度和高度。要知道，元素的实际大小，还必须添加填充，边框和边距

```css
div {
    width: 300px;
    height: 200px;
    border: 30px solid green;
    padding: 40px;
    margin: 50px;
}
```

最终元素的总宽度计算公式是这样的：

元素实际宽度 = 宽度 + 左内边距 + 右内边距 + 左边框 + 右边框 + 左边距 + 右边距
元素实际高度 = 高度 + 上内边距 + 下内边距 + 上边框 + 下边框 + 上边距 + 下边距

因此上边的元素宽度为： 300 + 30 + 30 + 40 + 40 + 50 + 50 = 540
因此上边的元素高度为： 200 + 30 + 30 + 40 + 40 + 50 + 50 = 440

# 内边距

```css
padding-top: 10px;

padding-left: 10px;

padding-bottom: 10px;

padding-right: 10px;

# 设置四边内边距
padding: 10px;

# 分别设置 上下 左右
padding: 30px 40px;

# 分别设置 上 左右 下
padding: 30px 40px 50px;

# 分别设置 上 右 下 左
padding: 30px 40px 50px 60px;
```

# 外边距

```css
margin-top: 10px;

margin-left: 10px;

margin-bottom: 10px;

margin-right: 10px;

# 设置四边外边距
margin: 10px;

# 分别设置 上下 左右
margin: 30px 40px;

# 分别设置 上 左右 下
margin: 30px 40px 50px;

# 分别设置 上 右 下 左
margin: 30px 40px 50px 60px;

# 自动水平居中
margin: auto;
```

# 外边距自动合并

外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。

合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。


**外边距合并**

外边距合并（叠加）是一个相当简单的概念。但是，在实践中对网页进行布局时，它会造成许多混淆。

简单地说，外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。

当一个元素出现在另一个元素上面时，第一个元素的下外边距与第二个元素的上外边距会发生合并。请看下图:

![img][img@2]

当一个元素包含在另一个元素中时（假设没有内边距或边框把外边距分隔开），它们的上和/或下外边距也会发生合并。请看下图：

![img][img@3]

[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_03.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_04.png
[img@3]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/css/05-13_05.png