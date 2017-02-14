#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: redis_queue.py
@time: 2016/10/24 下午10:42
"""


import sys
import redis
import json


class RedisQueue(object):
    """Simple Queue with Redis Backend"""

    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db = redis.Redis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            # ('queue:test', 'hello world')
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            # hello world
            item = self.__db.lpop(self.key)

        if isinstance(item, tuple):
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)


def test_put():
    q = RedisQueue('test')
    q.put('hello world')
    pass


def test_put_dict():
    q = RedisQueue('test')
    q.put(json.dumps({'key': 1, 'value': 1}))
    pass


def test_get():
    q = RedisQueue('test')
    result = q.get()
    print result, type(result)


def test_get_dict():
    q = RedisQueue('test')
    result = q.get()
    print result, type(result), json.loads(result)


def test_get_nowait():
    q = RedisQueue('test')
    result = q.get_nowait()
    print result


def run():
    # print sys.argv
    try:
        if len(sys.argv) > 1:
            fun_name = eval(sys.argv[1])
            fun_name()
        else:
            print '缺失参数'
    except NameError, e:
        print e
        print '未定义的方法[%s]' % sys.argv[1]


if __name__ == '__main__':
    run()


"""
测试：

✗ python tools/redis_queue.py test_put

✗ python tools/redis_queue.py test_get
hello world/阻塞，不退出

✗ python tools/redis_queue.py test_get_nowait
hello world/None
"""