#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_reduce.py
@time: 2017-12-05 22:04
"""

import sys
import json
from functools import reduce


def mapif(s, pred=None, f=None):
    r = []
    c = 0
    for v in s:
        c += 1
        if pred(v):
            t = f(v)
        else:
            t = v
        r.append(t)
    return r


def partition(s, size=None, step=None):
    step = step or size

    def pred(e):
        i = s.index(e)
        n = i % size if size else 0
        return i == n

    def f(e):
        i = s.index(e)
        n = i % size if size else 0
        start = step * n
        end = start + size
        return s[start:end]

    p = mapif(s, pred, f)

    # r = [i for i in p if isinstance(i, list) and len(i) > 0]
    r = p
    print(r)
    return r


def test():
    partition(range(1, 9), 4)  # [[1, 2, 3, 4], [5, 6, 7, 8]]
    partition(range(1, 9), 4, 2)  # [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8]]
    partition(range(1, 9), 4, 5)  # [[1, 2, 3, 4], [6, 7, 8]]


if __name__ == '__main__':
    test()
