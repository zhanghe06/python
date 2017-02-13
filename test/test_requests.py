#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_requests.py
@time: 2017/2/13 下午11:05
"""

import requests


def test_cookie():
    """
    测试cookies
    :return:
    """
    url = 'http://www.baixing.com'
    r = requests.get(url)
    print r.cookies.items()  # [('__city', 'shanghai'), ('__s', '2hpl4if6jromtarou0vcvvtnm4')]
    # 清除会话 cookie
    r.cookies.clear_session_cookies()
    print r.cookies.items()  # [('__city', 'shanghai')]


if __name__ == '__main__':
    test_cookie()
