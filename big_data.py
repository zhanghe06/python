# encoding: utf-8
__author__ = 'zhanghe'

"""
大数据效率测试
"""

import random
import tools.time_log


@tools.time_log.time_log
def create_data():
    """
    创建大数据
    """
    file_name = 'static/csv/data.csv'
    with open(file_name, 'wb') as f:
        for key in xrange(1000000):
            row = '%s\t%s\n' % (key, random.randint(100, 200))
            print row
            f.write(row)


@tools.time_log.time_log
def read_data_line():
    """
    逐行读取大数据
    """
    file_name = 'static/csv/data.csv'
    with open(file_name) as f:
        for line in f:
            print line.rstrip('\n').split('\t')


@tools.time_log.time_log
def read_data_all():
    """
    一次读取大数据
    """
    file_name = 'static/csv/data.csv'
    with open(file_name) as f:
        data_tmp = f.read()
        # print data_tmp  # 如果仅仅是读取数据，速度可以达到2.42S
    for i in data_tmp.split('\n'):
        print i.split('\t')


if __name__ == '__main__':
    # create_data()
    # read_data_line()
    read_data_all()


"""
运行状况：

方法create_data运行时间：19.08S
zhanghe@ubuntu:~/code/python$ du -h static/csv/data.csv
11M	static/csv/data.csv
zhanghe@ubuntu:~/code/python$ less static/csv/data.csv


方法read_data_line运行时间：68.91S
逐行读取文件时的状态
zhanghe@ubuntu:~/code/python$ top
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
10059 zhanghe   20   0   12656   4532   2632 R  95.2  0.2   0:13.74 python

方法read_data_all运行时间：47.39S
一次读取文件时的状态
zhanghe@ubuntu:~/code/python$ top
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
10744 zhanghe   20   0   58808  50632   2628 R  97.2  2.5   0:43.25 python

以上结果可以看出：
逐行读取文件比一次性加载文件节约内存，适合处理大数据的场景
一次性加载文件的方式适合数据量不大（占用内存可以忽略），但对速度要求较高的场景
"""