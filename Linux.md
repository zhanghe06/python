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