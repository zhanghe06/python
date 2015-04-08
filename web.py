# encoding: utf-8
__author__ = 'zhanghe'

import os
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
# from handlers import *

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('index.html')

    def post(self):
        self.render('index.html')


handlers = [
    (r'/', IndexHandler),
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
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    # app.listen(options.port)  # 貌似这一句可以替代上面两句，待研究
    tornado.ioloop.IOLoop.instance().start()