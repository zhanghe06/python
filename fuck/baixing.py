#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: baixing.py
@time: 2017/2/10 下午6:08
"""


import requests
import re
import time
import lxml.html


UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


def get_city():
    """
    获取所有城市
    :return:
    """
    header = {
        'Host': 'www.baixing.com',
        'User-Agent': UserAgent
    }
    city_url = 'http://www.baixing.com/?changeLocation=yes'

    response = requests.get(city_url, headers=header)
    html = response.text
    # print html
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//ul/li/a')
    # print link_list
    link_rule = u'<a href="//(.*?).baixing.com/">(.*?)</a>'
    for link in link_list:
        link_html = lxml.html.tostring(link, encoding='utf-8')
        city_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        for city in city_result:
            yield city


def get_area(city_code):
    """
    获取区域
    :return:
    """
    header = {
        'Host': '%s.baixing.com' % city_code,
        'Referer': 'http://%s.baixing.com/' % city_code,
        'User-Agent': UserAgent
    }
    city_url = 'http://%s.baixing.com/baomu/' % city_code
    # , proxies={'http': 'http://192.168.2.158:3128'}
    response = requests.get(city_url, headers=header)
    html = response.text
    # print html
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//div[contains(@class,"area")]')
    link_rule = u'<a href="/baomu/(.*?)/">(.*?)</a>'
    for link in link_list:
        link_html = lxml.html.tostring(link, encoding='utf-8')
        area_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        for area in area_result:
            yield area


def get_cate(cate_code):
    """
    获取区域
    :return:
    """
    header = {
        'Host': 'shanghai.baixing.com',
        'User-Agent': UserAgent
    }
    cate_url = 'http://shanghai.baixing.com/%s/' % cate_code
    # , proxies={'http': 'http://192.168.2.158:3128'}
    response = requests.get(cate_url, headers=header)
    html = response.text
    # print html
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//div[@class="links"]')
    link_rule = u'<a href="/%s/(.*?)/">(.*?)</a>' % cate_code
    # print link_list
    for link in link_list:
        link_html = lxml.html.tostring(link, encoding='utf-8')
        # print link_html
        cate_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        for cate in cate_result:
            yield cate


def output_area():
    """
    输出地区
    :return:
    """
    for city in get_city():
        print '# %s' % city[1]
        print '\'%s\': [' % city[0]
        for area in get_area(city[0]):
            print '\t\'%s\',  # %s' % (area[0], area[1])
        print ']'


def test_area(city_code):
    print '# %s' % ''
    print '\'%s\': [' % city_code
    for area in get_area(city_code):
        print '\t\'%s\',  # %s' % (area[0], area[1])
    print '],'


def test_city():
    for i in get_city():
        print i[0], i[1]


def test_cate(cate_code):
    print '# %s' % ''
    print '\'%s\': [' % cate_code
    for cate in get_cate(cate_code):
        print '\t\'%s\',  # %s' % (cate[0], cate[1])
    print '],'


if __name__ == '__main__':
    # output_area()
    # test_area('taian')
    # test_city()
    test_cate('siyi')
