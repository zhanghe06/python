# encoding: utf-8
"""
代理类
"""
__author__ = 'zhanghe'

import socket
import select
import sys

to_address = ('192.168.1.112', 8088)  # 转发的出口地址


class Proxy:
    def __init__(self, addr):
        self.proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy.bind(addr)
        self.proxy.listen(10)
        self.inputs = [self.proxy]
        self.route = {}

    def serve_forever(self):
        """
        服务转发
        """
        print 'proxy listen...'
        while 1:
            readable, _, _ = select.select(self.inputs, [], [])
            for sock in readable:
                if sock == self.proxy:
                    self.on_join()
                else:
                    data = sock.recv(8096)
                    if not data:
                        self.on_quit(sock)
                    else:
                        self.route[sock].send(data)

    def on_join(self):
        client, addr = self.proxy.accept()
        print addr, 'connect'
        forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        forward.connect(to_address)
        self.inputs += [client, forward]
        self.route[client] = forward
        self.route[forward] = client

    def on_quit(self, sock):
        for s in sock, self.route[sock]:
            self.inputs.remove(s)
            del self.route[s]
            s.close()


if __name__ == '__main__':
    try:
        Proxy(('192.168.1.112', 8089)).serve_forever()  # 代理服务器监听的地址
    except KeyboardInterrupt:
        sys.exit(1)