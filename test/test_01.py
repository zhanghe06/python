# coding=utf-8
__author__ = 'zhanghe'

import re
import json


test_html = '''<a href="/poi/5434861.html" target="_blank"
                                   data-tags=""><strong>苏州北塔</strong>  '''


def re_html(html):
    reg_a = '<a href="(.+?)".*?><strong>(.+?)</strong>'
    aa_list = re.compile(reg_a, re.S).findall(html)
    return json.dumps(aa_list, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print re_html(test_html)
