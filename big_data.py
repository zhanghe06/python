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
def read_data():
    """
    读取大数据
    """
    file_name = 'static/csv/data.csv'
    with open(file_name) as f:
        for line in f:
            print line.rstrip('\n').split('\t')


if __name__ == '__main__':
    # create_data()
    read_data()


"""
运行状况：

方法create_data运行时间：19.08S

方法read_data运行时间：65.21S

读取文件时的状态
zhanghe@ubuntu:~/code/python$ top
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
10059 zhanghe   20   0   12656   4532   2632 R  95.2  0.2   0:13.74 python


zhanghe@ubuntu:~/code/python$ du -h static/csv/data.csv
11M	static/csv/data.csv

zhanghe@ubuntu:~/code/python$ less static/csv/data.csv

"""