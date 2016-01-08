## Nginx

Nginx 官网：[http://nginx.org/](http://nginx.org/)

### 安装 Nginx

1、加入nginx repository signature
```
$ cd /tmp/
$ wget http://nginx.org/keys/nginx_signing.key
$ sudo apt-key add nginx_signing.key
$ cd /etc/apt/sources.list.d/
$ sudo vim nginx.list
```
将下面2行复制粘贴到这个文件[ubuntu 14.04]
```
deb http://nginx.org/packages/ubuntu/ trusty nginx
deb-src http://nginx.org/packages/ubuntu/ trusty nginx
```
其它系统参考这里:[http://nginx.org/en/linux_packages.html](http://nginx.org/en/linux_packages.html)

2、安装
```
$ sudo apt-get update
$ sudo apt-get install nginx
```

3、配置文件位置

/etc/nginx/nginx.conf

这个配置文件会包含/etc/nginx/conf.d/*.conf

默认主目录：/usr/share/nginx/html/

4、管理nginx服务
```
$ sudo service nginx start
$ sudo service nginx stop
$ sudo service nginx restart
```

访问[http://localhost](http://localhost)

Welcome to nginx!

安装成功
