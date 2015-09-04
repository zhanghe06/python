# encoding: utf-8
__author__ = 'zhanghe'

import requests
import json
import time
import os
import csv
from pyquery import PyQuery as Pq

# 登录页的url
url_base = 'http://sh.ganji.com/zpshichangyingxiao/'
url_root = '%s%s?hq=1' % (url_base, '')
# 伪装成浏览器
header = {
    'Host': 'sh.ganji.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()


# file_html = response.text
# # 保存文件
# with open('ganji.html', 'w') as f:
#     f.write(file_html.encode('utf-8'))

# # 读取抓取的页面
# with open('ganji.html', 'r') as f:
#     file_html = f.read()


def visit_page(url):
    """
    访问页面
    """
    response = s.get(url, headers=header)
    return response.text


def get_info(file_html):
    """
    获取页面关键信息
    """
    text_pq = Pq(file_html)
    tr_list = text_pq('.fir-messa').find('.name')

    for tr_item in tr_list:
        td_list = Pq(tr_item).find('a')
        item_dict = {
            u'公司编号': td_list.attr('company_id'),
            u'职位名称': td_list.text(),
            u'职位链接': td_list.attr('href'),
            u'薪资待遇': '',
            u'工作地点': '',
            u'工作经验': '',
            u'最低学历': '',
            u'招聘人数': '',
            u'公司规模': '',
        }

        introduce_list = Pq(tr_item).find('.s-butt.s-bb1 ul li')
        for introduce_item in introduce_list:
            item_text = Pq(introduce_item).text()
            item_list = item_text.split('： ')
            if len(item_list) < 2:
                continue
            key = item_list[0]
            value = item_list[1]
            item_dict[key] = value
        yield item_dict
    print '单页共 %s 条记录' % len(tr_list)


def get_info_5(file_html):
    """
    获取页面关键信息
    """
    text_pq = Pq(file_html)
    tr_list = text_pq('.normal-fir').find('.name')

    for tr_item in tr_list:
        td_list = Pq(tr_item).find('a')
        item_dict = {
            u'公司编号': td_list.attr('company_id'),
            u'职位名称': td_list.text(),
            u'职位链接': td_list.attr('href'),
            u'薪资待遇': '',
            u'工作地点': '',
            u'工作经验': '',
            u'最低学历': '',
            u'招聘人数': '',
            u'公司规模': '',
        }

        introduce_list = Pq(tr_item).find('.s-butt.s-bb1 ul li')
        for introduce_item in introduce_list:
            item_text = Pq(introduce_item).text()
            item_list = item_text.split('： ')
            if len(item_list) < 2:
                continue
            key = item_list[0]
            value = item_list[1]
            item_dict[key] = value
        yield item_dict
    print '单页共 %s 条记录' % len(tr_list)


def write_csv_head():
    """
    创建csv文件标题
    :return:
    """
    file_path = '../static/csv/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    # 创建CSV文件
    csv_file_name = file_path + 'ganji.csv'
    csv_file = file(csv_file_name, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(['公司编号', '职位名称', '职位链接', '薪资待遇', '工作地点', '工作经验', '最低学历', '招聘人数', '公司规模'])
    csv_file.close()


def save_csv(item_dict):
    """
    保存csv文件
    """
    file_path = '../static/csv/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    # 创建CSV文件
    csv_file_name = file_path + 'ganji.csv'
    csv_file = file(csv_file_name, 'a')
    writer = csv.writer(csv_file)
    # writer.writerow(['公司编号', '职位名称', '职位链接', '薪资待遇', '工作地点', '工作经验', '最低学历', '招聘人数', '公司规模'])
    item_tuple = (
        item_dict[u'公司编号'],
        item_dict[u'职位名称'],
        item_dict[u'职位链接'],
        item_dict[u'薪资待遇'],
        item_dict[u'工作地点'],
        item_dict[u'工作经验'],
        item_dict[u'最低学历'],
        item_dict[u'招聘人数'],
        item_dict[u'公司规模']
    )
    writer.writerow(item_tuple)
    csv_file.close()


def fuck(max_page_num=10):
    """
    主程序，获取max_page_num个页面的数据，并写入csv文件
    """
    write_csv_head()
    for i in xrange(max_page_num):
        if i > 0:
            page = 'o'+str(i+1)
            url = '%s%s?hq=1' % (url_base, page)
            page_pre = 'o'+str(i+1)
            header['Referer'] = '%s%s?hq=1' % (url_base, page_pre)
        else:
            url = url_root
        html_text = visit_page(url)
        if i < 5:
            for item in get_info(html_text):
                save_csv(item)
        else:
            for item in get_info_5(html_text):
                save_csv(item)
        # time.sleep(8)


if __name__ == "__main__":
    fuck(100)


"""
赶集网公司-职位列表页抓取

主要内容的区块
<div class="fir-messa">

根据company_id可以组装公司详情页面的地址：
http://www.ganji.com/gongsi/26735941/

太奇葩了，前4页源码居然和后面的不一致。也是醉了～～
"""