# encoding: utf-8
__author__ = 'zhanghe'

import socket

port = 8081
host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'hello,this is a test info !', (host, port))