#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: jobui.py
@time: 16-5-20 下午4:38
"""


import requests
import re
import json


# 伪装成浏览器
header = {
    'Host': 'www.jobui.com',
    'Referer': 'http://www.jobui.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()


def get_city_list():
    """
    获取城市列表
    """
    # 入口页的url
    url = 'http://www.jobui.com/changecity/'
    response = s.get(url, headers=header)
    html = response.text
    rule = '<a onclick="changeCity\(this\);" href=".*?" data_city="(.*?)" data_url=".*?">.*?</a>'
    city_list = re.compile(rule, re.S).findall(html)
    city_name_list = []
    for item in city_list:
        if item not in city_name_list:
            city_name_list.append(item)
    print json.dumps(city_name_list, indent=4).decode('raw_unicode_escape')


def get_industry_list():
    """
    获取行业列表
    """
    # 入口页的url
    url = 'http://www.jobui.com/cmp'
    response = s.get(url, headers=header)
    html = response.text
    rule = '<a href="/cmp\?industry=.*?" >(.*?)</a>'
    city_list = re.compile(rule, re.S).findall(html)
    industry_name_list = []
    for item in city_list:
        if item not in industry_name_list:
            industry_name_list.append(item)
    print json.dumps(industry_name_list, indent=4).decode('raw_unicode_escape')


if __name__ == '__main__':
    get_city_list()
    get_industry_list()

