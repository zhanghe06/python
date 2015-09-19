# encoding: utf-8
__author__ = 'zhanghe'

import os
import sys
sys.path.append("/usr/lib/python2.7/dist-packages")
import socket
from urlparse import urlparse

import tornado.httpserver
import tornado.ioloop
import tornado.iostream
import tornado.web
import tornado.httpclient

sys.path.append("/home/zhanghe/code/python/tools")
from log import Log
logger = Log()
logger.log_filename = 'test/forward_direction_proxy/tornado_proxy.log'
logger.log_config()

__all__ = ['ProxyHandler', 'run_proxy']


def get_proxy(url):
    """
    获取系统代理
    """
    url_parsed = urlparse(url, scheme='http')
    proxy_key = '%s_proxy' % url_parsed.scheme
    logger.debug('proxy_key: %s' % proxy_key)
    logger.debug('os.environ.get(proxy_key):%s' % os.environ.get(proxy_key))
    return os.environ.get(proxy_key)


def parse_proxy(proxy):
    """
    解析代理
    """
    proxy_parsed = urlparse(proxy, scheme='http')
    logger.debug('proxy_parsed.hostname:%s, proxy_parsed.port:%s\n' % (proxy_parsed.hostname, proxy_parsed.port))
    return proxy_parsed.hostname, proxy_parsed.port


def fetch_request(url, callback, **kwargs):
    """
    获取请求
    :param url:
    :param callback:
    :param kwargs:
    :return:
    """
    proxy = get_proxy(url)
    if proxy:
        logger.debug('Forward request via upstream proxy %s' % proxy)
        tornado.httpclient.AsyncHTTPClient.configure(
            'tornado.curl_httpclient.CurlAsyncHTTPClient')
        host, port = parse_proxy(proxy)
        kwargs['proxy_host'] = host
        kwargs['proxy_port'] = port

    req = tornado.httpclient.HTTPRequest(url, **kwargs)
    client = tornado.httpclient.AsyncHTTPClient()
    client.fetch(req, callback)


class ProxyHandler(tornado.web.RequestHandler):
    """
    代理请求处理类
    """
    SUPPORTED_METHODS = ['GET', 'POST', 'CONNECT']

    @tornado.web.asynchronous
    def get(self):
        logger.debug('Handle %s request to %s' % (self.request.method, self.request.uri))

        def handle_response(response):
            if (response.error and not
                    isinstance(response.error, tornado.httpclient.HTTPError)):
                self.set_status(500)
                self.write('Internal server error:\n' + str(response.error))
            else:
                self.set_status(response.code)
                for header in ('Date', 'Cache-Control', 'Server', 'Content-Type', 'Location'):
                    v = response.headers.get(header)
                    if v:
                        self.set_header(header, v)
                v = response.headers.get_list('Set-Cookie')
                if v:
                    for i in v:
                        self.add_header('Set-Cookie', i)
                if response.body:
                    self.write(response.body)
            self.finish()

        body = self.request.body
        if not body:
            body = None
        try:
            fetch_request(
                self.request.uri, handle_response,
                method=self.request.method, body=body,
                headers=self.request.headers, follow_redirects=False,
                allow_nonstandard_methods=True)
        except tornado.httpclient.HTTPError as e:
            if hasattr(e, 'response') and e.response:
                handle_response(e.response)
            else:
                self.set_status(500)
                self.write('Internal server error:\n' + str(e))
                self.finish()

    @tornado.web.asynchronous
    def post(self):
        return self.get()

    @tornado.web.asynchronous
    def connect(self):
        logger.debug('Start CONNECT to %s' % self.request.uri)
        host, port = self.request.uri.split(':')
        client = self.request.connection.stream

        def read_from_client(data):
            upstream.write(data)

        def read_from_upstream(data):
            client.write(data)

        def client_close(data=None):
            if upstream.closed():
                return
            if data:
                upstream.write(data)
            upstream.close()

        def upstream_close(data=None):
            if client.closed():
                return
            if data:
                client.write(data)
            client.close()

        def start_tunnel():
            """
            开启隧道连接
            """
            logger.debug('CONNECT tunnel established to %s' % self.request.uri)
            client.read_until_close(client_close, read_from_client)
            upstream.read_until_close(upstream_close, read_from_upstream)
            client.write(b'HTTP/1.0 200 Connection established\r\n\r\n')

        def on_proxy_response(data=None):
            if data:
                first_line = data.splitlines()[0]
                http_v, status, text = first_line.split(None, 2)
                if int(status) == 200:
                    logger.debug('Connected to upstream proxy %s' % proxy)
                    start_tunnel()
                    return

            self.set_status(500)
            self.finish()

        def start_proxy_tunnel():
            """
            开启代理隧道连接
            """
            upstream.write('CONNECT %s HTTP/1.1\r\n' % self.request.uri)
            upstream.write('Host: %s\r\n' % self.request.uri)
            upstream.write('Proxy-Connection: Keep-Alive\r\n\r\n')
            upstream.read_until('\r\n\r\n', on_proxy_response)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        upstream = tornado.iostream.IOStream(s)
        proxy = get_proxy(self.request.uri)
        logger.debug('proxy: %s' % proxy)
        if proxy:
            proxy_host, proxy_port = parse_proxy(proxy)
            logger.debug('proxy_host, proxy_port: %s\t%s' % (proxy_host, proxy_port))
            upstream.connect((proxy_host, proxy_port), start_proxy_tunnel)
        else:
            upstream.connect((host, int(port)), start_tunnel)


def run_proxy(port, start_ioloop=True):
    """
    Run proxy on the specified port. If start_ioloop is True (default),
    the tornado IOLoop will be started immediately.
    """
    app = tornado.web.Application([
        (r'.*', ProxyHandler),
    ])
    app.listen(port)
    ioloop = tornado.ioloop.IOLoop.instance()
    if start_ioloop:
        ioloop.start()

if __name__ == '__main__':
    port = 8888
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    print ("Starting HTTP proxy on port %d" % port)
    try:
        run_proxy(port)
    except KeyboardInterrupt:
        sys.exit(1)
