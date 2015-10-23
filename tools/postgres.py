# encoding: utf-8
__author__ = 'zhanghe'

from psycopg2 import *


# 本地环境
db_config_local = {
    'database': '',
    'user': 'xxxx',
    'password': 'xxxxxxxx',
    'host': '192.168.1.1',
    'port': 3306
}

# 线上环境
db_config_online = {
    'database': '',
    'user': 'xxxx',
    'password': 'xxxxxxxx',
    'host': '192.168.1.2',
    'port': 3306
}

db_config_current = db_config_local


class Postgres(object):
    """
    自定义Postgres工具
    """
    def __init__(self, db_config, db_name=None):
        self.db_config = db_config
        print db_config
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
            print e

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

    def get_columns_name(self, table_name=None):
        """
        获取数据表的字段名称
        :param table_name:
        :return:
        """
        if self.is_conn_open() is False:
            print '连接已断开'
            return None
        try:
            cursor = self.conn.cursor()
            sql = "select column_name from information_schema.columns where table_name = '%s'" % table_name
            print sql
            cursor.execute(sql)
            result = cursor.fetchall()
            row = [item[0] for item in result]
            cursor.close()
            return row
        except Exception, e:
            print e

    def get_row(self, table_name=None, condition=None):
        """
        获取单行数据
        :return:
        """
        if self.is_conn_open() is False:
            print '连接已断开'
            return None
        try:
            cursor = self.conn.cursor()
            if condition is not None:
                sql_condition = 'where '
                sql_condition += ' and '.join(condition)
            else:
                sql_condition = ''
            sql = 'select * from %s %s limit 1' % (table_name, sql_condition)
            print sql
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
            return row
        except Exception, e:
            print e

    def get_count(self, table_name=None):
        """
        获取记录总数
        :return:
        """
        if self.is_conn_open() is False:
            print '连接已断开'
            return None
        if table_name is None:
            print 0
            return 0
        try:
            cursor = self.conn.cursor()
            sql = 'select count(*) from %s' % table_name
            cursor.execute(sql)
            row = cursor.fetchone()
            count = row[0]
            cursor.close()
            print count
            return count
        except Exception, e:
            print e


import json
from datetime import date, datetime


def __default(obj):
    """
    支持datetime的json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


def test():
    """
    测试Mysql类
    :return:
    """
    # 实例化wl_crawl库的连接
    wl_crawl = Postgres(db_config_current, 'wl_crawl')
    # 查询总数
    count = wl_crawl.get_count('origin_company')
    print '总记录数：%s' % count
    # 关闭数据库连接
    # wl_crawl.close_conn()
    # 查询单条记录
    columns_name = wl_crawl.get_columns_name('origin_company')
    row = wl_crawl.get_row('origin_company', ['id=69011'])
    result = dict(zip(columns_name, row))
    if row is not None:
        print json.dumps(result, indent=4, ensure_ascii=False, default=__default)
    else:
        print '没有记录'
    # 关闭数据库连接(测试再次关闭)
    wl_crawl.close_conn()


if __name__ == '__main__':
    test()
