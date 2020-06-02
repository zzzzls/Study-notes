<!-- TOC -->

- [什么是 DOM](#%e4%bb%80%e4%b9%88%e6%98%af-dom)
- [什么是 HTML DOM](#%e4%bb%80%e4%b9%88%e6%98%af-html-dom)
- [DOM 操作](#dom-%e6%93%8d%e4%bd%9c)
  - [HTML DOM 节点](#html-dom-%e8%8a%82%e7%82%b9)
  - [Document 对象](#document-%e5%af%b9%e8%b1%a1)
    - [常用属性](#%e5%b8%b8%e7%94%a8%e5%b1%9e%e6%80%a7)
    - [获取元素](#%e8%8e%b7%e5%8f%96%e5%85%83%e7%b4%a0)
  - [Element对象](#element%e5%af%b9%e8%b1%a1)
    - [基本属性](#%e5%9f%ba%e6%9c%ac%e5%b1%9e%e6%80%a7)
    - [属性修改](#%e5%b1%9e%e6%80%a7%e4%bf%ae%e6%94%b9)
    - [节点操作](#%e8%8a%82%e7%82%b9%e6%93%8d%e4%bd%9c)
    - [样式操作](#%e6%a0%b7%e5%bc%8f%e6%93%8d%e4%bd%9c)
    - [文本操作](#%e6%96%87%e6%9c%ac%e6%93%8d%e4%bd%9c)
    - [元素/节点 增删](#%e5%85%83%e7%b4%a0%e8%8a%82%e7%82%b9-%e5%a2%9e%e5%88%a0)
- [事件](#%e4%ba%8b%e4%bb%b6)
  - [事件类型](#%e4%ba%8b%e4%bb%b6%e7%b1%bb%e5%9e%8b)
  - [绑定事件](#%e7%bb%91%e5%ae%9a%e4%ba%8b%e4%bb%b6)
  - [Event 对象常见应用](#event-%e5%af%b9%e8%b1%a1%e5%b8%b8%e8%a7%81%e5%ba%94%e7%94%a8)
  - [事件代理](#%e4%ba%8b%e4%bb%b6%e4%bb%a3%e7%90%86)
  - [常用事件速查手册](#%e5%b8%b8%e7%94%a8%e4%ba%8b%e4%bb%b6%e9%80%9f%e6%9f%a5%e6%89%8b%e5%86%8c)

<!-- /TOC -->

# 什么是 DOM

**文档对象模型** ( **D**ocument **O**bject **M**odel ) 是 HTML 和 XML 文档的编程接口。它提供了对文档的结构化的表述，并定义了一种方式可以从程序中对该结构进行访问，从而改变文档的结构，样式和内容。DOM 将文档解析为一个由节点和对象 ( 包含属性和方法 ) 组成的结构集合。简言之，它会将 WEB 页面和脚本或程序语言来连接起来

一个 WEB 页面是一个文档，这个文档可以在浏览器窗口或作为 HTML 源码显示出来。但上述两个情况中都是同一份文档，文档对象模型 ( DOM ) 提供了对同一份文档的另一种表现，存储和操作的方式。DOM 是 WEB 页面的完全面向对象的表述，它能够使用如 JavaScript 等脚本语言进行修改

# 什么是 HTML DOM

HTML DOM 是 HTML 的**标准对象模型和编程接口**，它定义了:

- 作为对象的 HTML 元素
- 所有 HTML 元素的属性
- 访问所有 HTML 元素的方法
- 所有 HTML 元素的事件

![img][img@1]

通过这个对象模型，JavaScript 可以获得创建动态 HTML 的所有力量：

- JavaScript 能改变页面中的所有 HTML 元素
- JavaScript 能改变页面中的所有 HTML 属性
- JavaScript 能改变页面中的所有 CSS 样式
- JavaScript 能删除已有的 HTML 元素和属性
- JavaScript 能添加新的 HTML 元素和属性
- JavaScript 能对页面中所有已有的 HTML 事件作出反应
- JavaScript 能在页面中创建新的 HTML 事件

# DOM 操作

## HTML DOM 节点

在 HTML DOM 中，每一个元素都是 节点

- 文档是一个文档节点
- 所有的 HTML 元素都是元素节点
- 所有的 HTML 属性都是属性节点
- 文本插入到 HTML 元素是文本节点
- 注释是注释节点

## Document 对象

当浏览器载入 HTML 文档，它就会成为 **Document 对象**
Document 对象是 HTML 文档的根节点
Document 对象使我们可以从脚本中对 HTML 页面中的所有元素进行访问

### 常用属性

|属性|描述|
|:---|:---|
|document.activeElement|返回当前获取焦点元素|
|document.cookie|设置或返回与当前文档有关的所有cookie|
|document.body|返回当前文档的 body 元素|
|document.baseURL|返回文档的绝对基础URL|
|document.documentElement|返回文档根节点|
|document.domain|返回当前文档的域名|
|document.forms|返回当前文档中所有 Form 对象引用|
|document.images|返回当前文档中所有 image 对象引用|
|document.links|返回文档中所有链接对象引用|
|document.head|返回文档 head 元素|
|document.referrer|返回载入当前文档的文档URL|
|document.title|返回当前文档的标题|
|document.URL|返回文档完整URL|
|document.readyState|返回当前文档加载状态|
|document.characterSet|返回当前文档使用的字符集|

### 获取元素

(1) 通过 **id属性** 获取元素对象

返回值为 元素对象

```javascript
var oDiv = document.getElementById("id值");
```

(2) 通过 **标签名字** 获取元素对象

返回值为 元素数组

```javascript
var oDiv = document.getElementsByTagName("标签名");
```

(3) 通过 **class属性** 获取元素对象

返回值为 元素数组

```javascript
var oDiv = document.getElementsByClassName("class值")
```

(4) 通过 **name值** 获取元素对象

返回值为 元素数组

```javascript
var oDiv = document.getElementsByName("name值")
```

(5) 通过 **CSS选择器** 获取元素对象

```javascript
# 返回文档中匹配 CSS选择器 的第一个元素
document.querySelector("CSS选择器")

# 返回文档中匹配 CSS选择器 的所有元素
document.querySelectorAll("CSS选择器");
```

## Element对象

**元素对象** ( Element ) 代表着一个 HTML 元素
元素对象的 子节点 可以是 元素节点，文本节点，注释节点

### 基本属性

|属性|描述|
|:---|:---|
|element.attributes|返回元素的属性数组|
|element.offsetHeight|返回元素的高度(包括border和padding)|
|element.offsetWidth|返回元素的宽度(包括border和padding)|
|element.offsetLeft|返回元素距离父元素左侧的距离(父元素需要具备定位属性)|
|element.offsetTop|返回元素距离父元素顶部的距离(父元素需要具备定位属性)|

### 属性修改

|函数|描述|
|:---|:---|
|element.hasAttributes()|判断元素是否具有属性|
|element.hasAttribute(attr)|判断元素是否具有指定属性|
|element.setAttribute(attr,value)|给元素设置属性|
|element.getAttribute(attr)|获取指定属性|
|element.removeAttribute(attr)|删除指定属性|

### 节点操作

|属性|描述|
|:---|:---|
|element.children|返回元素子元素节点|
|element.firstElementChild|返回元素第一个元素节点|
|element.lastElementChild|返回元素最后一个元素点|
|element.previousElementSibling|返回元素上一个兄弟元素|
|element.nextElementSibling|返回元素下一个兄弟元素|
|element.parentNode|返回元素父节点|
|element.hasChildNodes()|判断元素是否具有子元素|

### 样式操作

**1. element.style 读取/修改样式**

```javascript
// 获取元素对象
var div = document.getElementById("div");
// 获取样式
console.log(div.style.backgroundColor)
// 修改样式
div.style.backgroundColor = "red";
```

**2. getComputedStyle 获取样式**

```javascript
// 获取元素对象的 CSS样式 数组
var style = window.getComputedStyle(元素对象[,"伪类"]);
console.log(style);
```

**两者区别**

- 只读和读写
  - `getComputedStyle` 方法是只读的，只能获取样式，不能设置；
  - `element.style` 能读能写 

- 获取属性的范围
  - `getComputedStyle` 方法获取的是最终应用在元素上的所有 CSS属性对象；
  - `element.style` 只能获取 style 属性中的 CSS样式。
  
对于一个光秃秃的元素 `<p>`，`element.style `在获取样式方面就不如 `getComputedStyle` 方法了！




### 文本操作

|属性|描述|
|:---|:---|
|element.innerHTML|设置和查看标签内容，包含 HTML 格式|
|element.innerText|设置和查看标签内容，仅支持纯文本内容|


### 元素/节点 增删

**创建标签**

```javascript
var btu = document.createElement("button");
```

**创建文本节点**

```javascript
var text = document.createTextNode("hello");
```

**克隆节点**

`cloneNode(deep)` 克隆一个节点，deep 设置为 true 将递归克隆内部节点

```javascript
// 获取 div 元素
var div = div.insertBefore(h1,div.firstChild);
// 克隆 div 元素
var new_div = div.cloneNode()
```

**添加节点**

`appendChild(node)` 添加一个节点到末尾

```javascript
// 创建一个 h1 标签
var h1 = document.createElement("h1");
// 创建一个 文本节点
var text = document.createTextNode("hello");

// 将 文本节点 添加到 h1标签中
h1.appendChild(text);
```

**插入节点**
`insertBefore(new_node,old_node)` 插入一个节点到某个节点之前

```javascript
// 创建一个 h1 标签
var h1 = document.createElement("h1");
// 获取 div 元素
var div = document.getElementById("item");

// 插入 h1 标签到父节点第一个位置
div.insertBefore(h1,div.firstChild);
```

**删除节点**

`removeChild(node)` 删除一个子节点

```javascript
// 获取 div 元素
var div = document.getElementById("item");

// 删除 div 元素最后一个子节点
div.removeChild(div.lastChild)
```

# 事件

事件是 JavaScript 与 HTML 交互的基础，要实现用户与页面的交互，先要对目标元素绑定特定的事件，设置事件处理函数，然后用户触发事件，事件处理函数执行，产生交互效果

## 事件类型

在 HTML DOM 中有两种事件传播的方法：冒泡和捕获

事件传播是一种定义当发生事件时元素次序的方法，假如 `<div>` 元素内有一个 `<p>`，然后用户点击了这个 `<p>` 元素，应该首先传递哪个元素的 click 事件？

在冒泡中，最内侧元素的事件会首先处理，然后是更外侧的：首先处理 `<p>` 元素的点击事件，然后是 `<div>` 元素的点击事件  
在捕获中，最外侧元素的事件会首先被处理，然后是更内侧的：首先处理 `<div>` 元素的点击事件，然后是 `<p>` 元素的点击事件

## 绑定事件

**(1) DOM 0级事件**

```javascript
<button id="btu">提交</button>
<script>
    var btu = document.getElementById("btu");

    // 绑定事件
    btu.onclick = function(){
        console.log("hello!");
    };

    // 解绑事件
    btu.onclick = null;
</script>
```
> 缺点：无法设置多个事件处理函数

**(2) DOM 2级事件**

```javascript
<button id="btu">提交</button>
<script>
    var btu = document.getElementById("btu");

    // 绑定事件
    btu.addEventListener("click",showFn,false);
    btu.addEventListener("click",showFn2,false);

    function showFn(){
        console.log("hello fn1");
    };

    function showFn2(){
        console.log("hello fn2");
    }

    // 解绑事件
    btn.removeEventListener("click",showFn,false);
</script>
```

> 可以为元素绑定多个事件处理函数，可以通过第三个参数设置事件类型，默认为 false，将使用冒泡传播，如果设置为 true，则为捕获传播

## Event 对象常见应用

(1) `event.preventDefault()`

**如果调用这个方法，元素默认事件行为将不再触发。**  
什么是默认事件呢？例如表单 点击提交按钮跳转页面，a标签默认页面跳转或是锚点定位等

很多时候我们使用 a标签仅仅是想当做一个普通的按钮，点击实现一个功能，不想页面跳转

```javascript
<a id="test" href="http://www.cnblogs.com">链接</a>
<script>
var a = document.getElementById("test");
// 此时，点击a标签只会打印消息，而不会进行页面跳转
a.onclick = function(e){
    console.log("点击了a标签");
    e.preventDefault();
}
</script>
```

(2) `event.stopPropagation()`

**阻止事件冒泡到父元素**

前边提到事件冒泡是指事件从目标节点自下而上向 window对象传播的阶段，添加 `event.stopPropagation()` 这句话后，就阻止了父事件的执行

(3) `event.stopImmediatePropagation();`

**即能阻止事件向父元素冒泡，也能阻止元素同事件类型的其它监听器被触发**

例如，一个按钮元素绑定了多个 click 事件，当在某个 click() 事件中添加了 `event.stopImmediatePropagation();` 后，不仅阻止了父事件的执行，还阻止了其它 click 事件的执行

## 事件代理

由于事件会在冒泡阶段向上传播到父节点，因此可以把子节点的监听函数定义在父节点上，由父节点的监听函数统一处理多个子元素的事件，这种方法叫做事件的代理（delegation）

优点：

1. **减少内存消耗，提高性能**

假设有一个列表，列表之中有大量的列表项，我们需要在点击每个列表项的时候响应一个事件

如果给每个列表项一一绑定一个函数，那对于内存的消耗是非常庞大的，效率上需要消耗很多性能，借助事件代理，我们只需要给父容器 ul 绑定方法即可，这样不管点击的是哪一个后代元素，都会根据冒泡传播的传递机制，把容器的 click行为触发，然后把对应的方法执行，根据事件源，我们可以知道点击的是谁，从而完成不同的事

2. **动态绑定事件**

很多时候，我们需要动态的增删列表项元素，如果一开始给每个子元素绑定事件，那么在列表发生变化时，就需要重新给新增的元素绑定事件，给即将删除的元素解绑事件，如果用事件代理就会省去很多这样的麻烦！


## 常用事件速查手册

- [RUNOOB](https://www.runoob.com/jsref/dom-obj-event.html)
- [MDN](https://developer.mozilla.org/zh-CN/docs/Web/Events)
- [W3cSchool](https://www.w3school.com.cn/jsref/dom_obj_event.asp)



[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/JavaScript/05-16_01.png