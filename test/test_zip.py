#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_zip.py
@time: 2017/10/10 上午9:26
"""


def func():
    user_ids = [None, u'2', u'3', None]
    session_keys = ['111', '222', '333', '444']
    s = dict(zip(user_ids, session_keys))
    print s
    print map(lambda x: int(x) if x else 0, user_ids)


if __name__ == '__main__':
    func()
