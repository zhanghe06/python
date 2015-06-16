# encoding: utf-8
__author__ = 'zhanghe'

import requests
import re
import json
import random
import time
import os


# 入口
url_root = 'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'

# 验证参数
url_check = 'https://ssl.ptlogin2.qq.com/check'

# 图形验证码
url_img_verify = 'https://ssl.captcha.qq.com/getimage'

# 登录页的url
url_login = 'https://ssl.ptlogin2.qq.com/login'

# 配置User-Agent
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

# 加密salt
salt = ''

# 登录需要的参数
payload = {
    'u': '234567',
    'p': '2rDrq7sBKdqkqzHgyntOBpaM6p8RAAcBpEio3*UCWuMNiG0LUw6WRsKTDsps2GJ6vAf1CPd-HoNl-QFekDH9Lfn54h1KOvOZeQlARGNPON0JECRoSUF1*8kOezqzRqBFMVVPM5cMJ3PFjn00*5KbpSHkHAJHF9AV3kV-JKE0iChfjaXcOBkRKv75mM2j8RQByBz0KFPssmrgKqPIGGatXw__',
    # 'verifycode': '!NQA',
    'verifycode': '!QYD',
    # 隐藏域表单参数-------------start
    'webqq_type': '10',  # 10: "在线",20: "离线",30: "离开",40: "隐身",50: "忙碌",60: "Q我吧",70: "请勿打扰",
    'remember_uin': '1',
    'login2qq': '1',
    'aid': '501004106',
    'u1': 'http://w.qq.com/proxy.html?login2qq=1&webqq_type=10',
    'h': '1',
    'ptredirect': '0',
    'ptlang': '2052',
    'daid': '164',
    'from_ui': '1',
    'pttype': '1',
    'dumy': '',
    'fp': 'loginerroralert',
    # 隐藏域表单参数-------------end
    'action': '0-21-27455',
    # 前两个参数初始值[0, 0]分别对应鼠标点击，键盘按下的次数，最后一个是点击登录按钮与页面初次加载的时间差
    # 贱人，这明显是记录用户行为的～～腾讯的人品可见一斑
    'mibao_css': 'm_webqq',
    't': '1',
    'g': '1',
    'js_type': '0',
    'js_ver': '10125',
    'login_sig': '',
    'pt_randsalt': '0',
    'pt_vcode_v1': '0',
    'pt_verifysession_v1': 'e8dd4fef1f230072429cae05732530ef5d7df5fa61660a7311235e2315409046d556365705db19ae32cd082739370abd93a5f90e5a174a5a',
}

# 保持会话
s = requests.session()


def get_hide_params_html():
    """
    获取隐藏域表单内容
    :return:
    """
    response = s.get(url_root, headers=header)
    return response.content


def parse_hide_params(html):
    """
    解析隐藏域参数
    :param html:
    :return:
    """
    reg_params = '<input type="hidden" name="(.+?)" value="(.*?)".*?>'
    params_list = re.compile(reg_params, re.S).findall(html)
    return json.dumps(params_list, ensure_ascii=False, indent=4)


def get_check():
    """
    获取验证信息
    :return:
    """
    check_payload = {
        'pt_tea': '1',  # 固定值：1
        'uin': payload['u'],
        'appid': payload['aid'],
        'js_ver': 10125,  # 固定值
        'js_type': 0,  # 固定值
        'login_sig': '',  # 固定值
        'u1': 'http://w.qq.com/proxy.html',  # 固定值
        'r': random.random()
    }
    # 具体参数参考607行[https://ui.ptlogin2.qq.com/js/10125/mq_comm.js]
    response = s.get(url_check, params=check_payload, headers=header)
    check_dict = response.content
    payload['verifycode'] = check_dict.split(',')[1].strip('\'')
    salt = check_dict.split(',')[2].strip('\'')
    payload['pt_verifysession_v1'] = check_dict.split(',')[3].strip('\'')


def get_img_verify():
    """
    获取图形验证码
    :return:
    """
    img_payload = {
        'aid': payload['aid'],
        'r': random.random(),
        'uin': payload['u'],
        'cap_cd': payload['pt_verifysession_v1']
    }
    img_name = os.path.split(os.path.realpath(__file__))[0] + '/static/QQImgVerify/' + str(time.time()) + '.jpg'
    img_ret = s.get(url_check, params=img_payload, headers=header)
    with open(img_name, 'wb') as f:
        f.write(img_ret.content)
    print img_name
    return img_name


def login():
    """
    登录
    :return:
    """
    response = s.get(url_login, params=payload, headers=header)
    return response.content


if __name__ == "__main__":
    # 获取隐藏域表单参数
    params_html = get_hide_params_html()
    params = parse_hide_params(params_html)
    payload_hide_params = dict(json.loads(params))
    print payload_hide_params
    payload = dict(payload, **payload_hide_params)
    # 获取验证参数
    get_check()

    print json.dumps(payload, ensure_ascii=False, indent=4)
    # 登录
    result = login()
    print result


"""
对于加密部分，最好的方案是引入外部js到本地作为单独的服务
如果将算法集成到代码里，加密算法变更后，还要重写
"""
