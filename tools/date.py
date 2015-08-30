# coding=utf-8
__author__ = 'zhanghe'

import time


def add_time(time_str, second):
    """
    添加时间
    :param time_str:
    :param second:
    :return:
    """
    if time_str is None:
        return '0000-00-00 00:00:00'
    new_time_stamp = time.localtime(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')) + second)
    return time.strftime('%Y-%m-%d %H:%M:%S', new_time_stamp)


def test():
    """
    测试代码
    """
    print time.time()
    print time.localtime()
    print time.ctime()
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print time.strftime("%Y-%m-%d", time.localtime()) + ' 09:00:00'
    print ' '.join((time.strftime("%Y-%m-%d", time.localtime()), '09:00:00'))


if __name__ == "__main__":
    test()


"""
1.python获取当前时间
    time.time() 获取当前时间戳
    time.localtime() 当前时间的struct_time形式
    time.ctime() 当前时间的字符串形式

2.python格式化字符串
    格式化成2009-03-20 11:45:39形式
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

3.python中时间日期格式化符号：
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00-59）
    %S 秒（00-59）

    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
"""