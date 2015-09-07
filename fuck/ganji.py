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
    header['Host'] = 'sh.ganji.com'
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
            u'公司名称': '',
            u'公司链接': '',
            u'职位名称': td_list.text(),
            u'职位链接': td_list.attr('href'),
            u'薪资待遇': '',
            u'工作地点': '',
            u'工作经验': '',
            u'最低学历': '',
            u'招聘人数': '',
            u'公司规模': '',
        }

        company = Pq(tr_item).find('.s-tit14.fl')
        item_dict[u'公司名称'] = company.text()

        introduce_list = Pq(tr_item).find('.s-butt.s-bb1 ul li')
        for introduce_item in introduce_list:
            item_text = Pq(introduce_item).text()
            item_list = item_text.split('： ')
            if len(item_list) < 2:
                continue
            key = item_list[0]
            value = item_list[1]
            item_dict[key] = value
        # 获取公司联系方式
        contact_dict = get_contact(item_dict[u'公司编号'])
        item_dict = dict(item_dict, **contact_dict)
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
            u'公司名称': '',
            u'公司链接': '',
            u'职位名称': td_list.text(),
            u'职位链接': td_list.attr('href'),
            u'薪资待遇': '',
            u'工作地点': '',
            u'工作经验': '',
            u'最低学历': '',
            u'招聘人数': '',
            u'公司规模': '',
        }

        company = Pq(tr_item).find('.s-tit14.fl')
        item_dict[u'公司名称'] = company.text()

        introduce_list = Pq(tr_item).find('.s-butt.s-bb1 ul li')
        for introduce_item in introduce_list:
            item_text = Pq(introduce_item).text()
            item_list = item_text.split('： ')
            if len(item_list) < 2:
                continue
            key = item_list[0]
            value = item_list[1]
            item_dict[key] = value
        # 获取公司联系方式
        contact_dict = get_contact(item_dict[u'公司编号'])
        item_dict = dict(item_dict, **contact_dict)
        yield item_dict
    print '单页共 %s 条记录' % len(tr_list)


def get_contact(cid):
    """
    获取公司联系方式
    :param cid:
    :return:
    """
    wap_url = 'http://wap.ganji.com/gongsi/%s/?domain=sh' % str(cid)
    header['Host'] = 'wap.ganji.com'
    response = s.get(wap_url, headers=header)
    wap_html = response.content
    wap_pq = Pq(wap_html)
    contact_list = wap_pq('.detail-describe').eq(1)
    name_line = contact_list.find('p').eq(0).text()
    phone_line = contact_list.find('p').eq(1).text()
    contact_dict = {
        u'联系人': '',
        u'联系电话': ''
    }
    if name_line is not None:
        name_line_list = name_line.split('： ')
        if len(name_line_list) == 2:
            contact_dict[u'联系人'] = name_line_list[1]
    if phone_line is not None:
        phone_line_list = phone_line.split('： ')
        if len(phone_line_list) == 2:
            contact_dict[u'联系电话'] = phone_line_list[1].strip(' [拨打]')
    # print contact_dict
    return contact_dict


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
    writer.writerow(['公司编号', '公司名称', '联系人', '联系电话', '公司链接', '职位名称', '职位链接', '薪资待遇', '工作地点', '工作经验', '最低学历', '招聘人数', '公司规模'])
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

    item_tuple = (
        item_dict[u'公司编号'],
        item_dict[u'公司名称'],
        item_dict[u'联系人'],
        item_dict[u'联系电话'],
        'http://www.ganji.com/gongsi/%s/' % str(item_dict[u'公司编号']),
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
    start_time = time.time()
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
    print '程序耗时：%sS' % (time.time() - start_time)


if __name__ == "__main__":
    fuck(100)


"""
赶集网公司-职位列表页抓取

主要内容的区块
<div class="fir-messa">

根据company_id可以组装公司详情页面的地址：
http://www.ganji.com/gongsi/26735941/

太奇葩了，前4页源码居然和后面的不一致。也是醉了～～

准备进一步抓取公司联系人和联系电话
网站上的电话是带干扰功能的图片，尝试识别之后发现，识别率很低，没有意义
进一步发现wap站是文本显示，可以通过抓取wap站获取这类数据。
http://wap.ganji.com/gongsi/5504323/?domain=sh
特征
<div class="detail-describe">
    <p><span>联系人：</span>王小姐</p>
    <p><span>电话联系：</span>86656161 <a href="tel:86656161">[拨打]</a></p>

    <p>
        <span class="line-contact"><a href="tel:86656161">拨打电话</a></span>
        <span class="phone-contact"><a href="/wapim/getMsgs/?userId=64219650">给他留言</a></span>
    </p>
</div>

抓取文件统计

程序耗时：486.772469044S

zhanghe@ubuntu:~/code/python$ du -h static/csv/ganji.csv
720K	static/csv/ganji.csv
zhanghe@ubuntu:~/code/python$ wc -l static/csv/ganji.csv
2965 static/csv/ganji.csv

"""