<!-- TOC -->

- [Elastic](#elastic)
- [基本概念](#基本概念)
  - [Node 与 Cluster](#node-与-cluster)
  - [Index](#index)
  - [Type](#type)
  - [Document](#document)
- [索引操作](#索引操作)
  - [新建 & 删除 Index](#新建--删除-index)
  - [新建 Index 同时 设置 Type](#新建-index-同时-设置-type)
  - [查看索引](#查看索引)
- [插入数据](#插入数据)
- [检索数据](#检索数据)
  - [精确查询](#精确查询)
  - [多条件查询](#多条件查询)
  - [查询所有](#查询所有)
  - [分页查询](#分页查询)
  - [排序](#排序)

<!-- /TOC -->

# Elastic

Elastic 可以类似数据库进行学习

|关系型数据库|database|table|rows|column|
|:---|:---|:---|:---|:---|
|Elastic|index(索引)|Type(类型)|Document(文档)|fileds|

关系型数据库只能存储基本的数据类型，如果需要存储复杂的数据，就需要关联表 ( 一对一，一对多，多对多 )

![img][img@1]

Elastic 可以存储更加复杂的数据类型

```json
{
    "name": "tom",
    "age": 18,
    "img": [
        "xx1.jpg",
        "xx2.jpg",
        "xx3.jpg"
    ]
}
```

# 基本概念

## Node 与 Cluster

Elastic 本质上是一个分布式数据库，允许多态服务器协同工作，每台服务器可以运行多个 Elastic 实例

单个 Elastic 实例 称为一个节点 ( node )，一组节点构成一个集群 ( cluster )

## Index

Elastic 会索引所有字段，经过处理后写一个反向索引 ( Inverted Index )，查找数据的时候，直接查找该索引

所以，Elastic 数据管理的顶层单位就叫做 Index ( 索引 )。它是单个数据库的同义词，每个 Index ( 即数据库 ) 的名字必须是小写

## Type

> 根据规划，Elastic 6.x 版只允许每个 Index 包含一个 Type，7.x 版将会彻底移除 Type

例如 weather 这个 Index 里面，可以按城市分组（ 北京和上海 ），也可以按气候分组（晴天和雨天）。这种分组就叫做 Type，它是虚拟的逻辑分组。

不同的 Type 应该有相似的结构（ schema ），举例来说，id 字段不能在这个组是字符串，在另一个组是数值。这是与关系型数据库的表的一个区别。性质完全不同的数据（ 比如products和logs ）应该存成两个 Index，而不是一个 Index 里面的两个 Type（虽然可以做到）。

## Document

Index 里面的单条记录称为 Document ( 文档 )，许多条 Document 构成了一个 Index

Document 使用 JSON 格式表示，例如：

```json
{
    "name": "tom",
    "age": 18,
    "img": [
        "xx1.jpg",
        "xx2.jpg",
        "xx3.jpg"
    ]
}
```

# 索引操作

## 新建 & 删除 Index

新建 Index，可以直接向 Elastic 服务器发出 PUT 请求，下面是创建一个名叫 **carlist** 的 Index

```bash
curl -X PUT 'localhost:9200/carlist'
```

服务器返回一个 JSON 对象，里边的 `acknowledged` 字段表示操作成功

```json
{
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "carlist"
}
```

然后我们发出 DELETE 请求，删除这个 Index

```bash
curl -X DELETE 'localhost:9200/carlist'
```

## 新建 Index 同时 设置 Type

```bash
curl -X PUT 'http://192.168.0.105:9200/carlist' \
--header 'Content-Type: application/json' \
--data '{
    "mappings": {
        "car": {
            "properties": {
                "c_name": {
                    "type": "text"
                },
                "c_date": {
                    "type": "date",
                    "format": "yyyy-MM-dd"
                },
                "c_mileage": {
                    "type": "float"
                }
            }
        }
    }
}'
```

上面代码中，首先新建一个名为 `carlist` 的 Index(索引)，里面有一个名称为 `car` 的 Type(类型)，`car` 有三个字段：

c_name 字段类型为 **text(文本)**  
c_date 字段类型为 **date(日期)**，需要指明日期格式
c_mileage 字段类型为 **float**

**常用字段类型：**

![img][img@2]


## 查看索引

(1) 查看所有索引
```bash
curl -X GET 'localhost:9200/_cat/indices'

# 返回结果
yellow open carlist OlyQWbmYQp2TEXroOXSfkA 5 1 0 0 1.1kb 1.1kb
```

- yellow 代表当前索引的状态，蓝色： 代表健康，黄色代表警告，红色代表错误
- open 代表 索引开启，close 关闭的状态
- carlist 代表存在的索引的名字

(2) 查看指定索引

```bash
curl -X get 'http://192.168.0.105:9200/索引名'
```

# 插入数据

请求方式 `POST`  
请求地址 `ip:9200/索引/类型`  
请求数据 `要插入的 JSON 数据`  

```bash
curl -X POST 'http://192.168.0.105:9200/carlist/car' \
--header 'Content-Type: application/json' \
--data '{
    "c_name":"大奔",
    "c_date":"2020-06-17",
    "c_mileage":"20.0"
}'
```

> 如果没有创建 Index , 直接执行上面的命令 , Elastic 也不会报错 , 而是直接生成指定的 Index , 所以,打字时需要小心 , 不要写错 Index 的名字

# 检索数据

## 精确查询

请求方式 `GET`
请求地址 `ip:9200/索引/_search`
请求数据 `要查找的数据`

```bash
curl --request GET 'http://192.168.0.105:9200/carlist/_search' \
--header 'Content-Type: application/json' \
--data '{
    "query":{
        "term":{
            "c_name":"宝"
        }
    }
}'
```


## 多条件查询

## 查询所有

## 分页查询

## 排序




[img@1]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/Tornado/06-17_3288.png
[img@2]:https://raw.githubusercontent.com/zzzzls/Images/master/Study_nodes_img/Tornado/06-17_1.jpg