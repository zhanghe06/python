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
        with open(file_name, 'w') as f:
            f.write('%s\n' % num)


if __name__ == '__main__':
    write_file('data/a.log', 'odd')
    write_file('data/b.log', 'even')


"""
# 原始数据
✗ wc -l a.log
  100000 a.log
✗ wc -l b.log
  100000 b.log

# 验证数据
✗ wc -l n.log
  200000 n.log
✗ head -n 10 a.log
3
7
7
7
15
15
19
19
21
29
✗ head -n 10 b.log
2
8
8
10
10
14
16
20
28
30
✗ head -n 20 n.log
2
3
7
7
7
8
8
10
10
14
15
15
16
19
19
20
21
28
29
30

✗ tail -n 10 a.log
400495
400497
400501
400505
400505
400513
400517
400519
400527
400529
✗ tail -n 10 b.log
400474
400480
400484
400486
400494
400500
400508
400510
400512
400516
✗ tail -n 20 n.log
400484
400486
400487
400489
400494
400495
400497
400500
400501
400505
400505
400508
400510
400512
400513
400516
400517
400519
400527
400529
"""
