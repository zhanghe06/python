## 测试正向代理服务


开启代理服务
```
(pyenv)zhanghe@ubuntu:~/code/python$ python test/forward_direction_proxy/proxy.py 8888
```

测试代理服务
```
zhanghe@ubuntu:~/code/python$ python test/test_proxy.py
```

查看日志
```
zhanghe@ubuntu:~/code/python$ tail -f test/forward_direction_proxy/tornado_proxy.log
```

查看端口占用情况
```
$ netstat -an | grep 8888
```

测试结果
```
[
    "223.167.32.101", 
    "上海市 联通", 
    "GeoIP: Shanghai, China", 
    "CHINA UNICOM Shanghai network"
]
```

## Tornado的理解

[IOLoop] 是基于 epoll 实现的底层网络I/O的核心调度模块，用于处理 socket 相关的连接、响应、异步读写等网络事件。
每个 Tornado 进程都会初始化一个全局唯一的 IOLoop 实例，
IOLoop 中通过静态方法 instance() 进行封装，获取 IOLoop 实例直接调用此方法即可。

[Application] Tornado 使用 web 模块的 Application 做URI转发。

[RequestHandler] 这是Tornado的请求处理函数类，通过 RequestHandler 处理请求。
