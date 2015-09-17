# encoding: utf-8
__author__ = 'zhanghe'

if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time
    time.sleep(2)
    sock.send('1')
    print sock.recv(1024)
    sock.close()


"""
在终端运行server.py，然后运行clien.py，会在终端打印“welcome to server!"。
如果更改client.py的sock.send('1')为其它值，在终端会打印”please go out!“。
更改time.sleep(2)为大于5的数值，服务器将会超时。
"""