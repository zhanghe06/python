#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: factorial.py
@time: 2017/6/17 上午11:53

@title: 写一个算法计算n的阶乘末尾0的个数
"""


from math import factorial


print factorial(10)  # 3628800
print factorial(25)  # 15511210043330985984000000
print factorial(50)  # 30414093201713378043612608166064768844377641568960512000000000000


def end_zero_count(n):
    """
    n的阶乘末尾0的个数
    （求n的阶乘 质因数5的幂）
    :param n:
    :return:
    """
    num = 0
    while 1:
        n /= 5
        if n:
            num += n
        else:
            break
    return num


if __name__ == '__main__':
    print end_zero_count(10)  # 2
    print end_zero_count(25)  # 6
    print end_zero_count(50)  # 12
