#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_functool_wraps.py
@time: 2017-12-26 14:07
"""


from functools import partial


def wrap(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print 'before call'
        return func(*args, **kwargs)
    return call_it


@wrap
def hello():
    """say hello"""
    print 'hello world'


from functools import update_wrapper


def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print 'before call'
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)


@wrap2
def hello2():
    """test hello"""
    print 'hello world2'


from functools import wraps


def wrap3(func):
    @wraps(func)
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print 'before call'
        return func(*args, **kwargs)
    return call_it


@wrap3
def hello3():
    """test hello 3"""
    print 'hello world3'


if __name__ == '__main__':
    hello()
    print 'hello.__name__', hello.__name__
    print 'hello.__doc__', hello.__doc__

    print
    hello2()
    print 'hello2.__name__', hello2.__name__
    print 'hello2.__doc__', hello2.__doc__

    print
    hello3()
    print 'hello3.__name__', hello3.__name__
    print 'hello3.__doc__', hello3.__doc__


"""
before call
hello world
hello.__name__ call_it
hello.__doc__ wrap func: call_it

before call
hello world2
hello2.__name__ hello2
hello2.__doc__ test hello

before call
hello world3
hello3.__name__ hello3
hello3.__doc__ test hello 3

使用 from functools import wraps 修饰过的装饰器, 可以保证原函数的 name 和 doc, 在调试中会起到关键作用
"""
