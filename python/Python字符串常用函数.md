# 转换类函数
|函数| 描述 |
|--|--|
| [lower()](https://www.runoob.com/python3/python3-string-lower.html) | 大写 => 小写 |
|[upper()](https://www.runoob.com/python3/python3-string-upper.html)| 小写 => 大写|
|[swapcase()](https://www.runoob.com/python3/python3-string-swapcase.html)|翻转字符串中的大小写|
|[capitalize()](https://www.runoob.com/python3/python3-string-capitalize.html)|将字符串的第一个字母大写，其余字母全部小写|
|[title()](https://www.runoob.com/python3/python3-string-title.html)|将字符串中的所有单词的首字母大写，其余字母全部小写<br>这里单词的区分是以任何标点符号区分的|
|[expandtabs(tabsize=8)](https://www.runoob.com/python3/python3-string-expandtabs.html)|将字符串中的 \t 转为空格|
|[replace(old, new, count=-1)](https://www.runoob.com/python3/python3-string-replace.html)|将字符串中的 old字符 替换为 new字符|
|  [join()](https://www.runoob.com/python3/python3-string-join.html) |  将序列中的元素以指定的字符连接生成一个新的字符串 |
# 分割类函数
|函数| 描述 |
|--|--|
| [split()](https://www.runoob.com/python3/python3-string-split%28%29.html)  |  通过指定分隔符对字符串进行切片 |
| rsplit() |  通过指定分隔符对字符串进行切片，从字符串末尾开始分割 |
|   [splitlines()](https://www.runoob.com/python3/python3-string-splitlines.html) | 按照行 `\r, \r\n, \n` 分隔  |
|[partition()](https://www.runoob.com/python/att-string-partition.html)| 根据指定的分隔符将字符串进行分割，返回一个三元的元组  |
|  rpartition() | 根据指定的分隔符将字符串进行分割，从字符串末尾开始分割  |
|  strip()  |  从字符串头尾移除指定的字符（默认为空格） |
| [lstrip()](https://www.runoob.com/python3/python3-string-lstrip.html)  | 截掉字符串左边的指定字符  |
|  [rstrip()](https://www.runoob.com/python3/python3-string-rstrip.html) | 截掉字符串末尾的指定字符  |

`partition()函数`：  
根据指定的分隔符将字符串进行分割。
如果字符串包含指定的分隔符，则返回一个3元的元组，
第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
若分隔符 两侧无字符，则补充空字符串到元组中

# 查找类函数
|函数| 描述 |
|--|--|
|  [find()](https://www.runoob.com/python3/python3-string-find.html) |  查找字符串中指定的子字符串`第一次`出现的位置 |
| [rfind()](https://www.runoob.com/python3/python3-string-rfind.html)  |  返回指定的子字符串`最后一次`出现的位置|
| [index()](https://www.runoob.com/python3/python3-string-index.html)  | 查找指定的子字符串`第一次`出现的位置  |
|  [rindex()](https://www.runoob.com/python3/python3-string-rindex.html) |  查找指定的子字符串`最后一次`出现的位置 |
| [count()](https://www.runoob.com/python3/python3-string-count.html)  |  统计字符串里某个字符出现的次数 |

`find 与 index 的区别：`
- 两者实现的效果相同
- 如果find未找到内容，会返回 -1 ， index未找到内容，会抛出一个 ValueError 异常
- find 仅适用与 字符串中，index 可以用在 字符串 列表 元组 中

# 填充类函数
|函数| 描述 |
|--|--|
|  [center(width\[, fillchar\])](https://www.runoob.com/python3/python3-string-center.html) | 返回一个原字符串居中，两侧使用 fillchar 填充至指定长度的新字符串 |
|  [ljust(width\[, fillchar\])](https://www.runoob.com/python3/python3-string-ljust.html) |  返回一个原字符串左对齐，并使用 fillchar 填充至指定长度的新字符串 |
|  [rjust(width[, fillchar])](https://www.runoob.com/python3/python3-string-rjust.html) | 返回一个原字符串右对齐，并使用 fillchar 填充至指定长度的新字符串  |
|  [zfill(width)](https://www.runoob.com/python3/python3-string-zfill.html) |  返回指定长度的字符串，原字符串右对齐，前面填充0 |
# 判断类函数
|函数| 描述 |
|--|--|
| [startswith(str,\[start, end\])](https://www.runoob.com/python3/python3-string-startswith.html)  | 检查字符串是否是以指定子字符串开头  |
| [endswith(str,\[start, end\])](https://www.runoob.com/python3/python3-string-endswith.html)  | 检查字符串是否是以指定子字符串结尾 |
| [isalnum()](https://www.runoob.com/python3/python3-string-isalnum.html) | 检测字符串是否由字母和数字组成 |
| [isalpha()](https://www.runoob.com/python3/python3-string-isalpha.html)  | 检测字符串是否只由字母组成  |
| [isdigit()](https://www.runoob.com/python3/python3-string-isdigit.html)  |  检测字符串是否只由数字组成 |
| [islower()](https://www.runoob.com/python3/python3-string-islower.html)  |  检测字符串中的字母是否全由小写字母组成 |
| [isupper()](https://www.runoob.com/python3/python3-string-isupper.html)  |  检测字符串中的字母是否全由大写字母组成 |
| isprintable()  |  检测字符串中是否有打印后不可见的内容。如：\n \t  等字符|
| [isspace()](https://www.runoob.com/python3/python3-string-isspace.html)  | 检测字符串是否只由空格组成  |
|  [istitle()](https://www.runoob.com/python3/python3-string-istitle.html) |  检测判断字符串中所有单词的首字母是否为大写，且其它字母是否为小写 |


