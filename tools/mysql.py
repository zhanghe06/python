# coding=utf-8
__author__ = 'zhanghe'


try:
    from MySQLdb import *
except ImportError:
    from pymysql import *


class Mysql(object):
    """
    自定义mysql工具
    """
    def __init__(self, db_config, db_name=None):
        self.db_config = db_config
        if db_name is not None:
            self.db_config['db'] = db_name
        try:
            self.conn = Connection(
                self.db_config['host'],
                self.db_config['user'],
                self.db_config['passwd'],
                self.db_config['db'],
                self.db_config['port']
            )
        except Exception, e:
            print e

    def is_conn_open(self):
        """
        检测连接是否打开
        :return:
        """
        if self.conn is None or self.conn.open == 0:
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
            cursor.execute("set NAMES UTF8")  # 解决乱码
            if condition is not None:
                sql_condition = 'where '
                sql_condition += ' and '.join(condition)
            else:
                sql_condition = ''
            sql = 'select * from %s %s limit 1' % (table_name, sql_condition)
            print sql
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                print None
                return None
            else:
                # print type(row)
                if '??' in row[1]:
                    print '存在乱码'
                print '%s\t%s' % (row[0], row[1])
                # print '%s\t%s' % (type(row[0]), type(row[1]))
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
            # print 0
            return 0
        try:
            cursor = self.conn.cursor()
            sql = 'select count(*) from %s' % table_name
            cursor.execute(sql)
            row = cursor.fetchone()
            count = row[0]
            cursor.close()
            # print count
            return count
        except Exception, e:
            print e

    def get_count_by_sql(self, sql=None):
        """
        获取记录总数
        :return:
        """
        if self.is_conn_open() is False:
            print '连接已断开'
            return None
        if sql is None:
            print 'sql语句不能为空'
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("set NAMES UTF8")  # 解决乱码
            cursor.execute(sql)
            row = cursor.fetchone()
            count = row[0]
            cursor.close()
            # print count
            return count
        except Exception, e:
            print e

    def get_rows_by_sql(self, sql=None):
        """
        获取记录
        :return:
        """
        if self.is_conn_open() is False:
            print '连接已断开'
            return None
        if sql is None:
            print 'sql语句不能为空'
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("set NAMES UTF8")  # 解决乱码
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
            # print rows
            return rows
        except Exception, e:
            print e

    def delete(self, table_name, condition=None):
        """
        删除表记录
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
            sql = 'delete from %s %s' % (table_name, sql_condition)
            print sql
            result = cursor.execute(sql)
            cursor.close()
            self.conn.commit()
            return result
        except Exception, e:
            print e

    def insert(self, table_name, data={}):
        """
        插入表记录
        """
        if self.is_conn_open() is False:
            print '连接已断开'
            return None
        if not data:
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("set NAMES UTF8")  # 解决乱码
            sql_keys = ', '.join(str(item) for item in data.keys())
            sql_vals = ', '.join("'%s'" % str(item) for item in data.values())
            sql = 'insert into %s(%s) values(%s)' % (table_name, sql_keys, sql_vals)
            print sql
            result = cursor.execute(sql)
            cursor.close()
            self.conn.commit()
            return result
        except Exception, e:
            print e


def test():
    """
    测试Mysql类
    :return:
    """
    # 本地环境
    db_config_local = {
        'host': '192.168.1.1',
        'user': 'xxxx',
        'passwd': 'xxxxxxxx',
        'db': '',
        'port': 3306
    }

    # 线上环境
    db_config_online = {
        'host': '192.168.1.2',
        'user': 'xxxx',
        'passwd': 'xxxxxxxx',
        'db': '',
        'port': 3306
    }
    # 实例化db_company库的连接
    mysql_company = Mysql(db_config_local, 'db_company')
    # 查询总数
    count = mysql_company.get_count('company')
    print '总记录数：%s' % count
    # 关闭数据库连接
    # mysql_company.close_conn()
    # 查询单条记录
    row = mysql_company.get_row('company', ['cid=17'])
    if row is not None:
        print '单条记录：%s\t%s' % (row[0], row[1])
    else:
        print '没有记录'
    # 关闭数据库连接(测试再次关闭)
    mysql_company.close_conn()


if __name__ == '__main__':
    test()


"""
测试结果：

1748901
总记录数：1748901
select * from company where cid=18 limit 1
None
没有记录

1748901
总记录数：1748901
连接已断开
没有记录

1748901
总记录数：1748901
select * from company where cid=17 limit 1
17	四川XXX有限责任公司
单条记录：17	四川XXX有限责任公司

"""
