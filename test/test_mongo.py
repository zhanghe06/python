# encoding: utf-8
__author__ = 'zhanghe'


import sys
sys.path.append('..')
from tools.mongo import Mongodb


db_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'test_user'
}


test_date = [
    {
        '_id': 1,
        'id': 1,
        'name': 'Lily',
        'sex': 'F',
        'age': 20,
        'city': 'shanghai',
    },
    {
        '_id': 2,
        'id': 2,
        'name': 'Tom',
        'sex': 'M',
        'age': 22,
        'city': 'shanghai',
    },
    {
        '_id': 3,
        'id': 3,
        'name': 'Jerry',
        'sex': 'M',
        'age': 22,
        'city': 'beijing',
    }
]


def test():
    try:
        conn = Mongodb(db_config)
        print conn.db
        print conn.find_one('user')
        print conn.remove('user')
        print conn.insert('user', test_date)
        print conn.update('user', {'id': 1}, {'$set': {'age': 28}})
        conn.output_rows('user')
    except Exception, e:
        print e


if __name__ == '__main__':
    test()


"""
Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'test_user')
None
[1, 2, 3]
**********  表名[user]  [1/3]  **********
city : shanghai
name : Lily
 sex : F
 age : 20
  id : 1
 _id : 1
**********  表名[user]  [2/3]  **********
city : shanghai
name : Tom
 sex : M
 age : 22
  id : 2
 _id : 2
**********  表名[user]  [3/3]  **********
city : beijing
name : Jerry
 sex : M
 age : 22
  id : 3
 _id : 3
"""
