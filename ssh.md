## ssh

SSH分客户端openssh-client和服务端openssh-server

如果只是登陆别的机器，SSH只需要安装openssh-client（ubuntu有默认安装）
```
sudo apt-get install openssh-client
```

如果要使本机开放SSH服务就需要安装openssh-server
```
$ sudo apt-get install openssh-server
```

确认sshserver是否启动
```
$ ps -e | grep ssh
 1767 ?        00:00:00 sshd
 3383 ?        00:00:00 ssh-agent
```

如果看到sshd那说明ssh-server已经启动了。
如果没有则可以这样启动：
```
sudo /etc/init.d/ssh start
```

ssh-server配置文件位于/etc/ssh/sshd_config，可以定义SSH的服务端口，默认端口是22，可以自己定义成其他端口号。

查看ssh端口号
```
$ cat /etc/ssh/sshd_config | grep Port
```

查看22端口情况
```
$ netstat -antpl | grep -E '22|State'
```

然后重启SSH服务：
```
$ sudo /etc/init.d/ssh stop
$ sudo /etc/init.d/ssh start
```

然后使用以下方式登陆SSH：
```
$ ssh username@192.168.1.112
```
username为192.168.1.112 机器上的用户，需要输入密码。

断开连接：exit
