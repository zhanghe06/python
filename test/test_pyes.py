# encoding: utf-8
__author__ = 'zhanghe'

import pyes


conn = pyes.ES(['127.0.0.1:9200'])  # 连接es


def create():
    conn.create_index('test-index')  # 新建一个索引

    # 定义索引存储结构
    mapping = {u'id': {'boost': 1.0,
                       'index': 'not_analyzed',
                       'store': 'yes',
                       'type': u'string',
                       "term_vector": "with_positions_offsets"},
               u'user_id': {'boost': 1.0,
                            'index': 'not_analyzed',
                            'store': 'yes',
                            'type': u'string',
                            "term_vector": "with_positions_offsets"},
               u'nick': {'boost': 1.0,
                         'index': 'analyzed',
                         'store': 'yes',
                         'type': u'string',
                         "term_vector": "with_positions_offsets"},
               u'city': {'boost': 1.0,
                         'index': 'analyzed',
                         'store': 'yes',
                         'type': u'string',
                         "term_vector": "with_positions_offsets"},
               }

    conn.put_mapping("test-type1", {'properties': mapping}, ["test-index"])  # 定义test-type
    conn.put_mapping("test-type2", {"_parent": {"type": "test-type1"}}, ["test-index"])  # 从test-type继承

    # 插入索引数据
    # {"id":"1", "user_id":"u1", "nick":u"压力很大", "city":u"成都"}: 文档数据
    # test-index：索引名称
    # test-type: 类型
    # 1: id 注：id可以不给，系统会自动生成
    conn.index({"id": "1", "user_id": "u1", "nick": u"压力很大", "city": u"成都"}, "test-index", "test-type1", 1)
    conn.index({"id": "2", "user_id": "u2", "nick": u"压力很小", "city": u"北京"}, "test-index", "test-type1")
    conn.index({"id": "3", "user_id": "u3", "nick": u"没有压力", "city": u"成都"}, "test-index", "test-type1")

    conn.default_indices = ["test-index"]  # 设置默认的索引
    conn.refresh()  # 刷新以获得最新插入的文档


def query():
    # 查询nick中包含压力的记录
    q = pyes.StringQuery(u"压力", 'nick')
    results = conn.search(q)

    for r in results:
        print u"查询nick中包含压力的记录", r['nick'], r['city']

    # 查询city中包含成都的数据
    q = pyes.StringQuery(u"成都", 'city')
    results = conn.search(q)

    for r in results:
        print u"查询city中包含成都的数据", r['nick'], r['city']

    # 查询nick中包含很小或没有的数据
    q = pyes.StringQuery(u"很小 OR 没有", 'nick')
    results = conn.search(q)

    for r in results:
        print u"查询nick中包含很小或没有的数据", r['nick'], r['city']


if __name__ == '__main__':
    # create()
    query()