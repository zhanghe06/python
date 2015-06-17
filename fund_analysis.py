# coding=utf-8
__author__ = 'zhanghe'

import requests
import time
import json


url = 'http://fundex2.eastmoney.com/FundWebServices/MyFavorInformation.aspx?t=kf&s=desc&sc=&pstart=0&psize=10000'

fund_list = ['100056', '161024']

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

fc = ','.join(fund_list)

url += '&fc=' + fc

read_list = json.loads(requests.get(url).text)


def save_json(read_dict):
    # 保存json至服务器
    import os
    file_path = 'static/json/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    filename = 'static/json/' + read_dict[u'基金编号'] + '.json'
    result_json = json.dumps(read_dict, ensure_ascii=False, indent=0) + '\n'
    with open(filename, 'a') as f:
        f.write(result_json.encode('utf-8'))


def run():
    for i in read_list:
        item = {}
        # 基本信息
        item[u'记录时间'] = time.strftime('%H:%M')
        item[fund_dict['fundcode']] = i['fundcode']  # 基金编号
        item[fund_dict['name']] = i['name']  # 基金名称
        item[fund_dict['jjlx']] = i['jjlx']  # 基金类型
        # 估值信息
        item[fund_dict['gztime']] = i['gztime']  # 估值时间
        item[fund_dict['gsz']] = i['gsz']  # 估算净值
        item[fund_dict['gszzl']] = i['gszzl']  # 估算涨幅
        # 历史信息
        item[fund_dict['jzrq']] = i['jzrq']  # 净值日期
        item[fund_dict['dwjz']] = i['dwjz']  # 单位净值
        item[fund_dict['rzzl']] = i['rzzl']  # 日增长率
        print json.dumps(item, ensure_ascii=False, indent=4)
        save_json(item)


if __name__ == "__main__":
    run()


"""
fc=100056,161024
9点-16点
整个过程9小时
2分钟抓取一次
9*60/2 = 270次/天

# 100056.json 名称为基金编号
analysis_list = []

每2分钟 追加写入
{u'编号': xxx, u'名称': xxx, u'时间': xxx, u'估值': xxx},
{u'编号': xxx, u'名称': xxx, u'时间': xxx, u'估值': xxx},
{u'编号': xxx, u'名称': xxx, u'时间': xxx, u'估值': xxx},
{u'编号': xxx, u'名称': xxx, u'时间': xxx, u'估值': xxx},
{u'编号': xxx, u'名称': xxx, u'时间': xxx, u'估值': xxx},
{u'编号': xxx, u'名称': xxx, u'时间': xxx, u'估值': xxx},
"""
