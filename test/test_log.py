# encoding: utf-8
__author__ = 'zhanghe'


import logging


def first():
    """
    默认情况下python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志
    日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    """
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')

    # 终端输出：
    # WARNING:root:warning message
    # ERROR:root:error message
    # CRITICAL:root:critical message


def second():
    """
    日志按照不同等级分别向终端显示和文件写入
    """
    # 创建logger对象， 名称为my_logger
    logger = logging.getLogger('my_logger')

    # 给logger设置相对较低的日志等级（否则logger的默认WARNING等级会使handler设置的低等级不生效）
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    file_handler = logging.FileHandler('log_test.log')

    # 再创建一个handler，用于输出到控制台
    stream_handler = logging.StreamHandler()

    # 定义handler的输出格式formatter
    date_fmt = '%Y-%m-%d %H:%M:%S'
    fmt = '%(asctime)s - %(name)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt, date_fmt)

    # 设置日志输出格式
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # 给handler设置日志等级
    file_handler.setLevel(logging.INFO)
    stream_handler.setLevel(logging.DEBUG)

    # 给logger添加handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # 日志信息
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    # 终端输出：
    # 2015-10-30 23:35:42,575 - my_logger - test_log.py - [line:51] - DEBUG - debug message
    # 2015-10-30 23:35:42,576 - my_logger - test_log.py - [line:52] - INFO - info message
    # 2015-10-30 23:35:42,576 - my_logger - test_log.py - [line:53] - WARNING - warning message
    # 2015-10-30 23:35:42,576 - my_logger - test_log.py - [line:54] - ERROR - error message
    # 2015-10-30 23:35:42,577 - my_logger - test_log.py - [line:55] - CRITICAL - critical message

    # 文件写入：
    # 2015-10-30 23:35:42,576 - my_logger - test_log.py - [line:52] - INFO - info message
    # 2015-10-30 23:35:42,576 - my_logger - test_log.py - [line:53] - WARNING - warning message
    # 2015-10-30 23:35:42,576 - my_logger - test_log.py - [line:54] - ERROR - error message
    # 2015-10-30 23:35:42,577 - my_logger - test_log.py - [line:55] - CRITICAL - critical message


if __name__ == '__main__':
    # first()
    second()


"""
logging库提供了多个组件：
Logger、Handler、Filter、Formatter。

Logger       对象提供应用程序可直接使用的接口，
Handler      发送日志到适当的目的地，
Filter       提供了过滤日志信息的方法，
Formatter    指定日志显示格式。
"""