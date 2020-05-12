  
  
- [操作系统概述](#操作系统概述 )
- [操作系统发展历程](#操作系统发展历程 )
- [Linux操作系统](#linux操作系统 )
  - [Linux发行版](#linux发行版 )
  - [Linux优点](#linux优点 )
- [CentOS操作系统](#centos操作系统 )
  - [文件目录详解](#文件目录详解 )
  - [学习阶段的初始化配置](#学习阶段的初始化配置 )
  
#  操作系统概述
  
  
操作系统 ( 简称 OS，Operating System )，安装部署在硬件上的一个系统如那件，负责应用软件和硬件信息之间的信息交互，完成应用软件的数据通过硬件进行存储、共享等作用。
  
![img][img@1]
  
#  操作系统发展历程
  
  
操作系统的逐步标准化过程:
  
![img][img@2]
  
#  Linux操作系统
  
  
**Linux** 是一种自由和开放源码的 [类UNIX操作系统](# )。该操作系统的内核由`林纳斯·托瓦兹`在 1991年10月5日 首次发布，在加上用户空间的应用程序之后，成为 Linux操作系统。Linux也是自由软件和开放源代码软件发展中最著名的例子。只要遵循 `GNU通用公共许可证（GPL）`，任何个人和机构都可以自由地使用 Linux的所有底层源代码，也可以自由地修改和再发布。
  
##  Linux发行版
  
  
**Linux发行版** 指的就是通常所说的 `Linux操作系统`，它一般是由一些组织、团体、公司或者个人制作并发行的。Linux内核 主要作为 Linux发行版的一部分而使用。通常来讲，一个 Linux发行版包括Linux内核，以及将整个软件安装到电脑上的一套安装工具，还有各种GNU软件，和其他的一些自由软件，在一些Linux发行版中可能会包含一些专有软件。发行版为许多不同的目的而制作，包括对不同电脑硬件结构的支持，对普通用户或开发者使用方式的调整，针对实时应用或嵌入式系统的开发等等。当前，超过三百个发行版被积极的开发，最普遍被使用的发行版有大约十二个。
  
|    系统     |              描述              |
| :---------: | :----------------------------: |
|   RedHat    |         小红帽操作系统         |
|   CentOS    |      小红帽的社区免费系统      |
|   Ubuntu    | 流行的桌面版操作系统，入门简单 |
|  MintLiunx  |     最好用的桌面版操作系统     |
| ElementryOS |      界面最漂亮的操作系统      |
  
##  Linux优点
  
  
- 开源，免费
- 跨平台的硬件支持
- 丰富的软件支持
- 多用户多任务
- 可靠的安全性
- 良好的稳定性
- 完善的网络功能
  
#  CentOS操作系统
  
  
**CentOS**（Community Enterprise Operating System）是Linux发行版之一，它是来自于 `Red Hat Enterprise Linux（RHEL）` 依照开放源代码规定发布的源代码所编译而成。由于出自同样的源代码，因此有些要求高度稳定性的服务器以 CentOS 替代商业版的 Red Hat Enterprise Linux 使用。两者的不同，在于CentOS 并不包含封闭源代码软件。CentOS 对上游代码的主要修改是为了移除不能自由使用的商标。2014年，CentOS宣布与Red Hat合作，但CentOS将会在新的委员会下继续运作，并不受RHEL的影响。
  
##  文件目录详解
  
  
|目录|描述|
|:---:|:---|
|/| 根目录|
|/bin|可执行二进制文件的目录|
|/boot|系统引导目录|
|/dev|存放Linux系统下的设备文件|
|/etc|系统配置文件存放目录|
|/home|系统默认的用户家目录|
|/lib|一些软件的依赖模块存放目录|
|/media|媒体目录|
|/mnt|光盘默认挂载点|
|/opt|第三方操作软件存放的目录|
|/proc|此目录的数据都在内存中，如系统核心，外部设备，网络状态，比较重要的目录|
|/root|系统管理员root的家目录|
|/sbin|放置系统管理员使用的可执行命令，如fdisk，shutdown，mount等|
|/srv|服务启动之后需要访问的数据目录|
|/tmp|系统临时文件存放的目录|
|/var|系统临时信息存放的目录，如系统日志|
  
  
##  学习阶段的初始化配置
  
  
安装好了 Centos 系统，为了更好的使用这个系统，需要进行一些使用前的配置操作
  
**1. 关闭防火墙**
  
CnetOS 系统中的防火墙，就是一个后台服务，所以关闭防火墙就是关闭服务！
在终端使用超级管理员 root，执行命令关闭
  
```bash
systemctl stop firewalld # 关闭防火墙
systemctl start firewalld # 开启防火墙
systemctl status firewalld # 查看防火墙状态
```
  
> CentOS 6 版本中的防火墙： iptables
> CentOS 7 版本中的防火墙： firewalld
  
输入上边的命令关闭之后，仅仅是本次关闭了，如果重启系统防火墙仍会自动开启，因此，我们需要 禁止 防火墙开机启动！
  
```bash
system disable firewalld # 关闭开机启动
system enable firewalld # 打开开机启动
```
  
**2. 配置静态 IP地址**
  
如果安装系统的时候自动配置联网规则，DHCP协议自动分配IP地址，有可能每次启动操作系统的时候 IP地址发生变化，需要我们在每次开机后查看 IP地址，确保后续的操作。
  
因此，我们可以使用 STATIC协议静态指定 IP地址，这样每次启动都是固定的 IP地址，有利于后续的操作！
  
使用 root 修改 `/etc/sysconfig/network-scripts/` 目录下的 `ifcfg-ens33`[?] 文件
  
```bash
# 原有内容尽量不变，新增如下内容
  
ONBOOT="yes" # 开机启动本配置
BOOTPROTO="static" # 设置为 static模式
IPADDR="192.168.0.106" # 指定固定的IP地址
NETMASK="255.255.255.0" # 指定子网掩码
GATEWAY="192.168.0.1" # 指定网关地址
DNS1="114.114.114.114" # 指定DNS服务器
```
  
使用 root 用户重启网络服务：
`systemctl restart network`
  
查看配置的 IP地址信息
`ifconfig`

[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/CentOS%E5%88%9D%E8%AF%86/04-28_01.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/CentOS%E5%88%9D%E8%AF%86/04-28_02.png
  