#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: cart.py
@time: 16-1-27 上午10:27
"""


import redis


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Cart(object):
    """
    购物车
    """
    uid = ''
    prefix = ''

    def __init__(self, uid, prefix='cart'):
        self.uid = uid
        self.prefix = prefix

    def add_item(self, pid, num=1):
        """
        添加物品
        :param pid:
        :param num:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.uid, pid)
        # 判断物品是否存在
        if redis_client.exists(key):
            redis_client.hincrby(key, 'num', num)
        else:
            # 如果不存在，添加物品至购物车
            redis_client.hmset(key, {'pid': pid, 'num': num})
        return True

    def del_item(self, pid):
        """
        删除物品
        :param pid:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.uid, pid)
        # 判断物品是否存在
        if redis_client.exists(key):
            redis_client.delete(key)
        return True

    def increase(self, pid, num=1):
        """
        增加物品数量
        :param pid:
        :param num:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.uid, pid)
        # 判断物品是否存在
        if redis_client.exists(key):
            redis_client.hincrby(key, 'num', num)
            return True
        else:
            # 如果不存在，添加物品至购物车
            return False

    def decrease(self, pid, num=1):
        """
        减少物品数量
        :param pid:
        :param num:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.uid, pid)
        # 判断物品是否存在
        if redis_client.exists(key):
            if num >= int(redis_client.hget(key, 'num')):
                # 如果超过，设置默认最小数量
                redis_client.hmset(key, {'num': 1})
            else:
                redis_client.hincrby(key, 'num', -num)
        return True

    def cart_list(self):
        """
        显示购物车
        :return:
        """
        key = "%s:%s:*" % (self.prefix, self.uid)
        car_key_list = redis_client.keys(key)
        return [redis_client.hgetall(item) for item in car_key_list]

    def clean(self):
        """
        清空购物车
        :return: 0/int
        """
        key = "%s:%s:*" % (self.prefix, self.uid)
        car_key_list = redis_client.keys(key)
        return redis_client.delete(*car_key_list) if car_key_list else 0


def test():
    obj = Cart('02')
    print obj.cart_list()
    obj.add_item('3')
    print obj.cart_list()
    obj.del_item('4')
    print obj.cart_list()
    obj.increase('3')
    print obj.cart_list()
    obj.decrease('3')
    print obj.cart_list()
    obj.add_item('4')
    print obj.cart_list()
    obj.add_item('5', 10)
    print obj.cart_list()
    obj.decrease('4', 10)
    print obj.cart_list()


if __name__ == '__main__':
    test()


"""
测试结果
[]
[{'num': '1', 'pid': '3'}]
[{'num': '1', 'pid': '3'}]
[{'num': '2', 'pid': '3'}]
[{'num': '1', 'pid': '3'}]
[{'num': '1', 'pid': '4'}, {'num': '1', 'pid': '3'}]
[{'num': '10', 'pid': '5'}, {'num': '1', 'pid': '4'}, {'num': '1', 'pid': '3'}]
[{'num': '10', 'pid': '5'}, {'num': '1', 'pid': '4'}, {'num': '1', 'pid': '3'}]
"""
