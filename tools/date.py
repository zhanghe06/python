# coding=utf-8
__author__ = 'zhanghe'

import time
from datetime import datetime, timedelta
from pytz import timezone, utc


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


def interval_time(interval_type='year'):
    """
    获取时间差
    """
    # 方法一
    old_date = datetime.date(*time.strptime('2009-09-07', '%Y-%m-%d')[:3])
    new_date = datetime.date(*time.localtime()[:3])
    diff_days = (new_date-old_date).days
    print '%d' % round((diff_days if diff_days > 0 else 0)/365.0, 0)
    # 方法二
    diff_seconds = time.time() - time.mktime(time.strptime('2008-09-07', '%Y-%m-%d'))
    diff_years = '%d' % round((diff_seconds if diff_seconds > 0 else 0)/(365*24*3600), 0)
    print diff_years
    # diff_years = 0
    print (u'%s年工作经验' % diff_years) if int(diff_years) > 0 else u'无工作经验'


def time_pretty(delta_s):
    """
    时间友好显示
    :param delta_s:
    :return:
    """
    delta_s *= 1.00
    result = ''
    if delta_s >= (365 * 24 * 60 * 60):
        count = int(delta_s / (365 * 24 * 60 * 60))
        result += '%s年' % count
        delta_s -= count * 365 * 24 * 60 * 60
    if delta_s >= (30 * 24 * 60 * 60):
        count = int(delta_s / (30 * 24 * 60 * 60))
        result += '%s月' % count
        delta_s -= count * 30 * 24 * 60 * 60
    if delta_s >= (24 * 60 * 60):
        count = int(delta_s / (24 * 60 * 60))
        result += '%s天' % count
        delta_s -= count * 24 * 60 * 60
    if delta_s >= (60 * 60):
        count = int(delta_s / (60 * 60))
        result += '%s小时' % count
        delta_s -= count * 60 * 60
    if delta_s >= 60:
        count = int(delta_s / 60)
        result += '%s分' % count
        delta_s -= count * 60
    if delta_s > 0:
        count = int(delta_s)
        result += '%s秒' % count
    return result


def test():
    """
    测试代码
    """
    # 时间戳（timestamp）
    # 时间戳表示的是从 1970-01-01 00:00:00 开始按秒计算的偏移量。
    # 返回时间戳方式的函数主要有time()，clock()等
    print time.time()  # 1441632561.1
    print type(time.time())  # <type 'float'>

    # 元组（struct_time）
    # struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()
    print time.localtime()  # time.struct_time(tm_year=2015, tm_mon=9, tm_mday=7, tm_hour=21, tm_min=29, tm_sec=21, tm_wday=0, tm_yday=250, tm_isdst=0)
    print type(time.localtime())  # <type 'time.struct_time'>

    # 将一个元祖（struct_time）转化为时间戳
    print time.mktime(time.localtime())  # 1441633092.0
    print type(time.mktime(time.localtime()))  # <type 'float'>

    print time.ctime()  # Mon Sep  7 21:31:02 2015
    print type(time.ctime())  # <type 'str'>

    # 格式化字符串 time.strftime(format[, t])
    # 把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
    # 如果t未指定，将传入time.localtime()。
    # 如果元组中任何一个元素越界，ValueError的错误将会被抛出。
    print time.strftime("%Y-%m-%d %H:%M:%S")  # 2015-09-07 21:44:07
    print type(time.strftime("%Y-%m-%d %H:%M:%S"))  # <type 'str'>
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 2015-09-07 21:44:07
    print time.strftime("%Y-%m-%d", time.localtime()) + ' 09:00:00'  # 2015-09-07 09:00:00
    print ' '.join((time.strftime("%Y-%m-%d", time.localtime()), '09:00:00'))  # 2015-09-07 09:00:00

    # time.strptime(string[, format])
    # 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
    # format默认为："%a %b %d %H:%M:%S %Y"。
    print time.strptime('2015-09-07 21:44:07', '%Y-%m-%d %X')  # time.struct_time(tm_year=2015, tm_mon=9, tm_mday=7, tm_hour=21, tm_min=44, tm_sec=7, tm_wday=0, tm_yday=250, tm_isdst=-1)
    print type(time.strptime('2015-09-07 21:44:07', '%Y-%m-%d %X'))  # <type 'time.struct_time'>

    # 格式化时间字符串转时间戳
    # 实际分解成两步 第一步：字符串转为元祖；第二步：元祖（struct_time）转为时间戳
    print time.mktime(time.strptime('2015-09-07 21:44:07', '%Y-%m-%d %X'))  # 1441633447.0
    print type(time.mktime(time.strptime('2015-09-07 21:44:07', '%Y-%m-%d %X')))  # <type 'float'>

    # 日期时间元祖 datetime tuple(datetime obj)
    # MySql中DATETIME类型 对应的就是 python里的这种类型
    # 注意与时间元祖的区别
    print datetime.now()  # 2015-09-07 22:15:03.419781
    print type(datetime.now())  # <type 'datetime.datetime'>

    # 日期时间元祖 转为 时间元祖
    # date.timetuple()：返回日期对应的time.struct_time对象
    print datetime.now().timetuple()  # time.struct_time(tm_year=2015, tm_mon=9, tm_mday=7, tm_hour=22, tm_min=18, tm_sec=22, tm_wday=0, tm_yday=250, tm_isdst=-1)
    print type(datetime.now().timetuple())  # <type 'time.struct_time'>

    # 字符串日期转星期(星期（0-6），星期天为星期的开始)
    print time.strftime('%w', time.strptime('2016-01-17', '%Y-%m-%d'))

    # 格式转换
    print time.strftime('%Y-%m-%d %H:%M:%S', time.strptime('5/6/2016 10:02:47 PM', '%m/%d/%Y %I:%M:%S %p'))

    # 当前年份(4位)
    print datetime.now().year

    # 获取2个月之后的日期
    print datetime.now() + timedelta(days=60)

    # 显示友好时间
    print time_pretty(60 * 60 * 24 * 3 + 60 * 60 * 2 + 60 * 3)

    # 字符串转对象
    print datetime.strptime('2016-06-06', "%Y-%m-%d").date(), type(datetime.strptime('2016-06-06', "%Y-%m-%d").date())
    print datetime.strptime('2016-06-06 12:34:54', "%Y-%m-%d %H:%M:%S")
    # print datetime.strptime('2016-06', "%Y-%m-%d %H:%M:%S")  # 异常ValueError

    # 显示毫秒
    print datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # iso时间
    print datetime.utcnow().isoformat()
    print datetime.utcnow().date().isoformat()
    print datetime(2002, 10, 27, 12, 0, 0, tzinfo=utc).strftime('%Y-%m-%dT%H:%M:%S%Z%z')
    print datetime.now().replace(microsecond=0, tzinfo=utc)
    print datetime.fromtimestamp(0, timezone('Asia/Shanghai'))


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
    %Y 四位数的年份表示（0000-9999）
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

4.py中涉及的time有四种类型
    1. time string
    2. datetime tuple(datetime obj)
    3. time tuple(time obj)
    4. timestamp

time模块的官方文档
https://docs.python.org/2/library/time.html

"""