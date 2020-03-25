# 字典内置函数
|函数| 描述 |
|--|--|
| len(dict) | 计算字典元素个数，即键的总数|
| str(dict)  | 将字典转换为字符串  |

# 字典内置方法
### clear()
- 描述  
	删除字典内所有元素
	
- 语法  
	`dict.clear()`

- 参数  
	\\

- 返回  值
	\\
- 实例  
	```python
	dct = {"name":"zong","age":18}
	dct.clear()
	print(dct)
	>>>{}
	```

### copy()
- 描述  
	返回一个字典的浅拷贝
	
- 语法  
	dict.copy()

- 参数  
	\\

- 返回  值
	返回一个字典的浅拷贝
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	dct1 = dct.copy()
	print(dct1)
	>>>{"name":"zong","age":18}
	```

### fromkeys()
- 描述  
	创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
	
- 语法  
`dict.fromkeys(seq[, value])`

- 参数  
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。

- 返回  值
	返回一个新字典
	
- 实例  
	```python
	seq = ["name","age","sex"]
	dct = dct.fromkeys(seq)
	print(dct)
	>>>{'name': None, 'age': None, 'sex': None}
	```
	
### get()
- 描述  
	返回指定键的值，如果键不在字典中返回默认值
	
- 语法  
	`dict.get(key, default=None)`

- 参数  
	key -- 字典中要查找的键。
	default -- 如果指定键的值不存在时，返回该默认值值。

- 返回  值
	返回指定键的值，如果值不在字典中返回默认值
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	dct.get("name")
	dct.get("sex")
	dct.get("sex","空")
	>>>'zong'
	>>>None
	>>>空
	```
### setdefault()
- 描述  
	返回指定键的值，如果键不在字典中则插入并返回默认值
	
- 语法  
	`dict.setdefault(key, default=None)`

- 参数  
	key -- 查找的键值。
	default -- 键不存在时，设置的默认键值。

- 返回  值
	如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	print(dct.setdefault("age"))
	print(dct.setdefault("sex"))
	print(dct.setdefault("sex","男"))

	>>>18
	>>>None
	{'name': 'zong', 'age': 18, 'sex': None}

	>>>"男"
	{'name': 'zong', 'age': 18, 'sex': '男'}
	```
### items()
- 描述  
	以列表返回可遍历的(键, 值) 元组数组
	
- 语法  
	`dict.items()`

- 参数  
	\\

- 返回  值
	返回可遍历的(键, 值) 元组数组
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	print(dct.items())
	>>>dict_items([('name', 'zong'), ('age', 18)])
	```
### pop()
- 描述  
	删除字典给定键 key 所对应的值，返回值为被删除的值。如果给定键值不存在，返回 default 值
	
- 语法  
	`pop(key[,default])`

- 参数  
	key: 要删除的键值
	default: 如果key不存在，返回 default 值

- 返回  值
	返回被删除的值 或者 default的值
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	print(dct.pop("age"))
	# 如果要删除的 键 不存在，则必须设置默认值，否则会报错
	print(dct.pop("sex","空"))
	>>>18
	>>>空
	```
### popitem()
- 描述  
	删除并返回 字典中的最后一对键和值
	
- 语法  
	`dict.popitem()`

- 参数  
	\\

- 返回  值
	返回一个键值对(key,value)形式
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	print(dct.popitem())
	>>>('age', 18)
	```
### update()
- 描述  
	把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
	
- 语法  
	`dict.update(dict2)`

- 参数  
	dict2 -- 添加到指定字典dict里的字典

- 返回  值
	\\
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	dct2 = {"sex":"男"}
	dct.update(dct2)
	print(dct)
	>>>{'name': 'zong', 'age': 18, 'sex': '男'}
	```
### keys()
- 描述  
	返回字典中键对应的列表
	
- 语法  
	dict.keys()

- 参数  
	\\

- 返回  值
	返回字典中键对应的列表
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	print(dct.keys())
	>>>dict_keys(['name', 'age'])
	```
### values()
- 描述  
	返回字典中值对应的列表
	
- 语法  
	`dict.values()`

- 参数  
	\\

- 返回  值
	返回字典中值对应的列表
	
- 实例  
	```python
	dct = {"name":"zong","age":18}
	print(dct.values())
	>>>dict_values(['zong', 18])
	```

