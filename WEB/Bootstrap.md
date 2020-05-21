<!-- TOC -->

- [Bootstrap 简介](#bootstrap-%e7%ae%80%e4%bb%8b)
- [栅格系统](#%e6%a0%85%e6%a0%bc%e7%b3%bb%e7%bb%9f)
  - [栅格参数](#%e6%a0%85%e6%a0%bc%e5%8f%82%e6%95%b0)
  - [基本的网格结构](#%e5%9f%ba%e6%9c%ac%e7%9a%84%e7%bd%91%e6%a0%bc%e7%bb%93%e6%9e%84)
- [导航栏](#%e5%af%bc%e8%88%aa%e6%a0%8f)
- [标签页](#%e6%a0%87%e7%ad%be%e9%a1%b5)
- [面板](#%e9%9d%a2%e6%9d%bf)
- [表单](#%e8%a1%a8%e5%8d%95)
- [输入框组](#%e8%be%93%e5%85%a5%e6%a1%86%e7%bb%84)
- [表格](#%e8%a1%a8%e6%a0%bc)
- [列表组](#%e5%88%97%e8%a1%a8%e7%bb%84)
- [分页](#%e5%88%86%e9%a1%b5)
- [缩略图](#%e7%bc%a9%e7%95%a5%e5%9b%be)
- [模态框](#%e6%a8%a1%e6%80%81%e6%a1%86)
- [轮播图](#%e8%bd%ae%e6%92%ad%e5%9b%be)
- [图标](#%e5%9b%be%e6%a0%87)
- [参考文档](#%e5%8f%82%e8%80%83%e6%96%87%e6%a1%a3)

<!-- /TOC -->

# Bootstrap 简介

Bootstrap 是最受欢迎的响应式、移动设备优先的门户和应用前端框架，能够做到快速开发 Web 应用程序和网站

**为什么使用 Bootstrap**

- 移动设备优先: 自 Bootstrap 3 起，框架包含了贯穿于整个库的移动设备优先的样式
- 浏览器支持: 所有的主流浏览器都支持 Bootstrap
- 响应式设计: Bootstrap 的响应式 CSS 能够自适应 台式机，平板电脑和手机
- 为开发人员创建接口提供了一个简洁统一的解决方案
- 包含功能强大的内置组件，易于定制
- 提供了基于 Web 的定制
- 容易上手
- 开源

**Bootstrap 包的内容**

- **基本结构**: Bootstrap 提供了一个带有网格系统、链接样式、背景的基本结构
- **CSS**: Bootstrap 自带以下特性：全局的 CSS 设置，定义基本的 HTML 元素样式，可扩展的 class，以及一个先进的网格系统
- **组件**: Bootstrap 包含了十几个可重用的组件，用于创建图像，下拉菜单，导航，警告框，弹出框等
- **JavaScript插件**: Bootstrap包含了十几个自定义的 jQuery 插件
- **定制**: 可以定制 Bootstrap 的组件，LESS 变量和jQuery 插件来得到你自己的版本

**Bootstrap 环境安装**

**1. 下载文件**

  可以从 [https://getbootstrap.net/](https://getbootstrap.net/) 下载指定的版本的 Bootstrap，然后在 HTML 文件中引入使用

**2. CDN**

  ```html
  <!-- Bootstrap 3.3.7 css 文件 -->
  <link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

  <!-- jQuery 1.9.1，务必在bootstrap.min.js 之前引入 -->
  <script src="https://cdn.staticfile.org/jquery/1.9.1/jquery.min.js"></script>

  <!-- Bootstrap 3.3.7 js 文件 -->
  <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
  ```

# 栅格系统

Bootstrap 提供了一套响应式，移动设备优先的流式栅格系统，随着屏幕或视口( viewport )尺寸的增加，系统会自动分为最多 12 列，栅格系统用于通过一系列的行(row) 与 列(column) 的组合来创建页面布局，你的内容就可以放入这些创建好的布局中。下面就介绍以下 Bootstrap 栅格系统的工作原理：

- 行必须放置在 .container class 内，以便获得适当的对齐和内边框
- 使用行来创建列的水平组
- 内容应该放置在列内，且唯有列可以是行的直接子元素
- 预定义的网格类，比如 .row 和 .col-xs-4，可用于快速创建网格布局
- 列通过内边距（padding）来创建列内容之间的间隙。该内边距是通过 .rows 上的外边距（margin）取负，表示第一列和最后一列的行偏移
- 网格系统是通过指定您想要横跨的十二个可用的列来创建的。例如，要创建三个相等的列，则使用三个 .col-xs-4
- 如果一行中包含的列大于 12 ，多余的列所在的元素将被作为一个整体另起一行排列

## 栅格参数

|              | 超小设备手机(<768px)          | 小型设备平板电脑(>=768px)    | 中型设备台式电脑(>=992px)    | 大型设备(>=1200px)           |
| :----------- | :---------------------------- | :--------------------------- | :--------------------------- | :--------------------------- |
| 网格行为     | 一直是水平的                  | 以折叠开始，断点以上是水平的 | 以折叠开始，断点以上是水平的 | 以折叠开始，断点以上是水平的 |
| 最大容器宽度 | None (auto)                   | 750px                        | 970px                        | 1170px                       |
| class前缀    | `.col-xs-`                    | `.col-sm-`                   | `.col-md-`                   | `.col-lg-`                   |
| 列数量       | 12                            | 12                           | 12                           | 12                           |
| 最大列宽     | Auto                          | 60px                         | 78px                         | 95px                         |
| 间隙宽度     | 30px（一个列的每边分别 15px） | 30px（一个列的每边分别 15px  | 30px（一个列的每边分别 15px  | 30px（一个列的每边分别 15px  |
| 可嵌套       | √                             | √                            | √                            | √                            |
| 偏移量       | √                             | √                            | √                            | √                            |
| 列排序       | √                             | √                            | √                            | √                            |

## 基本的网格结构


```html
<div class="container-fluid">
    <div class="row">
        <div class="col-md-5 col-xs-5">
            <h3>这里是第一列，没错就是第一列了，是的呢，就是第一列啦，就是这里，确实是第一列</h3>
        </div>
        <div class="col-md-3 col-xs-3">
            <h3>这里是第一列，没错就是第一列了，是的呢，就是第一列啦，就是这里，确实是第一列</h3>
        </div>
        <div class="col-md-4 col-xs-4">
            <h3>这里是第一列，没错就是第一列了，是的呢，就是第一列啦，就是这里，确实是第一列</h3>
        </div>
    </div>

    <div class="row">
        <div class="col-xs-5">
            <h3>第二列啊</h3>
        </div>
        <div class="col-xs-3">
            <h3>第二列啊</h3>
        </div>
        <div class="col-xs-4">
            <h3>第二列啊</h3>
        </div>
    </div>
</div>
```

![img][img@1]

1. 栅格系统需要放在一个容器中
    `container`  固定宽度并支持响应式布局  
    `container-fluid`  类似于 100% 宽度，占据整个视口 (viewport) 的容器  
<br>
2. 栅格系统使用 `.row` 划分一行
<br>
3. 所有列 `col-md-*` 必须放在 `.row` 内
    一行分为 12份，每一列可以指定占据的份数  
    如果小于等于 12 占一行，如果大于 12 换行  

![img][img@2]


# 导航栏

导航栏在网站中作为导航页头的基础组件，包括了站点名称和基本的导航定义样式

![img][img@3]

创建一个默认的导航栏的步骤如下：

- 向 `<nav>` 标签添加 class `.navbar`, `.navbar-default`
- 向上面的元素添加 `role="navigation"`，有助于增加可访问性
- 向 `<div>` 元素添加一个标题 class `.navbar-header`，内部包含了带有 class `.navbar-brand` 的 `<a>` 元素，这样会让文本看起来更大一号
- 为了向导航栏添加链接，只需要简单地添加带有 class `.nav`,`.navbar-nav` 的无序列表即可
- 将导航栏移动到右边使用 `navbar-right` 或 `pull-right` 即可

```html
<nav class="navbar navbar-default" role="navigation">
    <!-- 导航栏 -->
    <div class="container">
        <!-- 导航栏左边 -->
        <div class="navbar-header">
            <a href="#" class="navbar-brand">宗宗宗在路上</a>
        </div>
        <!-- 导航栏右边 -->
        <div>
            <ul class="nav navbar-nav navbar-right">
                <li class="active">
                    <a href="">登录</a>
                </li>
                <li>
                    <a href="">注册</a>
                </li>
                <li>
                    <a href="">登出</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

more : [https://www.runoob.com/bootstrap/bootstrap-navbar.html](https://www.runoob.com/bootstrap/bootstrap-navbar.html)

# 标签页

**创建标签页**

![img][img@4]

- 以一个带有 class `.nav` 的无需列表开始
- 添加 class `.nav-tabs`

```html
<div class="container">
    <ul class="nav nav-tabs">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">Python</a></li>
        <li><a href="#">Java</a></li>
        <li><a href="#">PHP</a></li>
        <li><a href="#">JavaScript</a></li> 
    </ul>
</div>
```

**设置标签页对应的内容**

```html
<div class="container">
    <!-- 选项卡 -->
    <ul class="nav nav-tabs">
        <li class="active"><a href="#home" data-toggle="tab">Home</a></li>
        <li><a href="#menu1" data-toggle="tab">Python</a></li>
        <li><a href="#menu2" data-toggle="tab">Java</a></li>
        <li><a href="#menu3" data-toggle="tab">PHP</a></li>
    </ul>

    <!-- 对应的面板 -->
    <div class="tab-content">
        <div id="home" class="tab-pane fade in active">
            <h3>首页</h3>
            <p>Day Day Study Good Good up!</p>
        </div>
        <div id="menu1" class="tab-pane fade">
            <h3>menu1</h3>
            <p>这里是菜单1</p>
        </div>
        <div id="menu2" class="tab-pane fade">
            <h3>menu2</h3>
            <p>这里是菜单2</p>
        </div>
        <div id="menu3" class="tab-pane fade">
            <h3>menu3</h3>
            <p>这里是菜单3</p>
        </div>
    </div>
</div>
```

more: [https://www.runoob.com/bootstrap/bootstrap-navigation-elements.html](https://www.runoob.com/bootstrap/bootstrap-navigation-elements.html)

# 面板

面板 (Pabels) 用于把 DOM 组件插入到一个盒子中

**基本的面板**

- 只需要向 `<div>` 元素添加 class `.panel` 和 class `.panel-default`

**面板标题**

- 使用 `.panel-heading` class 可以简单地向面板添加标题容器
- 使用 `.panel-title` class 的 `<h1> - <h6>` 来添加预定义样式的标题

**面板脚注**

- 在面板中添加脚注，只需要把按钮或文本放在带有 class `.panel-footer` 的 div 中即可

**带语境的面板**

- 使用语境状态类 `panel-primary`，`panel-success`，`panel-info`，`panel-warning`，`panel-danger` 来设置带语境色彩的面板

![img][img@5]

```html
<div class="panel panel-success">
    <div class="panel-heading">
        <h3 class="panel-title">success 面板</h3>
    </div>
    <div class="panel-body">
        <h1>面板内容</h1>
    </div>
    <div class="panel-footer">
        面板脚注
    </div>
</div>
```

more: [https://www.runoob.com/bootstrap/bootstrap-panels.html](https://www.runoob.com/bootstrap/bootstrap-panels.html)

# 表单

Bootstrap 通过一些简单的 HTML 标签和扩展的类即可创建出不同样式的表单

Bootstrap 提供了以下类型的表单布局

**(1) 基本 (垂直) 表单**

- 向父 `<form>` 元素添加 `role="form"`
- 把标签和控件放在一个带有 class `.form-group` 的 `<div>` 中
- 向所有的文本元素 `<input>`，`<textarea>` 和 `<select>` 添加 class `form-control`

**(2) 内联表单**

- 向父 `<form>` 元素添加 class `form-inline`

**(3) 水平表单**

- 向父 `<form>` 元素添加 class `form-horizontal`

![img][img@6]

```html
<form action="#" class="form-horizontal" role="form">
    <div class="form-group row">
        <label for="name" class="control-label col-md-2">名称:</label>
        <div class="col-md-10">
            <input type="text" class="form-control" id="name" placeholder="请输入名称">
        </div>
    </div>

    <div class="form-group">
        <label for="file_upload" class="control-label col-md-2">文件上传:</label>
        <div class="col-md-10">
            <input type="file" class="form-control" id="file_upload">
        </div>
    </div>
    <div class="form-group">
        <div class="col-md-offset-2 col-md-10">
            <button class="btn btn-info">提交</button>
        </div>
    </div>
</form>
```

more: [https://www.runoob.com/bootstrap/bootstrap-forms.html](https://www.runoob.com/bootstrap/bootstrap-forms.html)

# 输入框组

输入框组扩展自 表单，使用输入框组，可以很容易地向基于文本的输入框添加作为前缀和后缀的文本或按钮

步骤如下：

- 把前缀或后缀元素放在一个带有 class `.input-group` 的 `<div>` 中
- 在相同的 div 内，在 class 为 `.input-group-addon` 的 span 内放置额外的文本
- 在相同的 div 内，在 class 为 `.input-group-btn` 的 span 内放置额外的按钮
- 把该 span 放置在 input 元素 前面或者后面

![img][img@7]

```html
<div class="input-group">
    <input type="text" class="form-control">
    <span class="input-group-btn">
        <button class="btn btn-primary">搜&nbsp;&nbsp;&nbsp;索</button>
    </span>
</div>
<br>
<div class="input-group">
    <span class="input-group-addon">￥</span>
    <input type="text" class="form-control">
    <span class="input-group-addon">.00</span>
</div>
<br>
<div class="input-group">
    <input type="text" class="form-control">
    <span class="input-group-addon">@</span>
    <input type="text" class="form-control">
</div>
```

more: [https://www.runoob.com/bootstrap/bootstrap-input-groups.html](https://www.runoob.com/bootstrap/bootstrap-input-groups.html)

# 表格

Bootstrap 提供了一个清晰的创建表格的布局，下表列出了 Bootstrap 支持的一些表格元素

|标签|描述|
|:---|:---|
|`<table>`|	为表格添加基础样式|
|`<thead>`|	表格标题行的容器元素 `<tr>`，用来标识表格列|
|`<tbody>`|	表格主体中的表格行的容器元素 `<tr>`|
|`<tr>`|	一组出现在单行上的表格单元格的容器元 `<td>` 或 `<th>`|
|`<td>`|	默认的表格单元格|
|`<th>`|	特殊的表格单元格，用来标识列或行（取决于范围和位置）,必须在 `thead` 内使用|
|`<caption>`|	关于表格存储内容的描述或总结|

**表格类**
下表样式可用于表格中

|类|描述|
|:---|:---|
|.table|	为任意 `table` 添加基本样式 (只有横向分隔线)|
|.table-striped|	在 `tbody` 内添加斑马线形式的条纹|
|.table-bordered|	为所有表格的单元格添加边框|
|.table-hover|	在 `tbody` 内的任一行启用鼠标悬停状态|
|.table-condensed|	让表格更加紧凑|

**tr, th 和 td 类**
下表的类可用于表格的行或者单元格

|类|描述|
|:---|:---|
|.active|	将悬停的颜色应用在行或者单元格上|
|.success|	表示成功的操作|
|.info|	表示信息变化的操作|
|.warning|	表示一个警告的操作|
|.danger|	表示一个危险的操作|

![img][img@8]

```html
<table class="table table-bordered">
    <caption>改变表格行或指定单元格背景颜色</caption>
    <thead>
        <tr>
            <th>序号</th>
            <th>名字</th>
        </tr>
    </thead>
    <tbody>
        <tr class="info">
            <th>1</th>
            <th>Python</th>
        </tr>
        <tr>
            <th>2</th>
            <th class="danger">JavaScript</th>
        </tr>
        <tr class="success">
            <th>3</th>
            <th>PHP</th>
        </tr>
    </tbody>
</table>
```

more: [https://www.runoob.com/bootstrap/bootstrap-tables.html](https://www.runoob.com/bootstrap/bootstrap-tables.html)

# 列表组

列表组件用于以列表形式呈现复杂的和自定义的内容，创建一个基本的列表组步骤如下：

- 向元素 ul 添加 class `.list-group`
- 向元素 li 添加 class `.list-group-item`

![img][img@9]

```html
<ul class="list-group">
    <li class="list-group-item active">常用语言</li>
    <li class="list-group-item">Python</li>
    <li class="list-group-item">JavaScript</li>
    <li class="list-group-item">HTML</li>
    <li class="list-group-item">CSS</li>
</ul>
```

more: [https://www.runoob.com/bootstrap/bootstrap-list-group.html](https://www.runoob.com/bootstrap/bootstrap-list-group.html)

# 分页

分页是一种无序列表，Bootstrap 像处理其它界面元素一样处理分页

下表列出了 Bootstrap 提供的处理分页的 class

|class|描述|
|:---|:---|
|.pagination|添加该 class 在页面上显示分页|
|.disabled|定义不可点击链接|
|.active|指示当前选中页面|

![img][img@10]

```html
<ul class="pagination">
    <li class="disabled"><a href="">上一页</a></li>
    <li class="active"><a href="">1</a></li>
    <li><a href="">2</a></li>
    <li><a href="">3</a></li>
    <li><a href="">4</a></li>
    <li><a href="">5</a></li>
    <li><a href="">下一页</a></li>
</ul>
```

# 缩略图

使用 Bootstrap 创建缩略图的步骤如下：

- 创建一个含有 class `.thumbnail` 的 div 标签
- 在 div 中添加图片
- 添加其它内容

![img][img@11]

```html
<div class="thumbnail">
    <a href=""><img src="./1.jpg"></a>
    <div class="caption">
        <h3 style="text-align: center;">emmm...</h3>
    </div>
</div>
```

more: [https://www.runoob.com/bootstrap/bootstrap-thumbnails.html](https://www.runoob.com/bootstrap/bootstrap-thumbnails.html)

# 模态框

模态框是覆盖在父窗体上的子窗体。可以在不离开父窗体的情况下有一些互动，子窗体可以提供信息，交互等

你可以使用以下方法，显示模态框：

- **通过 data 属性**：在控制器元素（比如按钮或者链接）上设置属性 `data-toggle="modal"`，同时设置 `data-target="#id"` 来指定要切换的特定的模态框
- **通过 JavaScript**: `$('#id').modal(options)`

![img][img@12]

```html
<button class="btn btn-success" data-toggle="modal" data-target="#myModal">激活</button>

<!-- 模态框：当触发事件后，激活一个对话框 -->
<div class="modal fade" id="myModal">
    <!-- 模态框 -->
    <div class="modal-dialog">
        <!-- 模态框内容 -->
        <div class="modal-content">
            <!-- 模块框头部 -->
            <div class="modal-header">
                <button class="close" data-dismiss="modal">&times;</button>
                <h4 class="model-title">删除用户？</h4>
            </div>
            <!-- 模态框body -->
            <div class="modal-body">
                是否确认删除？
            </div>
            <!-- 模态框页脚 -->
            <div class="modal-footer">
                <button class="btn btn-danger" data-dismiss="modal">是</button>
                <button class="btn btn-info" data-dismiss="modal">否</button>
            </div>
        </div>
    </div>
</div>
```

more: [https://www.runoob.com/bootstrap/bootstrap-modal-plugin.html](https://www.runoob.com/bootstrap/bootstrap-modal-plugin.html)

# 轮播图

Bootstrap轮播插件是一种灵活的响应式的向站点添加滑块的方式。除此之外，内容也是足够灵活的，可以是图像，内嵌框架，视频或者其它你想要放置的任何内容

![img][img@13]

```html
<!-- data-ride="carousel" 代表页面加载的时候  自动轮播 默认时间为5s-->
<div id="mycarousel" class="carousel slide" data-ride="carousel">
    <!--小点部分
        carousel-indicators   小点
        data-target   -> 目标
        data-slide-to  控制那一张图片，通过索引控制，从0开始
    -->
    <ol class="carousel-indicators">
        <li data-target="#mycarousel" data-slide-to="0"></li>
        <li data-target="#mycarousel" data-slide-to="1"></li>
        <li data-target="#mycarousel" data-slide-to="2"></li>
        <li data-target="#mycarousel" data-slide-to="3"></li>
    </ol>
    <!-- 图片部分 carousel-inner -->
    <div class="carousel-inner">
        <!-- item 代表图片部分的每一张图片  activa 当前显示的图片-->
        <div class="item active">
            <img src="./img/1.jpg" alt="">
        </div>
        <div class="item">
            <img src="./img/2.jpg" alt="">
        </div>
        <div class="item">
            <img src="./img/3.jpg" alt="">
        </div>
    </div>
    <!--控制部分-->
    <!--  上一张
        herf 值为 当前轮播图的id
        data-slide -> 控制获取上一张 下一张图片，接受两个值： prev（上一张）  next（下一张）
    -->
    <a class="left carousel-control" href="#mycarousel" role="button" data-slide="prev">
        <!-- 左箭头图标 -->
        <span class="glyphicon glyphicon-chevron-left"></span>
    </a>
    <!--下一张-->
    <a class="right carousel-control" href="#mycarousel" role="button" data-slide="next">
        <!-- 右箭头图标 -->
        <span class="glyphicon glyphicon-chevron-right"></span>
    </a>
</div>
```

more: [https://www.runoob.com/bootstrap/bootstrap-carousel-plugin.html](https://www.runoob.com/bootstrap/bootstrap-carousel-plugin.html)

# 图标

[点击查看图标列表](https://www.runoob.com/try/demo_source/bootstrap3-glyph-icons.htm)

```html
<span class="glyphicon glyphicon-search"></span>

<button type="button" class="btn btn-default">
    <span class="glyphicon glyphicon-user"></span> User
</button>
```

# 参考文档

[https://www.runoob.com/bootstrap/bootstrap-tutorial.html](https://www.runoob.com/bootstrap/bootstrap-tutorial.html)
[http://w3c.3306.biz/bootstrap_v3/](http://w3c.3306.biz/bootstrap_v3/)
[https://doc.yonyoucloud.com/doc/wiki/project/bootstrap/index.html](https://doc.yonyoucloud.com/doc/wiki/project/bootstrap/index.html)



[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-19_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-19_02.png
[img@3]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_03.png
[img@4]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_04.png
[img@5]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_05.png
[img@6]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_06.png
[img@7]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_07.png
[img@8]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_08.png
[img@9]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_09.png
[img@10]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_10.png
[img@11]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_11.png
[img@12]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_12.png
[img@13]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/html/html/05-20_13.png