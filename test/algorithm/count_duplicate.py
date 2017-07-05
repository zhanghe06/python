#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: count_duplicate.py
@time: 2017/6/17 下午12:32

@title: 查找集合中重复元素的个数
"""


from collections import Counter

print Counter([1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# Counter({2: 4, 4: 4, 3: 3, 1: 1})


if __name__ == '__main__':
    pass
