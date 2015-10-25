# encoding: utf-8
__author__ = 'zhanghe'


import json
from elasticsearch import Elasticsearch
from elasticsearch import exceptions
es = Elasticsearch()


def test_index():
    """
    测试创建索引
    """
    try:
        # row = [1, 'Lynda', '123456']
        # row = [2, 'Halley', '123457']
        row = [3, 'Randal', '123458']
        doc = {
            'user_id': row[0],
            'user_name': row[1],
            'user_phone': row[2]
        }
        res = es.index(index='user', doc_type='user_info', body=doc)
        print res
        # {u'_type': u'user_info', u'_id': u'AVCfrGw0nWFCzxDkZOGk', u'created': True, u'_version': 1, u'_index': u'user'}
        # {u'_type': u'user_info', u'_id': u'AVCfsgeanWFCzxDkZOK_', u'created': True, u'_version': 1, u'_index': u'user'}
        # {u'_type': u'user_info', u'_id': u'AVCftoEgnWFCzxDkZOOM', u'created': True, u'_version': 1, u'_index': u'user'}
    except Exception, e:
        print e


def test_update():
    """
    测试更新索引
    """
    try:
        doc = {
            'user_id': 5,
            'user_name': 'Lacy',
            'user_phone': '000000'
        }
        res = es.update(index='user', doc_type='user_info', id='AVCf2nv0nWFCzxDkZOn3', body={'doc': doc})
        print json.dumps(res, indent=4)
        # {
        #     "_type": "user_info",
        #     "_id": "AVCf2nv0nWFCzxDkZOn3",
        #     "_version": 2,
        #     "_index": "user"
        # }
    except exceptions.NotFoundError:
        print '文档不存在，或已被删除'
    except Exception, e:
        print e


def test_delete():
    """
    测试删除索引
    """
    try:
        res = es.delete(index='user', doc_type='user_info', id='AVCf2nv0nWFCzxDkZOn3')
        print json.dumps(res, indent=4)
        # {
        #     "found": true,
        #     "_type": "user_info",
        #     "_id": "AVCf2nv0nWFCzxDkZOn3",
        #     "_version": 3,
        #     "_index": "user"
        # }
    except exceptions.NotFoundError:
        print '文档不存在，或已被删除'
    except Exception, e:
        print e


def test_get():
    """
    测试查询索引
    """
    try:
        res = es.get(index='user', doc_type='user_info', id='AVCfrGw0nWFCzxDkZOGk')
        print json.dumps(res, indent=4)
        # {
        #     "_type": "user_info",
        #     "_source": {
        #         "user_id": 1,
        #         "user_phone": "123456",
        #         "user_name": "Lynda"
        #     },
        #     "_index": "user",
        #     "_version": 1,
        #     "found": true,
        #     "_id": "AVCfrGw0nWFCzxDkZOGk"
        # }
    except exceptions.NotFoundError:
        print '文档不存在，或已被删除'
    except Exception, e:
        print e


if __name__ == "__main__":
    # test_index()
    # test_update()
    # test_delete()
    test_get()
