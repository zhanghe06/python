# encoding: utf-8
__author__ = 'zhanghe'

import requests
import json
import logging
from pyquery import PyQuery as Pq
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
    with open('static/html/test.html', 'wb') as f:
        f.write(resume_list_page.text.encode('utf-8'))
    # 提取简历列表信息
    rows = Pq(resume_list_page.text).find('div.emailL_tab')
    i = 0
    resume_list = []
    for row in Pq(rows):
        j = 0
        item_list = []
        item_dict = {}
        for item in Pq(row).find('.email5'):
            item_text = Pq(item).text()
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
        url = Pq(row).find('.email5 .iconHover_2').attr('href')
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

# 进入简历管理页面，获取各个模块的url
if best_resume is not None:
    module_url_dict = {}
    module_list_page = s.get(best_resume['resume'])
    module_url_rows = Pq(module_list_page.text).find('.left .leftRow .leftRowCon ul.leftRowB')
    for module_url_row in Pq(module_url_rows).find('li.ok'):
        print Pq(module_url_row).html()
        title = Pq(module_url_row).text()
        url = zhilian.url_join(Pq(module_url_row).find('a').attr('href'), 'http://my.zhaopin.com')
        module_url_dict[title] = url
    print json.dumps(module_url_dict, indent=4).decode('raw_unicode_escape')

# 获取各个模块的数据
if u'个人信息' in module_url_dict:
    profile = s.get(module_url_dict[u'个人信息'])
    print profile.text
    profile_items_list = [
        'username',
        'gender',
        'birth_date_y',
        'birth_date_m',
        'experience',
        'experience_month',
        'hukou',
        'hukou_p',
        'residence',
        'residence_p',
        'residence_district',
        'contact_num',
        'email1',
    ]
    profile_items_dict = {}
    for item in profile_items_list:
        profile_items_dict[item] = Pq(profile.text).find('input[name="' + item + '"]').attr('value')
    # 婚姻状况js实现
    print json.dumps(profile_items_dict, indent=4).decode('raw_unicode_escape')
    pass

# 头像的存储
if best_resume is not None:
    module_url_dict = {}
    module_list_page = s.get(best_resume['resume'])
    avatar_url = Pq(module_list_page.text).find('.rightRow1 p.f_right a').attr('href')
    avatar = s.get(avatar_url)
    with open('static/avatar/test.jpg', 'wb') as f:
        for item in avatar:
            f.write(item)
# 映射关系转换

# 保存json至服务器
import os
filepath = 'static/json/'
if not os.path.isdir(filepath):
    os.mkdir(filepath)
filename = 'static/json/test.json'
result_json = json.dumps(profile_items_dict, indent=4, ensure_ascii=False)
with open(filename, 'wb') as f:
    f.write(result_json.encode('utf-8'))