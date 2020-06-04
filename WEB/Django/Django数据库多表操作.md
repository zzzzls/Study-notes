<!-- TOC -->

- [一对一关系](#%E4%B8%80%E5%AF%B9%E4%B8%80%E5%85%B3%E7%B3%BB)
- [一对多关系](#%E4%B8%80%E5%AF%B9%E5%A4%9A%E5%85%B3%E7%B3%BB)
- [多对多关系](#%E5%A4%9A%E5%AF%B9%E5%A4%9A%E5%85%B3%E7%B3%BB)

<!-- /TOC -->

## 一对一关系

**创建模型**

```python
# 一个学生 对应 一个老师
class Student(models.Model):
    username = models.CharField(max_length=32)
    gender = models.IntegerField()
    age = models.IntegerField()

class Teacher(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    # models.OneToOneField 创建一对一关系
    t_student = models.OneToOneField(to="Student",on_delete=models.CASCADE)
```

参数:
- `to` 指明关联哪张表
- `on_delete` 指的是 如果删除关联表的数据,Teacher 表应该做什么操作
    - `CASCADE` 级联删除，如果删除 Student 表数据，Teacher表中对应数据删除
    - `DO_NOTHING` 不做任何操作

> 如果删除 Teacher 表，Student 不受影响

**增加数据**

```python
s1 = Student.objects.create(username="张三",  gender=0, age=18)
Teacher.objects.create(username="李老师", age=35, t_student=s1)
```

**查询数据**

```python
# 正向查询  从 带映射关系 的表 -> 其它表
# 查询老师对应的学生
Teacher.objects.get(id=1).t_student

# 反向查询 从 其它表 -> 带映射关系的表
# 查询学生对应的老师   此时使用关联模型类的类名小写
Student.objects.get(id=1).teacher
```

## 一对多关系

**创建模型**

```python
# 一个老师 对应 多个学生 
class Teacher(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()

# Teacher 类 需要放到 Student 类上边
class Student(models.Model):
    username = models.CharField(max_length=32)
    gender = models.IntegerField()
    age = models.IntegerField()
    # 创建一对多关系
    t_teacher = models.ForeignKey(to="Teacher",on_delete=models.CASCADE)
```

**增加数据**

```python
t1 = Teacher.objects.create(username="laoshi1",age=35)

Student.objects.create(username="zong",gender=1,age=18,t_teacher=t1)
Student.objects.create(username="zs",gender=1,age=20,t_teacher=t1)
```

**查询数据**

```python
# 正向查询
# 查询学生对应老师
name = Student.objects.get(id=2).t_teacher.username

# 反向查询
# 查询老师所有的学生  此处使用 关联模型类的类名小写_set
stu_list = Teacher.objects.get(id=1).student_set.all()
```

## 多对多关系

多对多关系需要第三张表（关系表）进行维护关系

**创建模型**

一个学生有多位老师，一个老师有多位学生

```python
class Teacher(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()

class Student(models.Model):
    username = models.CharField(max_length=32)
    gender = models.IntegerField()
    age = models.IntegerField()
    t_teacher = models.ManyToManyField(to=Teacher)
```

**增加数据**

```python
# 创建数据
Teacher.objects.create(username="李老师",age=35)
Teacher.objects.create(username="江老师",age=23)

Student.objects.create(username="zong",gender=1,age=18)
Student.objects.create(username="zs",gender=1,age=20)
Student.objects.create(username="lisi",gender=1,age=18)

# 添加关系
# add() 方法用于 多对多关系中两表之间添加关系
# 参数可以是 对象 或者 对象id ,不能位 queryset 类型
Student.objects.get(id=1).t_teacher.add(
        Teacher.objects.get(id=1),
        Teacher.objects.get(id=1)
)

Student.objects.get(id=1).t_teacher.add(
        1,2
)
```

**查询数据**

```python
# 正向查询
# 查询 学生 对应的老师
Student.objects.get(id=2).t_teacher.all()

# 反向查询
# 查询 老师 对应的学生
Teacher.objects.get(id=1).student_set.all()
```