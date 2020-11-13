# Socket

**Socket** 又称 *套接字*，应用程序通常通过 `套接字` 向网络发出请求或者应答网络请求，使主机间或者一台计算机的进程间可以通讯



## 单工，半双工，全双工

-   单工

    单工就是指 A 只能发信号，而 B 只能接受信号，通信是单向的，类似 *收音机*



-   半双工

    两个事物都可以收发信号，但是不能同时进行

    类似一条窄窄的马路，同时只能有一辆车通过，如果两辆车对开，这种情况下就只能一辆车先过，等到头了另一辆车再开



-   全双工

    同个事物可以同时发送和接受信息

    举例：两个人互相打电话，你可以说也可以听，还可以两个人同时说（吵架的时候）



对于 Python 而言，同样支持 UDP 和 TCP 协议完成 **全双工，半双工 和 单工** 的网络通信

## socket() 函数

Python 中，我们用 `socket()`函数创建套接字，语法格式如下：

```python
socket.socket([family[, type[, proto]])
```

-   `family`：套接字家族可以使用 `AF_UNIX` 或者 `AF_INET`
-   `type`：套接字类型
    -   `SOCK_STREAM`：面向连接 TCP
    -   `SOCK_DGRAM`：面向非连接 UDP
-   `proto`：一般不填默认为 0



## Socket 对象方法

-   服务器端套接字

    | 函数         | 描述                                                         |
    | ------------ | ------------------------------------------------------------ |
    | `s.bind()`   | 绑定地址`（host,port）`到套接字， 在 `AF_INET`下，以元组`（host,port）`的形式表示地址。 |
    | `s.listen()` | 开始 TCP 监听。backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为 1，大部分应用程序设为 5 就可以了。 |
    | `s.accept()` | 被动接受 TCP 客户端连接, (阻塞式)等待连接的到来              |

    

-   客户端套接字

    | 函数             | 描述                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | `s.connect()`    | 主动初始化 TCP 服务器连接。一般 address 的格式为元组`（hostname,port）`，如果连接出错，返回 socket.error 错误。 |
    | `s.connect_ex()` | connect() 函数的扩展版本, 出错时返回出错码, 而不是抛出异常   |

    

-   公共用途套接字

    | 函数              | 描述                                                         |
    | ----------------- | ------------------------------------------------------------ |
    | `s.recv()`        | **接收 TCP 数据**，数据以字符串形式返回，bufsize 指定要接收的最大数据量。flag 提供有关消息的其他信息，通常可以忽略。 |
    | `s.send()`        | **发送 TCP 数据**，将 string 中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于 string 的字节大小。 |
    | `s.sendall()`     | **完整发送 TCP 数据**。将 string 中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回 None，失败则抛出异常。 |
    | `s.recvfrom()`    | **接收 UDP 数据**，数据没有收到之前一直处于阻塞状态，与 recv() 类似，但返回值是（data, address）。其中 data 是包含接收数据的字符串，address 是发送数据的套接字地址。 |
    | `s.sendto`        | **发送 UDP 数据**，将数据发送到套接字，address 是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。 |
    | `s.close()`       | 关闭套接字                                                   |
    | `s.getpeername()` | 返回连接套接字的远程地址。返回值通常是元组（ipaddr, port）   |
    | `s.getsockname()` | 返回套接字自己的地址。通常是一个元组 ( ipaddr, port)         |



## UDP 实例

-   UDP 发送数据

    ```python
    import socket
    
    # 创建 socket 对象
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 绑定本地信息
    # 此处若不绑定端口,则每次执行时由操作系统个随机分配端口
    udp_sock.bind(('', 7890))
    
    # 发送数据
    udp_sock.sendto('这个是udp的数据'.encode(), ('10.10.34.140', 8080))
    
    # 关闭连接
    udp_sock.close()
    ```



-   UDP 接收数据

    ```python
    import socket
    
    # 创建 socket 对象
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 绑定本地信息
    udp_sock.bind(('10.10.34.10', 8080))
    
    # 接收数据
    recv_data = udp_sock.recvfrom(1024)
    print(recv_data)
    
    # 关闭
    udp_sock.close()
    ```

    













































