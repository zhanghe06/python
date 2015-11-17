# encoding: utf-8
__author__ = 'zhanghe'


import math


def test_01(score, test_range):
    """
    测试期望工资与薪资范围的匹配程度
    :return:
    """
    print score
    print test_range
    result = 1
    if score not in test_range:
        result = 1-min(abs(score-test_range[0]), abs(score-test_range[1]))/(score+sum(test_range)/2.0)
    print '评分：%.2f\n' % result


def test_02(score, test_range):
    """
    测试二(欧氏距离)
    """
    avg_rang = sum(test_range)/2.0
    print math.sqrt(abs(score**2-avg_rang**2))


if __name__ == '__main__':
    test_01(20, [100, 200])
    test_01(100, [100, 200])
    test_01(90, [100, 200])
    test_01(1000, [100, 200])
    test_01(1000, [0, 0])
    test_01(1000, [10, 10])
    test_01(1000, [100, 100])
    test_01(1000, [1000, 1000])
    test_01(1000, [10000, 10000])
    test_01(1000, [80000, 100000])


"""
20
[100, 200]
评分：0.53

100
[100, 200]
评分：1.00

90
[100, 200]
评分：0.96

1000
[100, 200]
评分：0.30

1000
[0, 0]
评分：0.00

1000
[10, 10]
评分：0.02

1000
[100, 100]
评分：0.18

1000
[1000, 1000]
评分：1.00

1000
[10000, 10000]
评分：0.18

1000
[80000, 100000]
评分：0.13

"""
