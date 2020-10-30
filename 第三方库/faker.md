在软件需求，开发，测试过程中，有时候需要使用一些测试数据，针对这种情况，我们一般要么使用已有的系统数据，要么手动制造一些数据。

现在好了，有一个 Python 包能够协助你完成这方面的工作

### 什么是 Faker

Faker 是一个 Python 包，开源的 Github 项目，只需要调用 Faker 提供的方法，即可完成数据的生成。

>   项目地址: [https://github.com/joke2k/faker](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fjoke2k%2Ffaker)



### 安装 Faker

>   pip install faker



### Faker 的使用



#### 命令行语法

安装好了之后，可以在 CMD 或者 shell 中通过 faker 命令来调试，具体如下：

```
faker [-h] [--version] [-o output]
      [-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}]
      [-r REPEAT] [-s SEP]
      [-i {package.containing.custom_provider otherpkg.containing.custom_provider}]
      [fake] [fake argument [fake argument ...]]
```

**参数说明**

-   `faker`：环境中安装的脚本名称，在开发中，可以使用 `python -m faker`
-   `-h`：显示帮助信息
-   `--version`：显示程序的版本号
-   `-o FILENAME`：将输出重定向到指定文件中
-   `-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}`：生成本土化的数据
-   `-r REPEAT`：生成指定数量的结果
-   `-s SEP`：以特定的分隔符分割多个结果
-   `fake`：生成的伪数据的类别，例如 name ，address，text



**示例**

```bash
faker address
# 4876 Gallegos Vista Apt. 382
# Lake Christine, VA 92929

faker -l zh_CN name
# 钟晶

faker -l zh_CN -r 3 address
# 北京市浩县永川钱路r座 446453
# 安徽省峰县南长李街s座 859863
# 内蒙古自治区关岭市龙潭惠州街q座 586090
```



#### 在 Python 中使用

```python
from faker import Faker

# 初始化 指定语言环境,以返回本土化数据,默认为 en_US
f = Faker(locale='zh_CN')
```



**常用方法**

>   以下内容以 zh_CN 和 zh_TW 为准



-   **地理信息类**

    | 方法名           | 描述     |
    | ---------------- | -------- |
    | `city_suffix()`  | 市，县   |
    | `country()`      | 国家     |
    | `country_code()` | 国家编码 |
    |                  |          |