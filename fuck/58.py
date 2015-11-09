# encoding: utf-8
__author__ = 'zhanghe'


import requests
import re
import json

# 入口页的url
url = 'http://www.58.com/changecity.aspx'

# 伪装成浏览器
header = {
    'Host': 'www.58.com',
    'Referer': 'http://sh.58.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()


def get_city_list():
    """
    获取城市列表
    """
    response = s.get(url, headers=header)
    html = response.text
    rule = '<a href="http://.*?.58.com/" onclick="co\(\'(.*?)\'\)">(.*?)</a>'
    city_list = re.compile(rule, re.S).findall(html)
    city = {}
    for item in city_list:
        city[item[0]] = item[1]
    print json.dumps(city, indent=4).decode('raw_unicode_escape')


if __name__ == '__main__':
    get_city_list()