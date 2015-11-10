# encoding: utf-8
__author__ = 'zhanghe'

import json
import time
import os


class ExportBulk(object):
    """
    导出bulk文件工具类
    """
    def __init__(self, index_name, type_name, file_name=None):
        self._index = index_name
        self._type = type_name
        if file_name is None:
            file_name = 'bulk_%s.bulk' % time.time()
        file_path = os.path.dirname(file_name)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        self.bulk_fp = open(file_name, 'a')

    def write(self, index_id, body):
        """
        文件写入
        """
        self.bulk_fp.write(json.dumps({"index": {"_index": self._index, '_type': self._type, 'id': index_id}})+"\n")
        self.bulk_fp.write(json.dumps(body)+"\n")

    def close(self):
        """
        关闭文件资源
        """
        self.bulk_fp.close()


class ExportJson(object):
    """
    导出json文件工具类
    """
    def __init__(self, file_name):
        if file_name is None:
            file_name = 'json_%s.json' % time.time()
        file_path = os.path.dirname(file_name)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        self.json_fp = open(file_name, 'a')

    def write(self, data):
        """
        文件写入
        """
        self.json_fp.write(json.dumps(data).decode('raw_unicode_escape')+"\n")

    def close(self):
        """
        关闭文件资源
        """
        self.json_fp.close()


def test_bulk():
    """
    测试ExportBulk
    """
    export_bulk = ExportBulk('service', 'provider')
    test_id = '1'
    test_body = {'a': '001', 'b': '002'}
    export_bulk.write(test_id, test_body)
    export_bulk.close()


if __name__ == '__main__':
    test_bulk()