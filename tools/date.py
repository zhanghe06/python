# coding=utf-8
__author__ = 'zhanghe'


def add_time(time_str, second):
    """
    添加时间
    :param time_str:
    :param second:
    :return:
    """
    if time_str is None:
        return '0000-00-00 00:00:00'
    import time
    new_time_stamp = time.localtime(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')) + second)
    return time.strftime('%Y-%m-%d %H:%M:%S', new_time_stamp)
