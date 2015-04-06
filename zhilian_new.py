# encoding: utf-8
__author__ = 'zhanghe'

import requests
import json
import logging
from pyquery import PyQuery as pq

logging.basicConfig(level=logging.DEBUG, filename='zhilian.log', filemode='w')

# 登录页的url
url = 'https://passport.zhaopin.com/'
# 有些网站反爬虫，这里用headers把程序伪装成浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}
# 登录需要提交的表单
form_data = {
    'bkurl': '',
    'LoginName': '2627498748@qq.com',  # 填入网站的上网帐号
    'Password': '825716',  # 填入网站密码
    'RememberMe': 'false'
}
s = requests.session()
login_response = s.post(url, data=form_data, headers=header)
print login_response.text

# 新版特点https协议登录，成功后跳转
# window.location.href = "http://i.zhaopin.com";

if 'window.location.href = "http://i.zhaopin.com"' in login_response.text:
    i_zhaopin = s.get('http://i.zhaopin.com/')
    # 登录成功着陆页面
    print i_zhaopin.text
    pass

if 'window.location.href = "http://i.zhaopin.com"' in login_response.text:
    resume_list_page = s.get('http://my.zhaopin.com/myzhaopin/resume_list.asp')
    # 简历管理页面（简历列表）
    print type(resume_list_page)
    print type(resume_list_page.text)
    # print resume_list.text
    with open('00.html', 'wb') as f:
        f.write(resume_list_page.text.encode('utf-8'))
    # 提取简历列表信息
    rows = pq(resume_list_page.text).find('div.emailL_tab')
    i = 0
    resume_list = []
    for row in pq(rows):
        j = 0
        item_list = []
        for item in pq(row).find('.email5'):
            item_text = pq(item).text()
            print "[%s-%s]" % (i, j) + item_text
            # 0,1,2,6是有效的信息
            if j in (0, 1, 2, 6):
                item_list.append(item_text)
            # Python哲学的一句话：只用一种方式解决问题，所以自增操作完全可以用i+=1完成，就不需要i++了。
            j += 1
        if len(item_list) == 4:
            item_list[2] = item_list[2].split()[-1]
        # 简历url添加进item_list
        url = pq(row).find('.email5 .iconHover_2').attr('href')
        item_list.append('http://my.zhaopin.com/myzhaopin/' + url)
        print json.dumps(item_list).decode('raw_unicode_escape')
        i += 1
        resume_list.append(item_list)
    print json.dumps(resume_list, indent=4).decode('raw_unicode_escape')

# def select_best_resume(self):
#     '选择一个最佳的简历'
#     s = self.session
#
#     resume_list_url = 'http://my.zhaopin.com/myzhaopin/resume_list.asp'
#
#     res_resume_list = s.get(resume_list_url)
#     # print res_resume_list.text
#
#     d = Q(res_resume_list.text).find('div[class="emailL_tab emailL_tab_bgcolor"]')
#
#     # 简历列表
#     resume_list = []
#     for row in d:
#         resume_row = {
#             'resumes_url': '',  # 简历url
#             'wzd': '',  # 完整度
#             'update_date': '',  # 更新时间
#             'open_level': '',  # 公开程度
#             'language': '',  # 语言
#             'n': 0  # 深度
#         }
#         for i1 in Q(row).find('a[class="resumesIcon iconHover_2"]'):
#             # print Q(i1).attr('href')
#             resume_row['resumes_url'] = 'http://my.zhaopin.com/myzhaopin/' + Q(i1).attr('href')
#         for i2 in Q(row).find('.wzd_right'):
#             # print Q(i2).text()
#             resume_row['wzd'] = Q(i2).text().rstrip('%')
#         for i3 in Q(row).find('div[class="email5 tab9"]'):
#             # print Q(i3).text()
#             resume_row['update_date'] = Q(i3).text()
#         for i4 in Q(row).find('a[class="openSetno"]'):
#             # print Q(i4).text()
#             resume_row['open_level'] = Q(i4).text()
#         for i5 in Q(row).find('.select_title'):
#             # print Q(i5).text()
#             resume_row['language'] = Q(i5).text()
#
#         resume_list.append(resume_row)
#     # print(resume_list)
#     # exit()
#     url_list = {}
#     if resume_list == []:
#         # 如果简历为空
#         # return 'no_resume'
#         url_list['resume'] = None
#         return url_list
#
#     for item_en in resume_list:
#         if item_en['language'] == u'英文':
#             resume_list.remove(item_en)
#     #print(resume_list)
#
#     # 获取最优简历url
#     # 如果只有一个简历，直接返回
#     if len(resume_list) == 1:
#         url_list['resume'] = resume_list[0]['resumes_url']
#     else:
#         # 如果有多个简历，先取出各字段的最优值
#         wzd_range = []
#         for item in resume_list:
#             wzd_range.append(item['wzd'])
#             max_wzd = max(wzd_range)
#
#         update_date_range = []
#         for item in resume_list:
#             update_date_range.append(item['update_date'])
#         max_update_date = max(update_date_range)
#
#         open_level_range = []
#         for item in resume_list:
#             open_level_range.append(item['open_level'])
#         if u'开放' in open_level_range:
#             max_open_level = u'开放'
#         elif u'委托给智联' in open_level_range:
#             max_open_level = u'委托给智联'
#         else:
#             max_open_level = u'保密'
#
#         n_range = []  # 深度范围
#         for item_n in resume_list:
#             # 将每条简历与最优值比较，如果存在，则深度自增
#             if item_n['wzd'] == max_wzd:
#                 item_n['n'] += 100
#             if item_n['update_date'] == max_update_date:
#                 item_n['n'] += 10
#             if item_n['open_level'] == max_open_level:
#                 item_n['n'] += 1
#             #print item_n['n']
#
#             n_range.append(item_n['n'])
#         # 最大深度
#         max_n = max(n_range)
#
#         for item_max in resume_list:
#             # 查询简历列表中有最大深度的一条记录
#             if item_max['n'] == max_n:
#                 #print item_max
#                 url_list['resume'] = item_max['resumes_url']
#                 #print url_list['resume']
#
#     return url_list