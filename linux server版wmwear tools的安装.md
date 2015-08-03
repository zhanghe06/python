##安装VMware Tools

准备工作：安装gcc
```
$ sudo apt-get install gcc
```

挂载目录
```
$ sudo su
# mkdir /mnt/cdrom
# mount /dev/cdrom /mnt/cdrom
```

复制VMware Tools文件
```
# cd /mnt/cdrom
# ls
# cp /mnt/cdrom/VMwareTools-9.6.2-1688356.tar.gz /tmp
```

解压安装
```
# cd /tmp
# ls
# tar -zxf VMwareTools-9.6.2-1688356.tar.gz
# ls
# cd vmware-tools-distrib
# ls
# ./vmware-install.pl -d
# umount /dev/cdrom
# reboot
```

说明:./vmware-install.pl这里加 -d 后续就不需要一直敲回车了

设置共享目录，/mnt/hgfs/

补充，以上没卵用。