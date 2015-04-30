# encoding: utf-8
__author__ = 'zhanghe'

import time
from tools import time_log
# import gevent
# from gevent import monkey
# monkey.patch_all()
from multiprocessing import Pool


# @time_log.time_log
def foo_cpu(name):
    """
    模拟CPU密集场景（CPU单独占用2S）
    :return:
    """
    start_time = time.time()
    while 1:
        end_time = time.time()
        if (end_time - start_time) >= 2:
            print name
            break


@time_log.time_log
def run_cpu_gevent():
    threads = [gevent.spawn(foo_cpu, i) for i in range(9)]
    gevent.joinall(threads)


@time_log.time_log
def run_cpu_pool():
    p = Pool()
    for i in range(9):
        p.apply_async(foo_cpu, args=(i,))
    p.close()
    p.join()


# @time_log.time_log
def foo_io(name):
    """
    模拟IO密集场景（CPU挂起2S）
    :return:
    """
    while 1:
        time.sleep(2)
        print name
        break


@time_log.time_log
def run_io_gevent():
    threads = [gevent.spawn(foo_io, i) for i in range(9)]
    gevent.joinall(threads)


@time_log.time_log
def run_io_pool():
    p = Pool()
    for i in range(9):
        p.apply_async(foo_io, args=(i,))
    p.close()
    p.join()


if __name__ == '__main__':
    # CPU密集场景（适用于pool）
    # run_cpu_gevent()
    # run_cpu_pool()  # 需要注释掉gevent

    # IO密集场景（适用于gevent）
    # run_io_gevent()
    run_io_pool()  # 需要注释掉gevent

# CPU密集场景下gevent测试结果：
# 方法run_cpu_gevent开始时间：Thu Apr 30 13:11:01 2015
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 方法run_cpu_gevent结束时间：Thu Apr 30 13:11:19 2015
# 方法run_cpu_gevent运行时间：18.00S

# CPU密集场景下pool测试结果：
# 方法run_cpu_pool开始时间：Thu Apr 30 13:09:08 2015
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 方法run_cpu_pool结束时间：Thu Apr 30 13:09:14 2015
# 方法run_cpu_pool运行时间：6.04S

# IO密集场景下gevent测试结果：
# 方法run_io_gevent开始时间：Thu Apr 30 13:12:44 2015
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 方法run_io_gevent结束时间：Thu Apr 30 13:12:46 2015
# 方法run_io_gevent运行时间：2.00S

# IO密集场景下pool测试结果：
# 方法run_io_pool开始时间：Thu Apr 30 13:13:54 2015
# 0
# 2
# 1
# 3
# 5
# 4
# 7
# 6
# 8
# 方法run_io_pool结束时间：Thu Apr 30 13:14:00 2015
# 方法run_io_pool运行时间：6.12S

# 测试机器为4核心
# pool 不能与 gevent同时存在，一个同步，一个异步。所以当测试pool时，需要注释掉gevent及补丁
# 以上结果可以分析出：
# 一、对于CPU密集运算的场景，gevent无用武之地，需要多进程来支持
# 二、对于IO密集运算的场景，gevent再好不过了，pool提升不明显
