# encoding: utf-8
__author__ = 'zhanghe'


def test():
    """
    测试配置文件
    :return:
    """
    from config import db
    from config import proxy

    print db
    print proxy


if __name__ == '__main__':
    test()
