# encoding: utf-8
__author__ = 'zhanghe'

import sys
sys.path.append('..')
from tools.log import Log

# 实例化，修改日志文件名称，加载新配置
log_test = Log()
log_test.log_filename = 'log_test.log'
log_test.log_config()
# 测试
log_test.debug('This is debug message')
log_test.info('This is info message')
log_test.warning('This is warning message')

log_test.get_memory_usage()
print log_test.memory_usage


"""
测试结果：
内存使用4.14M
4.14M
"""