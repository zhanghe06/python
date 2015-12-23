## MariaDB 安装及配置

[官方下载地址](https://downloads.mariadb.org/mariadb/repositories/#mirror=opencas&distro=Ubuntu&distro_release=trusty--ubuntu_trusty&version=10.1)

安装过程
```
$ sudo apt-get install software-properties-common
$ sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
$ sudo add-apt-repository 'deb [arch=amd64,i386] http://mirrors.opencas.cn/mariadb/repo/10.1/ubuntu trusty main'
$ sudo apt-get update
$ sudo apt-get install mariadb-server
```

MariaDB 服务
```
$ sudo /etc/init.d/mysql stop
$ sudo /etc/init.d/mysql start
$ sudo /etc/init.d/mysql restart
```

终端连接客户端
```
$ mysql -uroot -p
```

设置MariaDB允许远程访问

使用nestat命令查看3306端口状态：
```
$ netstat -an | grep 3306
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN
```
从结果可以看出3306端口只是在IP 127.0.0.1上监听，所以拒绝了其他IP的访问。

解决方法：修改/etc/mysql/my.cnf文件。打开文件，找到下面内容：
```
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
bind-address  = 127.0.0.1
```

把上面这一行注释掉或者把127.0.0.1换成合适的IP，建议注释掉。

重新启动后，重新使用netstat检测：
```
$ netstat -an | grep 3306
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN
```

现在使用下面命令测试：
```
$ mysql -h 192.168.0.101 -u root -p
Enter password:
ERROR 1130 (00000): Host 'Ubuntu-Fvlo.Server' is not allowed to connect to this MySQL server
```
结果出乎意料，还是不行。

解决方法：原来还需要把用户权限分配各远程用户。

登录到mysql服务器，使用grant命令分配权限
```
$ mysql -uroot -p
```
查看权限
```
MariaDB [(none)]> SHOW GRANTS \G
*************************** 1. row ***************************
Grants for root@localhost: GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY PASSWORD '*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9' WITH GRANT OPTION
*************************** 2. row ***************************
Grants for root@localhost: GRANT PROXY ON ''@'%' TO 'root'@'localhost' WITH GRANT OPTION
2 rows in set (0.09 sec)
```
添加权限
```
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'zhanghe'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
Query OK, 0 rows affected (0.68 sec)
MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.30 sec)
```
重启服务
```
$ sudo /etc/init.d/mysql restart
```
测试服务器本地访问
```
$ mysql -p123456
MariaDB [(none)]>
```
测试远程访问
```
$ mysql -h 192.168.0.101 -u root -p
```
