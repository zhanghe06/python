# encoding: utf-8
__author__ = 'zhanghe'

# 导入智联企业账号密码，格式：
# zhi_lian = {'LoginName': 'xxxx', 'Password': 'xxxxxx'}
from password import zhi_lian
from PIL import Image
import pytesseract
import requests
import random
import time
import os
import json
import logging

# logging.basicConfig(level=logging.DEBUG, filename='zhilian.log', filemode='w')
logging.basicConfig(level=logging.DEBUG)

s = requests.session()
# 伪装成浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}


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
    login_response = s.post(url, data=form_data, headers=header)
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


if __name__ == '__main__':
    login()

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
"""
