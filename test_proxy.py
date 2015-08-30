# encoding: utf-8
__author__ = 'zhanghe'


import requests


source_site = 'http://phalcon/'

header = {
    # 'Host': 'phalcon',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()
proxies = {
    'http': 'http://192.168.59.139:80'
}
# 请求页面
r = s.get(source_site, headers=header, proxies=proxies)
# print r.headers
# print r.encoding
print r.content


"""
日志监控
$ tail -f /var/log/nginx/access.log

不添加header：
127.0.0.1 - - [30/Aug/2015:14:08:24 +0800] "GET / HTTP/1.1" 200 343 "-" "python-requests/2.5.0 CPython/2.7.6 Linux/3.13.0-36-generic" "-"

附加上header：
127.0.0.1 - - [30/Aug/2015:14:30:53 +0800] "GET / HTTP/1.1" 200 343 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36" "-"

设置代理：
192.168.59.139 - - [30/Aug/2015:22:22:17 +0800] "GET http://phalcon/ HTTP/1.1" 200 343 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36" "-"

"""