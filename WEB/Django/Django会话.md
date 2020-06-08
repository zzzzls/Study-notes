# Cookie

**(1) cookie 设置**

```python
resp = HttpResponseRedirect("/index/")
resp.set_cookie("username",username)
resp.set_cookie("password",password)
return resp
```

**(2) cookie 获取**

```python
username = request.COOKIES.get("username")
```

**(3) cookie 删除**

还可以获取到 , 仅将 cookie 的 key 置为 空

```python
resp = HttpResponseRedirect("/index/")
resp.delete_cookie("username")
return resp
```

# session

Django 中的 session 是存储在数据库中的

**(1) session 的设置**

```python
request.session['username'] = "lisi"
```

**(2) session 的获取**

```python
request.session.get("username")
```

**(3) session 的删除**

```python
del request.session["username"]
```

**(4) session 的过期时间**

Django 中的 session 的默认有效期为 两周

Django 的 session 时间计算默认使用 UTC 时区，可以修改为 **上海时区**(不修改也不影响使用)

**修改 `settings.py`**

```python
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

# USE_TZ = True
USE_TZ = False
```

设置 session 有效期，单位 秒
`request.session.set_expiry(120)`
