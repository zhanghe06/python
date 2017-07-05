#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sort.py
@time: 2017/6/7 上午9:48
"""


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print result
    return result


def merge_sort(lists):
    print lists
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    print '左 分',
    left = merge_sort(lists[:num])
    print '右 分',
    right = merge_sort(lists[num:])
    print '\t治',
    return merge(left, right)


if __name__ == '__main__':
    a = [7, 2, 4, 7, 9, 3, 5, 7, 8, 1, 3, 60, 4, 2, 6]
    print merge_sort(a)



"""
"""