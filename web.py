# encoding: utf-8
__author__ = 'zhanghe'

import os
import sys
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import requests
import json
# from handlers import *

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

s = requests.session()

# 登录页的url
url = 'https://trade.1234567.com.cn/do.aspx/CheckedCS'

# 配置User-Agent
header = {
    'Content-Type': 'application/json; charset=UTF-8',  # 因为是ajax请求，格式为json，这个必须指定
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
}


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('index.html')

    def post(self):
        self.render('index.html')


class LoginHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        payload = self.get_argument("payload", '')
        print payload
        response = s.post(url, data=payload, headers=header)
        content = response.text
        print content
        return self.render('login.html', payload=payload, content=content)


class QQHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('web_qq/index.html')


class QQPasswordHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('web_qq/password.html')


class TcLoginHandler(tornado.web.RequestHandler):
    """
    58同城
    """
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('tc.html')

    def post(self):
        password = self.get_argument("password", '')
        timesign = self.get_argument("timesign", '')
        print password, timesign
        data = {
            'password': password,
            'timesign': timesign
        }
        return self.render('tc_login.html', data=data)


class FutureHandler(tornado.web.RequestHandler):
    """
    HTML5 超酷的太空战舰操控仪表盘
    """
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('future.html')

handlers = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/qq', QQHandler),
    (r'/qq/password', QQPasswordHandler),
    (r'/tc', TcLoginHandler),
    (r'/future', FutureHandler),
    # (r'/member', memberHandler),
    # (r'/chat/(\d+)', chatHandler),
    # (r'/register', registerHandler),
    # (r'/logout', logoutHandler),
    # (r'/post', postHandler),
    # (r'/user/(\w+)', userHandler),
    # (r'/blog/(\d+)', blogHandler),
    # (r'/comment', commentHandler),
]
settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
}


if __name__ == '__main__':
    try:
        tornado.options.parse_command_line()
        app = tornado.web.Application(handlers, **settings)
        # http_server = tornado.httpserver.HTTPServer(app)
        # http_server.listen(options.port)
        app.listen(options.port)  # 貌似这一句可以替代上面两句，待研究
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print '服务关闭'
        sys.exit(1)