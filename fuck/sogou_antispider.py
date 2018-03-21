#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sogou_antispider.py
@time: 2017/11/28 下午11:55
"""


import time
import json
import math
import random
import requests
from HTMLParser import HTMLParser


html_parser = HTMLParser()


headers = {
    'Host': 'www.sogou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}


s = requests.session()


antispider_url = 'http://www.sogou.com/antispider/'


def _get_tc():
    tc = str('%13d' % (time.time() * 1000))
    return tc


def _get_antispider_page():
    r_g = s.get(antispider_url, headers=headers)
    cookies = r_g.cookies
    PHPSESSID = cookies.get('PHPSESSID')
    ABTEST = cookies.get('ABTEST')
    IPLOC = cookies.get('IPLOC')
    SUID = cookies.get('SUID')
    SUIR = cookies.get('SUIR')

    print 'ABTEST', ABTEST
    print 'SUID', SUID
    return ABTEST, SUID


def _get_a():
    a_url = 'http://pb.sogou.com/pv.gif'
    a_data = {
        'uigs_productid': 'webapp',
        'type': 'antispider',
        'subtype': 'verify_page',
        'domain': 'sogou',
        'suv': '',
        'snuid': '',
        't': _get_tc(),
        'pv': '',
    }
    res = s.get(a_url, params=a_data)
    SUV = res.cookies.get('SUV')
    print 'SUV', SUV
    return SUV


def _get_b():
    pass


def _h(a, b):
    return math.floor(random.random() * (b - a) + a)


def _get_sn(abtest, suid):
    e = int(abtest[0])
    SN = suid[e, _h(e, len(suid)) + 1]
    print 'SN', SN
    return SN


def _get_sn_uid(abtest, suid):
    url = 'http://www.sogou.com/antispider/detect.php'
    tc = _get_tc()
    data = {
        'sn': _get_sn(abtest, suid),
        '_': tc
    }
    random_dict = {}

    int(random.random(), base=36)


def _get_code_img():
    img_headers = dict(headers, **{
        'Referer': 'http://www.sogou.com/antispider/',
        'Pragma': 'no-cache'
    })

    img_tc = _get_tc()
    img_url = 'http://www.sogou.com/antispider/util/seccode.php?tc=%s' % img_tc
    print img_tc
    print img_url

    # 保存验证码图片
    img_name = 'sogou_%s.jpg' % img_tc
    img_r_g = s.get(img_url, headers=img_headers)
    print img_r_g.cookies.__dict__
    img_content = img_r_g.content
    with open(img_name, 'w') as f:
        f.write(img_content)
    time.sleep(3)


def _post_code_form(verify_code):

    form_headers = dict(headers, **{
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://www.sogou.com',
        'Referer': 'http://www.sogou.com/antispider/',
        'Pragma': 'no-cache'
    })
    print form_headers
    url = 'http://www.sogou.com/antispider/thank.php'
    data = {
        'c': verify_code,
        'r': '',
        'v': 5
    }
    r_p = s.post(url, data=data, headers=form_headers)
    r_p_json = json.loads(r_p.content)
    # {"code": 3,"msg": "验证码输入错误, 请重新输入！"}
    # {"code": 2,"msg": "未知访问来源"}
    print r_p_json
    if r_p_json.get('code') == 0:
        print u'识别成功'
    else:
        print r_p_json.get('msg')
    return True if r_p_json.get('code') == 0 else False


def fuck(c=3):
    ABTEST, SUID = _get_antispider_page()
    SUV = _get_a()

    SNUID = _get_sn_uid(ABTEST, SUID)

    while c >= 0:
        _get_code_img()

        verify_code = raw_input('verify_code')
        res = _post_code_form(verify_code)
        if res:
            break
        c -= 1


if __name__ == '__main__':
    fuck()


"""
注意 js substr substring 区别
"""
