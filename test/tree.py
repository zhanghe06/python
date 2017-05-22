#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tree.py
@time: 2017/5/22 下午6:57
"""


import json
from collections import defaultdict


def tree():
    """
    定义一棵树
    python 字典的特性，赋值操作必须事先声明，所以这里使用 collections 很方便的为字典设置初始值
    :return:
    """
    return defaultdict(tree)


if __name__ == '__main__':
    users = tree()
    users['jack_1']['jack_2_1']['jack_3_1'] = {}
    users['jack_1']['jack_2_1']['jack_3_2'] = {}
    users['jack_1']['jack_2_2'] = {}
    users['jack_1']['jack_2_2']['jack_3_1'] = {}

    users['lily_1']['lily_2_1']['lily_3_1'] = {}
    users['lily_1']['lily_2_2']['lily_3_2'] = {}
    users['lily_1']['lily_2_3']['lily_3_3'] = {}

    users['emma_1']['emma_2_1'] = {}

    # 打印 users 原始结构
    print users

    # 打印 users json 结构
    print(json.dumps(users, indent=4))

    # 第一层(users的key)
    print [i for i in users]

    # 第二层(users子节点的key)
    print [i for i in users['jack_1']]

    # 第三层(users孙节点的key)
    print [i for i in users['jack_1']['jack_2_1']]
