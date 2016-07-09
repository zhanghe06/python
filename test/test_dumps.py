#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_dumps.py
@time: 16-4-11 下午8:57
"""


import json
from datetime import date, datetime
from decimal import Decimal


def __default(obj):
    """
    支持 datetime Decimal 的 json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, Decimal):
        return str(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)


row = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306
    },
    'proxy': [
        'http://127.0.0.1:1080',
        'https://127.0.0.1:1080'
    ],
    'test_none': None,
    'test_bool': True,
    'time': datetime.now(),
    'price': Decimal('12.68'),
    'time_list': [
        datetime.now()
    ]
}

print json.dumps(row, indent=4, ensure_ascii=False, default=__default)


"""
{
    "time_list": [
        "2016-07-09 23:02:12"
    ],
    "price": "12.68",
    "db": {
        "host": "127.0.0.1",
        "port": 3306
    },
    "test_bool": true,
    "test_none": null,
    "proxy": [
        "http://127.0.0.1:1080",
        "https://127.0.0.1:1080"
    ],
    "time": "2016-07-09 23:02:12"
}
"""