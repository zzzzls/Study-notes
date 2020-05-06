# CentOS 源代码编译安装 Python开发环境

以下命令，都在 root 用户下执行操作

## 1. 安装依赖

```bash
yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
```

## 2. 安装编译库

```bash
yum install -y gcc
```

## 3. 下载源代码文件

```bash
cd \opt
# 此处为下载 python3.7版本
wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz
```

## 4. 解压 & 配置

```bash
# 解压下载的 python源代码文件
tar -xzvf Python-3.7.7.tgz
cd Python-3.7.7

# 配置Python安装位置
./configure --prefix=/usr/local/python37
```

## 5. 编译安装

```bash
make && make install
```

## 6. 配置环境变量

```bash
# 打开配置文件
vim /etc/profile

# 文件末行，添加如下配置
export PATH=/usr/local/python37/bin:$PATH

# 使配置文件生效
source /etc/profile

# 测试
python3 -V
```

