# encoding: utf-8
"""
将两个list组合为dict
"""
__author__ = 'zhanghe'


def test_01():
    """
    key value 数量相等
    """
    list_a = ['a', 'b', 'c']
    list_b = ['10', '20', '30']

    print dict(zip(list_a, list_b))
    print dict(zip(list_a[::-1], list_b))


def test_02():
    """
    key 数量小于 value
    """
    list_a = ['a', 'b', 'c']
    list_b = ['10', '20', '30', '50']

    print dict(zip(list_a, list_b))
    print dict(zip(list_a[::-1], list_b))


def test_03():
    """
    key 数量大于 value
    """
    list_a = ['a', 'b', 'c', 'd']
    list_b = ['10', '20', '30']

    print dict(zip(list_a, list_b))
    print dict(zip(list_a[::-1], list_b))


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()


"""
测试结果：
{'a': '10', 'c': '30', 'b': '20'}
{'a': '30', 'c': '10', 'b': '20'}
{'a': '10', 'c': '30', 'b': '20'}
{'a': '30', 'c': '10', 'b': '20'}
{'a': '10', 'c': '30', 'b': '20'}
{'c': '20', 'b': '30', 'd': '10'}
"""
