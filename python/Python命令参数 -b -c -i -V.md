Python命令参数，提供了一些很有用的功能，可以方便调试和运行，可以通过 `python -h` 命令查看，以下列举一下常用的参数使用实例及场景。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318222400998.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MDc4OTky,size_16,color_FFFFFF,t_70)
# python -b
-b 参数，在 import 的时候，不产生 `pyc` 文件
```python
# a.py
def echo():
	pass

# b.py
from a import echo
echo()
```
使用 `python -b a.py` 就不会产生 pyc 文件

# python -c
-c 参数，直接运行 python语句，如：
```python
单行
python -c "print('hello')"

多行
python -c "import time;print('1');time.sleep(1);print('2')"
```

# python -i
-i 参数，运行完 python脚本文件后进入交互检查，可以方便查看运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318224401883.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MDc4OTky,size_16,color_FFFFFF,t_70)

# python -V
打印 python版本信息

# python -u
在 print记录时很有用，使用这个参数会强制 stdin ，stdout ，stderr 变为无缓冲的，会立刻输出，而不是等缓冲区满了才打印数据。比如以下代码：
```python
# filename = test.py
import time
for _ in range(10):
	time.sleep(1)
	print(_)
```
运行的时候重定向到一个文件
`python test.py > print.log`
会等到缓冲区满了，或者程序退出了才会真正写入到 print.log
这时候使用 `python -u test.py > print.log` 执行，就会每次 print 后立刻写入文件！
