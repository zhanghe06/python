# coding=utf-8
__author__ = 'zhanghe'

import requests
import time
import json
import os
import csv

today = time.strftime("%Y-%m-%d", time.localtime())
import tools.timed_task
tools.timed_task.start_time = ' '.join((today, '09:00:00'))
tools.timed_task.end_time = ' '.join((today, '15:00:00'))
tools.timed_task.interval = 60*2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# app接口
url = 'http://fundex2.eastmoney.com/FundWebServices/MyFavorInformation.aspx?t=kf&s=desc&sc=&pstart=0&psize=10000'

# 待处理基金编号
fund_list = ['100056', '161024']

# 基金字典对应关系
fund_dict = {
    'gztime': u'估值时间',
    'shzt': u'赎回状态',
    'name': u'基金名称',
    'gszzl': u'估算涨幅',
    'gsz': u'估算净值',
    'jjlx': u'基金类型',
    'rzzl': u'日增长率',
    'jzrq': u'净值日期',
    'sgzt': u'申购状态',
    'fundcode': u'基金编号',
    'isgz': '',
    'syl': u'收益率',
    'htpj': '',
    'nkfr': '',
    'dwjz': u'单位净值',
    'ljjz': u'累计净值',
    'isbuy': '1'
}

# 组装接口
fc = ','.join(fund_list)
url += '&fc=' + fc


def save_json(read_dict):
    """
    保存json文件至服务器
    :param read_dict:
    :return:
    """
    file_path = 'static/json/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    filename = file_path + read_dict[u'基金编号'] + '.json'
    result_json = json.dumps(read_dict, ensure_ascii=False) + '\n'  # 单行存储
    with open(filename, 'a') as f:
        f.write(result_json.encode('utf-8'))


def read_line(code):
    """
    逐行读取数据
    :param code:
    :return:
    """
    filename = 'static/json/' + code + '.json'
    with open(filename, 'r') as files:
        for each_line in files:
            print each_line


def run_read():
    """
    读取本地数据
    """
    for i in fund_list:
        read_line(i)


@tools.timed_task.timed_task
def run_write():
    """
    获取数据，写入本地
    """
    response = requests.get(url)
    content = response.text
    read_list = json.loads(content)
    for item in read_list:
        item_dict = {
            # 基本信息
            u'记录时间': time.strftime('%H:%M'),
            fund_dict['fundcode']: item['fundcode'],
            fund_dict['name']: item['name'],
            fund_dict['jjlx']: item['jjlx'],
            # 估值信息
            fund_dict['gztime']: item['gztime'],
            fund_dict['gsz']: item['gsz'],
            fund_dict['gszzl']: item['gszzl'],
            # 历史信息
            fund_dict['jzrq']: item['jzrq'],
            fund_dict['dwjz']: item['dwjz'],
            fund_dict['rzzl']: item['rzzl']
        }
        print json.dumps(item_dict, ensure_ascii=False, indent=4)
        save_json(item_dict)


def save_csv(code):
    """
    读取json数据，保存csv文件
    """
    file_path = 'static/csv/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    # 创建CSV文件
    csv_file_name = file_path + str(code) + '.csv'
    csv_file = file(csv_file_name, 'wb')
    writer = csv.writer(csv_file)
    writer.writerow(['记录时间', '基金编号', '基金名称', '基金类型', '估值时间', '估算净值', '估算涨幅', '净值日期', '单位净值', '日增长率'])
    # 读取json数据文件
    filename = 'static/json/' + str(code) + '.json'
    with open(filename, 'r') as files:
        for each_line in files:
            item = json.loads(each_line)
            item_tuple = (
                item[u'记录时间'],
                item[u'基金编号'],
                item[u'基金名称'],
                item[u'基金类型'],
                item[u'估值时间'],
                item[u'估算净值'],
                item[u'估算涨幅'],
                item[u'净值日期'],
                item[u'单位净值'],
                item[u'日增长率']
            )
            writer.writerow(item_tuple)
    csv_file.close()


if __name__ == "__main__":
    # run_write()
    # run_read()
    run_write()
    # save_csv('161024')


"""
因为只有app接口数据实时更新
这里采用app接口作为数据来源
[使用Fiddler捕获接口即可]
fc=100056,161024
9点-16点
整个过程9小时
2分钟抓取一次
9*60/2 = 270次/天
# 100056.json 名称为基金编号
每2分钟 追加写入

备注：
本程序采用单条记录单独追加写入的保存方式
适合这种保存不太密集的场景
对于大数据的批量处理，不适合这种方式（每次单独打开文件句柄比较消耗资源）。
"""
