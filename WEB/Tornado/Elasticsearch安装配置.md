<!-- TOC -->

- [Elasticsearch](#elasticsearch)
  - [安装 Elasticsearch](#安装-elasticsearch)
    - [创建用户](#创建用户)
    - [下载 Elsaticsearch 6.3](#下载-elsaticsearch-63)
    - [修改配置文件](#修改配置文件)
    - [配置系统参数](#配置系统参数)
    - [启动](#启动)
    - [测试访问](#测试访问)

<!-- /TOC -->

# Elasticsearch

当数据量很大时，使用 Mysql 全局检索数据耗时很大，成本很高。

**Elasticsearch 是一个分布式，可扩展，高实时的搜索与数据分析引擎**，它能很方便的使大量数据具有搜索，分析与探索的能力。利用 Elasticsearch 的水平伸缩性，能使数据在生产环境变得更有价值。

Elasticsearch 使用 Java 编写，是一个开源的实时的**分布式搜索引擎**，建立在一个全文搜索引擎库 Apache ， Lucene 基础之上。通过隐藏 Lucene 的复杂性，取而代之的提供一套简单一致的 **RESTful API**

Elasticsearch 的实现原理主要分为以下几个步骤：首先，将数据提交到 Elasticsearch 数据库中，在通过分词控制器去将对应的语句分词，将其权重和分词结果一并存入数据，当用户搜索数据时候，根据权重将结果排名，打分，再将结果呈现给用户

Elasticsearch 还可以用于结构化搜索，数据分析，复杂的人类语言处理，地理位置和对象间关联关系等。能够**胜任上百服务节点的扩展，并支持 PB 级别的结构化或者非结构化的数据**，让你以前所未有的速度和规模，去探索你的数据。

Elasticsearch 将所有的功能打包成一个单独的服务，这样你可以通过程序与它提供的简单的 API 进行通信，可以使用自己喜欢的编程语言充当 Web 客户端，甚至可以使用命令行（ 去充当这个客户端 ）

## 安装 Elasticsearch

**准备：**

- Ceantos 7 系统 ( 4G+ 内存 )
- Elsaticsearch 6.3.1

**安装：**

### 创建用户

```bash
# 创建新用户
adduser esuser

# 设置密码
passwd esuser
```

> 也可以使用其它用户，但是不能使用 root 用户启动 elasticsearch

### 下载 Elsaticsearch 6.3

下载地址：[Elsaticsearch 6.3](https://www.elastic.co/cn/downloads/past-releases/elasticsearch-6-3-1)

下载后解压至 `/home/esuser/` 目录下**

### 修改配置文件

修改 `/elasticsearch-6.3.1/config/elasticsearch.yml` *先备份*：

```bash
# 配置服务名称
cluster.name: my-application
# 节点配置
node.name: node-1
# 数据 与 日志 存储路径 （ 手动建立文件夹 ）
path.data: /home/esuser/es_data
path.logs: /home/esuser/es_logs
# 配置内存锁
tstrap.memory_lock: true
# 服务器 ip 和 端口 配置
network.host: 0.0.0.0
http.port: 9200
# 多节点配置
discovery.zen.ping.unicast.hosts: ["host1", "host2"]
gateway.recover_after_nodes: 1
action.destructive_requires_name: true
```

### 配置系统参数

(1) `vim /etc/security/limits.conf`

```bash
esuser hard nofile 65536
esuser soft nofile 65536
esuser soft memlock unlimited
esuser hard memlock unlimited
```

(2) `vi /etc/sysctl.conf`

```bash
vm.max_map_count = 262144
```

执行命令：

`sysctl -p`

(3) `visudo`

```bash
esuser    ALL=(ALL)       ALL
```

(4) `vi /etc/security/limits.d/90-nproc.conf`

```bash
soft nproc 204800
hard nproc 204800
```

(5) 给予目录权限

```bash
chown -R esuser elasticsearch-6.3.1
chown -R esuser es_data
chown -R esuser es_logs
```

(6) 关闭防火墙

### 启动

切换为 `esuser` 用户

进入 `/home/elasticsearch-6.3.1/bin/` 文件夹下

启动 `./elasticsearch`


### 测试访问

打开浏览器，访问 `IP:9200`，Elastic 会返回一个 JSON 对象，包含当前节点、集群、版本等信息
