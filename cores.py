# encoding: utf-8
__author__ = 'zhanghe'

# from multiprocessing import Pool
from multiprocessing.dummy import Pool
import gevent
import os
import time
import random
from tools import time_log
from gevent import monkey
monkey.patch_all()


def long_time_task(name):
    """
    任务运行时间
    :param name:
    :return:
    """
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    # time.sleep(random.random() * 3)
    time.sleep(0.3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


@time_log.time_log
def run():
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all sub processes done...'
    p.close()
    p.join()
    print 'All sub processes done.'


@time_log.time_log
def run_gevent():
    threads = [gevent.spawn(long_time_task, i) for i in range(9)]
    gevent.joinall(threads)

if __name__ == '__main__':
    # run()
    run_gevent()

# 这是一个多进程的例子，同时运行的进程数与机器的核心数是对应的
# 根据任务池同时运行的进程数也可以看出当前cpu的核心数，运行结果：
# 可以看出进程池子最多有4个进程
# Parent process 10903.
# Waiting for all sub processes done...
# Run task 0 (10904)...
# Run task 1 (10905)...
# Run task 2 (10906)...
# Run task 3 (10907)...
# Task 2 runs 1.56 seconds.
# Run task 4 (10906)...
# Task 4 runs 0.18 seconds.
# Run task 5 (10906)...
# Task 3 runs 2.04 seconds.
# Run task 6 (10907)...
# Task 6 runs 0.05 seconds.
# Run task 7 (10907)...
# Task 1 runs 2.53 seconds.
# Run task 8 (10905)...
# Task 0 runs 2.62 seconds.
# Task 5 runs 1.52 seconds.
# Task 8 runs 1.68 seconds.
# Task 7 runs 2.77 seconds.
# All sub processes done.


# 查看系统CPU参数，四核心
# zhanghe@ubuntu:~$ cat /proc/cpuinfo | grep cpu
# cpu family : 6
# cpu MHz : 800.000
# cpu cores : 4
# cpuid level : 13
# cpu family : 6
# cpu MHz : 800.000
# cpu cores : 4
# cpuid level : 13
# cpu family : 6
# cpu MHz : 3101.000
# cpu cores : 4
# cpuid level : 13
# cpu family : 6
# cpu MHz : 800.000
# cpu cores : 4
# cpuid level : 13
# zhanghe@ubuntu:~$


# from multiprocessing import Pool
# time.sleep(0.3)
# 方法run开始时间：Thu Apr 30 00:48:04 2015
# Parent process 17113.
# Waiting for all sub processes done...
# Run task 1 (17115)...
# Run task 0 (17114)...
# Task 1 runs 0.30 seconds.
# Run task 2 (17115)...
# Task 0 runs 0.30 seconds.
# Run task 3 (17114)...
# Task 2 runs 0.30 seconds.
# Run task 4 (17115)...
# Task 3 runs 0.30 seconds.
# Run task 5 (17114)...
# Task 4 runs 0.30 seconds.
# Run task 6 (17115)...
# Task 5 runs 0.30 seconds.
# Run task 7 (17114)...
# Task 6 runs 0.30 seconds.
# Run task 8 (17115)...
# Task 7 runs 0.30 seconds.
# Task 8 runs 0.30 seconds.
# All sub processes done.
# 方法run结束时间：Thu Apr 30 00:48:05 2015
# 方法run运行时间：1.72S


# from multiprocessing.dummy import Pool
# time.sleep(0.3)
# 方法run开始时间：Thu Apr 30 00:51:27 2015
# Parent process 17244.
# Waiting for all sub processes done...
# Run task 0 (17244)...
# Run task 1 (17244)...
# Task 0 runs 0.30 seconds.
#  Task 1 runs 0.30 seconds.Run task 2 (17244)...
#
# Run task 3 (17244)...
# Task 2 runs 0.30 seconds.Task 3 runs 0.30 seconds.
# Run task 4 (17244)...
#
# Run task 5 (17244)...
# Task 4 runs 0.30 seconds.
# Task 5 runs 0.30 seconds.Run task 6 (17244)...
#
# Run task 7 (17244)...
# Task 6 runs 0.30 seconds.
# Run task 8 (17244)...
# Task 7 runs 0.30 seconds.
# Task 8 runs 0.30 seconds.
# All sub processes done.
# 方法run结束时间：Thu Apr 30 00:51:29 2015
# 方法run运行时间：1.54S


# import gevent
# time.sleep(0.3)
# 方法run_gevent开始时间：Thu Apr 30 01:13:52 2015
# Run task 0 (17964)...
# Task 0 runs 0.30 seconds.
# Run task 1 (17964)...
# Task 1 runs 0.30 seconds.
# Run task 2 (17964)...
# Task 2 runs 0.30 seconds.
# Run task 3 (17964)...
# Task 3 runs 0.30 seconds.
# Run task 4 (17964)...
# Task 4 runs 0.30 seconds.
# Run task 5 (17964)...
# Task 5 runs 0.30 seconds.
# Run task 6 (17964)...
# Task 6 runs 0.30 seconds.
# Run task 7 (17964)...
# Task 7 runs 0.30 seconds.
# Run task 8 (17964)...
# Task 8 runs 0.30 seconds.
# 方法run_gevent结束时间：Thu Apr 30 01:13:55 2015
# 方法run_gevent运行时间：2.74S


# import gevent
# time.sleep(0.3)
# from gevent import monkey
# monkey.patch_all()
# 方法run_gevent开始时间：Thu Apr 30 01:17:05 2015
# Run task 0 (18038)...
# Run task 1 (18038)...
# Run task 2 (18038)...
# Run task 3 (18038)...
# Run task 4 (18038)...
# Run task 5 (18038)...
# Run task 6 (18038)...
# Run task 7 (18038)...
# Run task 8 (18038)...
# Task 0 runs 0.30 seconds.
# Task 1 runs 0.30 seconds.
# Task 2 runs 0.30 seconds.
# Task 3 runs 0.30 seconds.
# Task 4 runs 0.30 seconds.
# Task 5 runs 0.30 seconds.
# Task 6 runs 0.30 seconds.
# Task 7 runs 0.30 seconds.
# Task 8 runs 0.30 seconds.
# 方法run_gevent结束时间：Thu Apr 30 01:17:05 2015
# 方法run_gevent运行时间：0.32S

# 结果可以看出使用multiprocessing.dummy模块比multiprocessing速度略有提升
# 使用打补丁后的gevent，效率最快