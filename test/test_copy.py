#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_copy.py
@time: 16-2-17 上午11:07
"""

import copy


def test_01():
    """
    测试可变类型对象的拷贝
    """
    a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
    b = a  # 赋值，传对象的引用
    c = copy.copy(a)  # 对象拷贝，浅拷贝
    d = copy.deepcopy(a)  # 对象拷贝，深拷贝

    a.append(5)  # 修改对象a
    a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

    print 'a = ', a
    print 'b = ', b
    print 'c = ', c
    print 'd = ', d


def test_02():
    """
    测试不可变类型对象的拷贝
    """
    a = [1, 2, 3, 4, 5]  # 原始对象
    b = a  # 赋值，传对象的引用
    c = copy.copy(a)  # 对象拷贝，浅拷贝
    d = copy.deepcopy(a)  # 对象拷贝，深拷贝

    a[4] = 6  # 修改对象a

    print 'a = ', a
    print 'b = ', b
    print 'c = ', c
    print 'd = ', d


if __name__ == '__main__':
    test_01()
    test_02()


"""
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]
a =  [1, 2, 3, 4, 6]
b =  [1, 2, 3, 4, 6]
c =  [1, 2, 3, 4, 5]
d =  [1, 2, 3, 4, 5]

如果对象本身是不可变的，那么浅拷贝时也会产生两个值
顺便回顾下Python标准类型的分类：
可变类型： 列表，字典
不可变类型：数字，字符串，元组
"""
