#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: taobao_item_list.py
@time: 16-6-6 上午8:51
"""


import requests
import json
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    }

s = requests.session()


def get_item_list(key=''):
    url = 'https://s.taobao.com/search?q=%s' % key
    response = s.get(url, headers=header)
    html = response.text
    # print html
    item_list_rule = re.compile('g_page_config = (.*);', re.I)
    g_page_configs = item_list_rule.findall(html)
    # print g_page_configs
    result = json.loads(g_page_configs[0]) if g_page_configs else None
    if result:
        print json.dumps(result['mods']['itemlist']['data']['auctions'], indent=4, ensure_ascii=False)
        print json.dumps(result['mods']['pager']['data'], indent=4, ensure_ascii=False)

if __name__ == '__main__':
    get_item_list(key='连衣裙')
