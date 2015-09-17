## 测试正向代理服务


开启代理服务
```
(pyenv)zhanghe@ubuntu:~/code/python$ python test/forward_direction_proxy/proxy.py 8888
```

测试代理服务
```
zhanghe@ubuntu:~/code/python$ python test/test_proxy.py
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