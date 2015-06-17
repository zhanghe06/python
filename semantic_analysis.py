# coding=utf-8
__author__ = 'zhanghe'

import re
import json


def compare_text(text_a, text_b):
    reg_a = '有(.+?)？'
    reg_b = '没(.+?)！'
    a_list = re.compile(reg_a, re.I).findall(text_a)
    b_list = re.compile(reg_b, re.I).findall(text_b)
    print json.dumps(a_list, ensure_ascii=False)
    print json.dumps(b_list, ensure_ascii=False)
    print(a_list == b_list)


if __name__ == '__main__':
    compare_text('有卵用？', '没卵用！')

"""
简单语义分析
["卵用"]
["卵用"]
True
"""
