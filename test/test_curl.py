# encoding: utf-8
__author__ = 'zhanghe'


import sys
sys.path.append('..')
from tools import curl


if __name__ == '__main__':
    print curl.get('https://www.baidu.com/s?wd=python')
    # print curl.post('http://www.wealink.com/passport/login', 'username=123456&password=123456')
