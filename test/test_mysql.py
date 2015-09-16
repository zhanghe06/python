# encoding: utf-8
__author__ = 'zhanghe'


from MySQLdb import *


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': '123456',
    'db': 'phalcon',
    'port': 3306,
}


def test():
    try:
        conn = Connection(db_config['host'], db_config['user'], db_config['passwd'], db_config['db'], db_config['port'])
        cur = conn.cursor()
        cur.execute("set NAMES UTF8")  # 解决乱码
        sql = 'select * from user where id = 4'
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            print None
            return None
        else:
            print type(row)
            if '??' in row[1]:
                print '存在乱码'
            print '%s\t%s' % (row[0], row[1])
            print '%s\t%s' % (type(row[0]), type(row[1]))
            return row
    except Exception, e:
        print e


if __name__ == '__main__':
    test()

"""
zhanghe@ubuntu:~$ mysql -uroot -p123456
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 49
Server version: 10.0.21-MariaDB-1~trusty-log mariadb.org binary distribution

Copyright (c) 2000, 2015, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| phalcon            |
| phpmyadmin         |
+--------------------+
5 rows in set (0.04 sec)

MariaDB [(none)]> use phalcon;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [phalcon]> show tables;
+-------------------+
| Tables_in_phalcon |
+-------------------+
| contact           |
| orderdetail       |
| orderlist         |
| product           |
| shipper           |
| user              |
+-------------------+
6 rows in set (0.00 sec)

MariaDB [phalcon]> select * from user limit 4;
+----+--------+
| id | name   |
+----+--------+
|  1 | 张三   |
|  2 | 李四   |
|  3 | 王五   |
|  4 | 关羽   |
+----+--------+
4 rows in set (0.00 sec)

MariaDB [phalcon]>
"""


"""
程序显示结果
1	??
居然乱码，查下原因

MariaDB [phalcon]> show variables like '%char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)

MariaDB [phalcon]>

执行sql语句之前加上以下设置：
cur.execute("set NAMES UTF8")
再次执行没有乱码
<type 'tuple'>
4	关羽
<type 'long'>	<type 'str'>
"""