<!-- TOC -->

- [Vue](#vue)
- [基本使用](#基本使用)
- [插值操作](#插值操作)
- [指令](#指令)
- [ajax 请求](#ajax-请求)
- [more](#more)

<!-- /TOC -->

# Vue

前后端分离，将绑定数据，页面的工作交给了前端，但是前端使用 js 或者 JQuery 完成数据绑定渲染相当繁琐，于是出现了 Vue 前端框架

Vue 是一种构建用户界面的 js 框架，目的就是完成数据绑定

# 基本使用

```html
<div id="connect">
    <h1>姓名: {{ name }}</h1>
    <h1>年龄: {{ age }}</h1>
    <h1>性别: {{ gender }}</h1>
    <h1>爱好: {{ sing() }}</h1>
</div>

<script>
    var vm = new Vue({
        el: '#connect',
        data: {
            name: "tom",
            age: "18",
            gender: "男"
        },
        methods: {
            sing: function(){
                return "I like sing!"
            }
        }
    })
</script>
```

可以看到 Vue 构造器中有一个 `el` 参数，它是 DOM元素中的 ID，这意味着接下来的改动全部在指定的 div 内

`data` : 用于定义属性
`methods` : 用于定义函数，可以通过 return 返回函数值
`{{ }}` : 用于输出对象属性 和 函数的返回值

当一个 Vue 实例被创建时，它向 Vue 响应式系统中加入了其 data 对象中能找到的所有属性。当这些属性的值发生改变时，HTML 视图也会产生相应的变化

# 插值操作

**(1) 文本**

数据绑定最常见的形式就是使用 `{{ }}` 的文本插值

```html
<div>
    {{ name }}
</div>
```

**(2) HTML**

使用 `v-html` 指令用于输出 HTML 代码

```html
<div id="app" v-html="message"></div>

<script>
new Vue({
  el: '#app',
  data: {
    message: '<h1>瑞克与莫迪</h1>'
  }
})
</script>
```

等效于

```html
<div id="app">
    <h1>瑞克与莫迪</h1>
</div>
```

**(3) 属性**

HTML 属性的值应使用 `v-bind` 指令

```html
<a id="app" v-bind:href="href">baidu</a>

<script>
new Vue({
  el: '#app',
  data: {
    href: 'https://www.baidu.com'
  }
})
</script>
```

# 指令

**(1) v-if**

判断绑定，元素只有当判断为 true 时显示，否则隐藏

```html
<div id="box" v-if="flag">
    this is a test div
</div>

<script>
    new Vue({
        el: "#box",
        data: {
            flag: true
        }
    })
</script>
```

**(2) v-for**

循环绑定

```html
<div id="box">
    <li v-for="one in hobby">
        {{ one }}
    </li>
</div>


<script>
    new Vue({
        el: "#box",
        data: {
            hobby: ["唱歌","扣腚","玩手机"]
        }
    })
</script>
```

**(3) v-on**

事件绑定

```html
<div id="box">
    <button v-on:click="say()">点我</button>
</div>


<script>
    new Vue({
        el: "#box",
        methods: {
            say: function(){
                alert("点我干嘛！");
            }
        }
    })
</script>
```

# ajax 请求

Vue 要实现异步加载需要使用到 `vue-resource` 库

导入
`<script src="https://cdn.staticfile.org/vue-resource/1.5.1/vue-resource.min.js"></script>`

基本使用

```html
<script>
    new Vue({
        el: "#box",
        data: {
            name: "",
            age: ""
        },
        // 初始化函数
        created:function(){
            // 发送请求 获取数据 数据绑定
            url = "/teacher/1/";
            // 发送 get 请求，then 为请求之后执行的代码
            this.$http.get(url).then(
                // 请求成功之后执行，类似 ajax 中的 success
                function(data){
                    // 数据绑定
                    this.name = data.body.username;
                    this.age = data.body.age;
                },
                // 请求失败之后执行，类似 ajax 中的 error
                function(error){
                    console.log(error);
                }
            )
        }
    })
</script>
```

> 由于 Django 模板语法 与 Vue 插值语法 类似，因此需要使用 
> {% verbatim %} ... {% endverbatim %}
> 将 Vue 代码包围起来，否则 Vue 代码可能不生效

# more

- [官网](https://cn.vuejs.org/)
- [官方文档](https://cn.vuejs.org/v2/guide/)
- [菜鸟教程](https://www.runoob.com/vue2/vue-tutorial.html)



