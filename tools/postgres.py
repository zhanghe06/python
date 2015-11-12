# encoding: utf-8
__author__ = 'zhanghe'

from psycopg2 import *
import json
from datetime import date, datetime

# 数据库日志专用配置
from log import Logger
my_logger = Logger('postgres', 'postgres.log', 'DEBUG')
my_logger.set_file_level('DEBUG')
my_logger.set_stream_level('WARNING')  # WARNING DEBUG
my_logger.set_stream_handler_fmt('%(message)s')
my_logger.load()
logger = my_logger.logger
# my_logger.get_memory_usage()


class Postgres(object):
    """
    自定义Postgres工具
    """
    def __init__(self, db_config, db_name=None):
        self.db_config = db_config
        if db_name is not None:
            self.db_config['database'] = db_name
        try:
            self.conn = connect(
                database=self.db_config['database'],
                user=self.db_config['user'],
                password=self.db_config['password'],
                host=self.db_config['host'],
                port=self.db_config['port']
            )
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

    def is_conn_open(self):
        """
        检测连接是否打开
        :return:
        """
        if self.conn is None or self.conn.closed == 1:
            return False
        else:
            return True

    def close_conn(self):
        """
        关闭数据库连接
        :return:
        """
        if self.is_conn_open() is True:
            self.conn.close()

    def truncate(self, table_name):
        """
        清空表
        :param table_name:
        :return:
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return []
        # 参数判断
        if table_name is None:
            logger.error('查询表名缺少参数')
            return []
        sql = 'truncate table %s' % table_name
        logger.info(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            logger.info('更新行数：%s' % cursor.rowcount)
            cursor.close()
            return True
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def get_columns_name(self, table_name):
        """
        获取数据表的字段名称
        :param table_name:
        :return:
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return []
        # 参数判断
        if table_name is None:
            logger.error('查询表名缺少参数')
            return []
        cursor = self.conn.cursor()
        sql = "select column_name from information_schema.columns where table_name = '%s'" % table_name
        logger.info(sql)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            row = [item[0] for item in result]
            return row
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def get_row(self, table_name, condition=None):
        """
        获取单行数据
        :return:
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return None
        # 参数判断
        if table_name is None:
            logger.error('查询表名缺少参数')
            return None
        if condition and not isinstance(condition, list):
            logger.error('查询条件参数格式错误')
            return None
        # 组装查询条件
        if condition:
            sql_condition = 'where '
            sql_condition += ' and '.join(condition)
        else:
            sql_condition = ''
        sql = 'select * from %s %s limit 1' % (table_name, sql_condition)
        logger.info(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def get_rows(self, table_name, condition=None, limit='limit 10 offset 0'):
        """
        获取多行数据
        con_obj.get_rows('company', ["type='6'"], 'limit 10 offset 0')
        con_obj.get_rows('company', ["type='6'"], 'limit 10')
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return None
        # 参数判断
        if table_name is None:
            logger.error('查询表名缺少参数')
            return None
        if condition and not isinstance(condition, list):
            logger.error('查询条件参数格式错误')
            return None
        # 组装查询条件
        if condition:
            sql_condition = 'where '
            sql_condition += ' and '.join(condition)
        else:
            sql_condition = ''
        sql = 'select * from %s %s %s' % (table_name, sql_condition, limit)
        logger.info(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def get_count(self, table_name, condition=None):
        """
        获取记录总数
        :return:
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return 0
        # 参数判断
        if table_name is None:
            logger.error('查询表名缺少参数')
            return 0
        if condition and not isinstance(condition, list):
            logger.error('查询条件参数格式错误')
            return 0
        # 组装查询条件
        if condition:
            sql_condition = 'where '
            sql_condition += ' and '.join(condition)
        else:
            sql_condition = ''
        sql = 'select count(*) from %s %s' % (table_name, sql_condition)
        logger.info(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            count = row[0]
            return count
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def output_row(self, table_name, condition=None, style=0):
        """
        格式化输出单个记录
        style=0 键值对齐风格
        style=1 JSON缩进风格
        """
        # 参数判断
        if not table_name:
            logger.error('查询数据缺少参数')
            return None
        if condition and not isinstance(condition, list):
            logger.error('查询条件参数格式错误')
            return None
        columns_name = self.get_columns_name(table_name)
        row = self.get_row(table_name, condition)
        if not columns_name:
            logger.error('表名不存在')
            return None
        if not row:
            logger.error('记录不存在')
            return None
        if style == 0:
            # 获取字段名称最大的长度值作为缩进依据
            max_len_column = max([len(each_column) for each_column in columns_name])
            str_format = '{0: >%s}' % max_len_column
            columns_name = [str_format.format(each_column) for each_column in columns_name]
            result = dict(zip(columns_name, row))
            print '**********  表名[%s]  **********' % table_name
            for key, item in result.items():
                print key, ':', item
        else:
            result = dict(zip(columns_name, row))
            print json.dumps(result, indent=4, ensure_ascii=False, default=self.__default)

    def output_rows(self, table_name, condition=None, limit='limit 10 offset 0', style=0):
        """
        格式化输出批量记录
        style=0 键值对齐风格
        style=1 JSON缩进风格
        """
        # 参数判断
        if not table_name:
            logger.error('查询数据缺少参数')
            return None
        if condition and not isinstance(condition, list):
            logger.error('查询条件参数格式错误')
            return None
        columns_name = self.get_columns_name(table_name)
        rows = self.get_rows(table_name, condition, limit)
        if not columns_name:
            logger.error('表名不存在')
            return None
        if not rows:
            logger.error('记录不存在')
            return None
        if style == 0:
            # 获取字段名称最大的长度值作为缩进依据
            max_len_column = max([len(each_column) for each_column in columns_name])
            str_format = '{0: >%s}' % max_len_column
            columns_name = [str_format.format(each_column) for each_column in columns_name]
            count = 0
            total = len(rows)
            for row in rows:
                result = dict(zip(columns_name, row))
                count += 1
                print '**********  表名[%s]  [%d/%d]  **********' % (table_name, count, total)
                for key, item in result.items():
                    print key, ':', item
        else:
            for row in rows:
                result = dict(zip(columns_name, row))
                print json.dumps(result, indent=4, ensure_ascii=False, default=self.__default)

    def update(self, table_name, update_field, condition=None):
        """
        更新数据
        con_obj.update('company', ["title='标题'", "flag='2'"], ["type='6'"])
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return False
        # 参数判断
        if not table_name or not update_field:
            logger.error('更新数据缺少参数')
            return False
        if not isinstance(update_field, list) or (condition and not isinstance(condition, list)):
            logger.error('更新数据参数格式错误')
            return False
        # 组装更新字段
        if update_field:
            sql_update_field = 'set '
            sql_update_field += ' and '.join(update_field)
        else:
            sql_update_field = ''
        # 组装更新条件
        if condition:
            sql_condition = 'where '
            sql_condition += ' and '.join(condition)
        else:
            sql_condition = ''
        # 拼接sql语句
        sql = 'update %s %s %s' % (table_name, sql_update_field, sql_condition)
        logger.info(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            logger.info('更新行数：%s' % cursor.rowcount)
            return True
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def delete(self, table_name, condition=None):
        """
        删除数据
        con_obj.delete('company', ["type='6'", "flag='2'"])
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return False
        # 参数判断
        if condition and not isinstance(condition, list):
            logger.error('删除数据参数格式错误')
            return False
        # 组装删除条件
        if condition:
            sql_condition = 'where '
            sql_condition += ' and '.join(condition)
        else:
            sql_condition = ''
        # 拼接sql语句
        sql = 'delete from %s %s' % (table_name, sql_condition)
        logger.info(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            logger.info('删除行数：%s' % cursor.rowcount)
            logger.info('删除成功')
            return True
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def query_by_sql(self, sql=None):
        """
        根据sql语句查询
        :return:
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return None
        if sql is None:
            logger.error('sql语句不能为空')
            return None
        # 安全性校验
        sql = sql.lower()
        logger.info(sql)
        if not sql.startswith('select'):
            logger.error('未授权的操作')
            return None
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()

    def update_by_sql(self, sql=None):
        """
        根据sql语句[增删改]
        :return:
        """
        if self.is_conn_open() is False:
            logger.error('连接已断开')
            return False
        if sql is None:
            logger.error('sql语句不能为空')
            return False
        # 安全性校验
        sql = sql.lower()
        logger.info(sql)
        if not (sql.startswith('update') or sql.startswith('insert') or sql.startswith('delete')):
            logger.error('未授权的操作')
            return False
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            logger.info('影响行数：%s' % cursor.rowcount)
            logger.info('执行成功')
            return True
        except Exception, e:
            logger.error(e)
        finally:
            cursor.close()
