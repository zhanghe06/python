#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tools_data.py
@time: 2017/3/28 上午12:41
"""


from random import randint


data_type_list = ['odd', 'even']


def write_file(file_name, data_type=None):
    """
    写文件
    :param file_name:
    :param data_type:
    :return:
    """
    c = 0
    num = 0
    if data_type == 'odd':  # 奇数
        num = 1
    if data_type == 'even':  # 偶数
        num = 2
    while c < 100000:
        c += 1
        num += randint(0, 4)*2
        with open(file_name, 'a') as f:
            f.write('%s\n' % num)


if __name__ == '__main__':
    write_file('a.log', 'odd')
    write_file('b.log', 'even')
