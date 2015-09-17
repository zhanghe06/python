## 测试反向代理服务


测试环境：

虚拟机ip:192.168.1.112
宿主机ip:192.168.1.102

虚拟机为服务器
宿主机为客户端


第一步：启动服务
```
zhanghe@ubuntu:~/code/python$ source pyenv/bin/activate
(pyenv)zhanghe@ubuntu:~/code/python$ python test/proxy/server.py
```

访问[http://192.168.1.112:8088/](http://192.168.1.112:8088/)返回正确页面

访问[http://192.168.1.112:8089/](http://192.168.1.112:8089/)返回空页面

第二步：开启代理
```
zhanghe@ubuntu:~/code/python$ python test/proxy/proxy.py 
```

访问[http://192.168.1.112:8088/](http://192.168.1.112:8088/)返回正确页面

访问[http://192.168.1.112:8089/](http://192.168.1.112:8089/)返回正确页面


测试目标：
通过8089端口代理访问8088服务的页面


虚拟机本机访问和宿主机访问运行的结果：

服务端：
请求来源IP（客户端出口IP）都是192.168.1.112
```
(pyenv)zhanghe@ubuntu:~/code/python$ python test/proxy/server.py 
[I 150917 17:41:34 web:1825] 200 GET / (192.168.1.112) 20.87ms
[I 150917 17:41:43 web:1825] 304 GET / (192.168.1.112) 1.42ms
```

代理端：
```
zhanghe@ubuntu:~/code/python$ python test/proxy/proxy.py 
proxy listen...
('192.168.1.112', 45098) connect
('192.168.1.112', 45100) connect
('192.168.1.102', 55251) connect
```