# 字符串是什么
根据维基百科定义：字符串是由零个或多个字符组成的有限序列。而在 Python3中，它有着更明确的意思：**字符串是由 Unicode码点组成的不可变序列**（Strings are immutable sequences of Unicode code points.）

# 字符串字面量
python 中的字符串字面量由单引号或双引号括起。`'hello'
`等同与`"hello"`，可以使用 `print()` 函数打印字符串字面量。
```python
print('hello')
print("hello")
```
# 向变量赋值
通过使用变量名称后跟等号和字符串，可以吧字符串赋值给变量。
```python
a = 'hello'
print(a)
```

# 多行字符串
可以使用三个引号将多行字符串赋值给变量
```python
a = '''Python is a widely used general-purpose, 
high level programming language. '''
print(a)
```
> 在结果中，换行符插入与代码中相同的位置。

# 字符串转义字符
|转义字符|描述  |
|--|--|
| \ (在行尾时) |续行符  |
|\\\\|反斜杠符号|
|\\'|单引号|
|\\"|双引号|
|\\n|换行符|
|\\r|回车|
|\\t|制表符|

# 字符串连接
### 1. `+`
```python
a = "Hello"
b = "world"
print(a+b)
```
### 2. `format()`
```python
a = "Hello"
b = "world"
print("{0} and {1}".format(a,b))
```
### 3. `f-string`
```python
a = "Hello"
b = "world"
print(f"{a} and {b}")
```

在拼接短的字面值时，由于 CPython中的 `常数折叠`（constant folding）功能，这些字面值会被转换成更短的形式，
例如 "a"+"b"+"c" 被转换成 "abc"，"hello"+"world" 也会被转换成 "hello world"。
这种转换是在编译期完成的，而到了运行期时就不会再发生任何拼接操作，因此会加快整体计算的速度。

常数折叠优化有一个限度，它要求拼接结果的长度不超过20。
所以，当拼接的最终字符串长度不超过20时，+ 号操作符的方式，会比其他方式拼接快得多。
长度超过20的情况，建议采用 f-string 或者 format 方式。

# 字符串重复
星号 `*` 表示重复当前字符串，紧跟的数字为重复的次数
```python
a = "Hello"
print(a * 3)
>>>HelloHelloHello
```

# 特殊字符串
### 1. 字符串前加 `r`
`r` 前缀表示：后面的字符串是普通字符串，字符串中的转义字符就会被当成普通的字符串，而不会起作用。
```python
a = r"hello world\n\n" # 此处 \n\n 就以字符串形式展示
```

### 2. 字符串前加`b`
`b`前缀表示：后面字符串是bytes 类型。
```python
a = b"hello world"
```

### 3. 字符串前加`u`
`u`前缀表示：后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
```python
a = u"你好世界"
```

# in & not in
```python
x in s       若 s 包含 x，返回 True，否则返回 False
x not in s   若 s 包含 x，返回 False，否则返回 True
```

# len() 方法
`len(str) `
返回字符串的长度

```python
the_str = "hello world"
print(len(the_str ))
>>>11
```

