#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ss.py
@time: 2017/6/19 下午11:51

@title: 链表
"""


# 生成器都是Iterator对象


# 方式一
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])  # 列表转生成器
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print x
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


# 方式二
l = [1, 2, 3, 4, 5]
a = (i for i in l)  # 列表转生成器
print next(a)  # next 是生成器的方法(需要考虑StopIteration异常情况)


def linked_list_invert(ol):
    """
    链表反转
    :param ol:
    :return:
    """
    l = []
    for i in ol:
        l.insert(0, i)
    nl = (i for i in l)
    return nl


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    a = (i for i in l)
    s = linked_list_invert(a)
    print s.next()
    print s.next()
    print s.next()
    print s.next()
    print s.next()
