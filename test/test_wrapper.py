#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_wrapper.py
@time: 2017/8/5 下午7:57
"""


def w1(func):
    def wrapper(*args, **kw):
        back_func = func(*args, **kw)
        print func.__name__, 'w1'
        return back_func
    return wrapper


def w2(func):
    def wrapper(*args, **kw):
        back_func = func(*args, **kw)
        print func.__name__, 'w2'
        return back_func
    return wrapper


def w3(func):
    def wrapper(*args, **kw):
        back_func = func(*args, **kw)
        print func.__name__, 'w3'
        return back_func
    return wrapper


@w1
@w2
@w3
def func1():
    return 1


@w1
@w2
@w3
def func2():
    return 2


@w1
@w2
@w3
def func3():
    return 3


@w1
@w2
@w3
def fuck(func):
    def wrapper(*args, **kw):
        back_func = func(*args, **kw)
        print func.__name__, 'fuck'
        return back_func
    return wrapper


@fuck
def test():
    return 'test'


if __name__ == '__main__':
    # print func1()
    # print func2()
    # print func3()
    # print test()
    pass
