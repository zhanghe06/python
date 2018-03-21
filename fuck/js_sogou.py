#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: js_sogou.py
@time: 2017/11/29 上午11:38
"""

import execjs


ss = u'''
    def res() {
        return d;
    }
'''

ctx = execjs.compile(ss)



if __name__ == '__main__':
    pass
