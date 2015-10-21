# encoding: utf-8
__author__ = 'zhanghe'

import sys


def test():
    """
    命令行测试python调用自定义方法
    """
    print sys.argv
    try:
        if len(sys.argv) > 1:
            fun_name = eval(sys.argv[1])
            fun_name()
        else:
            print '缺失参数'
    except NameError, e:
        print e
        print '未定义的方法[%s]' % sys.argv[1]


def fuck():
    print 'This is a test!'

if __name__ == '__main__':
    test()


"""
sys.argv[0] 文件名
sys.argv[1] 命令行输入的参数1
sys.argv[2] 命令行输入的参数2

测试用例：
$ python /home/zhanghe/code/python/test/test_sys_arg.py
$ python /home/zhanghe/code/python/test/test_sys_arg.py fuc
$ python /home/zhanghe/code/python/test/test_sys_arg.py fuck
"""
