## 本地git仓库上传到github账户操作
    zhanghe@ubuntu:~/code/python$ ssh-keygen -t rsa -C "zhang_he06@163.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/zhanghe/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/zhanghe/.ssh/id_rsa.
    Your public key has been saved in /home/zhanghe/.ssh/id_rsa.pub.
    The key fingerprint is:
    fa:a0:f5:f5:8f:f1:17:3b:5c:8d:e4:5d:ec:b5:16:8c zhang_he06@163.com
    The key's randomart image is:
    +--[ RSA 2048]----+
    |                 |
    |                 |
    |              o. |
    |             E.o+|
    |        S    o +*|
    |       .      o+=|
    |      +   . . o +|
    |     o + . . + +.|
    |    .   o   o.o..|
    +-----------------+
    zhanghe@ubuntu:~/code/python$ gedit /home/zhanghe/.ssh/id_rsa.pub
    # 复制公钥，进入https://github.com/settings/ssh
    # Personal settings >> SSH keys >> add SSH key >> 粘贴保存
    zhanghe@ubuntu:~/code/python$ git remote add origin git@github.com:zhanghe06/python.git
    fatal: 远程 origin 已经存在。
    zhanghe@ubuntu:~/code/python$ git remote rm origin
    zhanghe@ubuntu:~/code/python$ git remote add origin git@github.com:zhanghe06/python.git
    zhanghe@ubuntu:~/code/python$ git branch -a
    * master
    zhanghe@ubuntu:~/code/python$ git push -u origin master
    Counting objects: 1457, done.
    Compressing objects: 100% (1381/1381), done.
    Writing objects: 100% (1457/1457), 9.25 MiB | 24.00 KiB/s, done.
    Total 1457 (delta 225), reused 0 (delta 0)
    To git@github.com:zhanghe06/python.git
     * [new branch]      master -> master
    分支 master 设置为跟踪来自 origin 的远程分支 master。
    zhanghe@ubuntu:~/code/python$ git branch -a
    * master
      remotes/origin/master


## 程序所需依赖
    进入虚拟环境
    zhanghe@ubuntu:~/code/python$ source pyenv/bin/activate
    
    查看虚拟环境依赖
    (pyenv)zhanghe@ubuntu:~/code/python$ pip freeze
    Pillow==2.8.1
    argparse==1.2.1
    backports.ssl-match-hostname==3.4.0.2
    certifi==14.05.14
    cssselect==0.9.1
    gevent==1.0.1
    greenlet==0.4.5
    lxml==3.4.2
    pyasn1==0.1.7
    pyquery==1.2.9
    pytesseract==0.1.6
    requests==2.5.0
    rsa==3.1.4
    tornado==4.1
    wsgiref==0.1.2
    
    导出依赖库
    (pyenv)zhanghe@ubuntu:~/code/python$ pip freeze > requirements.txt


## 测试环境部署
    建立 虚拟环境
    virtualenv pyenv

    进入 虚拟环境
    source pyenv/bin/activate

    安装依赖库
    pip install -r requirements.txt

    离开 虚拟环境
    deactivate


## ubuntu下python 图片识别pytesseract安装记录

    Pillow 是 PIL 的替代版本

    仅仅 pip install Pillow 是不够的

    安装依赖
    $ sudo apt-get install libjpeg-dev
    $ sudo apt-get install libfreetype6-dev
    重新编译：
    $ pip install -I Pillow
    或者重装PIL：
    $ pip uninstall Pillow
    $ pip install Pillow

    检查系统是否已经安装依赖库：
    $ ldconfig -p | grep libpng
    $ ldconfig -p | grep libjpeg
    $ ldconfig -p | grep libtiff

    检查/usr/lib目录下的扩展
    $ cd /usr/lib
    /usr/lib$ ls -l |grep libjpeg
    如果没有，需要创建软连接
    先查找扩展的路径和文件名：
    $ ldconfig -p | grep libjpeg
    创建软链：
    $ sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so.8 /usr/lib/
    重新编译：
    $ pip install -I Pillow

    --------------------------------------------------------------------
    PIL SETUP SUMMARY
    --------------------------------------------------------------------
    version      Pillow 2.8.1
    platform     linux2 2.7.6 (default, Mar 22 2014, 22:59:38)
                 [GCC 4.8.2]
    --------------------------------------------------------------------
    *** TKINTER support not available
    --- JPEG support available
    *** OPENJPEG (JPEG2000) support not available
    --- ZLIB (PNG/ZIP) support available
    *** LIBTIFF support not available
    *** FREETYPE2 support not available
    *** LITTLECMS2 support not available
    *** WEBP support not available
    *** WEBPMUX support not available

    可以看出来已经支持JPEG了。

    pytesser 调用了 tesseract，因此需要安装 tesseract，
    安装 tesseract 需要安装 leptonica，
    否则编译tesseract 的时候出现 "configure: error: leptonica not found"。

    leptonica
    https://code.google.com/p/leptonica/downloads/list
    下载：leptonica-1.69.tar.gz

    tesseract-ocr
    https://code.google.com/p/tesseract-ocr/downloads/list
    下载：tesseract-ocr-3.02.02.tar.gz

    编译安装过程，进入解压后的目录，进行如下操作：
    $ sudo ./configure
    $ sudo make
    $ sudo make install

    如果去掉sudo，会报错：
    Permission denied

    记录一下，make过程太长了，看有没有解决办法。

    安装pytesseract
    $ pip install pytesseract

    运行测试程序
    报错：
    pytesseract.pytesseract.TesseractError: (127, 'tesseract: error while loading shared libraries: libtesseract.so.3: cannot open shared object file: No such file or directory')

    $ whereis libtesseract

    $ sudo ln -s /usr/local/lib/libtesseract.so /usr/lib/libtesseract.so.3

    $ sudo ln -s /usr/local/lib/liblept.so /usr/lib/liblept.so.3

    又报错
    (1, 'Error opening data file /usr/local/share/tessdata/eng.traineddata')
    是因为语言包没有安装

    tesseract-ocr语言包
    https://code.google.com/p/tesseract-ocr/downloads/list
    下载：tesseract-ocr-3.02.eng.tar.gz
    解压将tessdata目录下的文件（9个）拷贝到 "/usr/local/share/tessdata"目录下
    $ sudo cp eng.* /usr/local/share/tessdata

    python测试代码：

    # encoding: utf-8
    __author__ = 'zhanghe'
    from PIL import Image
    import pytesseract
    print(pytesseract.image_to_string(Image.open('test.jpg')))



## 模拟登录相关

Requests

    HTTP库，Requests 使用的是 urllib3，因此继承了它的所有特性。比Python 标准库中的 urllib 模块api简单
    http://cn.python-requests.org/zh_CN/latest/
    [高级用法]http://cn.python-requests.org/zh_CN/latest/user/advanced.html#advanced

Tornado

    用Python语言写成的Web服务器(非阻塞)兼Web应用框架
    http://demo.pythoner.com/itt2zh/index.html

Pyquery

    一个类似于jQuery的Python库
    https://pythonhosted.org/pyquery/api.html#module-pyquery.pyquery
    安装顺序：libxml2 \libxslt \lxml \pyquery

Gevent

    gevent是一个基于libev的并发库
    [英文原版]http://sdiehl.github.io/gevent-tutorial/
    [中文指南]http://xlambda.com/gevent-tutorial/


Gevent安装过程

    $ sudo apt-get install libevent-dev
    $ sudo apt-get install python-dev
    $ pip install greenlet
    $ pip install gevent

lxml安装过程

    使用：$ sudo apt-get install libxml2 libxml2-dev 安装 libxml2
    使用：$ sudo apt-get install libxslt1.1 libxslt1-dev 安装 libxslt
    安装 python-libxml2 和 python-libxslt1 ：
    $ sudo apt-get install python-libxml2 python-libxslt1
    $ pip install lxml
    （注意：虚拟环境下pip install不要sudo，否则会有提示：Requirement already satisfied (use --upgrade to upgrade): lxml in /usr/lib/python2.7/dist-packages
    ）
    安装完lxml之后，即可安装pyquery
    $ pip install pyquery

Tornado安装

    $ pip install tornado


## python

一、Python 禅道

    >>> import this

    美丽优于丑陋。
    明确优于含蓄。
    简单比复杂好。
    平倘优于嵌套。
    稀疏比密集更好。
    特殊情况不能特殊到打破规则。
    错误不应该默默传递。
    ......


二、代码风格

    PEP 8: Python 代码风格指南
    https://www.python.org/dev/peps/pep-0008/

    [空格]

    使用 4 个空格缩进。
    不要使用制表符。
    不要将制表符和空格混合使用。
    在使用 字典(dict), 列表(list), 元组(tuple), 参数(argument)列表时， 应在 "," 后添加一个空格,
    并且使用字典(dict)时，在 ":" 号后添加空格，而不是在前面添加。
    在括号之前或参数之前不添加空格。
    在文档注释中前后应该没有空格。

    [空行]

    每一个 Class 之间应该有两个空行。
    每个函数之间应该有一个空行。

    [命名]
    使用驼峰命名法命名类名
    使用下划线分隔方式命名方法或者函数


三、数据类型

    Python提供的基本数据类型主要有：布尔类型、整型、浮点型、字符串、列表、元组、集合、字典等等

    1、空（None）
    表示该值是一个空对象，空值是Python里一个特殊的值，用None表示。
    None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

    2、布尔类型（Boolean）

    3、整型(Int)

    4、浮点型(Float)

    5、字符串(String)

    6、列表(List)
    用符号[]表示列表，中间的元素可以是任何类型，用逗号分隔。
    List类似C语言中的数组，用于顺序存储结构（即列表的元素是有序的，但不必是唯一的）
    List的切片 list[m:n]表示返回一个新的列表，第m个元素到第n个元素，但是不包含第n个元素
    有append、insert、extend等方法来操作列表

    7、元组(Tuple)
    使用圆括号()表示
    元组是和列表相似的数据结构，但它一旦初始化就不能更改，速度比list快
    同样可以向List那样执行切片操作，来获得一个新的元组
    元组没有方法，不能对其进行添加、删除、修改，
    但是可以通过 in 关键字来判断某个元素是否存在于元组中
    以及通过index方法来查找某个元素的位置

    8、集合(Set)
    集合是无序的，不重复的元素集

    9、字典(Dict)
    字典是一种无序存储结构，字典的格式为：dictionary = {key: value}

四、控制语句

    pass
    空语句 do nothing
    保证格式完整
    保证语义完整
    充当占位符使用

    例子：可以（预）定义一个空函数



## 反向代理

    user nginx;
    worker_processes 5;
    
    error_log /var/log/nginx/error.log;
    
    pid /var/run/nginx.pid;
    
    events {
        worker_connections 1024;
        use epoll;
    }
    
    proxy_next_upstream error;
    
    upstream tornadoes {
        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
        server 127.0.0.1:8002;
        server 127.0.0.1:8003;
    }
    
    server {
        listen 80;
        server_name www.example.org *.example.org;
    
        location /static/ {
            root /var/www/static;
            if ($query_string) {
                expires max;
            }
        }
    
        location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://tornadoes;
        }
    }

## Supervisor(Supervisor是一个进程监控程序)

安装Supervisor

    $ sudo pip install supervisor

生成配置文件(supervisord.conf)

    $ sudo su
    # echo_supervisord_conf > /etc/supervisord.conf

修改配置文件(/etc/supervisord.conf)
    
    [group:tornadoes]
    programs=tornado-8000,tornado-8001,tornado-8002,tornado-8003
    
    [program:tornado-8000]
    command=python /var/www/main.py --port=8000
    directory=/var/www
    user=www-data
    autorestart=true
    redirect_stderr=true
    stdout_logfile=/var/log/tornado.log
    loglevel=info
    
    [program:tornado-8001]
    command=python /var/www/main.py --port=8001
    directory=/var/www
    user=www-data
    autorestart=true
    redirect_stderr=true
    stdout_logfile=/var/log/tornado.log
    loglevel=info
    
    [program:tornado-8002]
    command=python /var/www/main.py --port=8002
    directory=/var/www
    user=www-data
    autorestart=true
    redirect_stderr=true
    stdout_logfile=/var/log/tornado.log
    loglevel=info
    
    [program:tornado-8003]
    command=python /var/www/main.py --port=8003
    directory=/var/www
    user=www-data
    autorestart=true
    redirect_stderr=true
    stdout_logfile=/var/log/tornado.log
    loglevel=info


启动服务

    $ sudo supervisord
    或
    $ sudo supervisord -c /etc/supervisord.conf

启动supervisor的命令行窗口

    $ sudo supervisorctl
    tornadoes:tornado-8000           RUNNING    pid 969, uptime 0:00:58
    tornadoes:tornado-8001           RUNNING    pid 970, uptime 0:00:58
    tornadoes:tornado-8002           RUNNING    pid 971, uptime 0:00:58
    tornadoes:tornado-8003           RUNNING    pid 972, uptime 0:00:58
    supervisor>

修改配置后需要重新读取（或加载）配置

    $ sudo supervisorctl reread
    或
    $ sudo supervisorctl reload

更新状态

    $ sudo supervisorctl update

## 关于建站

云服务器带宽选择

    网站的带宽/8=同时访问数*平均页面大小
    1Byte=8bit
    1Mbps带宽，理论下每秒可以下载的文件大小约是128KB每秒。
    个人网站使用，一般1M起步都可以。
    如果是企业网站特别是有业务运营的云服务器，
    如淘宝品牌、企业电子商务平台、企业微信平台网站、微客来之类的网站，都推荐带宽选择3M-5M起。

框架选择

    世上没有最好的框架，只有最适合你自己、最适合你的团队的框架。
    在没有一定的访问量前谈性能其实是没有多大意义的，因为你的CPU和内存一直就闲着呢。
    而且语言和框架一般也不会是性能瓶颈，性能问题最常出现在数据库访问和文件读写上。


## 踩过的坑

### requests的乱码问题
```
是由于运行环境中缺少一个叫chardet的用于探测字符集的第三库导致的
chardet自称是一个非常优秀的编码识别模块
有人说这个第三方库也不怎么靠谱。
还有一种观点：
requests的编码检测是不符标准的，他有两个编码，一个是http head里面的编码，另一个是依据网页body的编码。
标准是网页内容声明的编码优先于http头的编码，requests没有做这个考虑，总是使用head里面的编码。
在head和body编码声明不一致时可能出现编码错误。
解决方案有三种（前两种Requests文档有提过，但没明确指明是解决这类问题）：
第一：直接用response.content以二进制字节的方式访问请求响应体；（推荐）
第二：改变Requests使用其推测的文本编码，response.encoding = 'utf-8' 再获取解码内容 response.text
第三：把requests的models.py给hack一下，写出自己的一套检测字符集的function。
```
```
说明一点，网上很多错误观点认为乱码与Accept-Encoding有关
header['Accept-Encoding'] = 'gzip, deflate, sdch'
纯属扯淡，Requests会自动为你解码 gzip 和 deflate 传输编码的响应数据。
```
```
如果保存文件的编码与文档定义的编码一致，还是乱码，需要删除这个文件，再次保存。
```

参考：
[python 模块 chardet](http://pypi.python.org/pypi/chardet "python 模块 chardet")


### pip安装第三方库报错

安装过程报错的解决办法
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 49:
由于是在虚拟环境中安装
先找到虚拟目录下的lib/python2.7/site.py文件
/home/zhanghe/code/project/env/lib/python2.7/site.py
```
def setencoding():
    """Set the string encoding used by the Unicode implementation.  The
    default is 'ascii', but if you're willing to experiment, you can
    change this."""
    encoding = "ascii"  # Default value set by _PyUnicode_Init()
    if 0:  # 改成 if 1 (只修改第一个if 0 为 if 1)
```
if 0 改成 if 1 (只修改第一个if 0 为 if 1)


## Python MySQLdb

Python interface to MySQL

测试安装状态
```
zhanghe@ubuntu:~$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import MySQLdb
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named MySQLdb
>>> 
```

apt方式安装
```
$ apt-cache search python-mysqldb
$ sudo apt-get install python-mysqldb
```

pip方式安装（虚拟环境推荐这种方式）
```
$ pip search MySQL-python | grep MySQL
$ sudo pip install MySQL-python
```

再次测试安装状态，不报错即可

如果报错 EnvironmentError: mysql_config not found
执行以下命令（可惜没有成功）
```
$ sudo apt-get install libmysqlclient-dev python-dev
```
原因：安装的是 mariadb 服务，所以需要安装：
```
$ sudo apt-get install libmariadbclient-dev
```
如果没有安装mysql/mariadb服务，还需要提前安装:
```
$ sudo apt-get install libmysqld-dev
or
$ sudo apt-get install libmariadbd-dev
```


说明：
python版本的MySQL库（不建议使用这个）
```
$ sudo pip install PyMySQL
```

生产环境推荐导入模块方式
```
try:
    import MySQLdb
except ImportError:
    import pymysql
```


## Python PostgreSQL

[PostgreSQL官网](http://www.postgresql.org/)

服务安装
```
$ apt-cache search postgresql
$ sudo apt-get install postgresql
```

PostgreSQL管理工具(客户端)安装
```
$ sudo apt-get install pgadmin3
```
pgadmin3已经包含了postgresql-client


驱动的安装
```
$ sudo apt-get install python-dev
$ sudo apt-get install libpq-dev
$ sudo pip install psycopg2
```

终端使用
```
# 切换到Linux下postgres用户
$ sudo su postgres
或者
$ sudo su - postgres
# Mac下切换
$ sudo su _postgres
# 登录postgres数据库
$ psql postgres
# 提示如下：
psql (9.3.9, server 9.3.10)
Type "help" for help.
postgres=# 
```

使用终端命令完成新建用户dbuser和数据库exampledb
```
# 切换到Linux下postgres用户
$ sudo su - postgres
# 查看createuser的帮助
$ createuser --help
# 创建数据库用户dbuser，并指定其为超级用户
$ createuser --superuser dbuser
# 登录数据库控制台，设置dbuser用户的密码，完成后退出控制台
$ psql
postgres=# \password dbuser
postgres=# \q（可以直接按ctrl+D）
# 创建数据库exampledb，并指定所有者为dbuser
$ createdb -O dbuser exampledb
```

服务指令
```
# 查看状态
$ sudo /etc/init.d/postgresql status
# 启动
$ sudo /etc/init.d/postgresql start
# 停止
$ sudo /etc/init.d/postgresql stop
# 重启
$ sudo /etc/init.d/postgresql restart
```

psql is the PostgreSQL interactive terminal.
```
# 查看版本
$ psql -V
psql (PostgreSQL) 9.3.9
```

控制台命令
```
\h：查看SQL命令的解释，比如\h select。
\?：查看psql命令列表。
\l：列出所有数据库。
\c [database_name]：连接其他数据库。
\d：列出当前数据库的所有表，包括模式。
\dt：列出当前数据库的所有表。
\d [table_name]：列出某一张表格的结构。
\du：列出所有用户。
\e：打开文本编辑器。
\conninfo：列出当前数据库和连接的信息。
```

终端远程连接 postgres 命令
```
$ psql -h [ip] -p [port] -U [user] -d [database]
```

打开扩展，格式化显示查询结果，使用 \x 切换显示效果
```
wl_crawl=# \x
Expanded display is on.
wl_crawl=# select * from [table] limit 10;
wl_crawl=# \x
Expanded display is off.
wl_crawl=# select * from [table] limit 10;
```

建立索引
```
create index idx_tab_col on tab(col);
tab: 表名
col: 字段名
```

删除索引
```
drop index idx_tab_col
```

虽然索引的目的在于提高数据库的性能，有时间时，应避免。使用索引时，应重新考虑下列准则:

- 索引不应该被用于小表上。
- 有频繁的，大批量的更新或插入操作的表。
- 索引不应使用含有大量的NULL值的列。
- 频繁操作的列都将不建议使用索引。


psql 是一个普通的 PostgreSQL 客户端应用。

为了与一个数据库联接，你需要知道你的目标数据库， 服务器的主机名和端口号以及你希望以哪个用户的身份进行联接等信息。

我们可以通过命令行参数告诉 psql 这些信息，分别是 -d， -h，-p，和 -U。

如果有个参数不属于任何选项开关， 那么它会被解释成数据库名（或者是用户名——如果数据库名称已经给出了。）

所以，上面远程连接可以有很多写法，是很方便，但是建议指明参数，后面调试起来方便。


postgresql 版本升级

https://www.postgresql.org/download/linux/ubuntu/

```
$ sudo vim /etc/apt/sources.list.d/pgdg.list
```
添加以下内容并保存
```
deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main
```

Import the repository signing key, and update the package lists
```
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo apt-get update
```

确认当前 postgresql 服务是否关闭，并卸载旧版本，安装新版
```
$ netstat -ant | grep 5432
$ sudo service postgresql stop
```

修改旧版本端口号为5433, 再安装新版本, 新版本端口号才能为5432

否则新版本端口号会默认为5433

```
$ sudo apt-get remove postgresql-9.3
$ sudo apt-get install postgresql-9.5
```

```
$ sudo vim /etc/postgresql/9.5/main/postgresql.conf
$ sudo vim /etc/postgresql/9.5/main/pg_hba.conf
```


## Python MongoDB

mongo数据库安装（包含服务端/客户端）
```
$ sudo apt-get install mongodb
```

mongo仅客户端安装
```
$ sudo apt-get install mongodb-clients
```

pymongo安装(虚拟环境不需要sudo)
```
$ sudo pip install pymongo
```

命令行简单命令：
```
> show dbs
> use [db]
> show tables
> show collections
> db.[table/collection].find().pretty()
```

最新版安装记录(3.0版本不支持32位系统，最后一步无法安装)
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

32位系统安装最新版（最高支持到2.6）方式：
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

服务启动关闭重启
```
$ sudo service mongod start
$ sudo service mongod stop
$ sudo service mongod restart
```

参考：

[mongo最新版安装，仅支持64位](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)

[mongo最新版安装，32位系统](https://docs.mongodb.org/v2.6/tutorial/install-mongodb-on-ubuntu/)

[pymongo安装](http://api.mongodb.org/python/current/installation.html)

[官网教程](http://api.mongodb.org/python/current/tutorial.html)


## ElasticSearch

[ElasticSearch安装](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html)

系统安装ElasticSearch

Download and install the Public Signing Key:
```
$ wget -O - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
```

Save the repository definition to /etc/apt/sources.list.d/elasticsearch-{branch}.list:
```
echo "deb http://packages.elastic.co/elasticsearch/1.7/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-1.7.list
```

Run apt-get update and the repository is ready for use. You can install it with:
```
$ sudo apt-get update && sudo apt-get install elasticsearch
```

Configure Elasticsearch to automatically start during bootup
```
sudo update-rc.d elasticsearch defaults 95 10
```

Start Elasticsearch Server
```
$ sudo service elasticsearch
 * Usage: /etc/init.d/elasticsearch {start|stop|restart|force-reload|status}
$ sudo /etc/init.d/elasticsearch --help
 * Usage: /etc/init.d/elasticsearch {start|stop|restart|force-reload|status}
$ sudo /etc/init.d/elasticsearch status
 * elasticsearch is not running
$ sudo /etc/init.d/elasticsearch start
 * Starting Elasticsearch Server
```

Test by curl
```
$ curl -X GET 'http://localhost:9200'
{
  "status" : 200,
  "name" : "Bedlam",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "1.7.3",
    "build_hash" : "05d4530971ef0ea46d0f4fa6ee64dbc8df659682",
    "build_timestamp" : "2015-10-15T09:14:17Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.4"
  },
  "tagline" : "You Know, for Search"
}
```

进入elasticsearch目录安装插件：
```
$ cd /usr/share/elasticsearch/bin
$ sudo ./plugin -install mobz/elasticsearch-head
$ sudo ./plugin -i elasticsearch/marvel/latest
```

测试插件:

重启Elasticsearch服务
```
$ sudo /etc/init.d/elasticsearch restart
```

[http://localhost:9200/_plugin/head/](http://localhost:9200/_plugin/head/)

[http://localhost:9200/_plugin/marvel/](http://localhost:9200/_plugin/marvel/)

测试搜索界面：[http://192.168.2.188:9200/_plugin/marvel/sense/index.html](http://192.168.2.188:9200/_plugin/marvel/sense/index.html)

安装Python客户端驱动
```
$ pip install elasticsearch
```

安装Elasticsearch python客户端pyes
```
$ pip install pyes
```

角色关系对照

ElasticSearch 跟 MySQL 中定义资料格式的角色关系对照表如下
```
MySQL                   ElasticSearch
database                _index
table                   _type
id(primary key)         _id
```

table schema mapping
```
row                     document
field                   field
```

参考文档:

[ElasticSearch中文指南](http://www.elasticsearch.cn/guide/)

[Elasticsearch 权威指南（中文版）](http://es.xiaoleilu.com/)

[Python Elasticsearch Client](http://elasticsearch-py.readthedocs.org/en/latest/)

[PyES - Python Elastic Search](http://pyes.readthedocs.org/en/latest/index.html)

[ELK中文指南](http://kibana.logstash.es/)

## Python Redis

安装
```
$ pip search redis
$ sudo pip install redis
```

删除 redis 所有 KEY

批量删除 Key
Redis 中有删除单个 Key 的指令 DEL，但好像没有批量删除 Key 的指令，不过我们可以借助 Linux 的 xargs 指令来完成这个动作
```
redis-cli keys "*" | xargs redis-cli del
```
如果 redis-cli 没有设置成系统变量，需要指定 redis-cli 的完整路径
如：/opt/redis/redis-cli keys "*" | xargs /opt/redis/redis-cli del

如果要指定 Redis 数据库访问密码，使用下面的命令
```
redis-cli -a password keys "*" | xargs redis-cli -a password del
```
如果要访问 Redis 中特定的数据库，使用下面的命令
```
# 下面的命令指定数据序号为0，即默认数据库
redis-cli -n 0 keys "*" | xargs redis-cli -n 0 del
```
删除所有 Key，可以使用 Redis 的 flushdb 和 flushall 命令
```
# 删除当前数据库中的所有Key
flushdb
# 删除所有数据库中的key
flushall
```
注：keys 指令可以进行模糊匹配，但如果 Key 含空格，就匹配不到了，暂时还没发现好的解决办法。


[官方文档](https://pypi.python.org/pypi/redis)

[Redis 命令参考](http://doc.redisfans.com/)


## Python的XML库

[用 ElementTree 在 Python 中解析 XML](http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/processing-xml-in-python-with-element-tree.html)

[模块手册](https://docs.python.org/2/library/xml.etree.elementtree.html)

使用：
```
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
```


## Beautiful Soup

安装
```
$ apt-get install Python-bs4
```
或者
```
$ pip install beautifulsoup4
```
或者[下载BS4的源码](http://www.crummy.com/software/BeautifulSoup/download/4.x/)，然后通过setup.py来安装
```
$ Python setup.py instal
```

使用
```
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html>data</html>")
```

[官方文档](http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)


## mysql workbench

使用 mysql workbench 建表时，字段中有PK,NN,UQ,BIN,UN,ZF,AI几个基本字段类型标识。
它们分别代表的意思是：
```
PK：primary key 主键
NN：not null 非空
UQ：unique 唯一索引
BIN：binary 二进制数据（比text更大）
UN：unsigned 无符号（非负数）
ZF：zero fill 填充0 例如字段内容是1 int(4), 则内容显示为0001
AI：auto increment 自增
```

## web 性能测试

```
$ sudo apt-get install apache2-utils
$ ab -n 100 -c 10 http://www.flask_app.com/
$ ab -n 10000 -c 100 http://www.flask_app.com/blog/new/
```

## Google Image Search API (Deprecated)

[Google Image Search API (Deprecated)](https://developers.google.com/image-search/v1/jsondevguide?csw=1)


## 关于gc

python的内存虽然会自动回收，但是回收完之后的内存并不是还给系统，而仍然是作为python的内存池。
所以最根本的解决方法就是如何尽量少的让python从系统申请内存和复用自身的内存池资源。


## Flask

全局安装（虚拟环境不需要sudo）
```
$ sudo pip install Flask
```

官网[http://flask.pocoo.org/](http://flask.pocoo.org/)

中文指南[http://docs.jinkan.org/docs/flask/](http://docs.jinkan.org/docs/flask/)

常用组件：

[Flask-WTF](http://docs.jinkan.org/docs/flask-wtf/) Flask 的简单 WTForms 集成，包含 CSRF、文件上传和 Recaptcha 集成。

[Flask-SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/) 是一个为您的 Flask 应用增加 SQLAlchemy 支持的扩展。

[Flask-Login](http://docs.jinkan.org/docs/flask-login/) 为 Flask 提供了会话管理。它处理日常的登入、登出并长期保留用户会话。


## PyExecJS

从Python运行JavaScript代码，默认需要nodejs环境支持

nodejs环境
```
$ sudo apt-get install nodejs
$ sudo apt-get install npm
```
[https://nodejs.org](https://nodejs.org)

安装PyExecJS
```
$ pip install PyExecJS
```

## jieba “结巴”中文分词

全局安装
```
$ sudo pip install jieba
```

github项目地址：
[https://github.com/fxsjy/jieba](https://github.com/fxsjy/jieba)


## web-application-frameworks排行榜

[github排名](https://github.com/showcases/web-application-frameworks?s=stars)


## json 序列化 反序列化

直接对应：

JSON类型 | Python类型
----|------
{} | dict
[] | list
"string" | 'str'或u'unicode'
1234.56 | int或float
true/false | True/False
null | None

需要特殊处理：

JSON类型 | Python类型
----|------
"2016-07-09 23:02:12" | datetime.datetime
"2016-07-09" | datetime.date
"12.68" | decimal.Decimal


```
import json
from datetime import date, datetime
from decimal import Decimal


def __default(obj):
    """
    支持 datetime Decimal 的 json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, Decimal):
        return str(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)


row = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306
    },
    'proxy': [
        'http://127.0.0.1:1080',
        'https://127.0.0.1:1080'
    ],
    'test_none': None,
    'test_bool': True,
    'time': datetime.now(),
    'price': Decimal('12.68'),
    'time_list': [
        datetime.now()
    ]
}

print json.dumps(row, indent=4, ensure_ascii=False, default=__default)
{
    "time_list": [
        "2016-07-09 23:02:12"
    ],
    "price": "12.68",
    "db": {
        "host": "127.0.0.1",
        "port": 3306
    },
    "test_bool": true,
    "test_none": null,
    "proxy": [
        "http://127.0.0.1:1080",
        "https://127.0.0.1:1080"
    ],
    "time": "2016-07-09 23:02:12"
}
```

## 分库分表

单表数据过大时，影响查询效率，可以根据业务逻辑进行合理的分表，库的操作同理

通常按照主键取模，为了便于扩展，这里对偶数取模

```
➜  ~ mysql.server start
Starting MySQL
. SUCCESS!
➜  ~ mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.1.17-MariaDB Homebrew

Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> select 1%4, 2%4, 3%4, 4%4, 5%4, 6%4, 7%4, 8%4;
+------+------+------+------+------+------+------+------+
| 1%4  | 2%4  | 3%4  | 4%4  | 5%4  | 6%4  | 7%4  | 8%4  |
+------+------+------+------+------+------+------+------+
|    1 |    2 |    3 |    0 |    1 |    2 |    3 |    0 |
+------+------+------+------+------+------+------+------+
1 row in set (0.00 sec)

MariaDB [(none)]> select 1%8, 2%8, 3%8, 4%8, 5%8, 6%8, 7%8, 8%8;
+------+------+------+------+------+------+------+------+
| 1%8  | 2%8  | 3%8  | 4%8  | 5%8  | 6%8  | 7%8  | 8%8  |
+------+------+------+------+------+------+------+------+
|    1 |    2 |    3 |    4 |    5 |    6 |    7 |    0 |
+------+------+------+------+------+------+------+------+
1 row in set (0.00 sec)

MariaDB [(none)]>
```


## 文档托管

Read the Docs

创建、托管和浏览文档。

[https://readthedocs.org/](https://readthedocs.org/)

## TODO

多线程

队列
