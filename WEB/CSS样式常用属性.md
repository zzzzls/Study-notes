<!-- TOC -->

- [CSS 颜色](#css-%e9%a2%9c%e8%89%b2)
- [背景属性](#%e8%83%8c%e6%99%af%e5%b1%9e%e6%80%a7)
- [字体属性](#%e5%ad%97%e4%bd%93%e5%b1%9e%e6%80%a7)
- [文本属性](#%e6%96%87%e6%9c%ac%e5%b1%9e%e6%80%a7)
- [边框属性](#%e8%be%b9%e6%a1%86%e5%b1%9e%e6%80%a7)
- [图片属性](#%e5%9b%be%e7%89%87%e5%b1%9e%e6%80%a7)

<!-- /TOC -->

## CSS 颜色

CSS 的颜色可以通过以下方法指定：

**十六进制颜色**

```css
p {
    background-color: #ff0000;
}
```

**RGB颜色**

```css
p {
    background-color: rgb(255,0,0);
}
```

**RGBA颜色**

```css
p {
    background-color: rgb(255,0,0,0.5);
}
```

**英文单词**

```css
p {
    background-color: red;
}
```

## 背景属性

```css
#item {
    background-image: url("./cs.png");
}
```

|属性|描述|
|:---|:---|
|background|	简写属性，作用是将背景属性设置在一个声明中|
|background-attachment|	背景图像是否固定或者随着页面的其余部分滚动|
|background-color|	设置元素的背景颜色|
|background-image|	把图像设置为背景|
|background-position	|设置背景图像的起始位置|
|background-size|设置背景图像大小|
|background-repeat|	设置背景图像是否及如何重复|


## 字体属性

```css
/* 按所列的顺序查找这些字体，遇到可用的字体则使用 */
h1 {
    font-family: "微软雅黑","宋体";
}
```

|属性|描述|
|:---|:---|
|font|	简写属性，作用是把所有针对字体的属性设置在一个声明中|
|font-family|	设置字体系列|
|font-size|	设置字体的尺寸|
|font-style|	设置字体风格|
|font-weight|	设置字体的粗细|

## 文本属性

```css
p {
    color：red;
    text-indent: 15px;
}
```

|属性|描述|
|:---|:---|
|color	|设置文本颜色|
|direction|	设置文本方向|
|text-align|	对齐元素中的文本|
|text-indent|	缩进元素中文本的首行|
|text-transform|	控制元素中的字母大小写|
|text-decoration|	向文本添加修饰|
|text-shadow	|向文本添加阴影|
|text-wrap|	规定文本的换行规则|
|line-height	|设置行高|
|white-space|	设置元素中空白的处理方式|
|word-spacing|	设置字间距|
|letter-spacing|	设置字符间距|

## 边框属性

```css
div {
    border: 1px solid red;
}
```

|属性|描述|
|:---|:---|
|border|	简写属性，用于把针对四个边的属性设置在一个声明|
|border-style|	设置元素边框样式|
|border-width|	设置元素边框宽度|
|border-color|	设置元素边框颜色|
|border-bottom|	设置元素下边框|
|border-left|	设置元素左边框|
|border-right|	设置元素右边框|
|border-top|	设置元素上边框|
|border-radius|设置边框圆角|
|box-shadow|设置边框阴影|

## 图片属性

```css
# 使文字和图片同排同行时候上下垂直居中
img { 
    vertical-align:middle;
}
```

**vertical-align 值:**

|值|描述|
|:---|:---|
|baseline|	默认。元素放置在父元素的基线上。|
|sub|	垂直对齐文本的下标。|
|super|	垂直对齐文本的上标|
|top|	把元素的顶端与行中最高元素的顶端对齐|
|text-top|	把元素的顶端与父元素字体的顶端对齐|
|middle|	把此元素放置在父元素的中部。|
|bottom|	把元素的底端与行中最低的元素的顶端对齐。|
|text-bottom	|把元素的底端与父元素字体的底端对齐。|


