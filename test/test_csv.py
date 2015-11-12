# encoding: utf-8
__author__ = 'zhanghe'


import csv


def test_read(file_name):
    """
    测试读CSV文件
    :param file_name:
    :return:
    """
    with open(file_name, 'rb') as csv_file:
        spam_reader = csv.reader(csv_file)
        for row in spam_reader:
            print '\t'.join(row)
        return [i for i in spam_reader]


def test_write(file_name):
    """
    测试写CSV文件
    :param file_name:
    :return:
    """
    with open(file_name, 'ab') as csv_file:
        spam_writer = csv.writer(csv_file)
        spam_writer.writerow(['淘宝', 54, 'E'])


if __name__ == '__main__':
    filename = 'eggs.csv'
    # test_read(filename)
    # test_write(filename)
    print '\n'
    test_read(filename)