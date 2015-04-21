# 本地git仓库上传到github账户操作
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


# 程序所需依赖
    zhanghe@ubuntu:~/code/python$ source pyenv/bin/activate
    (pyenv)zhanghe@ubuntu:~/code/python$ pip freeze
    Pillow==2.8.1
    argparse==1.2.1
    backports.ssl-match-hostname==3.4.0.2
    certifi==14.05.14
    cssselect==0.9.1
    gevent==1.0.1
    greenlet==0.4.5
    lxml==3.4.2
    pyquery==1.2.9
    pytesseract==0.1.6
    requests==2.5.0
    tornado==4.1
    wsgiref==0.1.2
    (pyenv)zhanghe@ubuntu:~/code/python$ pip freeze > requirements.txt


# 测试环境部署
    建立 虚拟环境
    virtualenv pyenv

    进入 虚拟环境
    source pyenv/bin/activate

    安装依赖库
    pip install -r requirements.txt






# ubuntu下python 图片识别pytesseract安装记录

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








# 模拟登录相关

    Requests
    HTTP库，Requests 使用的是 urllib3，因此继承了它的所有特性。比Python 标准库中的 urllib 模块api简单
    http://cn.python-requests.org/zh_CN/latest/

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

    ==================================
    python

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
