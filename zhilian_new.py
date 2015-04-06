# encoding: utf-8
__author__ = 'zhanghe'

import requests
import json
import logging
from pyquery import PyQuery as pq
from tools import zhilian

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
        item_dict = {}
        for item in pq(row).find('.email5'):
            item_text = pq(item).text()
            print "[%s-%s]" % (i, j) + item_text
            # 0,1,2,6是有效的信息
            if j in (0, 1, 2, 6):
                item_list.append(item_text)
            # Python哲学的一句话：只用一种方式解决问题，所以自增操作完全可以用i+=1完成，就不需要i++了。
            j += 1
        # 提取简历完整度
        if len(item_list) == 4:
            item_list[2] = item_list[2].split()[-1].rstrip('%')
        # 简历url添加进item_list
        url = pq(row).find('.email5 .iconHover_2').attr('href')
        item_list.append('http://my.zhaopin.com/myzhaopin/' + url)
        print json.dumps(item_list).decode('raw_unicode_escape')
        i += 1
        # 将列表转为可读性强的字典
        item_dict['update_date'] = item_list[0]
        item_dict['language'] = item_list[1]
        item_dict['integrity'] = item_list[2]
        item_dict['openness'] = item_list[3]
        item_dict['url'] = item_list[4]
        resume_list.append(item_dict)
    print json.dumps(resume_list, indent=4).decode('raw_unicode_escape')

    if resume_list is None:
        print('简历不存在')
        exit()
    # 去除英文简历
    for item in resume_list:
        if item['language'] == u'英文':
            resume_list.remove(item)
    print json.dumps(resume_list, indent=4).decode('raw_unicode_escape')
    # 根据PRD描述的规则获取最优简历
    best_resume = zhilian.select_best_resume(resume_list)
    print best_resume