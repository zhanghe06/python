#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: merge_sort.py
@time: 2017/3/27 下午11:40
"""

from collections import deque
from copy import copy


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left_lst = merge_sort(lst[:middle])
    right_lst = merge_sort(lst[middle:])
    return merge(left_lst, right_lst)


def test_merge_simple():
    """
    测试简单归并
    :return:
    """
    test_list_a = [1, 3, 4, 5, 9]
    test_list_b = [1, 2, 3, 6, 8, 10, 11]
    test_list = copy(test_list_a)
    test_list.extend(test_list_b)

    print test_list_a
    print test_list_b
    print test_list
    print merge_sort(test_list)


def g_next(g_l):
    """
    获取生成器元素
    :param g_l:
    :return:
    """
    try:
        r = int(g_l.next())
    except StopIteration:
        r = None
    return r


def merge_sort_t(m, n):
    """
    归并排序两个迭代器
    :param m:
    :param n:
    :return:
    """
    # 去除换行并转生成器
    g_a = (a.strip() for a in m)
    g_b = (b.strip() for b in n)

    n_a = g_next(g_a)
    n_b = g_next(g_b)
    while 1:
        print n_a, n_b
        if not (n_a or n_b):
            return
        elif n_a is None and n_b is not None:
            yield '+', n_b
            n_b = g_next(g_b)
        elif n_b is None and n_a is not None:
            yield '-', n_a
            n_a = g_next(g_a)
        elif n_a <= n_b:
            print '-', n_a
            yield n_a
            n_a = g_next(g_a)
        else:
            print '+', n_b
            yield n_b
            n_b = g_next(g_b)


def test_merge_big_file():
    """
    测试大文件归并
    :return:
    """

    # 打开文件（文件本身就是迭代器）
    f_a = open('a.log', 'r')
    f_b = open('b.log', 'r')

    for i in merge_sort_t(f_a, f_b):
        print i

    # 关闭文件
    f_a.close()
    f_b.close()


if __name__ == '__main__':
    # test_merge_simple()
    test_merge_big_file()
