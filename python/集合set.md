集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 创建集合
```python
sett = {value01,value02,...}
# 或者
sett = set([1,2,3,4])
```
# 集合内置方法
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
	
### update()
- 描述  
	给集合添加元素，参数可以是 列表，元组，字典等
	
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
### difference()
- 描述  
	返回当前集合与指定集合的差集
	
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
	从当前集合中移除与其他集合间非差集的元素
	
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
	从当前集合中移除与其他集合间非交集的元素
	
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
### symmetric_difference()
- 描述  
	返回两个集合中不重复的元素集合，即移除两个集合中都存在的元素
	
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
	移除当前集合中在另外一个集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
	
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

