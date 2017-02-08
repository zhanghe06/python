# encoding: utf-8
__author__ = 'zhanghe'

import sys
reload(sys)

sys.setdefaultencoding('utf-8')

import requests
import re
import json
import lxml.html
import csv


UserAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'


def get_city_list():
    """
    获取城市列表
    """
    # 入口页的url
    url = 'http://www.58.com/changecity.aspx'
    header = {
        'Host': 'www.58.com',
        'Referer': 'http://www.58.com/',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    rule = '<a href="http://(.*?).58.com/" onclick="co\(\'.*?\'\)">(.*?)</a>'
    city_list = re.compile(rule, re.S).findall(html)
    city = {}
    for item in city_list:
        city[item[0]] = item[1]
    print json.dumps(city, indent=4).decode('raw_unicode_escape')


def parse_city_list():
    """
    解析城市列表(去除海外城市)
    """
    # 入口页的url
    url = 'http://www.58.com/changecity.aspx'
    header = {
        'Host': 'www.58.com',
        'Referer': 'http://www.58.com/',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    # 省份
    province_list = doc.xpath('//dl[@id="clist"]//dt[not(@class)]/text()')[:-1]
    # for i in province_list:
    #     print i

    # 城市
    city_rule = '<a href="http://(.*?).58.com/" onclick="co\(\'.*?\'\)">(.*?)</a>'
    city_list = doc.xpath('//dl[@id="clist"]//dd[not(@class)]')[:-1]

    result = []
    for index, city_item in enumerate(city_list):
        city_link_list = city_item.xpath('./a')
        for city_link in city_link_list:
            city_link_html = lxml.html.tostring(city_link, encoding='utf-8')
            city_result = re.compile(city_rule, re.S).findall(city_link_html)
            print city_result[0][0], city_result[0][1], province_list[index]
            result.append([city_result[0][0], city_result[0][1], province_list[index]])

    # 校验省份城市数量
    # print len(province_list), len(city_list)

    return result


def get_cate_list_shenghuo():
    """
    获取分类列表
    """
    # 入口页的url
    url = 'http://sh.58.com/shenghuo.shtml'  # 家政服务

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    cate_list = doc.xpath('//div[@class="sublist"]//dl[@class="catecss-item"]')

    cate_title_rule = '<dt><a href="http://sh.58.com/(.*?)(.shtml|/)" target="_blank".*?>(.*?)</a>'
    cate_item_rule = '<a href="http://sh.58.com/(.*?)/" target="_blank".*?>(.*?)</a>'

    for i in cate_list:
        cate_title_html = lxml.html.tostring(i.xpath('./dt')[0], encoding='utf-8')
        cate_item_html = lxml.html.tostring(i.xpath('./dd')[0], encoding='utf-8')
        # 标题
        cate_title_result = re.compile(cate_title_rule, re.S).findall(cate_title_html)
        for cate_title_list in cate_title_result:
            print '#', '#', cate_title_list[0], cate_title_list[2]

        # 明细
        cate_item_result = re.compile(cate_item_rule, re.S).findall(cate_item_html)
        cate = {}
        for cate_item_list in cate_item_result:
            cate[cate_item_list[0]] = cate_item_list[1].strip()
            print cate_item_list[0], cate_item_list[1].strip()
        # print json.dumps(cate, indent=4).decode('raw_unicode_escape')


def get_cate_list_zhuangxiujc():
    """
    获取分类列表
    """
    # 入口页的url
    # url = 'http://sh.58.com/hunjiehunqing.shtml'  # 婚庆摄影
    url = 'http://sh.58.com/zhuangxiujc.shtml'  # 装修建材

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    cate_title_list = doc.xpath('//div[@class="banner-cont"]/div[@class="sidebar"]/ul/li//a')
    cate_list = doc.xpath('//div[@class="banner-cont"]/div[@class="sublist"]/div[@class="catecss"]')

    cate_title_rule = '<a href="http://sh.58.com/(.*?)" target="_blank".*?>(.*?)</a>'
    cate_item_rule = '<a href="http://sh.58.com/(.*?)/" target="_blank".*?>(.*?)</a>'

    # 标题
    title_list = []
    for i in cate_title_list:
        cate_title_html = lxml.html.tostring(i, encoding='utf-8')
        cate_title_result = re.compile(cate_title_rule, re.S).findall(cate_title_html)
        for cate_title_list in cate_title_result:
            # print '#', '#', cate_title_list[0], cate_title_list[1]
            title_list.append([cate_title_list[0], cate_title_list[1]])
    # 明细
    for i, m in enumerate(cate_list[:len(title_list)]):
        # 输出标题
        print '#', '#', title_list[i][0], title_list[i][1]
        for n in m.xpath('./a'):
            cate_item_html = lxml.html.tostring(n, encoding='utf-8')
            cate_item_result = re.compile(cate_item_rule, re.S).findall(cate_item_html)
            cate = {}
            # 输出明细
            for cate_item_list in cate_item_result:
                cate[cate_item_list[0]] = cate_item_list[1].strip()
                print cate_item_list[0], cate_item_list[1].strip()


def get_cate_list_shangwu():
    """
    获取分类列表
    """
    # 入口页的url
    url = 'http://sh.58.com/shangwu.shtml'  # 商务服务
    # url = 'http://sh.58.com/lvyouxiuxian.shtml'  # 旅游酒店
    # url = 'http://sh.58.com/zhaoshang.shtml'  # 招商加盟
    # url = 'http://sh.58.com/xiuxianyl.shtml'  # 休闲娱乐

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    cate_list = doc.xpath('//div[@class="sublist"]//div[@class="catecss"]/dl')

    cate_title_rule = '<a href="http://sh.58.com/(.*?)(.shtml|/)" target="_blank".*?>(.*?)</a>'
    cate_item_rule = '<a href="http://sh.58.com/(.*?)/" target="_blank".*?>(.*?)</a>'

    for i in cate_list:
        cate_title_html = lxml.html.tostring(i.xpath('./dt/a')[0], encoding='utf-8')
        cate_item_html = lxml.html.tostring(i.xpath('./dd')[0], encoding='utf-8')
        # 标题
        cate_title_result = re.compile(cate_title_rule, re.S).findall(cate_title_html)
        for cate_title_list in cate_title_result:
            print '#', '#', cate_title_list[0], cate_title_list[2]

        # 明细
        cate_item_result = re.compile(cate_item_rule, re.S).findall(cate_item_html)
        cate = {}
        for cate_item_list in cate_item_result:
            cate[cate_item_list[0]] = cate_item_list[1].strip()
            print cate_item_list[0], cate_item_list[1].strip()


def get_contacts():
    """
    获取联系方式
    :return:
    """
    url = 'http://sh.58.com/hyjk/listAjaxApi/'
    header = {
        'Host': 'sh.58.com',
        'Referer': 'http://sh.58.com/',
        'User-Agent': UserAgent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    s_ajax_param = 's_contact_baojie_196139473193474552186077834_'
    param = '25953277422517_38982245142801_0_adsumplayinfo_8DAA63759947EF47858F8EA3AD3D3F1D'
    form_data = {
        'ajax_param': s_ajax_param + param,
        'lmcate': ''
    }
    response = requests.post(url, data=form_data, headers=header)

    print json.dumps(response.json(), indent=4, ensure_ascii=False)


def get_promotion_info():
    """
    获取会员推广信息
    :return:
    """
    url = 'http://sh.58.com/hyjk/listAjaxApi/'
    header = {
        'Host': 'sh.58.com',
        'Referer': 'http://sh.58.com/',
        'User-Agent': UserAgent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    ajax_param = '{"platform":"pc","infoMethod":["renzheng","wltAge"],"dataParam":"27635365552076_42349714013201_0_adinfo,23978226171963_30110967056649_0_promationinfo,27228545116992_7715319655942_0_promationinfo,24267133521976_31011764_0_promationinfo,26341531878841_39825442758928_0_promationinfo,27537787529538_42349714013201_0_promationinfo,27369765592510_31131127077388_0_promationinfo,26203081582670_39732159639312_0_promationinfo,26852770947242_36265725460496_0_promationinfo,27227627875130_36460206072079_0_promationinfo,26919564208079_34723293059851_0_promationinfo,27297229859020_41908793267472_0_promationinfo,25970724472781_39209928147477_0_promationinfo,9709048675466_2881415678214_0_promationinfo,25526822994222_28276516466439_0_promationinfo,23733432686387_34539145627401_0_promationinfo,23746434952376_34806212995846_0_promationinfo,26428537311295_40089453348885_0_promationinfo,21175695050380_28305155861767_0_promationinfo,25897156976720_38365916388886_0_promationinfo,26760665594574_40165314644754_0_promationinfo,26671643928779_31928151670537_0_promationinfo,25743851768512_38681202520851_0_promationinfo,27374487786958_42065473327117_0_promationinfo,27094804372404_23677654908934_0_promationinfo,26576085167292_40404568069136_0_promationinfo,27646817870019_958976883975_0_promationinfo,26499543940540_40264006853649_0_promationinfo,18697452964869_24568846015751_0_promationinfo,26240781793081_39741342008592_0_promationinfo,27235189567049_41775030971412_0_promationinfo,25847911701436_28254579084295_0_promationinfo,26742286458571_40728598353936_0_promationinfo,27518150853831_42307833403927_0_promationinfo,19997647110789_27265893924870_0_promationinfo,22826141761824_17067318798087_0_promationinfo","dispCateId":168,"dispCateName":"baojie","pageIndex":8,"paramMap":null}'
    form_data = {
        'ajax_param': ajax_param,
        'lmcate': ''
    }
    response = requests.post(url, data=form_data, headers=header)

    print json.dumps(response.json(), indent=4, ensure_ascii=False)


def get_area_list(city_code, city_name, province='', district=''):
    """
    获取区域列表
    :param city_code:
    :param city_name:
    :param province:
    :param district:
    :return:
    """
    url = 'http://%s.58.com/banjia/' % city_code

    header = {
        'Host': '%s.58.com' % city_code,
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//dd[@id="local"]/a')
    link_rule = u'<a href="/(.*?)/banjia/">(.*?)</a>'
    area_list = []
    print "# %s" % city_name
    print "'%s': [" % city_code
    for i, link in enumerate(link_list):
        link_html = lxml.html.tostring(link, encoding='utf-8').strip()
        link_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        for v in link_result:
            area_list.append((v[0], v[1]))
            print "\t'%s'%s  # %s" % (v[0], ',' if (i + 1) < len(link_list) else '', v[1])
    print "]"

    return {
        'city_code': city_code,
        'city_name': city_name,
        'province': province,
        'district': district,
        'area_list': area_list,
    }


def print_city_area():
    """
    打印城市地区
    :return:
    """
    city_list = parse_city_list()
    for city_code, city_name, province_name in city_list:
        get_area_list(city_code, city_name)


def get_cate_list(cate_code, cate_name):
    """
    获取分类列表
    :param cate_code:
    :param cate_name:
    :return:
    """
    url = 'http://sh.58.com/%s/' % cate_code

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//dd[@id="ObjectType" or @id="objecttype"]/a')
    # link_rule = u'<a href="/(.*?)">(.*?)</a>'
    link_rule = u'<a href="http://sh.58.com/(.*?)/">(.*?)</a>'
    area_list = []
    print "# %s" % cate_name
    print "'%s': [" % cate_code
    for i, link in enumerate(link_list):
        link_html = lxml.html.tostring(link, encoding='utf-8').strip()
        # print link_html
        link_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        for v in link_result:
            area_list.append((v[0], v[1]))
            print "\t'%s'%s  # %s" % (v[0], ',' if (i + 1) < len(link_list) else '', v[1])
    print "]"


def read_csv(csv_file_path):
    """
    读取csv文件
    :param csv_file_path:
    :return:
    """
    with open(csv_file_path, 'rb') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print json.dumps(row, ensure_ascii=False)
            yield row


def write_csv(csv_file_path, rows):
    """
    写入csv文件
    :param csv_file_path:
    :param rows:
    :return:
    """
    with open(csv_file_path, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in rows:
            csv_writer.writerow(row)


def output_city_area():
    """
    输出城市地区到文件
    :return:
    """
    with open('city_area2.py', 'wb') as f:
        rows = read_csv('city_map_58.csv')
        f.write("# encoding: utf-8\n\n")
        f.write("area = {\n")
        for row in rows:
            city_code = row['city_code']
            city_name = row['city_name']
            province = row['province']
            district = row['district']
            city_info = get_area_list(city_code, city_name, province, district)
            f.write("    # %s %s %s\n" % (city_name, province, district))
            f.write("    '%s': [\n" % city_code)
            for area in city_info['area_list']:
                f.write("        '%s',  # %s\n" % (area[0], area[1]))
            f.write("    ],\n")
            f.flush()
        f.write("}\n")


if __name__ == '__main__':
    # get_city_list()
    # parse_city_list()
    # get_cate_list_shenghuo()
    # get_cate_list_zhuangxiujc()
    # get_cate_list_shangwu()
    # get_contacts()
    # get_promotion_info()
    # print get_area_list('sh', u'上海')
    # print_city_area()
    # read_csv('city_map_58.csv')
    # write_csv('test.csv', [['一', '二', '三'], [1, 2, 3], [5, 6, 7]])
    # output_city_area()
    get_cate_list('caishui', u'-')
