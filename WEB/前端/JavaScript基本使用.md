<!-- TOC -->

- [语法格式](#%e8%af%ad%e6%b3%95%e6%a0%bc%e5%bc%8f)
- [显示数据](#%e6%98%be%e7%a4%ba%e6%95%b0%e6%8d%ae)
- [变量](#%e5%8f%98%e9%87%8f)
- [变量提升](#%e5%8f%98%e9%87%8f%e6%8f%90%e5%8d%87)
- [数据类型](#%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
- [数据类型转换](#%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b%e8%bd%ac%e6%8d%a2)
- [运算符](#%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [算数运算符](#%e7%ae%97%e6%95%b0%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [比较运算符](#%e6%af%94%e8%be%83%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [逻辑运算符](#%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [三目运算符](#%e4%b8%89%e7%9b%ae%e8%bf%90%e7%ae%97%e7%ac%a6)
  - [void运算符](#void%e8%bf%90%e7%ae%97%e7%ac%a6)
- [定时器](#%e5%ae%9a%e6%97%b6%e5%99%a8)
  - [setInterval()](#setinterval)
  - [setTimeout()](#settimeout)
- [Json](#json)
- [异常](#%e5%bc%82%e5%b8%b8)
- [re](#re)

<!-- /TOC -->

## 语法格式

(1) **结尾**
- JavaScript 的语句需要使用 `;` 结尾

(2) **注释**
- 单行注释 //
- 多行注释 /* */

(3) **标识符**
JavaScript 标识符包括 变量名，函数名，参数名和属性名

合法的表示符应注意以下强制规则：

- 第一个字符必须是 字母、下划线 或 美元符号 $
- 不能与 JavaScript 关键字、保留字重名
- 严格区分大小写

## 显示数据

JavaScript 能够以以下方式 显示数据

- 使用 `alert()` 弹出警告框
- 使用 `document.write()` 写入 HTML 输出
- 使用 `innerHtml` 写入 HTML 元素
- 使用 `console.log()` 写入浏览器控制台

## 变量

js 是一门弱类型的语言，在 js 中的数据类型由值的类型决定，声明变量使用 **var** 语句

在一个 var语句中，可以声明一个或多个变量，也可以变量赋值，未赋值的变量初始化未 undefined(未定义的)

```javascript
var a;
var a,b,c;
var a = 1;
var a = 1, b = "123";
```

## 变量提升

```javascript
console.log(a); // undefined
a = 1;
console.log(a); // 1
var a;
```

在上面示例中，声明变量放在最后，赋值操作放在前面。由于 JavaScript 在预编译期已经对变量声明语句进行了预解析，所以第一行的代码读取变量值时不会抛出异常，而是返回未初始化的值 undefined，第三行带啊吗是在赋值操作之后读取，故显示为数字 1

## 数据类型

JavaScript 定义了 6 种基本数据类型，如下所示：

|数据类型|描述|
|:---|:---|
|null|空值|
|undefined|未定义的值，表示未赋值的初始化值|
|number|数字|
|string|字符串|
|boolean|布尔值|
|object|对象，复杂结构的数据集|

使用 `typeof()` 函数可以检测数据的基本类型

## 数据类型转换

|函数|描述|
|:---|:---|
|String()|转字符串|
|Number()|转数字|
|parseInt()|转 Int类型|
|parseFloat()|转 Float类型|
|Boolean()|转布尔值|

## 运算符

### 算数运算符

- `+` : 加法运算
- `-` : 减法运算
- `*` : 乘法运算
- `/` : 除法运算
- `%` : 求余运算
- `++` : 
  - a++ : 赋值后对自身加1
  - ++a : 对自身加1后赋值
- `--` : 同上

### 比较运算符

- `<` : 小于
- `>` : 大于
- `<=` : 小于等于
- `>=` : 大于等于
- `==` : 等于
- `===` : 绝对等于 (值和类型均相等)
- `!=` : 不等于
- `!==` : 不绝对等于

### 逻辑运算符

- `&&` : and
- `||` : or
- `!` : not

### 三目运算符

`<条件表达式> ? x : y`

如果条件表达式成立，则执行 x ，否则，执行 y

### void运算符

对给定的表达式进行求值，然后返回 **undefined**

```javascript
var a = 1;
void(a++); // undefined
console.log(a); // 2
```

**void应用场景**

(1) **JavaScript URLs**

当用户点击一个以 `javascript:URL` 时，他会执行 URL 中的代码，然后用返回的值替换页面内容，除非返回的值是 `undefined`  
void运算符可用于返回 `undefined` ，例如：

```html
<a href="javascript:void(document.body.style.backgroundColor='green');">
  点击这个链接会让页面背景变成绿色。
</a>
```

(2) **填充 a 标签**

有一些 a 标签，我们并不希望点击它们会跳转到另一个界面，而是引发一些交互操作

理论上而言，这类 a 标签都是没有 URL 的，但如果不写的化，点击它会刷新整个界面

因此，我们可以使用 `href="javascript:void(0)"` 的方式，确保点击它会执行一个纯粹无聊的 `void(0)`

## 定时器

### setInterval()

**间隔指定的毫秒数不停地执行指定的代码**

```javascript
//          执行的函数     毫秒
var timer = setInterval(function(){},1000);

// 停止
clearInterval(timer)
```

### setTimeout()

**在指定的毫秒数后指定指定代码**

```javascript
var timer = setTimeout(function(){},2000);

// 停止
clearTimeout(timer);
```

## Json

(1) **JSON.parse()**

将一个字符串转换为 JSON

```javascript
JSON.parse(text[, reviver])

// text 一个有效的json字符串
// reviver 可选 一个转换结果函数,将为对象每个成员调用此函数
```

(2) **JSON.stringify()**

将 Json 转换为 字符串

```javascript
JSON.stringify(value[, replacer[, space]])

// value 要转换的 json 值
// replacer 可选。用于转换结果的函数或数组
// 可选 文本添加缩进,空格和换行符
```

## 异常

try 语句测试代码块的错误。
catch 语句处理错误。
throw 语句创建自定义错误。
finally 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。

**try语句**

```javascript
try {
    ...
} catch(e) {
    ...
} finally {
    ...
}
```

**throw语句**

`throw exception`

抛出的内容可以是 JavaScript 字符串、数字、逻辑值或对象

```javascript
try{
  if(x == "")  throw "值为空";
  if(isNaN(x)) throw "不是数字";
  if(x < 5)    throw "太小";
  if(x > 10)   throw "太大";
}catch(err) {
  message.innerHTML = "错误: " + err;
}
```

## re

**(1) RegExp 修饰符**

修饰符用于执行不区分大小写和全文的搜索。

i - 修饰符是用来执行不区分大小写的匹配。

g - 修饰符是用于执行全文的搜索（而不是在找到第一个就停止查找,而是找到所有的匹配）

m - 执行多行匹配


```javascript

// 正则表达式
var reg = /^1[0-9]{10}$/;

// 带修饰符的正则表达式
var reg = /^1[0-9]{10}$/g;
```

**(2) test()**

搜索字符串的值，根据结果返回 true 或者 false

```javascript

// 判断字符串中是否包含 python 字符
var str = "hello python";
var reg = /python/;

console.log(reg.test(str));
```

**(3) exec()**

检索字符串中的指定值，返回被找到的值，如果没有无匹配，返回 null

```javascript
// 提取字符串中的 数字
var str = "please call 110";
var reg = /\d{3}/;

console.log(reg.exec(str));
```

**(4) 支持正则表达式的 String 对象 的方法**

|方法|描述|
|:---|:---|
|search()|检索于正则表达式相匹配的值|
|match()|找到一个或多个正则表达式的匹配|
|replace()|替换匹配正则表达式的子串|
|split()|把字符串分割为字符串数组|