#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_wrap.py
@time: 2017/7/28 下午2:14
"""

from functools import wraps


def singleton(func):
    @wraps(func)
    def getinstance(*args, **kw):
        back_func = func(*args, **kw)

    return back_func


@singleton
class MyClass(object):
    a = 1


def time_log(func):
    """
    装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kw):
        func_name = func.__name__
        start_time = time.time()
        print '方法%s开始时间：%s' % (func_name, time.ctime())
        back_func = func(*args, **kw)
        end_time = time.time()
        run_time = end_time - start_time
        print '方法%s结束时间：%s' % (func_name, time.ctime())
        print '方法%s运行时间：%0.2fS' % (func_name, run_time)
        return back_func
    return wrapper


if __name__ == '__main__':
    pass
