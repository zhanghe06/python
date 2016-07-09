#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_except.py
@time: 16-4-13 下午6:38
"""


try:
    # raise Exception('error_message')
    raise Exception('error_message', 'error_code')
except Exception as e:
    print type(e.message), e.message
    print type(e.args[0]), e.args[0]


if __name__ == '__main__':
    pass
