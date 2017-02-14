#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: redis_pub_sub.py
@time: 2017/2/14 下午11:03
"""


import sys
import redis
import json


class RedisPubSub(object):
    """
    Pub/Sub
    """
    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db = redis.Redis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    def pub(self, k, v):
        """
        Pub
        :param k:
        :param v:
        :return:
        """
        ch = '%s:%s' % (self.key, k)
        self.__db.publish(ch, v)

    def sub(self, k):
        """
        Sub
        :param k:
        :return:
        """
        ps = self.__db.pubsub()
        ch = '%s:%s' % (self.key, k)
        ps.subscribe(ch)
        for item in ps.listen():
            # {'pattern': None, 'type': 'subscribe', 'channel': 'queue:test:hh', 'data': 1L}
            # yield item
            yield item.get('data')

    def sub_not_loop(self, k):
        """
        Sub 非无限循环，取到结果即退出
        :param k:
        :return:
        """
        ps = self.__db.pubsub()
        ch = '%s:%s' % (self.key, k)
        ps.subscribe(ch)
        for item in ps.listen():
            if item['type'] == 'message':
                return item.get('data')


def test_pub():
    q = RedisPubSub('test')
    q.pub('hh', '123')


def test_sub():
    q = RedisPubSub('test')
    r = q.sub('hh')
    for i in r:
        print i


def test_sub_not_loop():
    q = RedisPubSub('test')
    r = q.sub_not_loop('hh')
    print r


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
测试一般模式
终端一：
✗ python redis_pub_sub.py test_sub
终端二：
✗ python redis_pub_sub.py test_pub


测试非无限循环模式
终端一：
✗ python redis_pub_sub.py test_sub_not_loop
终端二：
✗ python redis_pub_sub.py test_pub
"""