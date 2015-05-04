# encoding: utf-8
__author__ = 'zhanghe'

import logging


class Log:
    """
    调试日志工具类
    """
    def __init__(self):
        self.log_level = logging.DEBUG
        self.log_format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        self.log_datefmt = '%a, %d %b %Y %H:%M:%S'
        self.log_filename = 'myapp.log'
        self.log_filemode = 'w'

    def log_config(self):
        """
        加载配置信息
        """
        logging.basicConfig(level=self.log_level,
                            format=self.log_format,
                            datefmt=self.log_datefmt,
                            filename=self.log_filename,
                            filemode=self.log_filemode)


def debug(msg):
    return logging.debug(msg)


def info(msg):
    return logging.info(msg)


def warning(msg):
    return logging.warning(msg)


if __name__ == '__main__':
    # 实例化，修改日志文件名称，加载新配置
    xxx = Log()
    xxx.log_filename = 'myapp2.log'
    xxx.log_config()
    # 测试
    debug('This is debug message')
    info('This is info message')
    warning('This is warning message')

'''
logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
'''