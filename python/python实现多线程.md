<!-- TOC -->

- [Python 实现多线程](#python-%e5%ae%9e%e7%8e%b0%e5%a4%9a%e7%ba%bf%e7%a8%8b)
  - [基于函数实现多线程](#%e5%9f%ba%e4%ba%8e%e5%87%bd%e6%95%b0%e5%ae%9e%e7%8e%b0%e5%a4%9a%e7%ba%bf%e7%a8%8b)
  - [基于类实现多线程](#%e5%9f%ba%e4%ba%8e%e7%b1%bb%e5%ae%9e%e7%8e%b0%e5%a4%9a%e7%ba%bf%e7%a8%8b)
  - [线程中的属性](#%e7%ba%bf%e7%a8%8b%e4%b8%ad%e7%9a%84%e5%b1%9e%e6%80%a7)
  - [守护线程](#%e5%ae%88%e6%8a%a4%e7%ba%bf%e7%a8%8b)
  - [资源独占](#%e8%b5%84%e6%ba%90%e7%8b%ac%e5%8d%a0)
  - [多线程数据冲突](#%e5%a4%9a%e7%ba%bf%e7%a8%8b%e6%95%b0%e6%8d%ae%e5%86%b2%e7%aa%81)
    - [互斥锁](#%e4%ba%92%e6%96%a5%e9%94%81)
    - [死锁](#%e6%ad%bb%e9%94%81)
    - [GIL全局解释器锁](#gil%e5%85%a8%e5%b1%80%e8%a7%a3%e9%87%8a%e5%99%a8%e9%94%81)
- [more an more](#more-an-more)

<!-- /TOC -->

# Python 实现多线程

在 Python中，实现多线程的模块叫做 threading，是 Python自带的模块。

## 基于函数实现多线程

```python
from threading import Thread

# 创建线程 基于函数
t1 = Thread(taget=函数名称,args=(参数,))
# 启动线程
t1.start()
```

## 基于类实现多线程

```python
from threading import Thread

# 自定义类 继承自 Thread
class MyThread(Thread):
    def run(self):
        # 固定语法格式，当线程类对象启动start() 方法时自动调用执行该方法
        pass

# 创建线程对象
t1 = MyThread()
# 启动线程
t1.start()
```

> 基于类的多线程的构建方法，创建好线程对象，必须调用start() 方法，千万不要直接调用 run() 方法
> 如果通过对象调用执行 run() 方法，不会创建新的线程，只会将 run()方法当成实例方法去执行


## 线程中的属性

1. 获取当前线程

```python
threading.current_thread()
```

2. 多线程名称

```python
# 对象 - 设置名称
obj.name = "自定义名称"
obj.setName("自定义名称")

# 对象 - 获取名称
obj.name
obj.getName()

# 获取当前线程名称
threading.current_thread().name
```

3. 判断线程是否存活

```python
# 通过对象判断当前线程是否存活
ogj.is_alive()
```

4. 访问当前所有线程

```python
for t in threading.enumerate():
    print(t.getName())
```

## 守护线程

在线程中有一个叫做**守护线程**的概念，如果一下线程被设置为守护线程，那么意味这个线程是不重要的。这意味着，如果主线程结束了而该守护线程还没有运行完，那么它会被强制结束。在 Python中我们可以通过 `setDaemon` 方法来将某个线程设置为守护线程。

```python
# 创建线程
t1 = Thread(target=run)
# 设置守护线程
t1.setDaemon(True)
# 启动线程
t1.start()
```

> 大部分软件，主线程如果需要结束，子线程（不论子线程是否在运行）必须结束运行，如 退出QQ时，正在来哦天的窗口，正在视频的窗口，所有和 QQ有关的窗口必须全部关闭！

## 资源独占

某些情况下，一个子线程运行时优先级较高，所以需要分配更多的资源主要支持这个优先的进程，此时可以设置线程独占运行模式，通过调用线程的 join() 方法启动独占模式

```python
t1.start()
# 设置 t1 线程独占资源 ，当 t1 线程执行完毕，才会执行其它线程
t1.join()

======================
t1.start()
# 设置 t1 线程独占资源 5 秒
t1.join(5)
```

## 多线程数据冲突

在一个线程中的多个线程是共享资源的，比如在一个进程中，有一个全局变量 count用来计数，现在我们声明多个线程，每个线程运行时都给 count 加 1

```python
import threading
import time

count = 0

def add():
    global count
    temp = count + 1
    time.sleep(0.001)
    count = temp

if __name__ == "__main__":
    thread_list = []

    for i in range(1000):
        thread = threading.Thread(target=add)
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

print(count)
```

在这里，我们声明了 1000 个线程，每个线程都是现取到当前的全局变量 count 值，然后休眠一小段时间，然后对 count 赋予新的值。

按照常理来说，最终 count 的值应该为 1000，但其实不然，运行结果为 56

最后的结果居然只有 56 ，而且多次运行或者换个环境运行结果是不同的。

这是为什么呢？因为 count 这个值时共享的，每个线程都可以在执行 `temp = count + 1` 这行代码时拿到当前 count 的值，但是这些线程中的一些线程可能是并发或者并行执行的，这就导致不同的线程拿到的可能是同一个 count 的值，最后导致有些线程的 count 的加1操作并没有生效，导致最后的结果偏小。

所以，如果多个线程同时对某个数据进行读取或修改，就会出现不可预料的结果。为了避免这种情况，我们需要对多个线程进行同步，要实现同步，我们可以对需要操作的数据进行加锁保护，这里就需要用到 threading.Lock 了。

### 互斥锁

互斥锁是什么意思呢？就是说，某个线程在对数据进行操作前，需要先加锁，这样其它的线程发现了被加锁了之后，就无法继续向下执行，会一直等待锁被释放，只有加锁的线程把锁释放了，其它的线程才能继续加锁并对数据做修改，修改完了再释放锁。这样可以确保同一时间只有一个线程操作数据，多个线程不会再同时读取和修改同一个数据，这样最后的运行结果就是正确的了！

```python
# 引入锁
from threading import Lock
# 创建锁对象
lock = Lock()

# 上锁
lock.acquire()

访问修改共享数据的代码

# 解锁
lock.release()
```

> 上锁和解锁：将锁定的数据尽量控制再一个较小的共享数据访问范围中，这样才能尽量不影响多任务执行效率

### 死锁

锁在使用过程中对于数据的保护非常明显，但是某些时刻一定要注意避免死锁

由于在程序中出现了多个数据互斥锁，互相锁定对方的数据，导致程序挂死/假死（程序运行到一定阶段，等待获取数据时发现数据被锁定了，此时就会进入持续等待状态，如果锁定的数据不释放程序就会假死）

死锁不是一定会出现的，而是在多个锁的程序中，在某个时间片切换过程中可能发成

### GIL全局解释器锁

由于 Python 中 GIL 的限制，导致不论是在单核还是在多核条件下，在同一时刻只能运行一个线程，导致 Python多线程无法发挥多核并行的优势。

GIL 全称 Global Interpreter Lock，中文翻译为 全局解释器锁，其最初设计是出于数据安全而考虑的。

在 Python多线程下，每个线程的执行方式如下：

- 获取 GIL
- 执行对应线程的代码
- 释放 GIL

可见，某个线程想要执行，必须先拿到 GIL，我们可以把 GIL 看作是通行证，并且在一个 Python进程中，GIL只有一个。拿不到通行证的线程，就不允许执行。这样就导致，即使在多核条件下，一个 Python进程下的多个线程，同一时刻也只能执行一个线程。

# more an more

<https://docs.python.org/zh-cn/3.7/library/threading.html#module-threading>





