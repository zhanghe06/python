#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: token.py
@time: 2016/11/29 下午7:13
"""

import base64
import json


class Token(object):
    def __init__(self):
        self._key = '123qweasdzxc'

    def sign(self, data):
        data += '.%s' % self._key
        print data
        return base64.b64encode(data)

    def unsign(self, data):
        return base64.b64decode(data)


if __name__ == '__main__':
    token = Token()
    # 测试字符串
    a = token.sign('1234')
    b = token.unsign(a)
    print a, b
    # 测试字典
    test_dict_str = json.dumps({'z': 56, 'm': 12, 'p': 34}, sort_keys=True)
    a = token.sign(test_dict_str)
    b = token.unsign(a)
    print a, b
