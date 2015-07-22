# encoding: utf-8
__author__ = 'zhanghe'

import time


interval = 1  # 循环任务执行间隔时间(单位秒)
start_time = '2015-07-22 23:20:00'  # 任务启动时间
end_time = '2015-07-22 23:20:20'  # 任务结束时间


def timed_task(func):
    """
    循环定时任务装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kw):
        global back_func
        run_time = time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))
        exit_time = time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S'))
        rest_time = run_time - time.time()  # 启动剩余时间
        if rest_time > 0:
            print '启动时间未到，程序等待执行'
        while True:
            status = 'wait'
            count = 0
            while run_time <= time.time():
                if exit_time <= time.time():
                    status = 'exit'
                    break
                status = 'run'
                count += 1
                print '程序正在执行，运行次数：%s' % count
                back_func = func(*args, **kw)
                time.sleep(interval)  # 等待循环
            if status == 'exit':
                print '结束时间已到，程序运行完毕'
                break
        if exit_time > time.time():
            return back_func
    return wrapper


@timed_task
def foo():
    print 'I Love Python'


if __name__ == '__main__':
    foo()


"""
测试结果：
启动时间未到，程序等待执行
程序正在执行，运行次数：1
I Love Python
程序正在执行，运行次数：2
I Love Python
程序正在执行，运行次数：3
I Love Python
程序正在执行，运行次数：4
I Love Python
程序正在执行，运行次数：5
I Love Python
程序正在执行，运行次数：6
I Love Python
程序正在执行，运行次数：7
I Love Python
程序正在执行，运行次数：8
I Love Python
程序正在执行，运行次数：9
I Love Python
程序正在执行，运行次数：10
I Love Python
程序正在执行，运行次数：11
I Love Python
程序正在执行，运行次数：12
I Love Python
程序正在执行，运行次数：13
I Love Python
程序正在执行，运行次数：14
I Love Python
程序正在执行，运行次数：15
I Love Python
程序正在执行，运行次数：16
I Love Python
程序正在执行，运行次数：17
I Love Python
程序正在执行，运行次数：18
I Love Python
程序正在执行，运行次数：19
I Love Python
程序正在执行，运行次数：20
I Love Python
结束时间已到，程序运行完毕
"""