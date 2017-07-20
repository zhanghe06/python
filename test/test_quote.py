#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_quote.py
@time: 2017/7/25 下午4:28
"""


def f(x, l=[]):
    """
    引用测试
    :param x:
    :param l:
    :return:
    """
    print l
    for i in range(x):
        l.append(i*i)
    print l

f(2)
f(3, [3, 2, 1])
f(3)


def detail():
    """
    详细过程
    :return:
    """
    l_mem = []

    l = l_mem           # the first call
    for i in range(2):
        l.append(i*i)

    print l             # [0, 1]

    l = [3, 2, 1]       # the second call
    for i in range(3):
        l.append(i*i)

    print l             # [3, 2, 1, 0, 1, 4]

    l = l_mem           # the third call
    for i in range(3):
        l.append(i*i)

    print l             # [0, 1, 0, 1, 4]


if __name__ == '__main__':
    # detail()
    pass
