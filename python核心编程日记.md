## input()与raw_input()区别
```
14.3.5 input()
内建函数input()是eval()和raw_input()的组合，等价于eval(raw_input())。类似于
raw_input()，input()有一个可选的参数，该参数代表了给用户的字符串提示。如果不给定参数的
话，该字符串默认为空串。
从功能上看,input 不同于raw_input()，因为raw_input()总是以字符串的形式，逐字地返回用
户的输入。input()履行相同的的任务；而且，它还把输入作为python 表达式进行求值。这意味着
input()返回的数据是对输入表达式求值的结果：一个python 对象。
```

## xrange()与range()
```
8.6.5 xrange() 内建函数
xrange() 类似 range() , 不过当你有一个很大的范围列表时, xrange() 可能更为适合, 因为
它不会在内存里创建列表的完整拷贝. 它只被用在 for 循环中, 在 for 循环外使用它没有意义。
同样地, 你可以想到, 它的性能远高出 range(), 因为它不生成整个列表。
```

## print语句换行
```
print 语句默认在输出内容末尾后加一个换行符, 而在语句后加一个逗号就可以避免这个行为。
```

## 网络编程 - 655页
```
662页说：
from socket import * 比 import socket 化简代码
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
化简为
tcpSock = socket(AF_INET, SOCK_STREAM)
[典型的通用服务端伪代码]：
    ss = socket()       # 创建服务器套接字
    ss.bind()           # 把地址绑定到套接字上
    ss.listen()         # 监听连接
    inf_loop:           # 服务器无限循环
    cs = ss.accept()    # 接受客户的连接
    comm_loop:          # 通讯循环
    cs.recv()/cs.send() # 对话（接收与发送）
    cs.close()          # 关闭客户套接字
    ss.close()          # 关闭服务器套接字（可选）
[典型的通用客户端伪代码]：
    cs = socket()       # 创建客户套接字
    cs.connect()        # 尝试连接服务器
    comm_loop:          # 通讯循环
    cs.send()/cs.recv() # 对话（发送／接收）
    cs.close()          # 关闭客户套接字
```

## 单网卡绑定多IP的实现方法
```
$ sudo su
# ifconfig eth0:1 192.168.2.100 netmask 255.255.255.0
# ifconfig eth0:2 192.168.2.200 netmask 255.255.255.0
网络重启后以上配置失效
# service networking restart
如需加入开机启动项
$ sudo subl /etc/rc.local
在exit 0前面 添加以上两句配置
```
