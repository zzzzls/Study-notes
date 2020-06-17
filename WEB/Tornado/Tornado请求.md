# Tornado 请求

和 Django，flask 类似，Tornado 也提供了处理请求的方法

|属性|	说明|
|:---|:---|
|method|	请求类型|
|uri	|请求的路由|
|path|	请求中的路径|
|version|	http版本|
|headers	|请求头|
|body|	http请求的内容部分|
|remote_ip|	客户端ip|
|protocol|	请求协议，http https|
|host|	请求的主机|
|arguments|	请求的参数，GET和POST请求的参数|
|files|	请求的文件|


参考： [tornado HTTPServerRequest — Tornado 6.1.dev1 文档](https://www.osgeo.cn/tornado/httputil.html#tornado.httputil.HTTPServerRequest)