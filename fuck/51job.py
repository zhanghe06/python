# encoding: utf-8
__author__ = 'zhanghe'

import requests
from lxml import etree


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    }

s = requests.session()
tree = None

url_root = 'http://search.51job.com/jobsearch/search_result.php'
payload = {
    'fromJs': '1',
    'jobarea': '010000',    # 城市地区
    'funtype': '0000',      # 职能类别（0000：全部）
    'industrytype': '00',   # 行业
    'issuedate': '8',       # 发布时间（1：近1天，2：近2天，3：近3天，4：近1周，5：近2周，6：近1月，7：近6周，8：近两月，9：所有）
    'providesalary': '99',  # 工资
    'keywordtype': '1',     # 关键词类型（0：公司名，1：职位名，2：全文）
    'lang': 'c',            # 语言
    'stype': '2',           #
    'workyear': '99',       # 工作经验（99：所有）
    'cotype': '99',         # 公司性质（99：所有）
    'degreefrom': '99',     # 最低学历（99：所有）
    'jobterm': '01',        # 工作类型（0：全职，1：兼职，01：全部）
    'companysize': '99',    # 公司规模（99：所有）
    'fromType': '1'         #
}
# 筛选条件：职能类别/行业类别/工作地点 至少要有一个


position_dict = {
    # 公司信息
    'company_name': '',
    'company_url': '',
    'company_industry': '',  # 公司行业
    'company_property': '',  # 公司性质
    'company_size': '',  # 公司规模
    # 职位信息
    'position_create_time': '',  # 发布日期
    'position_area': '',  # 工作地点(地区)
    'position_recruit_num': '',  # 招聘人数
    'position_work_years': '',  # 工作年限
    'position_language_limit': '',  # 语言要求
    'position_degree_limit': '',  # 学    历
    'position_salary_range': '',  # 薪资范围
    'position_benefit': '',  # 薪酬福利
    'Position_function': '',  # 职位职能
    'position_description': '',  # 职位描述
    'position_address': '',  # 上班地址(详细地址)
}


def get_html(url):
    """
    获取页面内容
    """
    response = s.get(url, params=payload, headers=header)
    html = response.content.decode('GBK')
    return html


def load_tree(html):
    """
    加载树
    """
    global tree
    tree = etree.HTML(html)


def extract_list(xpath):
    """
    提取满足条件元素内容的列表
    """
    item_list = tree.xpath(xpath)
    if not item_list:
        return []
    return item_list


def extract_item(xpath):
    """
    提取满足条件的单个内容
    """
    item_list = tree.xpath(xpath)
    if not item_list:
        return None
    return item_list[0]


def get_position_url_list():
    """
    获取职位列表页中所有职位的链接列表
    """
    url_list = extract_list('//table[@id="resultList"]/tr[@class="tr0"]/td[@class="td1"]/a/@href')
    print url_list
    print '单页职位数：%s' % len(url_list)


def get_next_page():
    """
    获取下一页链接
    """
    url = extract_item('//table[@class="searchPageNav"]/tr/td[last()]/a/@href')
    print url
    return url


def get_list():
    pass


def get_detail():
    pass


def fuck():
    # 指定每个条件列表页面
    fetch_page_num_per_condition = 10
    load_tree(get_html(url_root))
    get_position_url_list()
    url_next = get_next_page()
    # 取前10页
    for i in xrange(fetch_page_num_per_condition-2):
        load_tree(get_html(url_next))
        get_position_url_list()
        url_next = get_next_page()


if __name__ == '__main__':
    fuck()


"""
分析页面：
职位搜索页面
http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000&funtype=0000&industrytype=00&issuedate=8&providesalary=99&keywordtype=1&lang=c&stype=2&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&fromType=1
http://search.51job.com/jobsearch/search_result.php?
fromJs=1
jobarea=010000
funtype=0000
industrytype=00
issuedate=8
providesalary=99
keywordtype=1
lang=c
stype=2
workyear=99
cotype=99
degreefrom=99
jobterm=01
companysize=99
fromType=1

第一页：
http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000&funtype=1101&industrytype=00&issuedate=3&lang=c&fromType=18
http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000%2C00&district=000000&funtype=1101&industrytype=00&issuedate=3&providesalary=99&keywordtype=1&curr_page=1&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=-1
第二页：
http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000%2C00&district=000000&funtype=1101&industrytype=00&issuedate=3&providesalary=99&keywordtype=1&curr_page=2&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=-1
第三页：
http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000%2C00&district=000000&funtype=1101&industrytype=00&issuedate=3&providesalary=99&keywordtype=1&curr_page=3&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=-1
"""
