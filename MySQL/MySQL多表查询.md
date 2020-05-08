<!-- TOC -->

- [多表查询](#%e5%a4%9a%e8%a1%a8%e6%9f%a5%e8%af%a2)
  - [交叉连接](#%e4%ba%a4%e5%8f%89%e8%bf%9e%e6%8e%a5)
    - [笛卡尔积](#%e7%ac%9b%e5%8d%a1%e5%b0%94%e7%a7%af)
  - [内连接](#%e5%86%85%e8%bf%9e%e6%8e%a5)
  - [外连接](#%e5%a4%96%e8%bf%9e%e6%8e%a5)
    - [左外连接](#%e5%b7%a6%e5%a4%96%e8%bf%9e%e6%8e%a5)
    - [右外连接](#%e5%8f%b3%e5%a4%96%e8%bf%9e%e6%8e%a5)
  - [子查询](#%e5%ad%90%e6%9f%a5%e8%af%a2)

<!-- /TOC -->

# 多表查询

在关系型数据库中，表与表之间是有练习的，所以在实际应用中，经常使用多表查询。多表查询就是同时查询两个或两个以上的表

在 MySQL 中，多表查询主要有 **交叉连接**，**内连接**，**外连接**，**子查询**

## 交叉连接

交叉连接 ( CROSS JOIN ) 一般用来返回连接表的笛卡尔积

**语法格式如下：**

```sql
# 多表交叉连接时，使用 `cross join` 或者 `,` 皆可，前者是官方建议的标准写法
select <字段名> from <tab_name> cross join <tab_name> [where子句]
select <字段名> from <tab_name>,<tab_name> [where子句]
```

当连接的表之间没有关系时，我们会省略掉 where子句，这时返回结果就是两个表的笛卡尔积，返回结果数量就是两个表的数据行相乘，如果每个表有 1000 行，那么返回数量就有 1000*1000=1000000 行，数据量是非常巨大的！

如果在交叉连接时使用 where子句，MySQL会先生成两个表的笛卡尔积，然后再选择满足 where条件的记录。因此，表的数量较多时，交叉连接会非常非常慢，一般情况下不建议使用交叉连接

### 笛卡尔积

笛卡尔积( Cartesian product ) 是指两个集合 x 和 y 的乘积

例如，有两个集合，它们值如下：

```python
A = {1,2}
B = {3,4,5}

# 集合 A*B 的结果集为：
A×B={(1,3), (1,4), (1,5), (2,3), (2,4), (2,5) };

# 集合 B*A 的结果集为：
B×A={(3,1), (3,2), (4,1), (4,2), (5,1), (5,2) };
```
以上 A*B 和 B*A 的结果就叫做两个集合各自的笛卡尔积

## 内连接

内连接 ( inner join ) 使用 `inner join` 关键字连接两张表，并使用 `on` 子句来设置连接条件

**语法格式如下：**

```sql
select <字段名> from <tab_name> <tab_name> inner join <tab_name> [on子句]
```

多个表连接时，再 from 后边连续使用 `inner join` 或 `join` 即可

**案例操作：**

```sql
# 在 学生表 和 课程表中，查询 学生对应的课程
select s.name c.course_name from student as s inner join course as c on s.course_id = c.id
```

> 注意：当对多个表进行查询时，要在 select 语句后面指定字段是来源自哪一张表  
> 语法为 `表名.列名` ，如果表名较长，可以给表设置别名，这样就可以直接在 select 后写 `表的别名.列名`

## 外连接

内连接查询的结果都是符合连接条件的结果，为外连接会先将连接的表分为基表和参考表，再以基表为依据返回满足与不满足条件的记录

外连接区分为 **左外连接** 和 **右外连接**

### 左外连接

左外连接又称为左连接，使用 `left outer join` 关键字连接两个表，也可以简写为 `left join`，并使用 `on` 设置连接条件

**语法格式如下：**

```sql
select <字段名> from <tab1> left join <tab2> [on子句]
```

上述语法中，**tab1 为基表**，**tab2 为参考表**，左连接查询时，可以查询处 tab1 中的所有记录和 tab2 中匹配连接条件的记录。如果 tab1 的某行在 tab2 中没有匹配行，那么在返回结果中，tab2 的字段值均为空值 NULL

![img][img@1]

### 右外连接

右外连接又称为右连接，右连接是左连接的反向连接。使用 `right outer join` 关键字连接两个表，可以简化为 `right join` ，并使用 `on` 子句来设置连接条件

**语法格式如下：**

```sql
select <字段名> from <tab1> right outer <tab2> [on子句]
```

与左连接相反，右连接以 tab2 为基表，tab1 为参考表，可以查询出 tab2 中所有记录和 tab1 中匹配连接条件的记录。如果 tab2 的某行在 tab1 中没有匹配项，那么在返回结果中，tab1 的字段值均为 NULL

![img][img@2]

多个表 左/右 连接时，在 on 子句后连续使用 `left/right join` 即可 


## 子查询

子查询是 MySQL 中比较常用的查询方法，通过子查询可以实现多表查询。**子查询指将一个查询语句嵌套在另一个查询语句中**。子查询可以在 select,update 和 delete 语句中使用，而且可以进行多层嵌套，实际开发中，子查询经常出现在 where 语句中

**语法格式如下：**

```sql
select <字段> from <tab_name>
    where <字段><操作符>(子查询)
    );
```

其中，操作符可以是 `in`，`not in`，`exists`，`not exists` 等关键字

**案例：**

```sql
# 查询学习 python 课程的学生
select name from student s
    where s.course_id = (select id from course c where c.name = "Python")

# 查询学习 python 和 html 的学生
SELECT name FROM student s WHERE s.course_id in
    (SELECT id FROM course c WHERE c.name="Python" OR c.name="Html");
```

**进阶用法：**

子查询语句可以嵌套在 SQL 语句中任何表达式出现的位置

```sql
select (子查询) from 表名；

select * from (子查询) as 别名；
```


[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/%E6%95%B0%E6%8D%AE%E5%BA%93/mysql/05-08_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/%E6%95%B0%E6%8D%AE%E5%BA%93/mysql/05-08_02.png