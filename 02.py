# coding:utf-8
__author__ = 'zhanghe'
import gevent
import random
import time
# from gevent import monkey
# monkey.patch_all()


def task(pid):
    gevent.sleep(random.randint(0, 2)*0.001)  # 模拟真实环境，等待时间随机，同步：0.183，顺序执行；异步：0.012，随机执行。
    # gevent.sleep(0.1)  # 如果等待时间固定，同步：10秒，顺序执行；异步：0.1秒多，表现为顺序执行。
    print('Task', pid, 'done')


def synchronous():  # 同步
    # for i in range(1,100):
    for i in xrange(100):
        task(i)


def asynchronous():  # 异步
    threads = [gevent.spawn(task, i) for i in xrange(100)]
    gevent.joinall(threads)


print('Synchronous:')
start = time.time()
synchronous()
stop = time.time()
print stop-start


print('Asynchronous:')
start = time.time()
asynchronous()
stop = time.time()
print stop-start

# 测试结果：
# gevent.sleep(0.1) 第一次
# 猴子补丁，同步：10.141；异步0.111
# 没有补丁，同步：10.148；异步0.126
# gevent.sleep(0.1) 第二次
# 猴子补丁，同步：10.241；异步0.112
# 没有补丁，同步：10.130；异步0.113
# gevent.sleep(random.randint(0,2)*0.001) 第一次
# 猴子补丁，同步：0.214；异步0.013
# 没有补丁，同步：0.182；异步0.015
# gevent.sleep(random.randint(0,2)*0.001) 第二次
# 猴子补丁，同步：0.176；异步0.016
# 没有补丁，同步：0.183；异步0.011
