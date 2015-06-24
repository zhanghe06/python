# encoding: utf-8
__author__ = 'zhanghe'

import requests
import re
import json
import random
import time
import os
import pswEncrypt


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

# 登录需要的参数
payload = {
    'u': '',
    'p': '',
    'verifycode': '!QYD',  # !QYD
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

qq_hash = ''

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
    print check_dict
    payload['verifycode'] = check_dict.split(',')[1].strip('\'')
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
    """
    response = s.get(url_login, params=payload, headers=header)
    return response


def check_sign(url):
    """
    检查签名
    """
    response = s.get(url, headers=header)
    return response


def get_session_id():
    """
    获取sessionId
    :return:
    """
    session_id_url = 'http://d.web2.qq.com/channel/login2'
    header['Host'] = 'd.web2.qq.com'
    header['Origin'] = 'http://d.web2.qq.com'
    header['Referer'] = 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2'
    session_id_dict = {
        "ptwebqq": ptwebqq,
        "clientid": ClientID,
        "psessionid": "",
        "status": "online"
    }
    session_id_payload = {'r': json.dumps(session_id_dict)}
    response = s.post(session_id_url, data=session_id_payload, headers=header)
    data = json.loads(response.content)
    return data['result']['psessionid']


def get_self_info():
    """
    获取个人信息
    """
    url_self_info = 'http://s.web2.qq.com/api/get_self_info2?t=1434857217484'
    header['Host'] = 's.web2.qq.com'
    header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
    response = s.get(url_self_info, headers=header)
    return json.dumps(response.content, ensure_ascii=False, indent=4)


def get_vf_web_qq():
    """
    获取验证令牌
    :return:
    """
    vf_web_qq_url = 'http://s.web2.qq.com/api/getvfwebqq'
    vf_web_qq_payload = {
        'ptwebqq': ptwebqq,  # 从cookie中获取
        'clientid': ClientID,
        'psessionid': '',
        't': time.time()
    }
    response = s.get(vf_web_qq_url, params=vf_web_qq_payload, headers=header)
    print response.content
    return json.loads(response.content)['result']['vfwebqq']


def get_hash(x, K):
    """
    获取hash令牌（由js转化过来）
    获取群组信息，好友信息需要用到
    """
    # x += ""
    N = [0, 0, 0, 0]
    for T in range(0, len(K)):
        N[T % 4] ^= ord(K[T])
    U = ["EC", "OK"]
    V = []
    V.append(int(x) >> 24 & 255 ^ ord(U[0][0]))
    V.append(int(x) >> 16 & 255 ^ ord(U[0][1]))
    V.append(int(x) >> 8 & 255 ^ ord(U[1][0]))
    V.append(int(x) & 255 ^ ord(U[1][1]))
    U = []
    for T in range(0, 8):
        U.append(T % 2)
        if U[T] == 0:
            U[T] = N[T >> 1]
        else:
            U[T] = V[T >> 1]
    N = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    V = ""
    for T in range(0, len(U)):
        V += N[U[T] >> 4 & 15]
        V += N[U[T] & 15]
    return V


def get_group_info():
    """
    获取群组信息
    """
    group_info_url = 'http://s.web2.qq.com/api/get_group_name_list_mask2'
    group_info_payload = {'r': json.dumps({"vfwebqq": vfwebqq, "hash": qq_hash})}
    header['Host'] = 's.web2.qq.com'
    header['Origin'] = 'http://s.web2.qq.com'
    header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
    response = s.post(group_info_url, data=group_info_payload, headers=header)
    print json.dumps({"vfwebqq": vfwebqq, "hash": qq_hash})
    return json.loads(response.content)


def get_friends_info():
    friends_info_url = 'http://s.web2.qq.com/api/get_user_friends2'
    friends_info_payload = {'r': json.dumps({"vfwebqq": vfwebqq, "hash": qq_hash})}
    header['Host'] = 's.web2.qq.com'
    header['Origin'] = 'http://s.web2.qq.com'
    header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
    response = s.post(friends_info_url, data=friends_info_payload, headers=header)
    print json.dumps({"vfwebqq": vfwebqq, "hash": qq_hash})
    return json.loads(response.content)


def send_group_msg(group_uin, msg):
    """
    发送群消息
    """
    group_msg_url = 'http://d.web2.qq.com/channel/send_qun_msg2'
    header['Host'] = 'd.web2.qq.com'
    header['Origin'] = 'http://d.web2.qq.com'
    header['Referer'] = 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2'
    group_msg_dict = {
        "group_uin": group_uin,
        "content": "[\"" + msg + "\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
        "face": 0,
        "clientid": ClientID,
        "msg_id": 52880001,  # todo 这个值怎么确定?
        "psessionid": PSessionID
    }
    group_msg_payload = {'r': json.dumps(group_msg_dict)}
    response = s.post(group_msg_url, data=group_msg_payload, headers=header)
    return json.loads(response.content)


if __name__ == "__main__":
    # 设置账号密码
    NAME = 455091702
    PASS = '123456'
    ClientID = 53999199
    AppID = 1003903
    PSessionID = ''

    payload['u'] = NAME
    # 获取隐藏域表单参数
    params_html = get_hide_params_html()
    params = parse_hide_params(params_html)
    payload_hide_params = dict(json.loads(params))
    print payload_hide_params
    payload = dict(payload, **payload_hide_params)
    # 获取验证参数
    get_check()
    # 获取加密的密码
    payload['p'] = pswEncrypt.get_tea_pass(NAME, PASS, payload['verifycode'])
    # 记录登录参数
    print json.dumps(payload, ensure_ascii=False, indent=4)
    # 登录
    r = login()
    result = r.content
    print result
    # 获取cookie
    supertoken = r.cookies['supertoken']
    pt2gguin = r.cookies['pt2gguin']
    # ETK = r.cookies['ETK']
    superuin = r.cookies['superuin']
    superkey = r.cookies['superkey']
    uin = r.cookies['uin']
    ptisp = r.cookies['ptisp']
    # ptnick_455091702 = r.cookies['ptnick_455091702']
    ptwebqq = r.cookies['ptwebqq']
    skey = r.cookies['skey']
    # 验证签名
    url_check_sign = result.split(',')[2].strip('\'')
    print url_check_sign

    cookies = {
        'supertoken': supertoken,
        'pt2gguin': pt2gguin,
        'superuin': superuin,
        'superkey': superkey,
        'uin': uin,
        'ptisp': ptisp,
        'ptwebqq': ptwebqq,
        'skey': skey
    }
    r_check_sign = s.get(url_check_sign, headers=header)

    print get_self_info()

    vfwebqq = get_vf_web_qq()
    print vfwebqq

    qq_hash = get_hash(NAME, ptwebqq)

    group_info = get_group_info()
    print json.dumps(group_info, ensure_ascii=False, indent=4)

    friends_info = get_friends_info()
    print json.dumps(friends_info, ensure_ascii=False, indent=4)

    PSessionID = get_session_id()




"""
对于加密部分，最好的方案是引入外部js到本地作为单独的服务，但这种方案没有成功
如果将算法集成到代码里，加密算法变更后，还要重写，目前是这种方式

登录失败提示：
ptuiCB('3','0','','0','您输入的帐号或密码不正确，请重新输入。', '10000');

登录成功提示：
ptuiCB('0','0','http://ptlogin4.web2.qq.com/check_sig?pttype=1&uin=455091702&service=login&nodirect=0&ptsigx=0cfd5d7d11011c487d8cd854cbb7cebb52ffd113651fde7f62bf959620ca6e24942484a017e32b37fc2bd677965f64b8b55a4edc5ae225eac27f0739f1a1b243&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=&ptlang=2052&ptredirect=100&aid=501004106&daid=164&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=1&pt_aid=0&pt_aaid=0&pt_light=0&pt_3rd_aid=0','0','登录成功！', '空ping子');

模拟登录成功实现
消息发送成功实现
下一步，进一步改进

"""
