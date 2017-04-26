#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_request.py
@time: 2017/4/26 上午9:55
"""


import requests
import time


def test_01():
    """
    测试请求延时
    request start   : 2017-04-26 10:05:56
    request response: 2017-04-26 10:06:06
    <Response [200]>
    process start:10:05:56
    process end  :10:06:06
    :return:
    """
    print 'request start   :', time.strftime("%Y-%m-%d %H:%M:%S")
    res = requests.get('http://0:8899')
    print 'request response:', time.strftime("%Y-%m-%d %H:%M:%S")
    print res
    print res.text


def test_02():
    """
    测试响应超时
    request start   : 2017-04-26 10:11:16
    HTTPConnectionPool(host='0', port=8899): Read timed out. (read timeout=2)
    request response: 2017-04-26 10:11:18
    :return:
    """
    print 'request start   :', time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        res = requests.get('http://0:8899', timeout=2)
        print res
        print res.text
    except requests.exceptions.ReadTimeout as e:
        print u'响应超时', e.message
    print 'request response:', time.strftime("%Y-%m-%d %H:%M:%S")


def test_03():
    """
    测试连接失败
    request start   : 2017-04-26 10:14:18
    HTTPConnectionPool(host='0', port=9999): Max retries exceeded with url: / (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x103e6f510>: Failed to establish a new connection: [Errno 61] Connection refused',))
    request response: 2017-04-26 10:14:18
    :return:
    """
    print 'request start   :', time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        res = requests.get('http://0:9999')
        print res
        print res.text
    # 连接错误
    except requests.exceptions.ConnectionError as e:
        print u'连接错误', e.message
    # 响应超时
    except requests.exceptions.ReadTimeout as e:
        print u'响应超时', e.message
    print 'request response:', time.strftime("%Y-%m-%d %H:%M:%S")


def test_04():
    """
    测试连接成功，无响应
    测试过程：
        开启监听：nc -l 9900
        测试请求
        断开监听
    测试结果：
        request start   : 2017-04-26 11:24:12
        连接错误 ('Connection aborted.', error(54, 'Connection reset by peer'))
        request response: 2017-04-26 11:24:18
    :return:
    """
    print 'request start   :', time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        res = requests.get('http://0:9900')
        print res
        print res.text
    # 连接错误
    except requests.exceptions.ConnectionError as e:
        print u'连接错误', e.message
    # 响应超时
    except requests.exceptions.ReadTimeout as e:
        print u'响应超时', e.message
    print 'request response:', time.strftime("%Y-%m-%d %H:%M:%S")


def test_05():
    """
    测试连接超时
    request start   : 2017-04-26 11:36:20
    连接错误 HTTPConnectionPool(host='www.x.com', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.HTTPConnection object at 0x1086d8750>, 'Connection to www.x.com timed out. (connect timeout=3)'))
    request response: 2017-04-26 11:36:23
    :return:
    """
    print 'request start   :', time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        res = requests.get('http://www.x.com', timeout=(3, 5))
        print res
        print res.text
    # 连接错误
    except requests.exceptions.ConnectionError as e:
        print u'连接错误', e.message
    # 响应超时
    except requests.exceptions.ReadTimeout as e:
        print u'响应超时', e.message
    print 'request response:', time.strftime("%Y-%m-%d %H:%M:%S")


def test_06():
    """
    测试重试
    测试结果：
        request start   : 2017-04-26 11:53:18
        连接错误 HTTPConnectionPool(host='www.x.com', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.HTTPConnection object at 0x107691ed0>, 'Connection to www.x.com timed out. (connect timeout=3)'))
        request response: 2017-04-26 11:53:40
    结果分析：
        backoff_factor： 超时补偿（默认值0）sleep seconds：{backoff factor} * (2 ^ ({number of total retries} - 1))
        1、backoff_factor = 0.1
        (5+1)*3 + (2**(1-1) + 2**(2-1) + 2**(3-1) + 2**(4-1) + 2**(5-1))*0.1
        = 18 + 3.1
        = 21.1

        2、backoff_factor = 0
        request start   : 2017-04-26 12:51:44
        连接错误 HTTPConnectionPool(host='www.x.com', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.HTTPConnection object at 0x10bae0ed0>, 'Connection to www.x.com timed out. (connect timeout=3)'))
        request response: 2017-04-26 12:52:02
        (5+1)*3
        = 18
    :return:
    """
    from requests.packages.urllib3.util.retry import Retry
    from requests.adapters import HTTPAdapter

    s = requests.Session()

    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])

    s.mount('http://', HTTPAdapter(max_retries=retries))
    s.mount('https://', HTTPAdapter(max_retries=retries))

    print 'request start   :', time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        res = s.get('http://www.x.com', timeout=(3, 5))
        print res
        print res.text
    # 连接错误
    except requests.exceptions.ConnectionError as e:
        print u'连接错误', e.message
    # 响应超时
    except requests.exceptions.ReadTimeout as e:
        print u'响应超时', e.message
    print 'request response:', time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    # test_01()
    # test_02()
    # test_03()
    # test_04()
    # test_05()
    test_06()


"""
测试页面
index.php

<?php
ini_set('date.timezone','Asia/Shanghai');
//打印时间
echo "process start:".date('h:i:s')."\n";

//暂停 10 秒
sleep(10);

//打印时间
echo "process end  :".date('h:i:s');
"""

"""
开启临时服务
php -S 0:8899
"""
