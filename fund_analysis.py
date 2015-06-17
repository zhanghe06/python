# coding=utf-8
__author__ = 'zhanghe'

#import requests
import time
import json


url = 'http://fundex2.eastmoney.com/FundWebServices/MyFavorInformation.aspx?t=kf&s=desc&sc=&pstart=0&psize=10000'

fund_list = ['100056', '161024']

fund_dict = {
    'gztime': '估值时间',
    'shzt': '赎回状态',
    'name': '基金名称',
    'gszzl': '估算涨幅',
    'gsz': '估算净值',
    'jjlx': '基金类型',
    'rzzl': '日增长率',
    'jzrq': '净值日期',
    'sgzt': '申购状态',
    'fundcode': '基金编号',
    'isgz': '',
    'syl': '收益率',
    'htpj': '',
    'nkfr': '',
    'dwjz': '单位净值',
    'ljjz': '累计净值',
    'isbuy': '1'
}


fc = ','.join(fund_list)

url += '&fc='+fc

dict_ls = [{"fundcode":"519158","name":"新华趋势领航","jzrq":"2015-06-16","dwjz":"2.9140","ljjz":"2.9140","rzzl":"-4.05","gsz":"2.9792","gszzl":"2.24","syl":"-4.05","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票型","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"161028","name":"富国中证新能源汽车指数分级","jzrq":"2015-06-16","dwjz":"1.3590","ljjz":"1.3590","rzzl":"-3.7535","gsz":"1.3691","gszzl":"0.74","syl":"-3.75","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票指数","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"161029","name":"富国中证银行指数分级","jzrq":"2015-06-16","dwjz":"1.0750","ljjz":"1.0750","rzzl":"-1.1040","gsz":"1.0796","gszzl":"0.43","syl":"-1.10","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票指数","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"000127","name":"农银行业领先","jzrq":"2015-06-16","dwjz":"2.3115","ljjz":"2.3115","rzzl":"-3.3088","gsz":"2.3592","gszzl":"2.06","syl":"-3.31","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票型","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"150182","name":"富国中证军工指数分级B","jzrq":"2015-06-16","dwjz":"1.5260","ljjz":"3.5980","rzzl":"-7.1776","gsz":"1.5430","gszzl":"1.11","syl":"-7.18","sgzt":"场内交易","shzt":"场内交易","jjlx":"分级杠杆","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"","nkfr":None},{"fundcode":"470006","name":"汇添富医药保健","jzrq":"2015-06-16","dwjz":"2.5660","ljjz":"2.6160","rzzl":"-3.7148","gsz":"2.6198","gszzl":"2.09","syl":"-3.71","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票型","htpj":"★★★★★","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"110023","name":"易方达医疗保健行业","jzrq":"2015-06-16","dwjz":"2.5700","ljjz":"2.5700","rzzl":"-3.8533","gsz":"2.6316","gszzl":"2.40","syl":"-3.85","sgzt":"限大额","shzt":"开放赎回","jjlx":"股票型","htpj":"★★★★","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"100056","name":"富国低碳环保","jzrq":"2015-06-16","dwjz":"3.3280","ljjz":"3.3280","rzzl":"-2.6331","gsz":"3.4126","gszzl":"2.54","syl":"-2.63","sgzt":"限大额","shzt":"开放赎回","jjlx":"股票型","htpj":"★★★★★","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"000697","name":"汇添富移动互联股票","jzrq":"2015-06-16","dwjz":"3.1750","ljjz":"3.1750","rzzl":"-4.6833","gsz":"3.2842","gszzl":"3.44","syl":"-4.68","sgzt":"限大额","shzt":"开放赎回","jjlx":"股票型","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"161024","name":"富国中证军工指数分级","jzrq":"2015-06-16","dwjz":"1.2670","ljjz":"2.3350","rzzl":"-4.4495","gsz":"1.2755","gszzl":"0.67","syl":"-4.45","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票指数","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None},{"fundcode":"163113","name":"申万菱信中证申万证券行业指数分级","jzrq":"2015-06-16","dwjz":"1.1768","ljjz":"2.2999","rzzl":"-1.0677","gsz":"1.1811","gszzl":"0.36","syl":"-1.07","sgzt":"开放申购","shzt":"开放赎回","jjlx":"股票指数","htpj":"","gztime":"2015-06-17","isgz":"","isbuy":"1","nkfr":None}]

for i in dict_ls:
    item = {}
    # 基本信息
    item[fund_dict['fundcode']] = i['fundcode']  # 基金编号
    item[fund_dict['name']] = i['name']          # 基金名称
    item[fund_dict['jjlx']] = i['jjlx']          # 基金类型
    # 估值信息
    item[fund_dict['gztime']] = i['gztime']  # 估值时间
    item[fund_dict['gsz']] = i['gsz']        # 估算净值
    item[fund_dict['gszzl']] = i['gszzl']    # 估算涨幅
    # 历史信息
    item[fund_dict['jzrq']] = i['jzrq']  # 净值日期
    item[fund_dict['dwjz']] = i['dwjz']  # 单位净值
    item[fund_dict['rzzl']] = i['rzzl']  # 日增长率
    print json.dumps(item, ensure_ascii=False, indent=4)


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
