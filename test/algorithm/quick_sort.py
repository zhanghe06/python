#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: quick_sort.py
@time: 2017/6/19 下午10:20

@title: 快速排序
"""


def quick_sort(arr, f=''):
    """
    快速排序演示过程
    :param arr:
    :param f:
    :return:
    """
    print u'拆分', f, arr
    less = []
    pivot_list = []
    more = []
    if len(arr) <= 1:
        print u'合并', f, arr
        return arr
    else:
        pivot = arr[0]  # 将第一个值做为基准
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        print 'L', less, 'M', pivot_list, 'R', more
        less = quick_sort(less, f='less')
        more = quick_sort(more, f='more')
        print u'合并', f, less + pivot_list + more
        return less + pivot_list + more


def quicksort(a):
    if len(a) <= 1:
        return a  # 如果a为一位数则直接传回a
    l = [x for x in a[1:] if x <= a[0]]  # 输出排序后的比a[0]小的数列
    r = [x for x in a[1:] if x > a[0]]  # 输出排序后的比a[0]大的数列
    return quicksort(l) + [a[0]] + quicksort(r)


if __name__ == '__main__':
    quick_sort([8, 7, 3, 6, 86, 32, 6, 9, 4])


"""
拆分  [8, 7, 3, 6, 86, 32, 6, 9, 4]

L [7, 3, 6, 6, 4] M [8] R [86, 32, 9]
拆分 less [7, 3, 6, 6, 4]
L [3, 6, 6, 4] M [7] R []
拆分 less [3, 6, 6, 4]
L [] M [3] R [6, 6, 4]
拆分 less []
合并 less []
拆分 more [6, 6, 4]
L [4] M [6, 6] R []
拆分 less [4]
合并 less [4]
拆分 more []
合并 more []
合并 more [4, 6, 6]
合并 less [3, 4, 6, 6]
拆分 more []
合并 more []
合并 less [3, 4, 6, 6, 7]

拆分 more [86, 32, 9]
L [32, 9] M [86] R []
拆分 less [32, 9]
L [9] M [32] R []
拆分 less [9]
合并 less [9]
拆分 more []
合并 more []
合并 less [9, 32]
拆分 more []
合并 more []
合并 more [9, 32, 86]

合并  [3, 4, 6, 6, 7, 8, 9, 32, 86]
"""