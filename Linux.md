## Linux Ubuntu 使用

关于版本选择，参考官网
[https://wiki.ubuntu.com/Releases](https://wiki.ubuntu.com/Releases)

安装全新系统需要更换国内镜像源以保证速度
```
$ sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup
$ sudo gedit /etc/apt/sources.list
# 更换源
$ sudo apt-get update
```

参考：[http://wiki.ubuntu.org.cn/源列表](http://wiki.ubuntu.org.cn/源列表)

注意版本：
```
Precise(12.04)版本，将上述列表地址中的 vivid 替换为 precise 即可
Trusty(14.04)版本，将上述列表地址中的 vivid 替换为 trusty
```

更新源 出现 Hash 校验和不符的解决办法
```
$ sudo rm -rf /var/lib/apt/lists/partial/*
# 更换源（排除网络问题，建议用阿里云源，速度不错）
$ sudo apt-get update
```

查看系统版本
```
$ cat /proc/version
```

显示操作系统32还是64位
```
$ sudo uname --m
i686    32位
x86_64  64位
```

显示内核名字
```
$ sudo uname --s
Linux
```

显示内核版本
```
$ sudo uname --r
3.13.0-36-generic
```

显示网络主机名
```
$ sudo uname --n
ubuntu
```

显示cpu
```
$ sudo uname --p
i686    32位
x86_64  64位
```

[Ubuntu设置系统防火墙](https://help.ubuntu.com/community/UFW)


刻录镜像文件制作U盘启动盘
```
$ dd if=ubuntu-14.04.1-desktop-amd64.iso of=/dev/sdb
```

ubuntu 14.04 没有笔记本wifi

查看硬件设备
```
$ lspci -vnn | grep Network
03:00.0 Network controller [0280]: Realtek Semiconductor Co., Ltd. RTL8192EE PCIe Wireless Network Adapter [10ec:818b]
```

安装驱动
```
$ git clone git@github.com:lwfinger/rtlwifi_new.git
$ cd rtlwifi_new
$ make
$ sudo make install
```

关闭ubuntu桌面上的错误报告
```
$ sudo vim /etc/default/apport
enabled=1
修改为
enabled=0
```

ubuntu 连接 vpn 失败的解决办法
```
打开：网络链接，选择VPN标签，编辑选择的VPN，在VPN标签里，选择“高级”。
选中“使用点到点加密(MPPE)”
```

tree 显示目录树形结构
```
$ sudo apt-get install tree
$ tree ./
```

shell获取当前执行脚本的路径
```
file_path=$(cd "$(dirname "$0")"; pwd)
或者
file_path=$(cd `dirname $0`; pwd)
```
脚本文件的绝对路径存在了环境变量 file_path 中，可以用
```
echo $file_path
```
查看完整路径

在shell中：
```
$0: 获取当前脚本的名称
$#: 传递给脚本的参数个数
$$: shell脚本的进程号
$1, $2, $3...：脚本程序的参数
```


ubuntu shell 终端中以窗口形式打开一个文件夹
```
$ nautilus
$ nautilus /tmp
```

可以用 alias 命令来给 nautilus 命令设置别名
```
$ alias opendir='nautilus'
```

但是这样操作只能在本次打开的shell终端中有用，下次启动shell终端命令失效，
可以将命令写入配置文件中
```
$ vim ~/.bashrc
```
打开配置文件后将 alias opendir='nautilus' 添加到配置文件中:
```
alias openpdf='xdg-open'
alias opendir='nautilus'
```
这样在下次启动 shell 时命令还能使用


linux 终端打开图片文件（图片需要完整路径才能打开）
```
$ eog example.png
```
eog 全称：eye of gnome，是 linux 下内置的图片查看器。


linux 终端打开 Google Chrome 浏览器
```
$ google-chrome
```

linux 终端通过代理打开 Google Chrome 浏览器
```
$ google-chrome　--proxy-server="socks5://192.168.2.157"
```

ubuntu 解压 RAR
```
# 安装
$ sudo apt-get install rar
# 解压
$ rar x FileName.rar
```

统计当前目录下指定后缀名的文件总个数命令
```
$ find . -name "*.html" | wc -l
```

统计项目目录中代码行数
```
# 指定后缀
$ find . -type f -name "*.py" | xargs wc -l
# 指定后缀(方式二)
$ find . -name "*.py" | xargs wc -l
# 过滤某些后缀
$ find . -type f ! -name "*.pyc" | xargs wc -l
```