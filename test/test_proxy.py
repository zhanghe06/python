# encoding: utf-8
__author__ = 'zhanghe'


import requests


def test_lan():
    """
    局域网反向代理测试
    """
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


def test_wan():
    """
    广域网正向代理测试
    """
    source_site = 'http://ip.cn/index.php'

    header = {
        'Host': 'ip.cn',
        'Referer': 'http://ip.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
    }

    s = requests.session()
    # 查询参数
    payload = {
        # 'ip': '101.81.89.102'
        'ip': '223.167.32.101'
    }
    # 代理配置
    proxies = {
        'http': 'http://127.0.0.1:8888'  # 代理服务
    }
    # 请求页面
    try:
        # r = s.get(source_site, params=payload, headers=header)
        r = s.get(source_site, params=payload, headers=header, proxies=proxies)
        print get_ip_info(r.content)
    except:
        print '代理连接失败'


def get_ip_info(html):
    """
    通过正则表达式获取页面IP信息
    :param html:
    :return:
    """
    import re
    import json
    reg_rule = r'<div id="result"><div class="well"><p>查询的 IP：<code>(.+?)</code>&nbsp;来自：(.+?)</p><p>(.+?)</p><p>(.+?)</p></div></div>'
    reg = re.compile(reg_rule)
    try:
        html_list = re.findall(reg, html)
        return json.dumps(html_list[0], ensure_ascii=False, indent=4)
    except:
        return None


if __name__ == "__main__":
    # test_lan()
    test_wan()


"""
局域网测试：
日志监控
$ tail -f /var/log/nginx/access.log

不添加header：
127.0.0.1 - - [30/Aug/2015:14:08:24 +0800] "GET / HTTP/1.1" 200 343 "-" "python-requests/2.5.0 CPython/2.7.6 Linux/3.13.0-36-generic" "-"

附加上header：
127.0.0.1 - - [30/Aug/2015:14:30:53 +0800] "GET / HTTP/1.1" 200 343 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36" "-"

设置代理：
192.168.59.139 - - [30/Aug/2015:22:22:17 +0800] "GET http://phalcon/ HTTP/1.1" 200 343 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36" "-"

"""

"""
广域网测试：

[
    "101.81.89.102",
    "上海市 电信",
    "GeoIP: Shanghai, China",
    "China Telecom Shanghai"
]


"""