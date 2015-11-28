# encoding: utf-8
__author__ = 'zhanghe'


from pymongo import MongoClient
from pymongo import errors
import json
from datetime import date, datetime

# 数据库日志专用配置
from log import Logger
my_logger = Logger('mongodb', 'mongodb.log', 'DEBUG')
my_logger.set_file_level('DEBUG')
my_logger.set_stream_level('WARNING')  # WARNING DEBUG
my_logger.set_stream_handler_fmt('%(message)s')
my_logger.load()
logger = my_logger.logger
# my_logger.get_memory_usage()


class Mongodb(object):
    """
    自定义mongodb工具
    """
    def __init__(self, db_config, db_name=None):
        self.db_config = db_config
        if db_name is not None:
            self.db_config['database'] = db_name
        try:
            # 实例化mongodb
            self.conn = MongoClient(self.db_config['host'], self.db_config['port'])
            # 获取数据库对象(选择/切换)
            self.db = self.conn.get_database(self.db_config['database'])
        except errors.ServerSelectionTimeoutError, e:
            logger.error('连接超时：%s' % e)
        except Exception, e:
            logger.error(e)

    @staticmethod
    def __default(obj):
        """
        支持datetime的json encode
        TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
        :param obj:
        :return:
        """
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            raise TypeError('%r is not JSON serializable' % obj)

    def close_conn(self):
        """
        关闭连接
        关闭所有套接字的连接池和停止监控线程。
        如果这个实例再次使用它将自动重启和重新启动线程
        """
        self.conn.close()

    def find_one(self, table_name, condition=None):
        """
        查询单条记录
        :param table_name:
        :param condition:
        :return:
        """
        return self.db.get_collection(table_name).find_one(condition)

    def find_all(self, table_name, condition=None):
        """
        查询多条记录
        :param table_name:
        :param condition:
        :return:
        """
        return self.db.get_collection(table_name).find(condition)

    def count(self, table_name, condition=None):
        """
        查询记录总数
        :param table_name:
        :param condition:
        :return:
        """
        return self.db.get_collection(table_name).count(condition)

    def distinct(self, table_name, field_name):
        """
        查询某字段去重后值的范围
        :param table_name:
        :param field_name:
        :return:
        """
        return self.db.get_collection(table_name).distinct(field_name)

    def insert(self, table_name, data):
        """
        插入数据
        :param table_name:
        :param data:
        :return:
        """
        try:
            ids = self.db.get_collection(table_name).insert(data)
            return ids
        except Exception, e:
            logger.error('插入失败：%s' % e)
            return None

    def update(self, table_name, condition, update_data, update_type='set'):
        """
        批量更新数据
        upsert : 如果不存在update的记录，是否插入；true为插入，默认是false，不插入。
        :param table_name:
        :param condition:
        :param update_data:
        :param update_type: 范围：['inc', 'set', 'unset', 'push', 'pushAll', 'addToSet', 'pop', 'pull', 'pullAll', 'rename']
        :return:
        """
        if update_type not in ['inc', 'set', 'unset', 'push', 'pushAll', 'addToSet', 'pop', 'pull', 'pullAll', 'rename']:
            logger.error('更新失败，类型错误：%s' % update_type)
            return None
        try:
            result = self.db.get_collection(table_name).update_many(condition, {'$%s' % update_type: update_data})
            logger.info('更新成功，匹配数量：%s；更新数量：%s' % (result.matched_count, result.modified_count))
            return result.modified_count  # 返回更新数量，仅支持MongoDB 2.6及以上版本
        except Exception, e:
            logger.error('更新失败：%s' % e)
            return None

    def remove(self, table_name, condition=None):
        """
        删除文档记录
        :param table_name:
        :param condition:
        :return:
        """
        result = self.db.get_collection(table_name).remove(condition)
        if result.get('err') is None:
            logger.info('删除成功，删除行数%s' % result.get('n', 0))
            return result.get('n', 0)
        else:
            logger.error('删除失败：%s' % result.get('err'))
            return None

    def output_row(self, table_name, condition=None, style=0):
        """
        格式化输出单个记录
        style=0 键值对齐风格
        style=1 JSON缩进风格
        :param table_name:
        :param condition:
        :param style:
        :return:
        """
        row = self.find_one(table_name, condition)
        if style == 0:
            # 获取KEY最大的长度作为缩进依据
            max_len_key = max([len(each_key) for each_key in row.keys()])
            str_format = '{0: >%s}' % max_len_key
            keys = [str_format.format(each_key) for each_key in row.keys()]
            result = dict(zip(keys, row.values()))
            print '**********  表名[%s]  **********' % table_name
            for key, item in result.items():
                print key, ':', item
        else:
            print json.dumps(row, indent=4, ensure_ascii=False, default=self.__default)

    def output_rows(self, table_name, condition=None, style=0):
        """
        格式化输出批量记录
        style=0 键值对齐风格
        style=1 JSON缩进风格
        :param table_name:
        :param condition:
        :param style:
        :return:
        """
        rows = self.find_all(table_name, condition)
        total = self.count(table_name, condition)
        if style == 0:
            count = 0
            for row in rows:
                # 获取KEY最大的长度作为缩进依据
                max_len_key = max([len(each_key) for each_key in row.keys()])
                str_format = '{0: >%s}' % max_len_key
                keys = [str_format.format(each_key) for each_key in row.keys()]
                result = dict(zip(keys, row.values()))
                count += 1
                print '**********  表名[%s]  [%d/%d]  **********' % (table_name, count, total)
                for key, item in result.items():
                    print key, ':', item
        else:
            for row in rows:
                print json.dumps(row, indent=4, ensure_ascii=False, default=self.__default)
