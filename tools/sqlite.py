# encoding: utf-8
__author__ = 'zhanghe'

import sqlite3


class SqLite(object):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def close(self):
        """
        关闭Connection
        """
        self.conn.close()

    def create(self):
        """
        创建数据表
        """
        # 创建一个Cursor:
        cursor = self.conn.cursor()
        # 执行一条SQL语句，创建user表:
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        # 继续执行一条SQL语句，插入一条记录:
        cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
        # 通过rowcount获得插入的行数:
        print cursor.rowcount
        # 关闭Cursor:
        cursor.close()
        # 提交事务:
        self.conn.commit()

    def show_tables(self):
        """
        显示数据库表名
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = cursor.fetchall()
        cursor.close()
        print result
        return result

    def get_row(self):
        """
        获取多行数据
        :return:
        """
        cursor = self.conn.cursor()
        # 执行查询语句:
        cursor.execute('select * from user where id=?', '1')
        # 获得查询结果集:
        values = cursor.fetchall()
        cursor.close()
        print values
        return values


def test():
    """
    测试
    """
    db = SqLite('test.db')
    # db.create()
    db.show_tables()
    db.get_row()
    db.close()


if __name__ == '__main__':
    test()