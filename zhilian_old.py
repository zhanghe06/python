# encoding: utf-8
__author__ = 'zhanghe'

import requests

# 登录页的url
url = 'http://i.zhaopin.com/Login/LoginManager/Login'
# 有些网站反爬虫，这里用headers把程序伪装成浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}
# 登录需要提交的表单
form_data = {
    'loginname': '2627498748@qq.com',  # 填入网站的上网帐号
    'password': '825716',  # 填入网站密码
    'int_count': 999,
    'errTimes': 0,
    'bkurl': ''
}
s = requests.session()
response = s.post(url, data=form_data, headers=header)
print response.text