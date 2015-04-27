# encoding: utf-8
__author__ = 'zhanghe'

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    """
    任务运行时间
    :param name:
    :return:
    """
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all sub processes done...'
    p.close()
    p.join()
    print 'All sub processes done.'


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
