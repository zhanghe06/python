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
        # self.log_date_fmt = '%a, %d %b %Y %H:%M:%S'
        self.log_date_fmt = '%Y-%m-%d %H:%M:%S'
        self.log_filename = 'myapp.log'
        self.log_filemode = 'w'  # 默认'a'
        self.memory_usage = '0.00M'

    def log_config(self):
        """
        加载配置信息
        """
        logging.basicConfig(
            level=self.log_level,
            format=self.log_format,
            datefmt=self.log_date_fmt,
            filename=self.log_filename,
            filemode=self.log_filemode
        )

    def get_memory_usage(self):
        """
        获取当前进程内存使用情况(单位M)
        """
        import os
        # 获取当前脚本的进程ID
        pid = os.getpid()
        # 获取当前脚本占用的内存
        cmd = 'ps -p %s -o rss=' % pid
        output = os.popen(cmd)
        result = output.read()
        if result == '':
            memory_usage_value = 0
        else:
            memory_usage_value = int(result.strip())
        memory_usage_format = memory_usage_value/1024.0
        print '内存使用%.2fM' % memory_usage_format
        self.memory_usage = '%.2fM' % memory_usage_format

    @staticmethod
    def debug(msg):
        logging.debug(msg)

    @staticmethod
    def info(msg):
        logging.info(msg)

    @staticmethod
    def warning(msg):
        logging.warning(msg)


class Logger:
    """
    日志工具类
    按照不同等级分别向终端显示和文件写入
    使用方式：
    from log import Logger
    my_logger = Logger('logger_name', 'log_name.log', 'DEBUG')
    my_logger.load()
    logger = my_logger.logger
    my_logger.get_memory_usage()
    """
    def __init__(self, logger_name, logger_filename, logger_level='DEBUG'):
        self.logger_name = logger_name
        self.logger_filename = logger_filename
        self.logger_level = logger_level
        self.logger_fmt = '%(asctime)s - %(name)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
        self.logger_date_fmt = '%Y-%m-%d %H:%M:%S'
        self.file_handler_fmt = None
        self.file_handler_date_fmt = None
        self.stream_handler_fmt = None
        self.stream_handler_date_fmt = None
        self.file_handler_level = logging.INFO
        self.stream_handler_level = logging.DEBUG
        self.memory_usage = '0.00M'
        self.logger = logging.getLogger(self.logger_name)

    def load(self):
        """
        加载logger配置
        """
        try:
            # 给logger设置相对较低的日志等级（否则小于logger的默认WARNING级别的信息将被忽略，可能会使handler设置无效）
            self.logger.setLevel(eval('logging.%s' % self.logger_level))  # 这里输出所有信息，将日志等级控制权限交给handler
            # 分别创建两个handler，用于写入日志文件和输出到控制台
            file_handler = logging.FileHandler(self.logger_filename)
            stream_handler = logging.StreamHandler()
            # 给handler设置日志等级
            file_handler.setLevel(self.file_handler_level)
            stream_handler.setLevel(self.stream_handler_level)
            # 定义handler的输出格式formatter
            # formatter = logging.Formatter(self.logger_fmt, self.logger_date_fmt)
            if self.file_handler_fmt is None:
                self.file_handler_fmt = self.logger_fmt
            if self.stream_handler_fmt is None:
                self.stream_handler_fmt = self.logger_fmt
            if self.file_handler_date_fmt is None:
                self.file_handler_date_fmt = self.logger_date_fmt
            if self.stream_handler_date_fmt is None:
                self.stream_handler_date_fmt = self.logger_date_fmt
            file_handler_formatter = logging.Formatter(self.file_handler_fmt, self.file_handler_date_fmt)
            stream_handler_formatter = logging.Formatter(self.stream_handler_fmt, self.stream_handler_date_fmt)
            # 设置日志输出格式
            file_handler.setFormatter(file_handler_formatter)
            stream_handler.setFormatter(stream_handler_formatter)
            # 给logger添加handler
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)
        except Exception, e:
            return e

    def set_file_level(self, level):
        """
        设置文件写入等级
        """
        self.file_handler_level = eval('logging.%s' % level)

    def set_stream_level(self, level):
        """
        设置终端输出等级
        """
        self.stream_handler_level = eval('logging.%s' % level)

    def set_stream_handler_fmt(self, fmt='%(message)s'):
        """
        设置终端输出格式
        """
        self.stream_handler_fmt = fmt

    def get_memory_usage(self):
        """
        获取当前进程内存使用情况(单位M)
        """
        import os
        # 获取当前脚本的进程ID
        pid = os.getpid()
        # 获取当前脚本占用的内存
        cmd = 'ps -p %s -o rss=' % pid
        output = os.popen(cmd)
        result = output.read()
        if result == '':
            memory_usage_value = 0
        else:
            memory_usage_value = int(result.strip())
        memory_usage_format = memory_usage_value/1024.0
        print '[pid:%s]内存使用%.2fM' % (pid, memory_usage_format)
        self.memory_usage = '%.2fM' % memory_usage_format


def test_log():
    # 实例化，修改日志文件名称，加载新配置
    xxx = Log()
    xxx.log_filename = 'myapp2.log'
    xxx.log_config()
    # 测试
    xxx.debug('This is debug message')
    xxx.info('This is info message')
    xxx.warning('This is warning message')


def test_logger():
    """
    测试Logger工具类
    """
    my_logger = Logger('my_logger', 'my_app.log')
    my_logger.load()
    logger = my_logger.logger
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
    my_logger.get_memory_usage()


if __name__ == '__main__':
    test_logger()


'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

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