<!-- TOC -->

-   [多表关系](#多表关系)

- [多表查询](#%E5%A4%9A%E8%A1%A8%E6%9F%A5%E8%AF%A2)
    - [交叉连接](#%E4%BA%A4%E5%8F%89%E8%BF%9E%E6%8E%A5)
        - [笛卡尔积](#%E7%AC%9B%E5%8D%A1%E5%B0%94%E7%A7%AF)
    - [内连接](#%E5%86%85%E8%BF%9E%E6%8E%A5)
    - [外连接](#%E5%A4%96%E8%BF%9E%E6%8E%A5)
        - [左外连接](#%E5%B7%A6%E5%A4%96%E8%BF%9E%E6%8E%A5)
        - [右外连接](#%E5%8F%B3%E5%A4%96%E8%BF%9E%E6%8E%A5)
    - [子查询](#%E5%AD%90%E6%9F%A5%E8%AF%A2)
    - [自关联](#自关联)

<!-- /TOC -->

## 多表关系

两张表的关联关系，主要通过外键体现，外键就是两张表之间的联系

>   外键约束，是将两张表之间的关联关系，通过执行的手段进行关联的，没有外键也可以关联（人为约定，容易造成垃圾数据），通过外键进行关联就可以在语法层面上约束插入的数据必须保持一致



#### （1）一对一

**示例：**

- 人和身份证号
- 丈夫和妻子

>   外键可以添加在任意一个表中



**实现方式：**

1.  通过修改表结构添加外键

    ```sql
    ALTER TABLE 当前表名 ADD CONSTRAINT FOREIGN KEY(当前表的键) REFERENCES 关联表名(关联表键)
    ```

    

2.  建表时，添加外键约束

    ```sql
    CREATE TABLE card(
    	id INT PRIMARY KEY AUTO_INCREMENT,
        card_num VARCHAR(20),
        cid INT UNIQUE,
        FOREIGN KEY(cid) REFERENCES user(id)
    );
    ```

    

#### （2）一对多

**示例：**

	- 班级和学生 （一个学生有一个班级，一个班级有多个学生）

>   外键应该添加到多表中



**实现方式：**

1.  在多的表中添加外键，关联少的一方主键

2.  新建一个关系表，用于关联之前两个表各自键

    ```sql
    -- 新建关系表
    CREATE TABLE stu_class(
    	id INT PRIMARY KEY AUTO_INCREMENT,
        s_id INT UNIQUE NOT NULL, -- 此处使用唯一, 对应一个学生只能属于一个班级
        c_id INT NOT NULL
    );
    ```

    

#### （3）多对多

**示例：**

-   学生和学科 （一个学生可以选择多个学科，一个学科可以有多个学生）



**实现方式：**

1.  新建一个关系表，用于关联之前两个表各自键

    ```sql
    -- 新建关系表
    CREATE TABLE stu_course(
    	id INT PRIMARY KEY AUTO_INCREMENT,
        s_id INT NOT NULL,
        c_id INT NOT NULL
    );
    ```

    

## 多表查询

在关系型数据库中，表与表之间是有联系的，所以在实际应用中，经常使用多表查询。多表查询就是同时查询两个或两个以上的表

在 MySQL 中，多表查询主要有 **交叉连接**，**内连接**，**外连接**，**子查询**

### 交叉连接

交叉连接 ( CROSS JOIN ) 一般用来返回连接表的笛卡尔积

**语法格式如下：**

```sql
# 多表交叉连接时，使用 `cross join` 或者 `,` 皆可，前者是官方建议的标准写法
select <字段名> from <tab_name> cross join <tab_name> [where子句]
select <字段名> from <tab_name>,<tab_name> [where子句]
```

当连接的表之间没有关系时，我们会省略掉 where子句，这时返回结果就是两个表的笛卡尔积，返回结果数量就是两个表的数据行相乘，如果每个表有 1000 行，那么返回数量就有 1000*1000=1000000 行，数据量是非常巨大的！

如果在交叉连接时使用 where子句，MySQL会先生成两个表的笛卡尔积，然后再选择满足 where条件的记录。因此，表的数量较多时，交叉连接会非常非常慢，一般情况下不建议使用交叉连接

#### 笛卡尔积

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

### 内连接

内连接 ( inner join ) 使用 `inner join` 关键字连接两张表，并使用 `on` 子句来设置连接条件

**语法格式如下：**

```sql
select <字段名> from <tab_name> inner join <tab_name> [on子句]
```

多个表连接时，在 from 后边连续使用 `inner join` 或 `join` 即可

**案例操作：**

```sql
# 在 学生表 和 课程表中，查询 学生对应的课程
select s.name c.course_name from student as s inner join course as c on s.course_id = c.id
```

> 注意：当对多个表进行查询时，要在 select 语句后面指定字段是来源自哪一张表  
> 语法为 `表名.列名` ，如果表名较长，可以给表设置别名，这样就可以直接在 select 后写 `表的别名.列名`

### 外连接

内连接查询的结果都是符合连接条件的结果，为外连接会先将连接的表分为基表和参考表，再以基表为依据返回满足与不满足条件的记录

外连接区分为 **左外连接** 和 **右外连接**

#### 左外连接

左外连接又称为左连接，使用 `left outer join` 关键字连接两个表，也可以简写为 `left join`，并使用 `on` 设置连接条件

**语法格式如下：**

```sql
select <字段名> from <tab1> left join <tab2> [on子句]
```

上述语法中，**tab1 为基表**，**tab2 为参考表**，左连接查询时，可以查询处 tab1 中的所有记录和 tab2 中匹配连接条件的记录。如果 tab1 的某行在 tab2 中没有匹配行，那么在返回结果中，tab2 的字段值均为空值 NULL

![img][img@2]

#### 右外连接

右外连接又称为右连接，右连接是左连接的反向连接。使用 `right outer join` 关键字连接两个表，可以简化为 `right join` ，并使用 `on` 子句来设置连接条件

**语法格式如下：**

```sql
select <字段名> from <tab1> right outer <tab2> [on子句]
```

与左连接相反，右连接以 tab2 为基表，tab1 为参考表，可以查询出 tab2 中所有记录和 tab1 中匹配连接条件的记录。如果 tab2 的某行在 tab1 中没有匹配项，那么在返回结果中，tab1 的字段值均为 NULL

![img][img@1]

多个表 左/右 连接时，在 on 子句后连续使用 `left/right join` 即可 

### 子查询

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

### 自关联

[自关联](#https://www.yiibai.com/mysql/self-join.html)



[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/%E6%95%B0%E6%8D%AE%E5%BA%93/mysql/05-08_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/%E6%95%B0%E6%8D%AE%E5%BA%93/mysql/05-08_02.png