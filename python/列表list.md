<!-- TOC -->

- [python内置函数](#python%e5%86%85%e7%bd%ae%e5%87%bd%e6%95%b0)
- [列表常用方法](#%e5%88%97%e8%a1%a8%e5%b8%b8%e7%94%a8%e6%96%b9%e6%b3%95)
	- [增加数据](#%e5%a2%9e%e5%8a%a0%e6%95%b0%e6%8d%ae)
		- [append()](#append)
		- [insert()](#insert)
		- [extend()](#extend)
	- [删除数据](#%e5%88%a0%e9%99%a4%e6%95%b0%e6%8d%ae)
		- [remove()](#remove)
		- [pop()](#pop)
		- [clear()](#clear)
	- [其它操作](#%e5%85%b6%e5%ae%83%e6%93%8d%e4%bd%9c)
		- [reverse()](#reverse)
		- [sort()](#sort)
		- [copy()](#copy)
		- [count()](#count)
		- [index()](#index)

<!-- /TOC -->

# python内置函数
| 函数                                                                      | 说明                           |
| ------------------------------------------------------------------------- | ------------------------------ |
| [len(list)](https://www.runoob.com/python3/python3-att-list-len.html)     | 列表元素个数                   |
| [max(list)](https://www.runoob.com/python3/python3-att-list-max.html)     | 返回列表元素的最大值           |
| [min(list)](https://www.runoob.com/python3/python3-att-list-min.html)     | 返回列表元素的最小值           |
| [list(object)](https://www.runoob.com/python3/python3-att-list-list.html) | 将其他可迭代数据转换为列表类型 |

# 列表常用方法

## 增加数据

### append()

- 描述  
	用于在列表末尾添加新的对象
	
- 语法  
`list.append(obj)`

- 参数  
obj -- 添加到列表末尾的对象

- 返回值  
	\\
- 实例 

	```python
	lst = ["python","java","c"]
	lst.append("javascript")
	print(lst)
	>>>["python","java","c","javascript"]
	```

### insert()

- 描述  
	将指定对象插入列表的指定位置
	
- 语法  
	`list.insert(index, obj)`

- 参数  
	index -- 对象obj需要插入的索引位置。
	obj -- 要插入列表中的对象。
	
- 返回值  
	\\
- 实例  
	```python
	lst = ["python","java","c"]
	lst.insert(0,"javascript")
	print(lst)
	>>>["javascript","python","java","c"]
	```

### extend()
- 描述  
	在列表的末尾追加另一个序列的值
	
- 语法  
	`list.extend(seq)`
- 参数  
	seq -- 序列，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾
	
- 返回值  
	\\
- 实例  
	```python
	lst1 = ["python","java","c"]
	lst2 = [1,2,3,4,5]
	lst1.extend(lst2)
	print(lst1)
	>>>["python","java","c",1,2,3,4,5]
	```

## 删除数据

### remove()
- 描述  
	移除列表中某个值的第一个匹配项
	
- 语法  
	`list.remove(obj)`

- 参数  
	obj -- 列表中要移除的对象
	
- 返回值  
	\\
- 实例  
	```python
	lst = ["python","java","c"]
	lst.remove("java")
	print(lst)
	>>>["python","c"]
	```

### pop()
- 描述  
	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
	
- 语法  
	`list.pop([index=-1])`

- 参数  
	index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值
	
- 返回值  
	返回从列表中移除的元素对象
	
- 实例  
	```python
	lst = ["python","java","c"]
	remove_obj = lst.pop()
	print(remove_obj)
	print(lst )
	>>>"c"
	>>>["python","java"]
	```
	
### clear()
- 描述  
	清空列表
	
- 语法  
	`list.clear()`

- 参数  
	\\
	
- 返回值  
	\\
- 实例  
	```python
	lst = ["python","java","c"]
	lst.clear()
	print(lst)
	>>>[]
	```

## 其它操作	

### reverse()
- 描述  
	反向列表中元素
	
- 语法  
	list.reverse()

- 参数  
	\\
	
- 返回值  
	\\
- 实例  
	```python
	lst = ["python","java","c"]
	lst.reverse()
	print(lst)
	>>>['c', 'java', 'python']
	```
	
### sort()
- 描述  
	对原列表进行排序
	
- 语法  
	`list.sort(key=None,reverse=False)`

- 参数  
	key -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序
	reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
	
- 返回值  
	\\
- 实例  
	```python
	lst = [1,-3,8,-4,2]
	lst.sort(key=lambda x:abs(x))
	print(lst)
	>>>[1, 2, -3, -4, 8]
	```
	
### copy()
- 描述  
	复制列表，浅拷贝
	
- 语法  
	`list.copy()`

- 参数  
	\\
	
- 返回值  
	返回复制后的新列表
	
- 实例  
	```python
	lst1 = [1,2,3]
	lst2 = lst1.copy()
	print(lst2)
	>>>[1,2,3]
	```

### count()
- 描述  
	统计某个元素在列表中出现的次数
	
- 语法  
	`list.count(obj)`

- 参数  
	obj -- 列表中统计的对象
	
- 返回值  
	返回元素在列表中出现的次数
- 实例  
	```python
	lst = [1,2,1,2,1]
	count = lst.count(1)
	print(count)
	>>>3
	```

### index()
- 描述  
	从列表中找出某个值第一个匹配项的索引位置
	
- 语法  
	`list.index(x[, start[, end]])`

- 参数  
	x -- 查找的对象。
	start -- 可选，查找的起始位置。
	end -- 可选，查找的结束位置。
		
- 返回值  
	返回查找对象的索引位置，如果没有找到对象则抛出异常
	
- 实例  
	```python
	lst = ["python","java","c"]
	print(lst.index("java"))
	>>>1
	```

