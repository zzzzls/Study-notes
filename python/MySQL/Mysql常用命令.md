<!-- TOC -->

- [数据库管理](#%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86)  
        - [查看 MySQL版本](#%E6%9F%A5%E7%9C%8B-mysql%E7%89%88%E6%9C%AC)  
        - [数据库登录](#%E6%95%B0%E6%8D%AE%E5%BA%93%E7%99%BB%E5%BD%95)  
        - [查询数据库引擎](#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E5%BC%95%E6%93%8E)  
        - [查看所有数据库](#%E6%9F%A5%E7%9C%8B%E6%89%80%E6%9C%89%E6%95%B0%E6%8D%AE%E5%BA%93)  
        - [退出数据库](#%E9%80%80%E5%87%BA%E6%95%B0%E6%8D%AE%E5%BA%93)  
- [创建数据库](#%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E5%BA%93) 
        - [创建数据库](#%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E5%BA%93)  
        - [删除数据库](#%E5%88%A0%E9%99%A4%E6%95%B0%E6%8D%AE%E5%BA%93)  
        - [进入指定数据库](#%E8%BF%9B%E5%85%A5%E6%8C%87%E5%AE%9A%E6%95%B0%E6%8D%AE%E5%BA%93)  
        - [查看已进入的数据库名](#%E6%9F%A5%E7%9C%8B%E5%B7%B2%E8%BF%9B%E5%85%A5%E7%9A%84%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D)  
- [创建数据表](#%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E8%A1%A8)  
        - [查看数据表](#%E6%9F%A5%E7%9C%8B%E6%95%B0%E6%8D%AE%E8%A1%A8)  
        - [创建数据表](#%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E8%A1%A8)  
            - [数据类型](#%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)  
            - [表约束](#%E8%A1%A8%E7%BA%A6%E6%9D%9F)  
        - [查看表结构](#%E6%9F%A5%E7%9C%8B%E8%A1%A8%E7%BB%93%E6%9E%84)  
        - [重命名表](#重命名表)  
        - [查看表创建语句](#查看表的创建语句)  
        - [备份表](#%E5%A4%87%E4%BB%BD%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%BB%93%E6%9E%84)  
        - [清空表内容](#%E6%B8%85%E7%A9%BA%E8%A1%A8%E5%86%85%E5%AE%B9)  
        - [删除表](#%E5%88%A0%E9%99%A4%E8%A1%A8)  
- [修改表结构](#%E4%BF%AE%E6%94%B9%E8%A1%A8%E7%BB%93%E6%9E%84)  
        - [增加列](#%E5%A2%9E%E5%8A%A0%E5%88%97)  
        - [删除列](#%E5%88%A0%E9%99%A4%E5%88%97)  
        - [修改列](#%E4%BF%AE%E6%94%B9%E5%88%97)  
- [数据表中数据 CRUD](#%E6%95%B0%E6%8D%AE%E8%A1%A8%E4%B8%AD%E6%95%B0%E6%8D%AE-crud)  
        - [INSERT语句](#insert%E8%AF%AD%E5%8F%A5)  
        - [UPDATE语句](#update%E8%AF%AD%E5%8F%A5)  
        - [DELETE语句](#delete%E8%AF%AD%E5%8F%A5)  
        - [SELECT语句](#select%E8%AF%AD%E5%8F%A5)  
            - [查询数据表](#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E8%A1%A8)  
            - [去重](#%E5%8E%BB%E9%87%8D)  
            - [设置别名](#%E8%AE%BE%E7%BD%AE%E5%88%AB%E5%90%8D)  
            - [where条件](#where%E6%9D%A1%E4%BB%B6)  
            - [范围查询](#%E8%8C%83%E5%9B%B4%E6%9F%A5%E8%AF%A2)  
            - [范围匹配查询](#%E8%8C%83%E5%9B%B4%E5%8C%B9%E9%85%8D%E6%9F%A5%E8%AF%A2)  
            - [空值查询](#%E7%A9%BA%E5%80%BC%E6%9F%A5%E8%AF%A2)  
            - [模糊查询](#%E6%A8%A1%E7%B3%8A%E6%9F%A5%E8%AF%A2)  
            - [排序查询](#%E6%8E%92%E5%BA%8F%E6%9F%A5%E8%AF%A2)  
            - [分页查询](#%E5%88%86%E9%A1%B5%E6%9F%A5%E8%AF%A2)  
            - [聚合函数](#聚合函数)  
            - [分组](#分组)  
            - [more](#more)  

<!-- /TOC -->

# 数据库管理

### 查看 MySQL版本

`mysql --version`

### 数据库登录

`mysql -u用户名 -p`

### 查询数据库引擎

`show engines;`

> 常见的 MySQL数据库的操作引擎有8种，需要了解的只有两种 [ InnoDB | MyISAM ]  
> **InnoDB**: 数据库支持事物操作，数据库行级锁，外键等功能，默认引擎  
> **MyISAM**：不支持事物操作，但是数据的读写性能非常友好

### 查看所有数据库

`show databases [like '<db_name>'];`

### 退出数据库

`quit | exit`

# 创建数据库

### 创建数据库

```sql
# 创建一个数据库 并设置默认编码为 utf8
create database [IF NOT EXISTS] <db_name> default charset='UTF8';
```

### 删除数据库

```sql
drop database <db_name>;
```

### 进入指定数据库

```sql
# 数据库创建成功后并不表示选定并使用它，你必须明确操作进入指定数据库
use <db_name>;
```

> 进入数据库后，可使用 use 语句切换其它数据库

### 查看已进入的数据库名

`select database();`

# 创建数据表

### 查看数据表

`show tables;`

### 创建数据表

```sql
# 基本语法
create table <tab_name>(
    列名称 数据类型 [表约束],
    列名称 数据类型 [表约束]
);

############################

create table student(
    id int primary key auto_increment,
    name varchar(20) not null,
    age int
)
```

#### 数据类型

|类型|描述|
|:---|:---|
|int|整数|
|float|浮点数|
|datetime|日期时间|
|timestamp|时间戳|
|char|定长字符串|
|varchar|变长字符串|
|text|长文本数据|

#### 表约束

|语法|描述|
|:---|:---|
|not null|非空约束|
|unique|唯一约束|
|primary key|主键约束|
|auto_increment|自动增长|
|default|默认约束|

### 查看表结构

```sql
desc <tab_name>;
```

### 重命名表

```sql
rename table <old_tab_name> to <new_tab_name>
```

### 查看表的创建语句

```sql
show create table <tab_name>
```

### 备份数据表

```sql
# 备份表结构
create table <new_tab_name> select * from <old_tab_name> where 1 = 2;

# 备份表内容
create table <new_tab_name> select * from <old_tab_name>
```

### 清空表内容

```sql
truncate table <tab_name>
```

### 删除表

```sql
drop table <tab_name>
```

# 修改表结构

### 增加列

```sql
# 增加一列到末尾
alter table <tab_name> add column <col_name> <col_definition>

# 增加一列到开头
alter table <tab_name> add column <col_name> <col_definition> first

# 增加一列到指定列后
alter table <tab_name> add column <col_name> <col_definition> after <col_name>
```

### 删除列

```sql
alter table <tab_name> drop <col_name>
```

### 修改列

```sql
# 修改 列数据类型
alter table <tab_name> modify <col_name> <new_col_definition>

# 修改 列名 及 数据类型
alter table <tab_name> change <old_col_name> <new_col_name> <new_col_definition>

# 修改字段默认值
alter table <tab_name> alter <col_name> set default <default_value>
```

# 数据表中数据 CRUD

### INSERT语句

```sql
insert into <tab_name> [(col_name,col_name...)] values (值1，值2...);

# 全字段增加数据
insert into student values (1,"小明",18);

# 指定字段增加数据
insert into student (name,age) values ("小红",16)

# 增加多条数据
insert into student values (3,"tom",15),(4,"jey",19);

# 插入其他表数据到新表
insert into <new_tab_name> as select * from <old_table_name>
```

### UPDATE语句

```sql
-- 修改数据
update <tab_name> set <col_name> = <value>,<col_name> = <value>... where 条件;

-- 在原数据基础上修改数据
-- int 类型
update <tab_name> set age = age + 1

-- varchar类型
-- 增加 'zs' ==> 'user_zs'
update <tab_name> set name = concat("user_", name);

-- 减少 'user_zs'  ==> 'zs'
update <tab_name> set name = replace(name, 'user_', '')
```

### DELETE语句

```sql
-- 指定条件删除
delete from <tab_name> where 条件

-- 指定数量删除
delete from <tab_name> limit 5
```

### SELECT语句

#### 查询数据表

```sql
select {* | col_name} from <tab_name>
[
where <表达式>
group by <字段>
order by <字段>
limit <字段>
]

# 查询表中所有字段
select * from 表名;

# 查询表中指定字段
select <col_name,col_name....> from 表名：
```

#### 去重

```sql
select distinct <col_name> from <tab_name>;
```

备注：

- distinct 关键字只能在 select 中使用
- 在对一个或多个字段去重时，distinct 关键字必须在所有字段的最前面
- 如果 distinct 关键字后有多个字段，则会对多个字段进行组合去重，也就是，只有多个字段组合起来完全是一样的情况下才会被去重 

#### 设置别名

在使用 select 语句查询的时候，MySQL会显示每个 select后面输出的字段，有时为了显示结果更加直观，我们可以为字段指定一个别名

```sql
select <col_name> as 别名 from <tab_name>;
```

#### where条件

```sql
select * from 表名 where <条件>

# 单条件
select * from student where age > 18

# 多条件
# and : 记录满足所有条件，才会被查询出来
# or ： 记录满足任意一个条件，才会被查询出来
# xor ： 满足一个条件并且不满足另一个条件，才会被查询出来

select * from student where age > 15 and id > 10
```

#### 范围查询

MySQL 提供了 between and 关键字，用来判断字段的数值是否在指定范围内

between and 需要两个参数，即范围的起始值和终止值。如果字段值在指定的范围内，则这些记录被返回

```sql
select * from <tab_name> where <col_name> between n1 and n2

# 查询年纪在 15 到 18 岁之间的学生
select * from student where age between 15 and 18
```

#### 范围匹配查询

MySQL 提供了 in /not in ，用来范围匹配查询

进行离散数据（不连续的数据）检索时，通常会采用 in 查询的方式

```sql
select * from <tab_name> where <col_name> in (value1,value2,value3...)

# 查询年纪为 15，20，25 的学生
select * from student where age in (15,20,25)
```

#### 空值查询

MySQL 提供了 is null 关键字，判断字段的值是否为空值（MULL），**空值不等于0，也不同于空字符串**

```sql
select * from <tab_name> where <col_name> is null
```

#### 模糊查询

MySQL 提供了 like 关键字，用于模糊查询

like 关键字 支持 `%` 和 `_` 通配符

- `%` 代表任何长度的字符串，字符串长度可以为0
- `_`  代表单个字符

>注意：  
> **不要过度使用通配符**，MySQL对通配符的处理一般会比其它操作符花费更长时间  
> 除非有必要，否则**不要把通配符用在字符串的开始处**，放在开始处搜索起来是最慢的

```sql
select * from <tab_name> where <col_name> like <str>

# 查询名字中包含 n 的学生
select * from student where name like "%n%"
```

#### 排序查询

通过条件语句查询到的数据一般都是按照数据表中的顺序来显示，为了使查询结果的顺序满足用户的要求，MySQL提供了 order by 关键字来对查询结果进行排序

- asc : 默认值，按升序排列
- desc : 按降序排列

```sql
select * from <tab_name> order by <col_name> [asc|desc]

# 单字段排序
select * from student order by age

# 多字段排序
# 首先按照 age 进行排序 ，如果有多条数据 age 相同，按照 name 数据排序
select * from student order by age,name
```

#### 分页查询

当数据量较大时，一次性查询表中全部数据会降低数据返回速度，同时查阅不方便，这时候就可以使用 limit 关键字按照分页的方式进行查询

limit 是一个特殊的放剪子，用于指定查询结果从哪条记录开始显示，一共显示多少条数据，第一条记录的位置是 0

```sql
select * from <tab_name> limit 开始位置，查询记录数

# 查询数据表中 从第 3 条记录开始的两行记录
select * from student limit 2,2
```

#### 聚合函数

-   **count()** 计数

-   **max()** / **min()** 最大值 / 最小值

-   **sum()** 求和

-   **avg()** 平均值

>   除了 count 函数外，其余函数在计算时会自动忽略 null 值

#### 分组

根据给定列或者表达式的每一个不同值将表中的行分为不同的组，使组函数返回每一组的统计信息

**语法：**

```sql
SELECT 字段名... FROM 表名
	[WHERE 条件]
	[GROUP BY 字段名]
	[HAVING 过滤条件]
```

**注意**：

-   出现在 select 子句中单独的列，必须出现在 GROUP BY 子句中作为分组列
-   分组列可以不出现在 select 子句中



##### （1） group by + group_concat()

group_concat(字段名)  可以作为一个输出字段来使用

表示分组之后，根据分组结果，使用 group_concat() 来放置每一组字段的值的集合



![img][img@1]



##### （2） group by + 聚合函数

```sql
-- 根据性别分组并统计每组人数
SELECT gender, count(gender) FROM users GROUP BY gender;
```



##### （3） group by + having

having 表达式：对分组后数据进行过滤 （where 用于对分组前数据进行过滤），只能用于 group by

```sql
-- 根据课程对所有学员进行分组, 并展示学习人数大于10的小组
SELECT class, COUNT(class) FROM users GROUP BY class HAVING COUNT(class) > 10;
```



#### more

<http://c.biancheng.net/mysql/70/>

[img@1]:./image/img_1.png
