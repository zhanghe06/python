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

阿里云源(ubuntu 14.04)
```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
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

主机名一般存放在 /etc/hostname；
但是 Fedora 发行版将主机名存放在 /etc/sysconfig/network

修改主机名称
```
$ vim /etc/hostname
```
保存，重启系统

需要同时修改 hosts
```
$ vim /etc/hosts
```

```
127.0.1.1       ubuntu
```

显示cpu
```
$ sudo uname --p
i686    32位
x86_64  64位
```

查看 cpu 逻辑核心数，型号
```
$ cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
      4  Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
```

查看物理 cpu 颗数
```
$ cat /proc/cpuinfo | grep physical | uniq -c
      1 physical id	: 0
      1 address sizes	: 39 bits physical, 48 bits virtual
      1 physical id	: 0
      1 address sizes	: 39 bits physical, 48 bits virtual
      1 physical id	: 0
      1 address sizes	: 39 bits physical, 48 bits virtual
      1 physical id	: 0
      1 address sizes	: 39 bits physical, 48 bits virtual
```

查看 cpu 运行模式
```
$ getconf LONG_BIT
64
```
如果显示32，说明当前 CPU 运行在32bit模式下, 但不代表 CPU 不支持64bit

查看 cpu 是否支持64bit
```
$ cat /proc/cpuinfo | grep flags | grep ' lm ' | wc -l
4
```
结果大于0, 说明支持64bit计算. lm指long mode, 支持lm则是64bit

查看 cpu 信息概要
```
$ lscpu
```

    Architecture:          x86_64
    CPU 运行模式：    32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                4
    On-line CPU(s) list:   0-3
    每个核的线程数：2
    每个座的核数：  2
    Socket(s):             1
    NUMA 节点：         1
    厂商 ID：           GenuineIntel
    CPU 系列：          6
    型号：              69
    步进：              1
    CPU MHz：             759.000
    BogoMIPS:              4589.28
    虚拟化：           VT-x
    L1d 缓存：          32K
    L1i 缓存：          32K
    L2 缓存：           256K
    L3 缓存：           3072K
    NUMA node0 CPU(s):     0-3


查看 cpu 详情
```
$ cat /proc/cpuinfo
```
    
    processor	: 0
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 69
    model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
    stepping	: 1
    microcode	: 0x17
    cpu MHz		: 759.000
    cache size	: 3072 KB
    physical id	: 0
    siblings	: 4
    core id		: 0
    cpu cores	: 2
    apicid		: 0
    initial apicid	: 0
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
    bogomips	: 4589.28
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 39 bits physical, 48 bits virtual
    power management:
    
    processor	: 1
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 69
    model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
    stepping	: 1
    microcode	: 0x17
    cpu MHz		: 759.000
    cache size	: 3072 KB
    physical id	: 0
    siblings	: 4
    core id		: 0
    cpu cores	: 2
    apicid		: 1
    initial apicid	: 1
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
    bogomips	: 4589.28
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 39 bits physical, 48 bits virtual
    power management:
    
    processor	: 2
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 69
    model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
    stepping	: 1
    microcode	: 0x17
    cpu MHz		: 759.000
    cache size	: 3072 KB
    physical id	: 0
    siblings	: 4
    core id		: 1
    cpu cores	: 2
    apicid		: 2
    initial apicid	: 2
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
    bogomips	: 4589.28
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 39 bits physical, 48 bits virtual
    power management:
    
    processor	: 3
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 69
    model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
    stepping	: 1
    microcode	: 0x17
    cpu MHz		: 759.000
    cache size	: 3072 KB
    physical id	: 0
    siblings	: 4
    core id		: 1
    cpu cores	: 2
    apicid		: 3
    initial apicid	: 3
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
    bogomips	: 4589.28
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 39 bits physical, 48 bits virtual
    power management:

查看内存信息
```
$ cat /proc/meminfo
```

[Ubuntu设置系统防火墙](https://help.ubuntu.com/community/UFW)

格式化U盘(需卸载/取消挂载后才能格式化)
```
$ sudo fdisk -l
$ sudo mkfs.vfat -F 32 /dev/sdb1即可将u盘格式化为fat32格式
```

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
$ google-chrome --proxy-server="socks5://192.168.2.157"
```

ubuntu 解压 RAR
```
$ sudo apt-get install p7zip-rar
```

ubuntu 解压 windows 的 zip 文件出现乱码
```
$ sudo apt-get install unar
$ unar file.zip
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

SSH 免密登陆远程主机

将本机公钥添加到对方 authorized_keys 中
```
$ ssh-copy-id user@host
or
$ ssh user@host 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```
注意权限设置:
```
1) .ssh目录的权限必须是700
2) .ssh/authorized_keys文件权限必须是600
$ chmod 600 authorized_keys
```

查看系统所有 shell 版本
```
$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
```

查看当前 shell 版本
```
$ echo $SHELL
/bin/bash
```

安装 zsh
```
$ sudo apt-get install zsh
```

安装 oh-my-zsh
Oh My Zsh 只是一个对 zsh 命令行环境的配置包装框架，但它不提供命令行窗口，更不是一个独立的 APP。
Oh My Zsh 并不是某个命令行工具的替代品，而是和它们互为补充。
```
$ wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
```

[http://ohmyz.sh](http://ohmyz.sh)

替换bash为zsh：
```
$ chsh -s /bin/zsh
or
$ chsh -s $(which zsh)
```

查看 zsh 当前的版本号
```
zsh --version
```

将主题设置为随机
```
$ vim ~/.zshrc
ZSH_THEME="random"
```

命令输出当前主题的名称
```
$ echo $ZSH_THEME
```

pip 安装时默认访问 pypi 的，但是 pypi 的速度对于国内来说有点慢，还在国内也有一些 pip 的镜像源，造福广大程序员
```
pipy 国内镜像目前有：
http://pypi.douban.com/ 豆瓣
http://pypi.hustunique.com/ 华中理工大学
http://pypi.sdutlinux.org/ 山东理工大学
http://pypi.mirrors.ustc.edu.cn/ 中国科学技术大学
```

安装时我们可以手动指定 pip 源
```
$ pip -i http://pypi.douban.com/simple install Flask
```

或者修改 pip 源配置
```
$ mkdir ~/.pip
$ vim ~/.pip/pip.conf
```

```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```
或者
```
[global]
index-url = http://pypi.douban.com/simple

[install]
trusted-host=pypi.douban.com
```
由于最新的 pip 安装需要使用的 https 加密，所以在此需要添加 trusted-host


pip 安装 gnureadline 报错： /usr/bin/ld: cannot find -lncurses
```
$ sudo apt-cache search ncurses- | grep ncurses
$ sudo apt-get install libncurses5-dev
```


添加 curl 代理 （curl/wget）
```
$ vim ~/.curlrc
```
添加
```
proxy = http://127.0.0.1:8087
```


帅气终端（亮点是快速分屏）
```
$ apt-get install terminator
```
首先设置等宽字体 mono 12号

然后可以设置背景图片 透明度


杀掉当前所有的MySQL连接
```
MariaDB [(none)]> select concat('KILL ',id,';') from information_schema.processlist where user='www' and db='test';
```


shadowsocks(python)

[shadowsocks project](https://github.com/shadowsocks/shadowsocks/tree/master)

[shadowsocks wiki](https://github.com/shadowsocks/shadowsocks/wiki)

```
pip install shadowsocks
```

[server config file](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)
```
{
    "server":"my_server_ip",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```

To run in the foreground:
```
ssserver -c /etc/shadowsocks.json
```
To run in the background:
```
ssserver -c /etc/shadowsocks.json -d start
ssserver -c /etc/shadowsocks.json -d stop
```

桌面版系统也可以安装图形版 shadowsocks-qt5

[shadowsocks-qt5 wiki](https://github.com/shadowsocks/shadowsocks-qt5/wiki)
```
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```

