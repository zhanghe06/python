#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_pandas.py
@time: 2017/2/27 下午3:21
"""


from pandas import Series, DataFrame
import pandas as pd
import json


def test_csv():
    file_path = 'test_pandas.csv'
    df = pd.read_csv(file_path)
    print df.keys()
    print df.values
    print df.add_prefix('a')
    print df.add_suffix('c')
    print df.index
    print df.dtypes
    print df.rename(columns=['网站', '权重', '类型'])


def test_excel():
    file_path = 'test_pandas.xls'
    df = pd.read_excel(file_path, sheetname='Sheet1')  # sheet_name=str(0)
    print df

    with pd.ExcelWriter('newxls.xls') as writer:
        df.to_excel(writer, sheet_name=str(0))


def test_csv_encode():
    """
    测试csv读取，设置编码，并跳过头部
    :return:
    """
    file_path = 'test_pandas_gb2312.csv'
    df = pd.read_csv(file_path, encoding='gb2312', skiprows=8, error_bad_lines=False)
    print df.keys()
    print df


def test_read_sem_excel():
    file_path = 'SEM.xls'
    df = pd.read_excel(file_path, sheetname='sem')  # sheet_name=str(0)
    # [u'sem_site', u'sem_plan', u'sem_unit', u'sc_site', u'sc_site_name', u'cate_id', u'cate_name', u'city_id', u'city_name', u'sc_plat', u'sc_plat_name']
    print list(df.keys())
    # print df.to_dict()
    sem_map = {}
    for i in df.values:
        sem_map[(i[0], i[1], i[2])] = {
            'sc_site': i[3],
            'sc_site_name': i[4],
            'cate_id': i[5],
            'cate_name': i[6],
            'city_id': i[7],
            'city_name': i[8],
            'sc_plat': i[9],
            'sc_plat_name': i[10],
        }
    # print json.dumps(sem_map, indent=4, ensure_ascii=False)
    print sem_map
    return sem_map


if __name__ == '__main__':
    # test_csv()
    # test_excel()
    # test_csv_encode()
    test_read_sem_excel()


"""
pip install pandas
# 操作excel
pip install xlrd
"""

