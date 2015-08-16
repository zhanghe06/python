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


@tools.time_log.time_log
def create_dict():
    """
    创建大数据字典(作为模块使用)
    """
    write_file_name = 'config_dict/data_dict.py'
    with open(write_file_name, 'wb') as wf:
        # 写入开始头部定义
        wf.write('DataDict = {\n')
        # 逐行读取文件
        read_file_name = 'static/csv/data.csv'
        with open(read_file_name) as rf:
            for line in rf:
                line_list = line.rstrip('\n').split('\t')
                row = '\t\'%s\': \'%s\',\n' % (line_list[0], line_list[1])
                print row
                # 写入单行数据
                wf.write(row)
        # 写入尾行
        wf.write('}\n')


@tools.time_log.time_log
def load_dict():
    """
    加载大数据字典
    """
    from config_dict.data_dict import DataDict
    return DataDict


@tools.time_log.time_log
def get_dict_value(big_dict, key):
    """
    查找大数据字典的值
    """
    print big_dict.get(key)


if __name__ == '__main__':
    # create_data()
    # read_data_line()
    # read_data_all()
    # create_dict()
    dict_tmp = load_dict()
    get_dict_value(dict_tmp, '1550')


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

"""

方法create_dict运行时间：17.35S

zhanghe@ubuntu:~/code/python$ du -h config_dict/data_dict.py
18M	config_dict/data_dict.py

方法load_dict开始时间：Fri Aug 14 00:25:42 2015
方法load_dict结束时间：Fri Aug 14 00:25:43 2015
方法load_dict运行时间：0.85S
方法get_dict_value开始时间：Fri Aug 14 00:25:43 2015
153
方法get_dict_value结束时间：Fri Aug 14 00:25:43 2015
方法get_dict_value运行时间：0.00S

可以看出将大字典作为模块导入，效率是最快的。
"""

"""
问题记录
线上一次性加载400M的字典数据，显示实际内存占用4G
使用了大量的交换分区，机器很快假死
所以使用字典的方式解决大数据关联数据处理不现实

最后冬哥巧妙的利用数据库的主键查询关联数据，因为主键有索引，所以很快。
"""