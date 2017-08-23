#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: fishc.py
@time: 2017/6/1 上午9:08
"""


import requests

url = 'http://bbs.fishc.com/misc.php?mod=seccode&update=51882&idhash=cSp1R1BV'

header = {
        'Host': 'bbs.fishc.com',
        'Referer': 'http://bbs.fishc.com/member.php?mod=logging&action=login&referer=',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }


def run():
    res = requests.get(url, headers=header)
    open('logo.gif', 'wb').write(res.content)


if __name__ == '__main__':
    run()
