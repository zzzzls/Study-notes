# JavaScript 历史

1995 年 2 月，Netscape 公司发布 Netscape Navigator 2 浏览器，并在这个浏览器中免费提供了一个开发工具——LiveScript。由于当时 Java 比较流行，Netscape 便把 LiveScript 改名为 JavaScript，这也是最初的 JavaScript 1.0 版本。

由于 JavaScript 1.0 很受欢迎，不久，微软在 Internet Explorer 3 中也加入了脚本编程功能。为了避免与 Netscape 的 JavaScript 产生纠纷，微软特意将其命名为 JScript。

1997 年，欧洲计算机制造商协会（ECMA）以 JavaScript 1.1 为基础制订了脚本语言标准——ECMA-262，并命名为 ECMAScript。

1998 年，国际标准化组织和国际电工委员会（ISO/IEC）采用了 ECMAScript 标准（即 ISO/IEC-16262）。自此，浏览器厂商就以 ECMAScript 作为各自 JavaScript 实现的规范标准。JavaScript 正式从各自为政走向了规范统一。

# JavaScript 构成

ECMAScript 是 JavaScript 的标准，但它并不等同于 JavaScript，也不是唯一被标准化的规范

实际上，一个完整的 JavaScript 实现由以下 3 个不同部分组成：

- **核心** ( ECMAScript): 语言核心部分
- **文档对象模型** ( Document Object Model , DOM ): 网页文档操作标准
- **浏览器对象模型** ( BOM ): 客户端和浏览器窗口操作基础

Web 浏览器知识 ECMAScript 实现的宿主环境之一。宿主环境不仅提供基本的 ECMAScript 实现，同时也会提供各种扩展功能

文档对象模型是 HTML 的应用程序编程接口 ( API )，DOM 把整个文档映射为一个树形节点结构，以方便 JavaScript 脚本快速访问和操作

浏览器对象模型 ( BOM ) 可以对浏览器窗口进行访问和操作，如移动窗口，访问历史记录，动态导航等。与 DOM 不同，BOM 只是 JavaScript 的一个部分，并没有形成规范性标准，但是所有浏览器都默认支持

# 为什么学习 JavaScript

JavaScript web 开发人员必须学习的 3 门语言中的一门：

1. HTML 定义了网页的内容
2. CSS 描述了网页的布局
3. JavaScript 网页的行为

# 编写第一个程序

JavaScript 程序不能够独立执行，只能在宿主环境中执行，一般情况下可以把 JavaScript 代码放在网页中，借助浏览器环境来运行

在 HTML 页面中嵌入 JavaScript 脚本需要使用 `<script>` 标签，用户可以在 `<script>` 标签中直接编写 JavaScript 代码，具体步骤如下：

- 新建 HTML 文档
- 在 `<head>` 标签内插入一个 `<script>` 标签
- 为 `<script>` 标签设置 `type="text/javascript"` 属性

> 现代浏览器默认 `<script>` 标签的脚本类型为 JavaScript，因此也可以省略 type 属性

- 在 `<script>` 标签输入 JavaScript 代码: `document.write("<h1>Hi,JavaScript!</h1>")；`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>第一个JavaScript程序</title>
    <script type="text/javascript">
        document.write("<h1>Hi,JavaScript!</h1>");
    </script>
</head>
<body></body>
</html>
```

在 JavaScript 脚本中，document 表示网页文档对象，document.write() 表示调用 Document 对象的 write() 方法，在当前网页源代码中写入 HTML 字符串 `<h1>Hi,JavaScript!</h1>`

保存网页文档，在浏览器中预览，显示效果如图所示：

![img][img@1]

# 引入外部 js 文件

JavaScript 程序不仅可以直接放在 HTML 文档中，也可以放在 JavaScript 文件中

JavaScript 文件是文本文件，扩展名为 `.js`

- (1) 新建文本文件，保存为 test.js
- (2) 打开 js 文件，在其中编写如下内容

```javascript
alert("hello javascript");
```
在上面的代码中，alert() 是 Window 对象的方法，调用该方法讲坛是一个提示对话框，显示参数字符串 hello javascript

- (3) 打开 HTML 文档，在 `<head>` 标签内插入一个 `<script>` 标签。定义 src 属性，设置属性值指向外部 JavaScript 文件路径

```javascript
<script src="./test.js"></script>
```

- (4) 在浏览器中预览，显示效果如图所示

![img][img@2]


[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/JavaScript/05-14_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/JavaScript/05-14_02.png



