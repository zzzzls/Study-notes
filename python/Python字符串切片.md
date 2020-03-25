# 1. 索引
Python的字符串是有序集合，我们可以通过索引来提取想要获取的字符，可以把 Python的字符串也做为字符串的列表就更好理解，

字符串的索引编号有两种表示方式
1. 顺序索引，从起始元素到末尾元素，第一个起始元素索引为0，末尾元素索引为-1，每个元素索引编号+1
2. 逆序索引，从末尾元素到起始元素，末尾元素索引为 -1，每个元素索引编号-1，以此类推

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200320195108707.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MDc4OTky,size_16,color_FFFFFF,t_70#pic_center)

```python
the_str = "Python"

取第一个元素
print(the_str[0])
print(the_str[-6])
>>> "Y"

取最后一个元素
print(the_str[5])
print(the_str[-1])
>>> "n"
```
# 2. 切片
切片操作（slice）可以从一个字符串中获取子字符串（字符串的一部分）。使用一对方括号、起始偏移量start、终止偏移量end 以及可选的步长step 来定义一个分片。

格式： `[start:stop:step]`
> 切片操作 含左不含右   

| 格式 |说明  |
|:-|:-|
[:]       |  取全部字符串|
[start:]  |  从start提取到结尾|
[:end]    |  从开始到end|
[start:end] |从 start 提取到 end |
[start:stop:step]| 从 start 提取到 end，每 step 个字符提取 1 个

```python
the_str = "You need python"

# 提取区间字符串
print(the_str[4:8])
>>>need

# start为负数，则从尾部某一位置，开始向后截取
print(the_str[-6:])
>>>python

# 若索引错误,则结果为空
print(the_str[5:2])
>>>

# 打码指定区间
print(the_str[:3] + "*"*len(the_str[3:-4]) + the_str[-4:])
>>>You********thon
```
# 3. 步长
执行切片操作时，你显式或隐式地指定 start 和 end，但通常省略另一个参数，即步长。在普通切片中，步长默认值为1。


|步长|  描述|
|--|:-|
| 1 | 从左向右提取元素     |
|-1|从右向左提取元素 |
|n|每隔 n-1个元素提取一个元素|


