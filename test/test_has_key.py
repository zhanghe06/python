#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_has_key.py
@time: 2017/5/27 下午2:13
"""


a = {
    'foo': '1',
    'bar': '2',
}


def func():
    print a.has_key('foo')  # deprecated
    print a.has_key('fob')  # deprecated
    print 'foo' in a
    print 'fob' in a


if __name__ == '__main__':
    func()
