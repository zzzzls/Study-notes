<!-- TOC -->

- [数据库管理](#%e6%95%b0%e6%8d%ae%e5%ba%93%e7%ae%a1%e7%90%86)
    - [查看 MySQL版本](#%e6%9f%a5%e7%9c%8b-mysql%e7%89%88%e6%9c%ac)
    - [数据库登录](#%e6%95%b0%e6%8d%ae%e5%ba%93%e7%99%bb%e5%bd%95)
    - [查询数据库引擎](#%e6%9f%a5%e8%af%a2%e6%95%b0%e6%8d%ae%e5%ba%93%e5%bc%95%e6%93%8e)
    - [查看所有数据库](#%e6%9f%a5%e7%9c%8b%e6%89%80%e6%9c%89%e6%95%b0%e6%8d%ae%e5%ba%93)
    - [退出数据库](#%e9%80%80%e5%87%ba%e6%95%b0%e6%8d%ae%e5%ba%93)
- [创建数据库](#%e5%88%9b%e5%bb%ba%e6%95%b0%e6%8d%ae%e5%ba%93)
    - [创建数据库](#%e5%88%9b%e5%bb%ba%e6%95%b0%e6%8d%ae%e5%ba%93-1)
    - [删除数据库](#%e5%88%a0%e9%99%a4%e6%95%b0%e6%8d%ae%e5%ba%93)
    - [进入指定数据库](#%e8%bf%9b%e5%85%a5%e6%8c%87%e5%ae%9a%e6%95%b0%e6%8d%ae%e5%ba%93)
    - [查看已进入的数据库名](#%e6%9f%a5%e7%9c%8b%e5%b7%b2%e8%bf%9b%e5%85%a5%e7%9a%84%e6%95%b0%e6%8d%ae%e5%ba%93%e5%90%8d)
- [创建数据表](#%e5%88%9b%e5%bb%ba%e6%95%b0%e6%8d%ae%e8%a1%a8)
    - [查看数据表](#%e6%9f%a5%e7%9c%8b%e6%95%b0%e6%8d%ae%e8%a1%a8)
    - [创建数据表](#%e5%88%9b%e5%bb%ba%e6%95%b0%e6%8d%ae%e8%a1%a8-1)
      - [数据类型](#%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
      - [表约束](#%e8%a1%a8%e7%ba%a6%e6%9d%9f)
    - [查看表结构](#%e6%9f%a5%e7%9c%8b%e8%a1%a8%e7%bb%93%e6%9e%84)
    - [备份数据表结构](#%e5%a4%87%e4%bb%bd%e6%95%b0%e6%8d%ae%e8%a1%a8%e7%bb%93%e6%9e%84)
    - [清空表内容](#%e6%b8%85%e7%a9%ba%e8%a1%a8%e5%86%85%e5%ae%b9)
    - [删除表](#%e5%88%a0%e9%99%a4%e8%a1%a8)
- [修改表结构](#%e4%bf%ae%e6%94%b9%e8%a1%a8%e7%bb%93%e6%9e%84)
    - [增加列](#%e5%a2%9e%e5%8a%a0%e5%88%97)
    - [删除列](#%e5%88%a0%e9%99%a4%e5%88%97)
    - [修改列](#%e4%bf%ae%e6%94%b9%e5%88%97)
- [数据表中数据 CRUD](#%e6%95%b0%e6%8d%ae%e8%a1%a8%e4%b8%ad%e6%95%b0%e6%8d%ae-crud)
    - [INSERT语句](#insert%e8%af%ad%e5%8f%a5)
    - [UPDATE语句](#update%e8%af%ad%e5%8f%a5)
    - [DELETE语句](#delete%e8%af%ad%e5%8f%a5)
    - [SELECT语句](#select%e8%af%ad%e5%8f%a5)
      - [查询数据表](#%e6%9f%a5%e8%af%a2%e6%95%b0%e6%8d%ae%e8%a1%a8)
      - [去重](#%e5%8e%bb%e9%87%8d)
      - [设置别名](#%e8%ae%be%e7%bd%ae%e5%88%ab%e5%90%8d)
      - [where条件](#where%e6%9d%a1%e4%bb%b6)
      - [范围查询](#%e8%8c%83%e5%9b%b4%e6%9f%a5%e8%af%a2)
      - [范围匹配查询](#%e8%8c%83%e5%9b%b4%e5%8c%b9%e9%85%8d%e6%9f%a5%e8%af%a2)
      - [空值查询](#%e7%a9%ba%e5%80%bc%e6%9f%a5%e8%af%a2)
      - [模糊查询](#%e6%a8%a1%e7%b3%8a%e6%9f%a5%e8%af%a2)
      - [排序查询](#%e6%8e%92%e5%ba%8f%e6%9f%a5%e8%af%a2)
      - [分页查询](#%e5%88%86%e9%a1%b5%e6%9f%a5%e8%af%a2)
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
    id int primary auto_increment,
    name varchar(20) not null,
    age int
)
```

#### 数据类型

|类型|描述|
|:---|:---|
|int|整数|
|float|浮点数|
|datatime|日期时间|
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

### 备份数据表结构

```sql
create table <new_tab_name> as select * from <old_tab_name> where 1 = 2;
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

# 备份数据到新表
insert into <new_tab_name> as select * from <old_table_name>
```

### UPDATE语句

```sql
update <tab_name> set <col_name> = <value>,<col_name> = <value>... where 条件;
```

### DELETE语句

```sql
delete from <tab_name> where 条件
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
select * from <tab_name> limit 初始位置，记录数

# 查询数据表中 从第 3 条记录开始的 2 行记录
select * from student limit 2,2
```

#### more

<http://c.biancheng.net/mysql/70/>

