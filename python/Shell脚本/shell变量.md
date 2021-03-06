<!-- TOC -->

- [定义变量](#%e5%ae%9a%e4%b9%89%e5%8f%98%e9%87%8f)
- [使用变量](#%e4%bd%bf%e7%94%a8%e5%8f%98%e9%87%8f)
- [单引号和双引号区别](#%e5%8d%95%e5%bc%95%e5%8f%b7%e5%92%8c%e5%8f%8c%e5%bc%95%e5%8f%b7%e5%8c%ba%e5%88%ab)
- [将命令的结果赋值给变量](#%e5%b0%86%e5%91%bd%e4%bb%a4%e7%9a%84%e7%bb%93%e6%9e%9c%e8%b5%8b%e5%80%bc%e7%bb%99%e5%8f%98%e9%87%8f)
- [只读变量](#%e5%8f%aa%e8%af%bb%e5%8f%98%e9%87%8f)
- [删除变量](#%e5%88%a0%e9%99%a4%e5%8f%98%e9%87%8f)
- [标准输入 read](#%e6%a0%87%e5%87%86%e8%be%93%e5%85%a5-read)
- [显式声明变量类型](#%e6%98%be%e5%bc%8f%e5%a3%b0%e6%98%8e%e5%8f%98%e9%87%8f%e7%b1%bb%e5%9e%8b)

<!-- /TOC -->

变量是任何贬称该语言都必不可少的组成部分，变量用来存放各种数据。Shell中定义变量时通常不需要指明类型，直接复制即可！

在 Bash shell 中，默认情况下不会区分变量类型，每一个变量的值都是字符串，当然，如果有必要，你也可以使用 Shell declare 关键字显式定义变量的类型

# 定义变量

Shell支持以下三种定义变量的方式：

```bash
var=value
var='value'
var="value"
```

变量的设置规则：

- 变量与变量内容以一个等号 = 来连接
- 等号的两边不能有空格
- 变量名由数字，字母，下划线组成，开头字符不能是数字
- 变量内容若有空格，可以使用单/双引号将变量内容包含起来

# 使用变量

使用一个定义过的变量，只要在变量名前面加美元符号 $ 即可

```bash
author="test"
echo $author
echo ${author}
```

变量名外边的花括号 {} 是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界，比如下边这种情况：

```bash
lang="python"
echo "${lang}_language is powerful!"
```

如果不给 lang 变量加花括号，写成 `echo "$lang_language is powerful!"`，解释器就会把 $lang_language 当成一个变量，代码执行结果就不是我们期望的样子了！

# 单引号和双引号区别

定义变量时，变量的值可以由单引号包围，也可以由双引号包围，它们由什么区别呢？让我们来看下边的例子：

```bash
url='https://www.baidu.com'
website1='url is ${url}'
website2="url is ${url}"
echo ${website1}
echo ${website2}

=================
# 执行结果
url is ${url}
url is https://www.baidu.com
```

以单引号包围变量的值时，单引号里边时什么就输出什么，即使内容中由变量和命令也会把它们原样输出，这种方式比较适合定义显示纯字符串的情况

以双引号包围变量的值时，输出时会先解析里边的变量和命令，这种方式适合字符串中附带由变量和命令并且想将其解析后在输出的变量定义。

# 将命令的结果赋值给变量

Shell也支持将命令的执行结果赋值给变量，常见的有以下两种方式：

```bash
var1=`ls`
var1=$(ls)
```

第一种方式把命令用反引号`\`\``包围起来
第二种方式把命令用`$()`包围起来，推荐使用这种方式

# 只读变量

使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变

```bash
url="https://www.baidu.com"
readonly url
```

# 删除变量

使用 unset 可以删除变量，unset 无法删除只读变量

```bash
unset name
```

# 标准输入 read

读取来自键盘输入的内容，存储到变量中，使用 read 就对了，先来看一下 read 的相关语法吧！

```bash
read [-pt] variable

# 选项及参数：
-p：后面可以接提示字符
-t：后面可以接等待的秒数，指定时间内没有输入，命令自动略过
-s: 静默模式，不会在屏幕显示输入的内容
variable：接收用户输入内容的变量
```

# 显式声明变量类型

declare 是 Shell 内建命令，用开设置变量的属性，用法如下：

`declare [+/-][aAirxp][变量名=变量值]`

其中，`-` 表示设置属性，`+` 表示取消属性，`aAirx` 都是具体的选项，含义如下表所示：

|选项|描述|
|:---:|:---|
|a|声明变量为数组（array）类型|
|A|声明变量为关联数据（支持索引下标为字符串）|
|i|声明变量为整数（integer）类型|
|r|声明变量为 readonly 类型|
|x|声明变量为环境变量，类似 export|
|p|显示指定变量的属性和值|

```bash
# 将多个变量声明为整数
declare -i a b c
a=10
b=20
c=$a+$v
echo $c
```