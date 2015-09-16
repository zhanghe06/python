# encoding: utf-8
__author__ = 'zhanghe'


import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
# 添加数据
print r.set('foo', 'bar')  # True
# 查询数据
print r.get('foo')  # bar


"""
测试结果：

程序启动前
redis 127.0.0.1:6379> keys *
(empty list or set)

启动后
redis 127.0.0.1:6379> keys *
1) "foo"

清除数据
redis 127.0.0.1:6379> del foo
(integer) 1
redis 127.0.0.1:6379> keys *
(empty list or set)
"""
