#!coding:utf-8
import socket
import logging

log=logging.getLogger('httpclient')

from tornado.iostream import IOStream


__author__ = 'sdm'

from  tornado.simple_httpclient import SimpleAsyncHTTPClient

# /Library/Python/2.7/site-packages/tornado/tcpclient.py
from tornado.tcpclient import TCPClient


class MySimpleAsyncHTTPClient(SimpleAsyncHTTPClient):
    def initialize(self, io_loop, max_clients=10,
                   hostname_mapping=None, max_buffer_size=104857600,
                   resolver=None, defaults=None, max_header_size=None):
        super(MySimpleAsyncHTTPClient, self).initialize(io_loop, max_clients,
                                                        hostname_mapping, max_buffer_size,
                                                        resolver, defaults, max_header_size)
        self.tcp_client = MyTCPClient(resolver=self.resolver, io_loop=io_loop)
        log.debug("new tcp MyTCPClient client ")


class MyTCPClient(TCPClient):
    def _create_stream(self, max_buffer_size, af, addr):
        # Always connect in plaintext; we'll convert to ssl if necessary
        # after one connection has completed.
        s = socket.socket(af)
        log.debug("connect:%s" % (af))
        #s.bind(('192.168.2.143',0))
        s.bind(('192.168.0.50',0))
        stream = IOStream(s,
                          io_loop=self.io_loop,
                          max_buffer_size=max_buffer_size)
        return stream.connect(addr)
