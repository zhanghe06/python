#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: DDDD.py
@time: 2017/6/6 下午1:54
"""

import time
# import ipdb
import inspect

import signal


# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    print signum, frame
    # ipdb.set_trace()
    inspect.getframeinfo(frame)
    raise Exception('Function TimeOut!')


def with_time_out(s=10):
    """
    函数超时装饰器
    :param s:
    :return:
    """
    signal.signal(signal.SIGALRM, myHandler)
    signal.alarm(s)

    def decorator(func):
        def wrapper(*args, **kw):
            return func(*args, **kw)
        return wrapper
    return decorator


def set_timeout():
    signal.signal(signal.SIGALRM, myHandler)
    signal.alarm(1)


@with_time_out(1)
def a():
    print 'a'
    b()


def b():
    time.sleep(10)
    print 'b'


# # register signal.SIGALRM's handler
# signal.signal(signal.SIGALRM, myHandler)
# signal.alarm(2)
# while True:
#     # time.sleep(3)
#     try:
#         a()
#     except Exception as e:
#         print 'get err:', e.message
#         # print('not yet')


try:
    a()
except Exception as e:
    print e
