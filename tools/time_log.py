# encoding: utf-8
__author__ = 'zhanghe'

import time


def time_log(func):
    """
    记录方法运行时间的装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kw):
        func_name = func.__name__
        start_time = time.time()
        print '方法%s开始时间：%s' % (func_name, time.ctime())
        back_func = func(*args, **kw)
        end_time = time.time()
        run_time = end_time - start_time
        print '方法%s结束时间：%s' % (func_name, time.ctime())
        print '方法%s运行时间：%0.2fS' % (func_name, run_time)
        return back_func
    return wrapper


def time_log_with_des(text='执行'):
    """
    记录方法运行时间的装饰器（带描述）
    :param text:
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kw):
            func_name = func.__name__
            start_time = time.time()
            print '%s方法%s开始时间：%s' % (text, func_name, time.ctime())
            back_func = func(*args, **kw)
            end_time = time.time()
            run_time = end_time - start_time
            print '%s方法%s结束时间：%s' % (text, func_name, time.ctime())
            print '%s方法%s运行时间：%0.2fS' % (text, func_name, run_time)
            return back_func
        return wrapper
    return decorator


# @time_log
# @time_log_with_des()
@time_log_with_des('调用')
def foo():
    for i in xrange(100000000):
        pass


if __name__ == '__main__':
    foo()