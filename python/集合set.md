<!-- TOC -->

- [集合简介](#%e9%9b%86%e5%90%88%e7%ae%80%e4%bb%8b)
- [集合内部存储数据的步骤](#%e9%9b%86%e5%90%88%e5%86%85%e9%83%a8%e5%ad%98%e5%82%a8%e6%95%b0%e6%8d%ae%e7%9a%84%e6%ad%a5%e9%aa%a4)
- [创建集合](#%e5%88%9b%e5%bb%ba%e9%9b%86%e5%90%88)
- [集合内置方法](#%e9%9b%86%e5%90%88%e5%86%85%e7%bd%ae%e6%96%b9%e6%b3%95)
	- [增加数据](#%e5%a2%9e%e5%8a%a0%e6%95%b0%e6%8d%ae)
		- [add()](#add)
	- [删除数据](#%e5%88%a0%e9%99%a4%e6%95%b0%e6%8d%ae)
		- [remove()](#remove)
		- [discard()](#discard)
		- [pop()](#pop)
		- [clear()](#clear)
	- [判断类函数](#%e5%88%a4%e6%96%ad%e7%b1%bb%e5%87%bd%e6%95%b0)
		- [isdisjoint()](#isdisjoint)
		- [issubset()](#issubset)
		- [issuperset()](#issuperset)
	- [两个集合：部分差集](#%e4%b8%a4%e4%b8%aa%e9%9b%86%e5%90%88%e9%83%a8%e5%88%86%e5%b7%ae%e9%9b%86)
		- [difference()](#difference)
		- [difference_update()](#differenceupdate)
	- [两个集合：完整差集](#%e4%b8%a4%e4%b8%aa%e9%9b%86%e5%90%88%e5%ae%8c%e6%95%b4%e5%b7%ae%e9%9b%86)
		- [symmetric_difference()](#symmetricdifference)
		- [symmetric_difference_update()](#symmetricdifferenceupdate)
	- [两个集合：交集](#%e4%b8%a4%e4%b8%aa%e9%9b%86%e5%90%88%e4%ba%a4%e9%9b%86)
		- [intersection()](#intersection)
		- [intersection_update()](#intersectionupdate)
	- [两个集合：并集](#%e4%b8%a4%e4%b8%aa%e9%9b%86%e5%90%88%e5%b9%b6%e9%9b%86)
		- [union()](#union)
		- [update()](#update)

<!-- /TOC -->

# 集合简介

集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

集合在项目中使用较多（没有列表多），更多的时候集合的操作是**对数据的过滤**。这里所说的集合与数学中的集合有点类似。

# 集合内部存储数据的步骤

向集合中添加一个数据时，会执行以下两步：
1. 通过数据的哈希值快捷判断需要添加的数据是否重复
2. 通过数据的 **==** 判断，依次遍历所有的数据是否存在重复，若不存在，则添加该数据

![img][img@1]

# 创建集合

```python
sett = {value01,value02,...}
# 或者
sett = set([1,2,3,4])
```

# 集合内置方法

## 增加数据

### add()

- 描述  
	给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作

- 语法  
	`set.add(elmnt)`

- 参数  
	elmnt -- 必需，要添加的元素。

- 返回值  
	\\
- 实例  
	```python
	fruits = {"apple","banana","cherry"}
	fruits.add("orange")
	print(fruits)
	>>>{'cherry', 'banana', 'orange', 'apple'}
	```

## 删除数据

### remove()

- 描述  
	移除集合中的指定元素，如果元素不存在会抛出错误
	
- 语法  
	`set.remove(item)`

- 参数  
	item -- 要移除的元素

- 返回值  
	\\
- 实例  
	```python
	fruits = {"apple", "banana", "cherry"}
	fruits.remove("banana") 
	print(fruits)
	>>>{'cherry', 'apple'}
	```

### discard()

- 描述  
	移除集合中的指定元素，如果元素不存在不会抛出错误
	
- 语法  
	`set.discard(value)`

- 参数  
	value -- 必需，要移除的元素

- 返回值  
	\\
- 实例  
	```python
	x = {"apple", "banana", "cherry"}
	x.discard("apple")
	print(x)
	>>>{'cherry', 'banana'}
	```

### pop()
- 描述  
	随机移除一个元素
	
- 语法  
	`set.pop()`

- 参数  
	\\

- 返回值  
	返回移除的元素。
	
- 实例  
	```python
	x= {"apple", "banana", "cherry"}
	delete = x.pop() 
	print(delete)
	print(x)
	>>>"cherry"
	>>>{"apple", "banana"}
	```

### clear()
- 描述  
	移除集合中的所有元素
	
- 语法  
	`set.clear()`

- 参数  
	\\

- 返回值  
	\\
- 实例  
	```python
	fruits = {"apple", "banana", "cherry"}
	fruits.clear()
	print(fruits)
	>>>set()
	```

## 判断类函数

### isdisjoint()
- 描述  
	判断两个集合是否包含相同的元素，没有返回True，否则返回 False
	
- 语法  
	`set.isdisjoint(set)`

- 参数  
	set -- 必需，要比较的集合

- 返回值  
	返回布尔值，如果不包含返回 True，否则返回 False。
	
- 实例  
	```python
	x = {1,2,3}
	y = {4,5,6}
	print(x.isdisjoint(y))
	>>>True
	```

### issubset()
- 描述  
	判断当前集合是不是指定集合的子集
	
- 语法  
	`set.issubset(set)`

- 参数  
	set -- 必需，指定的集合

- 返回值  
	返回布尔值，如果是子集返回 True，否则返回 False
	
- 实例  
	```python
	>>> x = {1,2}
	>>> y = {1,2,3,4}
	>>> x.issubset(y)
	True
	```

### issuperset()
- 描述  
	判断当前集合是不是指定集合的父集
	
- 语法  
	`set.issuperset(set)`

- 参数  
	set -- 必需，指定的集合

- 返回值  
	返回布尔值，如果是父集返回 True，否则返回 False
- 实例  
	```python
	>>> x = {1,2,3,4,5}
	>>> y = {3,4}
	>>> x.issuperset(y)
	True
	```

## 两个集合：部分差集

### difference()
- 描述  
	返回当前集合相对于指定集合中，不同的数据
	
- 语法  
	`set.difference(set)`

- 参数  
	set -- 必需，用于计算差集的集合

- 返回值  
	返回一个新的集合
	
- 实例  
	```python
	>>> x={1,2,3,4,5}
	>>> y={3,4}
	>>> z=x.difference(y)
	>>> print(z)
	{1, 2, 5}
	```

### difference_update()
- 描述  
	得到当前集合相对于指定集合中，不同的数据，并将其赋值给当前集合
	
- 语法  
	`set.difference_update(set)`

- 参数  
	set -- 必需，用于比较的集合

- 返回值  
	\\
	
- 实例  
	```python
	>>> x={1,2,3,4,5}
	>>> y={4,5,6,7,8}
	>>> x.difference_update(y)
	>>> print(x)
	{1, 2, 3}
	```

## 两个集合：完整差集

### symmetric_difference()
- 描述  
	返回两个集合中所有不同的数据，即移除两个集合中都存在的元素
	
- 语法  
	`set.symmetric_difference(set)`

- 参数  
		set -- 其他相比较的集合
		
- 返回值  
	返回一个新的集合。
	
- 实例  
	```python
	>>> x={1,2,3}
	>>> y={3,4,5}
	>>> x.symmetric_difference(y)
	{1, 2, 4, 5}
	```

### symmetric_difference_update()
- 描述  
	获取两个集合中所有不同的数据，并将其赋值给当前集合
	
- 语法  
	`set.symmetric_difference_update(set)`

- 参数  
	set -- 其他相比较的集合
		
- 返回值  
	\\
	
- 实例  
	```python
	>>> x={1,2,3}
	>>> y={3,4,5}
	>>> x.symmetric_difference_update(y)
	>>> x
	{1, 2, 4, 5}
	```

## 两个集合：交集

### intersection()
- 描述  
	返回两个或者更多集合中都包含的元素，即交集
	
- 语法  
	`set.intersection(set1, set2 ...)`

- 参数  
		set1 -- 必需，要进行比较的集合
		set2 -- 可选，其他进行比较的集合，多个使用逗号 , 隔开

- 返回值  
	返回一个新的集合
	
- 实例  
	```python
	>>> x={1,2,3}
	>>> y={2,3,4}
	>>> z={3,4,5}
	>>> x.intersection(y,z)
	{3}
	```

### intersection_update()
- 描述  
	得到两个或者更多集合中都包含的元素，并将其赋值给当前集合
	
- 语法  
	`set.intersection_update(set1, set2 ...)`

- 参数  
		set1 -- 必需，要进行比较的集合
		set2 -- 可选，其他进行比较的集合，多个使用逗号 , 隔开
		
- 返回值  
	\\
	
- 实例  
	```python
	>>> x={1,2,3}
	>>> y={2,3,4}
	>>> x.intersection_update(y)
	>>> x
	{2, 3}
	```

## 两个集合：并集

### union()
- 描述  
	返回两个或多个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次
	
- 语法  
	`set.union(set1, set2...)`

- 参数  
		set1 -- 必需，比较目标集合
		set2 -- 可选，其他要比较的集合，多个使用逗号 , 隔开。
		
- 返回值  
	返回一个新集合
	
- 实例  
	```python
	>>> x={1,2,3}
	>>> y={3,4,5,6}
	>>> x.union(y)
	{1, 2, 3, 4, 5, 6}
	```

### update()

- 描述  
	获取两个集合的并集，并将其赋值给当前集合
	
- 语法  
	`set.update(set)`

- 参数  
	set -- 必需，可以是元素或集合

- 返回值  
	\\
- 实例  
	```python
	x = {"apple", "banana", "cherry"}
	y = {"google", "runoob", "apple"}
	x.update(y)
	print(x)
	>>>{'cherry', 'google', 'runoob', 'apple', 'banana'}
	```


[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/%E9%9B%86%E5%90%88set/04-06_1.png