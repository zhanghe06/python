# encoding: utf-8
"""
将两个list组合为dict
"""
__author__ = 'zhanghe'


import itertools
import json


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


def test_04():
    """
     测试列表子元素算术运算
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
    print c


def test_group():
    """
    测试分组
    """
    a = [
        {
            "update_time": "2016-08-17 13:51:54",
            "name": "尺寸",
            "value": "小",
            "create_time": "2016-08-17 13:51:54",
            "id": 1,
            "product_id": 1
        },
        {
            "update_time": "2016-08-17 13:51:54",
            "name": "尺寸",
            "value": "大",
            "create_time": "2016-08-17 13:51:54",
            "id": 2,
            "product_id": 1
        },
        {
            "update_time": "2016-08-17 13:51:54",
            "name": "颜色",
            "value": "蓝",
            "create_time": "2016-08-17 13:51:54",
            "id": 3,
            "product_id": 1
        },
        {
            "update_time": "2016-08-17 13:51:54",
            "name": "颜色",
            "value": "绿",
            "create_time": "2016-08-17 13:51:54",
            "id": 4,
            "product_id": 1
        },
        {
            "update_time": "2016-08-17 13:51:55",
            "name": "颜色",
            "value": "红",
            "create_time": "2016-08-17 13:51:55",
            "id": 5,
            "product_id": 1
        }
    ]

    result = dict([(g, [i['value'] for i in list(k)]) for g, k in itertools.groupby(a, lambda x: x['name'])])
    print json.dumps(result, indent=4, ensure_ascii=False)
    result = [({'name': g, 'value': [i['value'] for i in list(k)]}) for g, k in itertools.groupby(a, lambda x: x['name'])]
    print json.dumps(result, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()
    test_04()
    test_group()


"""
测试结果：
{'a': '10', 'c': '30', 'b': '20'}
{'a': '30', 'c': '10', 'b': '20'}
{'a': '10', 'c': '30', 'b': '20'}
{'a': '30', 'c': '10', 'b': '20'}
{'a': '10', 'c': '30', 'b': '20'}
{'c': '20', 'b': '30', 'd': '10'}
{
    "尺寸": [
        "小",
        "大"
    ],
    "颜色": [
        "蓝",
        "绿",
        "红"
    ]
}
[
    {
        "name": "尺寸",
        "value": [
            "小",
            "大"
        ]
    },
    {
        "name": "颜色",
        "value": [
            "蓝",
            "绿",
            "红"
        ]
    }
]
"""
