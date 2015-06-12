# encoding: utf-8
__author__ = 'zhanghe'

import requests
import re
import json


# 入口
url_root = 'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'

# 登录页的url
url_login = 'https://ssl.ptlogin2.qq.com/login'

# 配置User-Agent
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

# 登录需要的参数
payload = {
    'u': '123456',
    'p': '2rDrq7sBKdqkqzHgyntOBpaM6p8RAAcBpEio3*UCWuMNiG0LUw6WRsKTDsps2GJ6vAf1CPd-HoNl-QFekDH9Lfn54h1KOvOZeQlARGNPON0JECRoSUF1*8kOezqzRqBFMVVPM5cMJ3PFjn00*5KbpSHkHAJHF9AV3kV-JKE0iChfjaXcOBkRKv75mM2j8RQByBz0KFPssmrgKqPIGGatXw__',
    'verifycode': '!NQA',
    # 隐藏域表单参数-------------start
    'webqq_type': 10,  # 10: "在线",20: "离线",30: "离开",40: "隐身",50: "忙碌",60: "Q我吧",70: "请勿打扰",
    'remember_uin': 1,
    'login2qq': 1,
    'aid': 501004106,
    'u1': 'http://w.qq.com/proxy.html?login2qq=1&webqq_type=10',
    'h': 1,
    'ptredirect': 0,
    'ptlang': 2052,
    'daid': 164,
    'from_ui': 1,
    'pttype': 1,
    'dumy': '',
    'fp': 'loginerroralert',
    # 隐藏域表单参数-------------end
    'action': '0-12-229270',
    'mibao_css': 'm_webqq',
    't': 1,
    'g': 1,
    'js_type': 0,
    'js_ver': 10125,
    'login_sig': '',
    'pt_randsalt': 0,
    'pt_vcode_v1': 0,
    'pt_verifysession_v1': 'e8dd4fef1f230072429cae05732530ef5d7df5fa61660a7311235e2315409046d556365705db19ae32cd082739370abd93a5f90e5a174a5a',
}

# 保持会话
s = requests.session()


def get_hide_params_html():
    response = s.get(url_root, headers=header)
    return response.content


def parse_hide_params(html):
    reg_params = '<input type="hidden" name="(.+?)" value="(.*?)".*?>'
    params_list = re.compile(reg_params, re.S).findall(html)
    return json.dumps(params_list, ensure_ascii=False, indent=4)


def login():
    """
    登录
    :return:
    """
    response = s.get(url_login, params=payload, headers=header)
    return response.content


if __name__ == "__main__":
    params_html = get_hide_params_html()
    params = parse_hide_params(params_html)
    #result = login()
    print dict(json.loads(params))