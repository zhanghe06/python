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


def test_users():
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


l = [
    {'u': 4, 'p': 1},
    {'u': 10, 'p': 1},
    {'u': 5, 'p': 1},
    {'u': 6, 'p': 2},
    {'u': 7, 'p': 2},
    {'u': 8, 'p': 3},
    {'u': 9, 'p': 3},
    {'u': 11, 'p': 3},
    {'u': 12, 'p': 3},
    {'u': 13, 'p': 5},
    {'u': 14, 'p': 6},
    {'u': 15, 'p': 10},
    {'u': 17, 'p': 10},
    {'u': 19, 'p': 10},
    {'u': 20, 'p': 15},
    {'u': 21, 'p': 15},
    {'u': 22, 'p': 17},
    {'u': 23, 'p': 22},
]


def get_child_users(uid):
    """
    获取子节点
    :param uid:
    :return:
    """
    r = []
    for i in l:
        if i['p'] == uid:
            r.append(i['u'])
    return r


def test_team(uid):
    """
    测试
    :return:
    """
    team = tree()
    child_users = get_child_users(uid)
    for uid1 in child_users:
        team[uid1] = {}
        child_users2 = get_child_users(uid1)
        for uid2 in child_users2:
            team[uid1][uid2] = {}
            child_users3 = get_child_users(uid2)
            for uid3 in child_users3:
                team[uid1][uid2][uid3] = {}
    print json.dumps(team, indent=4)


if __name__ == '__main__':
    # test_users()
    test_team(1)
