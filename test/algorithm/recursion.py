#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: recursion.py
@time: 2017/6/17 下午4:26

@title: 递归实现阶乘
"""


def factorial(n):
    print n
    if n == 1:
        return 1  # 递归结束
    return n * factorial(n - 1)  # 问题规模减1，递归调用


nodes = [
    {'id': 1, 'parent': None},
    {'id': 2, 'parent': 1},
    {'id': 3, 'parent': 1},
    {'id': 4, 'parent': 2},
    {'id': 5, 'parent': 2},
    {'id': 6, 'parent': 5},
    {'id': 7, 'parent': 6},
    {'id': 8, 'parent': 3}
]


node_list = []


def pop_list(nodes, parent=None, node_list=None):
    """
    递归父子关系
    :param nodes:
    :param parent:
    :param node_list:
    :return:
    """
    if parent is None:
        return node_list
    next_parent = None
    node_list.append([])
    for node in nodes:
        if node['parent'] == parent:
            node_list[-1].append(node)
        if node['id'] == parent:
            next_parent = node['parent']

    pop_list(nodes, next_parent, node_list)
    return node_list

print pop_list(nodes, 5, node_list)


if __name__ == '__main__':
    print factorial(10)
