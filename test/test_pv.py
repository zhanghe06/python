#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_pv.py
@time: 2017/7/27 下午3:21
"""


import requests

s = requests.session()

url = 'http://www.ribble.top/article-detials/7'


def fk():
    r = s.get(url)
    print r.url


def run():
    for i in range(1000):
        print i,
        fk()

if __name__ == '__main__':
    run()
