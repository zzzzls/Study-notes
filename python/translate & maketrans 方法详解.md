# maketrans()
用于创建字符映射的转换表
> 注：Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。

### 语法：
`str.maketrans(dict)`  
`str.maketrans(intab,outtab[,delchars])`

### 参数：
只有一个参数时，必须是 Unicode序数（整数）或字符（长度为 1 的 String，会被转换为 Unicode 序数）映射到 Unicode 序数（整数）、任意长度字符串、None 的 dict 字典。

如果有两个参数，则它们必须是长度相等的字符串，并且在结果字典中，x中的每个字符都将映射到中相同位置的字符。 如果有第三个参数， 必须是一个字符串，其字符将在结果中映射为None。

### 返回值：
返回一个字符映射转换表供 translate() 方法调用

### 示例：

```python
# 一个参数
>>> dct = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
>>> table = str.maketrans(dct)
>>> print(table)
{97: 1, 98: 2, 99: 3, 100: 4, 101: 5, 102: 6}

# 多个参数
>>> intab = "abcdef"
>>> outtab = "123456"
>>> delchars = "f"
>>> table = str.maketrans(intab,outtab,delchars)
>>> print(table)
{97: 49, 98: 50, 99: 51, 100: 52, 101: 53, 102: None}
```

# translate()
根据参数 table给出的表转换字符串
>根据 python3.7.3 文档，str 类型的 translate() 函数只接受一个参数，没有第二个 delete参数了。

### 语法
`str.translate(table)`  
`bytes.translate(table[, delete])`  
`bytearray.translate(table[, delete])`

### 参数
table -- 翻译表，翻译表是通过maketrans方法转换而来。
deletechars -- 字符串中要过滤的字符列表。

### 返回值
返回翻译后的字符串

### 示例

```python
>>> intab = "ehlocans"
>>> outtab = "!@#$%^&*"
>>> trantab = str.maketrans(intab, outtab)
>>> text = "hello can you speak chinese"
>>> print(text.translate(trantab))
@!##$ %^& y$u *p!^k %@i&!*!
```

# 小案例
加密 / 解密 古诗

```python
# 转换函数
def encrypt(text,type="encrypt"):
    old_text = "上不举乡低光前啼地声处多夜头少床思故明春是晓月望来疑眠知花落觉闻雨霜风鸟，。"
    new_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL"

    # 加密映射表
    encrypt_map = str.maketrans(old_text,new_text)

    # 解密映射表
    decrypt_map = str.maketrans(new_text,old_text)

    if type == "encrypt":
        result = text.translate(encrypt_map)
    elif type == "decrypt":
        result = text.translate(decrypt_map)
    else:
        return False
    return result

if __name__ == "__main__":
    text = "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。"
    text2 = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"

    encrypt1 = encrypt(text)
    encrypt2 = encrypt(text2)

    print("text加密："+encrypt1)
    print("text2加密："+encrypt2)
    print()

    decrypt1 = encrypt(encrypt1,"decrypt")
    decrypt2 = encrypt(encrypt2,"decrypt")
    print(f"{encrypt1} 解密：{decrypt1}")
    print(f"{encrypt2} 解密：{decrypt2}")
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200324154725191.png#pic_center)

