# encoding: utf-8
__author__ = 'zhanghe'

from tools import log


def test():
    # 实例化，修改日志文件名称，加载新配置
    xxx = log.Log()
    xxx.log_filename = 'test_log.log'
    xxx.log_config()
    # 测试
    log.debug('This is debug message')
    log.info('This is info message')
    log.warning('This is warning message')


if __name__ == '__main__':
    test()