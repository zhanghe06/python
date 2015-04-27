# encoding: utf-8
__author__ = 'zhanghe'

from multiprocessing import Process, Queue
import time
import random


def write(q):
    """
    写数据进程执行的代码
    :param q:
    :return:
    """
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    """
    读数据进程执行的代码
    :param q:
    :return:
    """
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程，一个写，一个读，从而实现进程间通信：
    queue = Queue()
    pw = Process(target=write, args=(queue,))
    pr = Process(target=read, args=(queue,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()