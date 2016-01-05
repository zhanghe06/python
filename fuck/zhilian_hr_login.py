# encoding: utf-8
__author__ = 'zhanghe'

# 导入智联企业账号密码，格式：
# zhi_lian = {'LoginName': 'xxxx', 'Password': 'xxxxxx'}
from password import zhi_lian
from PIL import Image
import pytesseract
import requests
from bs4 import BeautifulSoup
from urllib import quote
import random
import time
import os
import json
import logging

# logging.basicConfig(level=logging.DEBUG, filename='zhilian.log', filemode='w')
logging.basicConfig(level=logging.DEBUG)

s = requests.session()
s.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}
s.proxies = {
    'http': 'http://192.168.2.158:3128'
}


def get_code_img():
    """
    获取验证码并保存为本地图片
    :return:返回全路经的图片文件名
    """
    img_name = './' + str(time.time()) + '.jpg'
    img_url = 'https://passport.zhaopin.com/checkcode/imgrd?r=%s' % random.random()
    img_ret = s.get(img_url)
    with open(img_name, 'wb') as f:
        f.write(img_ret.content)
    logging.info('验证码图片路径：%s' % img_name)
    return img_name


def code_img_to_string(img_name):
    """
    图片转为字符串
    :param img_name:
    :return:
    """
    img = Image.open(img_name)
    text = pytesseract.image_to_string(img)
    logging.info('验证码识别结果：%s' % text)
    return text


def try_login():
    """
    尝试登录
    """
    # 获取验证码（4位）
    code_text = ''
    while 1:
        if len(str(code_text)) == 4:
            break
        else:
            code_text = code_img_to_string(get_code_img())
    # 登录页的url
    url = 'https://passport.zhaopin.com/org/login'
    # 登录需要提交的表单
    form_data = {
        'LoginName': zhi_lian['LoginName'],
        'Password': zhi_lian['Password'],
        'CheckCode': code_text,
        'Submit': ''
    }
    login_response = s.post(url, data=form_data)
    status = check_login_status(login_response.text)  # login_response.text unicode
    logging.info('登录状态：%s' % status)
    if status in ['name_or_pass_error', 'login_error']:
        logging.info('登录失败的用户名：%s，密码：%s') % (zhi_lian['LoginName'], zhi_lian['Password'])
    return status


def check_login_status(login_response_text):
    """
    登录状态检查
    """
    if u'<div style="zoom:normal;" class="msg_error">验证码错误！</div>' in login_response_text:
        return 'code_error'
    if u'<div style="zoom:normal;" class="msg_error">用户名或密码错误！</div>' in login_response_text:
        return 'name_or_pass_error'
    if u'window.location.href = "http://rd2.zhaopin.com/s/loginmgr/loginproc_new.asp";' in login_response_text:
        return 'login_ok'
    return 'login_error'  # 未知错误


def login():
    """
    登录，对于验证码错误做5次尝试
    """
    for i in range(5):
        login_status = try_login()
        if login_status == 'code_error':
            continue
        else:
            break


def get_position_list():
    """
    获取并解析发布中的职位列表
    """
    # 登录成功后处理跳转
    url = 'http://rd2.zhaopin.com/s/loginmgr/loginproc_new.asp'
    res = s.get(url)
    if res.status_code != 200:
        print '登录失败'
        return None
    url = 'http://jobads.zhaopin.com/Position/PositionManage'
    res = s.get(url)
    # with open('01.html', 'w') as f:
    #     f.write(res.text.encode('utf-8'))
    print res.url, type(res.text), type(res.text.encode('utf-8'))
    return read_position_list(res.text)  # 解析发布中的职位列表


def read_position_list(html=None):
    """
    解析发布中的职位列表
    """
    with open('01.html', 'r') as f:
        html = f.read()
    # print html
    soup = BeautifulSoup(html, 'lxml')
    positions = []
    trs = soup.select('table.publishingTable tr')
    if trs:
        trs.pop(0)
        trs.pop()
    for tr in trs:
        position = {
            'job_id': tr.select('td span.checkbox')[0].get('data-value'),
            'edit_id': tr.select('input[id^="position_"]')[0].get('data-editid'),  # 用于动态查询简历投递数量
            'title': tr.select('td.jobTitle')[0].get_text(),
            'date_pub': tr.select('td.tb-start-date')[0].get_text(),
            'date_end': tr.select('td.font12')[0].get_text(),
            'city': tr.select('td span.cityleft')[0].get_text(),
            'resume_count': tr.select('td.td-resume')[0].get_text(),
        }
        positions.append(position)
    print json.dumps(positions, indent=4).decode('raw_unicode_escape')
    return positions


def get_resume_count(edit_ids):
    """
    获取简历投递数量
    http://jobads.zhaopin.com/Resume/GetResumCount?editIds=153009962;170777962&ntype=0
    {
      "Code": 200,
      "Message": "成功取到数据",
      "Data": [
        {
          "EditId": 153009962,
          "ResumeCount": 67
        },
        {
          "EditId": 170777962,
          "ResumeCount": 7
        }
      ]
    }
    获取邀请简历数 ntype=1
    """
    if not edit_ids:
        return []
    edit_ids = [str(i) for i in edit_ids]
    edit_id_str = ';'.join(edit_ids)
    url = 'http://jobads.zhaopin.com/Resume/GetResumCount?editIds=%s&ntype=0' % edit_id_str
    res = s.get(url)
    # print res.text, res.headers['content-type'], type(res.text)
    result = res.json()
    data = result.get('Data', [])
    # print data
    return data


def get_resume_list(position_list):
    """
    获取简历列表
    viewResumes('CC198378613J90250035000',131455223,0,1)
    """
    for position in position_list:
        url = 'http://rd2.zhaopin.com/rdapply/resumes/apply/position?SF_1_1_46=0&SF_1_1_44=%s&JobTitle=%s&JobStatus=3&IsInvited=0' % (position['edit_id'].encode('utf-8'), quote(position['title'].encode('utf-8')))
        res = s.get(url)
        # print res.text
        with open('resume_list.html', 'w') as f:
            f.write(res.text.encode('utf-8'))
        break


def read_resume_list(html=None):
    """
    解析主动投递简历待处理列表
    """
    with open('resume_list.html', 'r') as f:
        html = f.read()
    # print html
    soup = BeautifulSoup(html, 'lxml')
    resumes = []
    trs = soup.select('table.listTab tr[class^="list"]')
    for tr in trs:
        resume = {
            'link': tr.select('td a.link')[0].get('href'),
            'name': tr.select('td a.link')[0].get_text(),
            # 'edit_id': tr.select('input[id^="position_"]')[0].get('data-editid'),  # 用于动态查询简历投递数量
            # 'title': tr.select('td.jobTitle')[0].get_text(),
            # 'date_pub': tr.select('td.tb-start-date')[0].get_text(),
            # 'date_end': tr.select('td.font12')[0].get_text(),
            # 'city': tr.select('td span.cityleft')[0].get_text(),
            # 'resume_count': tr.select('td.td-resume')[0].get_text(),
        }
        resumes.append(resume)
    print json.dumps(resumes, indent=4).decode('raw_unicode_escape')
    return resumes


def pub_position():
    """
    发布职位
    """
    pass


def get_resume(resume_link):
    """
    获取简历页面
    """
    res = s.get(resume_link)
    with open('resume.html', 'w') as f:
        f.write(res.text.encode('utf-8'))


def read_resume(html=None):
    """
    解析简历详情页面
    """
    user_info = {}
    with open('resume.html', 'r') as f:
        html = f.read()
    # print html
    soup = BeautifulSoup(html, 'lxml')
    user_info['user_name'] = soup.select('div#resumeContentBody div#userName')[0].get_text().strip()

    # 简介
    user_info['user_img'] = soup.select('div.summary img.headerImg')[0].get('src')
    # 默认头像 http://rd.zhaopin.com/img/lookResumes.jpg
    summary_top = soup.select('div.summary-top')[0].get_text().strip()
    summary_top_str = replace_all(summary_top, {'\n': '', '\r': ''})
    user_info['summary_top_01'] = summary_top_str.split('        ')[0].split('    ')
    user_info['summary_top_02'] = summary_top_str.split('        ')[1].split(' | ')
    print json.dumps(user_info, indent=4, ensure_ascii=False)
    # 解析求职意向
    read_intent(soup)
    # 解析自我评价
    read_self_evaluate(soup)
    # 解析工作经历
    read_work(soup)
    # 项目经历
    read_project(soup)
    # 教育经历
    read_edu(soup)
    # 培训经历
    read_train(soup)
    # 证书
    read_cert(soup)
    # 语言能力
    read_language(soup)
    # 专业技能
    read_skill(soup)


def read_intent(soup):
    """
    求职意向
    """
    title = soup.find('h3', text=u'求职意向')
    trs = title.find_next_siblings('div')[0].select('tr')
    intent = []
    for tr in trs:
        tds = tr.select('td')
        row = {tds[0].get_text().strip('：'): tds[1].get_text()}
        intent.append(row)
    print json.dumps(intent, indent=4, ensure_ascii=False)


def read_self_evaluate(soup):
    """
    自我评价
    """
    title = soup.find('h3', text=u'自我评价')
    self_evaluate = title.find_next_siblings('div')[0].get_text().strip()
    print json.dumps(self_evaluate, indent=4, ensure_ascii=False)


def read_work(soup):
    """
    工作经历
    """
    title = soup.find('h3', text=u'工作经历')
    project = []
    count = len(title.find_next_siblings('h2'))
    if count == 0:
        return []
    for i in xrange(count):
        row = {}
        h2 = title.find_next_siblings('h2')[i].get_text()
        h5 = title.find_next_siblings('h5')[i].get_text()
        row['c_name'] = h2
        row['title'] = h5
        row['industry'] = title.find_next_siblings('div')[2*i].get_text().strip()
        trs = title.find_next_siblings('div')[2*i+1].select('tr')
        for tr in trs:
            tds = tr.select('td')
            row[tds[0].get_text().strip('：')] = tds[1].get_text()
        project.append(row)
    print json.dumps(project, indent=4, ensure_ascii=False)


def read_project(soup):
    """
    项目经历
    """
    title = soup.find('h3', text=u'项目经历')
    project = []
    count = len(title.find_next_siblings('h2'))
    if count == 0:
        return []
    for i in xrange(count):
        row = {}
        h2 = title.find_next_siblings('h2')[i].get_text()
        row['title'] = h2
        trs = title.find_next_siblings('div')[i].select('tr')
        for tr in trs:
            tds = tr.select('td')
            row[tds[0].get_text().strip('：')] = tds[1].get_text()
        project.append(row)
    print json.dumps(project, indent=4, ensure_ascii=False)


def read_edu(soup):
    """
    教育经历
    """
    title = soup.find('h3', text=u'教育经历')
    edu_str = title.find_next_siblings('div')[0].get_text().strip()
    edu = edu_str.split('\r\n')
    print json.dumps(edu, indent=4, ensure_ascii=False)


def read_train(soup):
    """
    培训经历
    """
    title = soup.find('h3', text=u'培训经历')
    project = []
    count = len(title.find_next_siblings('h2'))
    if count == 0:
        return []
    for i in xrange(count):
        row = {}
        h2 = title.find_next_siblings('h2')[i].get_text()
        row['title'] = h2
        trs = title.find_next_siblings('div')[i].select('tr')
        for tr in trs:
            tds = tr.select('td')
            row[tds[0].get_text().strip('：')] = tds[1].get_text()
        project.append(row)
    print json.dumps(project, indent=4, ensure_ascii=False)


def read_cert(soup):
    """
    证书
    """
    title = soup.find('h3', text=u'证书')
    h2s = title.find_next_siblings('h2')
    cert = []
    for h2 in h2s:
        cert.append(h2.get_text().strip(''))
    print json.dumps(cert, indent=4, ensure_ascii=False)


def read_language(soup):
    """
    语言能力
    """
    title = soup.find('h3', text=u'语言能力')
    skill_str = title.find_next_siblings('div')[0].get_text().strip()
    skill = skill_str.split('\r\n')
    print json.dumps(skill, indent=4, ensure_ascii=False)


def read_skill(soup):
    """
    专业技能
    """
    title = soup.find('h3', text=u'专业技能')
    skill_str = title.find_next_siblings('div')[0].get_text().strip()
    skill = skill_str.split('\r\n')
    print json.dumps(skill, indent=4, ensure_ascii=False)


def replace_all(input_html, replace_dict):
    """
    用字典实现批量替换
    """
    for k, v in replace_dict.iteritems():
        input_html = input_html.replace(k, v)
    return input_html


if __name__ == '__main__':
    # login()
    # position_list = get_position_list()
    # read_position_list()
    # # get_resume_count([153009962, 170777962])
    # get_resume_list(position_list)
    # resume_list = read_resume_list()
    # get_resume(resume_list[2]['link'])
    read_resume()

"""
模拟登录分析：

Request URL:https://passport.zhaopin.com/org/login
Request Method:POST

LoginName:asdfghjk
Password:12345678
CheckCode:4444
Submit:

Host:passport.zhaopin.com
Origin:http://rd2.zhaopin.com
Referer:http://rd2.zhaopin.com/portal/myrd/regnew.asp?za=2
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36

验证码错误的特征：
<title>企业用户自助注册 - 智联招聘</title>
<div style="zoom:normal;" class="msg_error">验证码错误！</div>

登录失败的特征：
<title>企业用户自助注册 - 智联招聘</title>
<div style="zoom:normal;" class="msg_error">用户名或密码错误！</div>

登录成功后的特征：
<title>正在跳转</title>
window.location.href = "http://rd2.zhaopin.com/s/loginmgr/loginproc_new.asp";


ajax
http://img01.zhaopin.cn/2014/rd2/js/positionmanage.js
"""
