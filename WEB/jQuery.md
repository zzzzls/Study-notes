<!-- TOC -->

- [jQuery 简介](#jquery-%e7%ae%80%e4%bb%8b)
- [jQuery 版本](#jquery-%e7%89%88%e6%9c%ac)
  - [下载 jQuery](#%e4%b8%8b%e8%bd%bd-jquery)
  - [替代方案](#%e6%9b%bf%e4%bb%a3%e6%96%b9%e6%a1%88)
  - [查看当前 jQuery 版本](#%e6%9f%a5%e7%9c%8b%e5%bd%93%e5%89%8d-jquery-%e7%89%88%e6%9c%ac)
- [$ 符号](#%e7%ac%a6%e5%8f%b7)
- [jQuery 选择器](#jquery-%e9%80%89%e6%8b%a9%e5%99%a8)
- [样式操作](#%e6%a0%b7%e5%bc%8f%e6%93%8d%e4%bd%9c)
  - [返回 css 属性](#%e8%bf%94%e5%9b%9e-css-%e5%b1%9e%e6%80%a7)
  - [设置 css 属性](#%e8%ae%be%e7%bd%ae-css-%e5%b1%9e%e6%80%a7)
  - [设置多个 css 属性](#%e8%ae%be%e7%bd%ae%e5%a4%9a%e4%b8%aa-css-%e5%b1%9e%e6%80%a7)
- [DOM 操作](#dom-%e6%93%8d%e4%bd%9c)
  - [内容操作](#%e5%86%85%e5%ae%b9%e6%93%8d%e4%bd%9c)
  - [属性操作](#%e5%b1%9e%e6%80%a7%e6%93%8d%e4%bd%9c)
  - [创建元素](#%e5%88%9b%e5%bb%ba%e5%85%83%e7%b4%a0)
  - [添加元素](#%e6%b7%bb%e5%8a%a0%e5%85%83%e7%b4%a0)
  - [删除元素](#%e5%88%a0%e9%99%a4%e5%85%83%e7%b4%a0)
  - [克隆元素](#%e5%85%8b%e9%9a%86%e5%85%83%e7%b4%a0)
  - [尺寸](#%e5%b0%ba%e5%af%b8)
- [事件](#%e4%ba%8b%e4%bb%b6)
  - [语法](#%e8%af%ad%e6%b3%95)
  - [常见事件](#%e5%b8%b8%e8%a7%81%e4%ba%8b%e4%bb%b6)
- [动画](#%e5%8a%a8%e7%94%bb)
  - [隐藏 & 显示](#%e9%9a%90%e8%97%8f--%e6%98%be%e7%a4%ba)
  - [淡入淡出](#%e6%b7%a1%e5%85%a5%e6%b7%a1%e5%87%ba)
  - [滑动](#%e6%bb%91%e5%8a%a8)
  - [自定义动画](#%e8%87%aa%e5%ae%9a%e4%b9%89%e5%8a%a8%e7%94%bb)
    - [语法](#%e8%af%ad%e6%b3%95-1)
    - [操作多个属性](#%e6%93%8d%e4%bd%9c%e5%a4%9a%e4%b8%aa%e5%b1%9e%e6%80%a7)
    - [使用相对值](#%e4%bd%bf%e7%94%a8%e7%9b%b8%e5%af%b9%e5%80%bc)
    - [使用预定义的值](#%e4%bd%bf%e7%94%a8%e9%a2%84%e5%ae%9a%e4%b9%89%e7%9a%84%e5%80%bc)
    - [使用队列功能](#%e4%bd%bf%e7%94%a8%e9%98%9f%e5%88%97%e5%8a%9f%e8%83%bd)
  - [停止动画](#%e5%81%9c%e6%ad%a2%e5%8a%a8%e7%94%bb)

<!-- /TOC -->

# jQuery 简介

jQuery 是一个 Javascript 函数库
jQuery 是一个轻量级的 "写多少，做的多" 的 Javascript 库
jQuery 可以帮助我们做这些事情：

- 消除浏览器差异：不需要自己写冗长的代码来针对不同的浏览器绑定事件，编写 AJAX 等代码
- 简介的操作 DOM 的方法：写 `$("#item")` 肯定比 `document.getElementById("item")` 来的简洁
- 轻松实现动画，修改 CSS 等各种操作

# jQuery 版本

目前 jQuery 有 `1.x`、`2.x`，、`3.x` 三个版本:

| 版本 | 描述                                                       |
| :--- | :--------------------------------------------------------- |
| 1.x  | 兼容ie 678，使用最广泛                                     |
| 2.x  | 不兼容ie 678，代码更为简洁，不考虑兼容低版本浏览器可以使用 |
| 3.x  | 不兼容ie 678，只支持最新浏览器                             |

## 下载 jQuery

有两个版本的 jQuery 可供下载

- **Production version** - 用于实际的网站中，已被精简和压缩
- **Development version** - 用于测试和开发（未压缩，是可读的代码）

以上两个版本都可以从 [jquery.com](https://jquery.com) 中下载

jQuery 库是一个 Javascript 文件，你可以在 head 中使用 script 标签引用它：

```html
<head>
<script src="./jquery-1.8.3.min.js"></script>
</head>
```

## 替代方案

如果您不希望下载并存放 jQuery，那么也可以通过 CDN(内容分发网路) 引用它

[Staticfile CDN](https://staticfile.org/)、百度、又拍云、新浪、谷歌和微软的服务器都存有 jQuery

**Staticfile CDN**

```html
<head>
<script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js">
</script>
</head>
```

**baidu CDN**

```html
<head>
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js">
</script>
</head>
```

## 查看当前 jQuery 版本

我们可以使用在浏览器的 Console 窗口使用 `$.fn.jquery` 命令来查看当前 jQuery 使用的版本


# $ 符号

`$` 是著名的 jQuery 符号。实际上，jQuery 把所有功能全部封装在一个全局变量 jQuery 中，而 `$` 也是一个合法的变量名，它是变量 `jQuery` 的别名

```Javascript
window.jQuery; // jQuery(selector, context)
window.$; // jQuery(selector, context)
$ === jQuery; // true
typeof($); // 'function'
```

`$` 本质就是一个函数，既是函数也是对象，于是 `$` 处理可以直接调用外，也可以有很多其它属性

# jQuery 选择器

| 选择器                   | 描述                                                |
| :----------------------- | :-------------------------------------------------- |
| `$('div')`               | 元素选择器                                          |
| `$('#id')`               | id选择器                                            |
| `$('.class')`            | class选择器                                         |
|`$(this)`|选择当前 html 元素|
|`$('div>p')`|子代选择器|
|`$('div+p')`|获取某元素后一个同级元素|
|`$('div~p')`|获取某元素后所有同级元素|
|`$('a[title]')`|获取具有 title 属性的 a 元素|
|`$('a[title=num]')`|获取title 属性等于 num 的 a 元素|
|`$('a[xz][title=num]')`|获取具有xz属性且title属性=num的 a 元素|
|`$('li:first')`|获取第一个元素|
|`$('li:last')`|获取最后一个元素|
|`$('li:eq(2)')`|获取索引等于index的元素|
|`$('li:gt(2)')`|获取索引大于index的元素|
|`$(':contains("aaa")')`|选取含有"xzavier"文本的元素|
|`$('li:only-child')`|获取只有一个子元素的元素|
|`$('li:nth-child(n)')`|获取每个父元素中第n个元素(索引值从1开始计算|
|`$(':text')`|所有 type="text" 的 <input> 元素|
|`$(':button')`|所有 type="button" 的 <input> 元素|

更多选择器：[jQuery-选择器浅析](https://segmentfault.com/a/1190000006667079)


所有 jQuery选择器 的返回值均为 **jQuery 对象**
jQuery 对象类似数组，有 length 属性，并且可以通过下标的方式取值，但是并没有数组中其它 api函数

# 样式操作

## 返回 css 属性

```javascript
// 返回首个匹配元素的 backgroundColor 属性
$(".item>div").css("background-color");

// 返回第二个匹配元素的 backgroundColor 属性
$(".item>div").eq(1).css("background-color");
```

## 设置 css 属性

```javascript
$(".item>div").css("background-color","red");
```

## 设置多个 css 属性

```javascript
$(".item>div").css({
    "background-color":"red",
    "border":"5px sloid green"
});
```

# DOM 操作

## 内容操作

三个简单实用的用于 DOM 操作的 jQuery 方法：

- text() - 设置或返回所选元素的文本内容
- html() - 设置或返回所选元素的内容（包括 HTML 标记）
- val() - 设置或返回表单字段的值

```javascript
// 获得内容
$("#test").html();

//设置内容
$("#test").html("<p>123</p>");
```

## 属性操作


```javascript
// 获取属性
$("#item").attr("href")

// 设置属性
$("#item").attr("href","https://www.baidu.com")

// 设置多个属性
$("#item").attr({
  "href": "https://www.baidu.com",
  "title": "baidu"
})

// 删除属性
$("#item").removeAttr('name');
```

## 创建元素

```javascript
// 创建元素
var h1 = $('<h1></h1>');

// 创建文本
var text = $('<h1>这个是 h 标签</h1>');

// 创建属性
var h = $('<h1 title="标题">这个是 h 标签</h1>');
```

## 添加元素

插入内容要元素内部

- `append()` 在元素结尾插入内容
- `prepend()` 在元素开头插入内容

插入内容到元素外部

- `after()` 在元素之后插入内容
- `before()` 在元素之前插入内容

```javascript
// 在元素结尾插入文本
$('item').append('THE END');

//在元素结尾插入子元素
$('item').append('<p>THE END</p>');
```

## 删除元素

- remove() 删除被选元素
- empty() 清空元素

```javascript
// 删除当前元素
$("#outter").remove();

// 删除 class为inner 的 div元素
$("div").remove(".inner");

// 清空当前元素内容
$("#outter").remove();

```

## 克隆元素

`clone(events, deep )`

- *events* 布尔值，默认 false，是否克隆元素的事件处理函数
- *deep* 布尔值，默认 false，是否克隆元素子节点

## 尺寸

- **元素宽高** : `width()` / `height()`
- **元素宽高(padding)** : `innerWidth()` / `innerHeight()`
- **元素宽高(padding+border)** : `outerWidth()` / `outerHeight()`
- **元素宽高(padding+border+margin)** : `outerWidth(true`) \ `outerHeight(true)`

# 事件

## 语法

```javascript
$("p").click(function(){
    // 动作触发后执行的代码!!
});
```

## 常见事件

(1) `$(document).ready()`

在文档完全加载完后执行函数
  
(2) `click()`

点击 HTML 元素时执行

(3) `dblclick()`

当双击元素时，会发生 dblclick 事件

(4) `mouseover()`

鼠标移入元素事件

(5) `mouseout()`

鼠标移出元素事件

# 动画

## 隐藏 & 显示

- hide() 隐藏元素
- show() 显示元素
- toggle() 显示已隐藏的元素，隐藏已显示的元素

## 淡入淡出

- `fadeIn(spead,callback)`  淡入元素
- `fadeOn(spead,callback)`  淡出元素
- `fadeToggle(spead,callback)` 切换淡入淡出

  可选的 speed 参数规定效果的时长，它可以取以下值：**slow**、**fast** 或 **毫秒**  
  可选的 callback 参数是动画完成后所执行的函数名称  
  
  <br>

  ```javascript
  $("#outter").fadeIn("3000");

  $("#outter").fadeOn("slow");
  ```

- `fadeTo(speed,opacity,callback)`  渐变元素透明度
  <br>
  ```javascript
  $("#outter").fadeTo("3000","0.3");
  ```

## 滑动

- `slideDown(speed,callback)`  向下滑动元素
- `slideUp(speed,callback)`  向上滑动元素
- `slideToggle(speed,callback)`  切换滑动状态
  <br>
  可选的 speed 参数规定效果的时长，它可以取以下值：**slow**、**fast** 或 **毫秒**  
  可选的 callback 参数是动画完成后所执行的函数名称  

```javascript
$(".inner").slideToggle("2000");
```

## 自定义动画

animate() 方法用于创建自定义动画

### 语法

`$(selector).animate({params},speed,callback);`

- 必需的 params 参数定义形成动画的 CSS 属性。

- 可选的 speed 参数规定效果的时长。它可以取以下值："slow"、"fast" 或毫秒。

- 可选的 callback 参数是动画完成后所执行的函数名称。

```javascript
// 点击按钮后在1秒内将 #outter 元素向左移动250px
$("button").click(function(){
  $("#outter").animate({left:'250px'},1000);
})
```

> 默认情况下，所有 HTML 元素都有一个静态位置，且无法移动。
> 如需对位置进行操作，要记得首先把元素的 CSS position 属性设置为 relative、fixed 或 absolute！


### 操作多个属性

```javascript
$("button").click(function(){
  $("div").animate({
    left:'250px',
    opacity:'0.5',
    height:'150px',
    width:'150px'
  });
});
```

### 使用相对值

也可以使用相对值（该值相对于元素的当前值），需要在值的前面加上 **+=** 或 **-=**

```javascript
$("button").click(function(){
  $("div").animate({
    left:'250px',
    height:'+=150px',
    width:'+=150px'
  });
});
```

### 使用预定义的值

可以把属性的动画值设置为 **show**、**hide** 或 **toggle**

```javascript
$("button").click(function(){
  $("div").animate({
    height:'toggle'
  });
});
```

### 使用队列功能

默认地，jQuery 提供针对动画的队列功能。
如果编写多个 animate() 调用，jQuery 会逐一运行这些 animate 调用

```javascript
$("button").click(function(){
  var div=$("div");
  div.animate({height:'300px',opacity:'0.4'},"slow");
  div.animate({width:'300px',opacity:'0.8'},"slow");
  div.animate({height:'100px',opacity:'0.4'},"slow");
  div.animate({width:'100px',opacity:'0.8'},"slow");
});
```

## 停止动画

stop() 方法用于在动画或效果完成前对它们进行停止

`$(selector).stop(stopAll,goToEnd);`

可选的 stopAll 参数规定是否应该清除动画队列。默认是 false，即仅停止活动的动画，允许任何排入队列的动画向后执行。

可选的 goToEnd 参数规定是否立即完成当前动画。默认是 false。

```javascript
$("#stop").click(function(){
  $("#panel").stop();
});
```
