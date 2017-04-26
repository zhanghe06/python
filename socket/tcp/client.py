# encoding: utf-8
__author__ = 'zhanghe'

from socket import *


class TcpClient:
    # 测试，连接本机
    HOST = '127.0.0.1'
    # 设置侦听端口
    PORT = 1122
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    LOCAL_ADDR = ('', 2225)

    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        # self.client.bind(self.LOCAL_ADDR)  # 绑定本地端口，可选
        self.client.connect(self.ADDR)

        while True:
            data = input('>')
            if not data:
                break
            # python3传递的是bytes，所以要编码
            self.client.send(data.encode('utf8'))
            print('发送信息到%s：%s' % (self.HOST, data))
            if data.upper() == "QUIT":
                break
            data = self.client.recv(self.BUFSIZ)
            if not data:
                break
            print('从%s收到信息：%s' % (self.HOST, data.decode('utf8')))


if __name__ == '__main__':
    client = TcpClient()