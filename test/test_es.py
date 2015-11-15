# encoding: utf-8
__author__ = 'zhanghe'


import json
import os
import glob
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


def test_search():
    """
    测试搜索索引
    """
    try:
        res = es.search(index='user', doc_type='user_info', q='user_name:Lynda')
        print json.dumps(res, indent=4)
        # {
        #     "hits": {
        #         "hits": [
        #             {
        #                 "_score": 1.0,
        #                 "_type": "user_info",
        #                 "_id": "AVCfrGw0nWFCzxDkZOGk",
        #                 "_source": {
        #                     "user_id": 1,
        #                     "user_phone": "123456",
        #                     "user_name": "Lynda"
        #                 },
        #                 "_index": "user"
        #             }
        #         ],
        #         "total": 1,
        #         "max_score": 1.0
        #     },
        #     "_shards": {
        #         "successful": 5,
        #         "failed": 0,
        #         "total": 5
        #     },
        #     "took": 777,
        #     "timed_out": false
        # }
    except exceptions.NotFoundError:
        print '文档不存在，或已被删除'
    except Exception, e:
        print e


def load_bulk(bulk_file, es_url='localhost:9200'):
    """
    加载bulk文件
    :param bulk_file:
    :param es_url:
    :return:
    """
    cmd = 'curl -s -X POST %s/_bulk?pretty=1 --data-binary @%s' % (es_url, bulk_file)
    output = os.popen(cmd)
    result = output.read()
    print result


def upload_bulk(bulk_dir, suffix='bulk'):
    """
    bulk文件导入ES
    :param bulk_dir:
    :return:
    """
    bulk_dir = ''.join([bulk_dir.rstrip('/'), '/'])
    suffix = suffix.lstrip('.')
    try:
        for file_name in glob.glob(r'%s*.%s' % (bulk_dir, suffix)):
            print('导入bulk文件：%s' % file_name)
            # 导入bulk文件
            load_bulk(file_name)
            # 导入成功修改bulk文件名称，防止下一次重复导入
            os.rename(file_name, ''.join([file_name, '.bak']))
    except OSError:
        print('读取文件失败')
    except Exception, e:
        print(e)


if __name__ == "__main__":
    # test_index()
    # test_update()
    # test_delete()
    # test_get()
    test_search()
    # load_bulk('/data/export/bulk_1447149152.71.bulk')
    # upload_bulk('/data/export/bulk/')
