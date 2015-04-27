# encoding: utf-8
__author__ = 'zhanghe'

import time
import threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


def run_thread_lock(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


def run_without_lock():
    """
    不带锁的主程序
    :return:
    """
    start_time = time.time()
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print end_time - start_time
    print balance


def run_with_lock():
    """
    带锁的主程序
    :return:
    """
    start_time = time.time()
    t1 = threading.Thread(target=run_thread_lock, args=(5,))
    t2 = threading.Thread(target=run_thread_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print end_time - start_time
    print balance

if __name__ == '__main__':
    # 这是银行账户修改的简单例子，以下分别测试不加锁与加锁的运行情况
    run_without_lock()
    # run_with_lock()


'''
run_without_lock()运行结果：
0.209647893906
8（不固定）

run_with_lock()运行结果：
0.441839933395
0

可以看出，在有全局变量的情况下，需要用锁机制防止修改过程中的冲突
这样一来，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
多线程的并发在Python中就是一个美丽的梦。

多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响。

深入分析：
一个任务在执行的过程中大部分时间都在等待IO操作，
单进程单线程模型会导致别的任务无法并行执行，
因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。
现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO
如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，
这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，
它在单核CPU上采用单进程模型就可以高效地支持多任务。
在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。
由于系统总的进程数量十分有限，因此操作系统调度非常高效。


处理多任务推荐的做法是： 多进程 + 协程
'''
