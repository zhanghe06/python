# encoding: utf-8
__author__ = 'zhanghe'


import requests
import re
import json


def test(ip=None):
    """
    正向代理测试
    """
    if ip is None:
        ip_str = ''
        get_ip_info_fuc = 'get_ip_info'
    else:
        ip_str = str(ip)
        # todo ip地址合法性校验
        get_ip_info_fuc = 'get_ip_info_by_ip'
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
        # 'ip': '223.167.32.101'
        'ip': ip_str
    }
    # 代理配置
    proxies = {
        'http': 'http://192.168.111.129:8888'  # 代理服务
        # 'http': 'http://202.38.128.221:8086'  # 北京市 高能物理所
    }
    # 请求页面
    try:
        # r = s.get(source_site, params=payload, headers=header)
        r = s.get(source_site, params=payload, headers=header, proxies=proxies)
        print eval(get_ip_info_fuc)(r.content)
    except:
        print '代理连接失败'


def get_ip_info(html):
    """
    查询当前的IP信息
    :param html:
    :return:
    """
    reg_rule = r'<div id="result"><div class="well"><p>当前 IP：<code>(.+?)</code>&nbsp;来自：(.+?)</p><p>GeoIP: (.+?)</p></div></div>'
    reg = re.compile(reg_rule)
    try:
        html_list = re.findall(reg, html)
        return json.dumps(html_list[0], ensure_ascii=False, indent=4)
    except:
        return None


def get_ip_info_by_ip(html):
    """
    查询具体IP地址的详细信息
    :param html:
    :return:
    """
    reg_rule = r'<div id="result"><div class="well"><p>查询的 IP：<code>(.+?)</code>&nbsp;来自：(.+?)</p><p>(.+?)</p><p>(.+?)</p></div></div>'
    reg = re.compile(reg_rule)
    try:
        html_list = re.findall(reg, html)
        return json.dumps(html_list[0], ensure_ascii=False, indent=4)
    except:
        return None


if __name__ == "__main__":
    test('42.51.13.103')
    test()


"""
测试：
zhanghe@ubuntu:~/code/python$ python test/normal_proxy/test_proxy.py
[
    "202.38.128.221",
    "北京市 高能物理所",
    "Beijing, China"
]
[
    "42.51.13.103",
    "河南省郑州市 电联通信技术",
    "GeoIP: Zhengzhou, Henan, China",
    "Henan Telcom Union Technology Co., LTD"
]
[
    "223.167.32.101",
    "上海市 联通",
    "Shanghai, China"
]
"""