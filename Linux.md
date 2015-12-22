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
