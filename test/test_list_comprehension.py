#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_list_comprehension.py
@time: 2017/7/25 下午5:37
"""


def run():
    """
    列表解析
    {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    []
    [1, 3, 2, 5, 4]  # 字典无序
    [1, 2, 3, 4, 5]
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
    :return:
    """
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    A1 = range(10)
    A2 = [i for i in A1 if i in A0]
    A3 = [A0[s] for s in A0]
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]

    print A0
    print A1
    print A2
    print A3
    print A4
    print A5
    print A6


if __name__ == '__main__':
    run()
    pass
