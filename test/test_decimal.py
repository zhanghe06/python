#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_decimal.py
@time: 16-6-2 下午2:56
"""


from decimal import Decimal
import json

# float(浮点型[二进制]) 转 decimal(十进制)
# float 先转 str 再转 decimal
print Decimal('0.12'), repr(Decimal('0.12'))
print str(Decimal('0.12')), repr(str(Decimal('0.12')))
print Decimal(0.00), repr(Decimal(0.00))
print Decimal(0.12), repr(Decimal(0.12))
print Decimal(0.12)+Decimal(0.36), repr(Decimal(0.12)+Decimal(0.36))


p_info = {
    'p_name': 'a',
    'p_price': Decimal('8.12')
}

print p_info
# print json.dumps(p_info)  # raise TypeError(repr(o) + " is not JSON serializable")


def __default(obj):
    """
    支持datetime的json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, Decimal):
        return str(obj)
    else:
        raise TypeError('%r is not JSON serializable' % repr(obj))

print json.dumps(p_info, default=__default)

"""
# 测试结果：
0.12 Decimal('0.12')
0.12 '0.12'
0 Decimal('0')
0.11999999999999999555910790149937383830547332763671875 Decimal('0.11999999999999999555910790149937383830547332763671875')
0.4799999999999999822364316060 Decimal('0.4799999999999999822364316060')
{'p_price': Decimal('8.12'), 'p_name': 'a'}
{"p_price": "8.12", "p_name": "a"}

# 订单系统必须采用 Decimal 类型存储, 避免浮点型误差累计产生的效应
"""
