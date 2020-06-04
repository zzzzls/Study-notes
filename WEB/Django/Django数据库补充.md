# 查看 ORM 对应的sql语句

```python
from django.db import connection

Student.objects.create(username="ss",gender=1,age=18)

print(connection.queries)

# [{'sql': 'INSERT INTO "test_app_student" ("username", "gender", "age") VALUES (\'ss\', 1, 18)', 'time': '0.095'}]
```

