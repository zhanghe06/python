# encoding: utf-8
__author__ = 'zhanghe'


import requests
import re
import sys
sys.path.append('..')
from tools.export import ExportFile


# 伪装成浏览器
header = {
    'Host': 'wow.techbrood.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()
export_json = ExportFile('./tech_brood_title.json')


def get_title_list():
    """
    获取标题列表
    """
    rule = u'<title>(.*?)-踏得网云开发平台</title>'
    # title_list = []
    for i in range(1, 13930):
        url = 'http://wow.techbrood.com/fiddle/%s?vm=full' % i
        print url
        response = s.get(url, headers=header)
        html = response.text
        title = re.compile(rule, re.S).findall(html)
        if title:
            # title_list.append({i: title[0]})
            export_json.write({i: title[0]})
    export_json.close()


if __name__ == '__main__':
    get_title_list()

"""
故事是这样的：
偶尔在这个网站发现了一个很炫的页面
当时没有收藏下来，只收藏了首页地址
本想搜索这个页面，但是功能限制……
只好出此下策，实属无奈，还望见谅
最后成功找到：
{"13108": "HTML5 超酷的太空战舰操控仪表盘"}
"""