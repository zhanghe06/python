#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: variance.py
@time: 2017/10/8 下午9:55

@title: 方差
"""


import random
import math
import time
from decimal import Decimal


def standard_deviation(list_num):
    """
    标准差
    :param list_num:
    :return:
    """
    len_num = len(list_num)
    sum_num = 0.0
    sum_square = 0.0
    for i in list_num:
        sum_num += i
        sum_square += i ** 2
    mean = sum_num / len_num
    var = sum_square / len_num - mean ** 2  # 方差
    res = Decimal(round(math.sqrt(var) / 100) * 100)  # 标准差改良版
    return res


def match(list_a, list_b):
    """
    匹配测试
    :param list_a:
    :param list_b:
    :return:
    """
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    print 'list_a 和', sum_a
    print 'list_b 和', sum_b
    if sum_a != sum_b:
        raise Exception('金额不匹配')
    print 'list_a 标准差', standard_deviation(list_a)
    print 'list_b 标准差', standard_deviation(list_b)
    list_a_new, list_b_new, list_match = [], [], []
    while list_a or list_b:
        max_a = max(list_a) if list_a else 0
        max_b = max(list_b) if list_b else 0

        if max_a >= max_b:
            list_a.remove(max_a)
            list_a_new.append(max_a)
            match_a = [max_a]
            match_b = []
            while sum(match_a) != sum(match_b):
                min_b = min(list_b) if list_b else 0
                need_b = sum(match_a) - sum(match_b)

                if need_b in list_b:
                    get_b = need_b
                    list_b.remove(need_b)
                elif need_b > min_b:
                    get_b = min_b
                    list_b.remove(min_b)
                else:
                    # 拆分最小值
                    get_b = need_b
                    list_b.remove(min_b)
                    list_b.append(min_b - need_b)

                list_b_new.append(get_b)
                match_b.append(get_b)
        else:
            list_b.remove(max_b)
            list_b_new.append(max_b)
            match_a = []
            match_b = [max_b]
            while sum(match_a) != sum(match_b):
                min_a = min(list_a) if list_a else 0
                need_a = sum(match_b) - sum(match_a)

                if need_a in list_a:
                    get_a = need_a
                    list_a.remove(need_a)
                elif need_a > min_a:
                    get_a = min_a
                    list_a.remove(min_a)
                else:
                    # 拆分最小值
                    get_a = need_a
                    list_a.remove(min_a)
                    list_a.append(min_a - need_a)

                list_a_new.append(get_a)
                match_a.append(get_a)

        match_num = (match_a, match_b)
        list_match.append(match_num)
    return list_a_new, list_b_new, list_match


def match_dict_list(x, y):
    """
    匹配测试
    :param x:
    :param y:
    :return:
    """
    print 'x', x
    print 'y', y

    # 列表转字典
    m_d = {}
    for i in x:
        m_d[i['id']] = i['price']
    n_d = {}
    for i in y:
        n_d[i['id']] = i['price']

    sum_a = sum(m_d.values())
    sum_b = sum(n_d.values())
    print 'list_a 和', sum_a
    print 'list_b 和', sum_b
    if sum_a != sum_b:
        raise Exception('金额不匹配')
    print 'list_a 标准差', standard_deviation(m_d.values())
    print 'list_b 标准差', standard_deviation(n_d.values())
    list_a_new, list_b_new, list_match = [], [], []

    while m_d.values() or n_d.values():
        max_a = max(m_d.values()) if m_d.values() else 0
        max_b = max(n_d.values()) if n_d.values() else 0

        if max_a >= max_b:
            max_a_id = m_d.keys()[m_d.values().index(max_a)]
            m_d.pop(max_a_id)
            list_a_new.append(max_a)
            match_a_item = {'id': max_a_id, 'price': max_a}
            match_a_items = [match_a_item]

            match_a = [max_a]
            match_b = []
            match_b_items = []

            while sum(match_a) != sum(match_b):
                min_b = min(n_d.values()) if n_d.values() else 0
                need_b = sum(match_a) - sum(match_b)

                if need_b in n_d.values():
                    get_b = need_b
                    b_id = n_d.keys()[n_d.values().index(get_b)]
                    n_d.pop(b_id)
                elif need_b > min_b:
                    get_b = min_b
                    b_id = n_d.keys()[n_d.values().index(get_b)]
                    n_d.pop(b_id)
                else:
                    # 拆分最小值
                    get_b = need_b
                    b_id = n_d.keys()[n_d.values().index(min_b)]
                    n_d[b_id] = min_b - get_b

                list_b_new.append(get_b)
                match_b.append(get_b)
                match_b_item = {'id': b_id, 'price': get_b}
                match_b_items.append(match_b_item)
        else:
            max_b_id = n_d.keys()[n_d.values().index(max_b)]
            n_d.pop(max_b_id)
            list_b_new.append(max_b)
            match_b_item = {'id': max_b_id, 'price': max_b}
            match_b_items = [match_b_item]

            match_a = []
            match_b = [max_b]
            match_a_items = []

            while sum(match_a) != sum(match_b):
                min_a = min(m_d.values()) if m_d.values() else 0
                need_a = sum(match_b) - sum(match_a)

                if need_a in m_d.values():
                    get_a = need_a
                    a_id = m_d.keys()[m_d.values().index(get_a)]
                    m_d.pop(a_id)
                elif need_a > min_a:
                    get_a = min_a
                    a_id = m_d.keys()[m_d.values().index(get_a)]
                    m_d.pop(a_id)
                else:
                    # 拆分最小值
                    get_a = need_a
                    a_id = m_d.keys()[m_d.values().index(min_a)]
                    m_d[a_id] = min_a - get_a

                list_a_new.append(get_a)
                match_a.append(get_a)
                match_a_item = {'id': a_id, 'price': get_a}
                match_a_items.append(match_a_item)

        match_item = (match_a_items, match_b_items)
        list_match.append(match_item)

    return list_a_new, list_b_new, list_match


def test_standard_deviation():
    """
    测试标准差
    :return:
    """
    test_list_num = range(8000, 10000, 500)
    print test_list_num
    print standard_deviation(test_list_num)


def test_match():
    """
    测试匹配
    :return:
    """
    # 普通情况
    # list_a = [20000, 18000, 18000, 6000]
    # list_b = [18000, 16000, 14000, 8000, 2000, 2000, 2000]

    # 恰好拼凑（无需拆分，只需组合）
    # list_a = [20000, 18000, 16000]
    # list_b = [18000, 16000, 14000, 2000, 2000, 2000]

    # 差大于最小值
    # list_a = [21000, 18000, 16000]
    # list_b = [18000, 16000, 14000, 2000, 2000, 2000, 1000]

    # 差小于最小值（互相拆分）
    list_a = [21000, 18000, 16000]
    list_b = [20000, 16000, 19000]

    print 'list_a', list_a
    print 'list_b', list_b
    list_a_new, list_b_new, list_match = match(list_a, list_b)
    print 'list_a_new', list_a_new
    print 'list_b_new', list_b_new
    print 'list_match', list_match


def test_match_dict_list():
    """
    测试匹配(字典列表)
    :return:
    """
    # 普通情况
    # list_a = [20000, 18000, 18000, 6000]
    # list_b = [18000, 16000, 14000, 8000, 2000, 2000, 2000]

    # 恰好拼凑（无需拆分，只需组合）
    # list_a = [20000, 18000, 16000]
    # list_b = [18000, 16000, 14000, 2000, 2000, 2000]
    # m = [{'id': 1, 'price': 20000}, {'id': 2, 'price': 18000}, {'id': 3, 'price': 16000}]
    # n = [{'id': 1, 'price': 18000}, {'id': 2, 'price': 16000}, {'id': 3, 'price': 14000}, {'id': 4, 'price': 2000}, {'id': 5, 'price': 2000}, {'id': 6, 'price': 2000}]

    # 差大于最小值
    # list_a = [21000, 18000, 16000]
    # list_b = [18000, 16000, 14000, 2000, 2000, 2000, 1000]
    # m = [{'id': 1, 'price': 21000}, {'id': 2, 'price': 18000}, {'id': 3, 'price': 16000}]
    # n = [{'id': 1, 'price': 18000}, {'id': 2, 'price': 16000}, {'id': 3, 'price': 14000}, {'id': 4, 'price': 2000}, {'id': 5, 'price': 2000}, {'id': 6, 'price': 2000}, {'id': 7, 'price': 1000}]

    # 差小于最小值（互相拆分）
    # list_a = [21000, 18000, 16000]
    # list_b = [20000, 16000, 19000]
    m = [{'id': 1, 'price': 21000}, {'id': 2, 'price': 18000}, {'id': 3, 'price': 16000}]
    n = [{'id': 1, 'price': 20000}, {'id': 2, 'price': 16000}, {'id': 3, 'price': 19000}]

    list_a_new, list_b_new, list_match = match_dict_list(m, n)
    print 'list_a_new', list_a_new
    print 'list_b_new', list_b_new
    print 'list_match', list_match


def random_choice_list():
    """
    步骤：
    1、设定匹配总金额：total_price
    2、根据标准差估算取值个数：random_num
    3、随机选取 n 个元素求和等于 total_price
    :return:
    """
    time_out = 3  # 正常速度 0.00003
    total_price = 40000
    test_random_list = [21000, 18000, 16000, 4000, 20000, 7000]

    sum_num = sum(test_random_list)
    len_num = len(test_random_list)
    print 'sum_num', sum_num
    print 'len_num', len_num

    choice_num = int(min(round(len_num / (sum_num / total_price)), len_num))

    print 'choice_num', choice_num
    std_dev = standard_deviation(test_random_list)
    print 'std_dev', std_dev
    for i in test_random_list:
        print round(i / std_dev)

    choice_list = []
    c = 0
    start_time = time.time()
    while sum(choice_list) != total_price:
        if time.time() - start_time > time_out:
            choice_list = []
            break
        c += 1
        print '随机次数', c
        choice_list = random.sample(test_random_list, choice_num)

    if choice_list:
        print choice_list
    else:
        print '超时'


def random_choice_dict_list():
    """
    步骤：
    1、设定匹配总金额：total_price
    2、根据标准差估算取值个数：random_num
    3、随机选取 n 个元素求和等于 total_price
    :return:
    """
    time_out = 3  # 正常速度 0.00003
    total_price = 40000
    # test_random_list = [21000, 18000, 16000, 4000, 20000, 7000]
    test_random_dict_list = [{'id': 1, 'price': 21000}, {'id': 2, 'price': 18000}, {'id': 3, 'price': 16000}, {'id': 4, 'price': 4000}, {'id': 5, 'price': 20000}, {'id': 6, 'price': 7000}, {'id': 7, 'price': 16000}]

    test_random_list = [item['price'] for item in test_random_dict_list]
    sum_num = sum(test_random_list)
    len_num = len(test_random_list)
    print 'sum_num', sum_num
    print 'len_num', len_num

    choice_num = int(min(round(len_num / (sum_num / total_price)), len_num))

    print 'choice_num', choice_num
    std_dev = standard_deviation(test_random_list)
    print 'std_dev', std_dev
    for i in test_random_list:
        print round(i / std_dev)

    choice_list = []
    c = 0
    start_time = time.time()
    while sum(choice_list) != total_price:
        if time.time() - start_time > time_out:
            choice_list = []
            break
        c += 1
        print '随机次数', c
        choice_list = random.sample(test_random_list, choice_num)

    if choice_list:
        res_choice_dict_list = []
        print choice_list
        for i in test_random_dict_list:
            if i['price'] in choice_list:
                res_choice_dict_list.append(i)
                choice_list.remove(i['price'])
        print res_choice_dict_list
    else:
        print '超时'


if __name__ == '__main__':
    # test_standard_deviation()
    # test_match()
    test_match_dict_list()
    # random_choice_list()
    # random_choice_dict_list()
