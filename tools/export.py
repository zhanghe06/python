# encoding: utf-8
__author__ = 'zhanghe'

import json
import time
import os
from datetime import datetime, date


class ExportBulk(object):
    """
    导出bulk文件工具类
    """
    def __init__(self, index_name, type_name, file_name=None):
        self._index = index_name
        self._type = type_name
        if file_name is None:
            file_name = './es_%s_%s_%s.bulk' % (index_name, type_name, time.time())
        file_path = os.path.dirname(file_name)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        self.bulk_fp = open(file_name, 'a')

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

    def write(self, index_id, body):
        """
        文件写入
        """
        self.bulk_fp.write(json.dumps({"index": {"_index": self._index, '_type': self._type, '_id': index_id}})+"\n")
        self.bulk_fp.write(json.dumps(body, ensure_ascii=False, default=self.__default)+"\n")

    def close(self):
        """
        关闭文件资源
        """
        self.bulk_fp.close()


class ExportFile(object):
    """
    导出json/csv文件工具类
    """
    def __init__(self, file_name=None):
        if file_name is None:
            file_name = 'json_%s.json' % time.time()
        file_path = os.path.dirname(file_name)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        self.json_fp = open(file_name, 'a')

    def write(self, data, file_type='json'):
        """
        文件写入
        """
        if file_type == 'json':
            self.json_fp.write(json.dumps(data).decode('raw_unicode_escape')+"\n")
        if file_type == 'csv':
            self.json_fp.write(','.join(data)+"\n")

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