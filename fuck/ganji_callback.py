#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ganji_callback.py
@time: 2017/8/18 下午4:18
"""


import time
import lxml.html
import requests
from urlparse import urljoin

from requests.exceptions import Timeout


header = {
    'Host': 'callback.ganji.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}


s = requests.session()


callback_url = 'http://callback.ganji.com/firewall/valid/1709685058.do?namespace=ganji_hy_list_pc&url=http%3A%2F%2Fanshan.ganji.com%2Fbanjia%2F'


def fuck():
    r_g = s.get(callback_url)
    html = r_g.text
    doc = lxml.html.fromstring(html)

    # 获取页面隐藏域表单
    uuid = doc.xpath('//input[@id="uuid"]/@value')[0].strip()
    url = doc.xpath('//input[@id="url"]/@value')[0].strip()
    namespace = doc.xpath('//input[@id="namespace"]/@value')[0].strip()
    ip = doc.xpath('//input[@id="ip"]/@value')[0].strip()

    # 获取验证码图片
    img_url_text = doc.xpath('//img[@id="verify_img"]/@src')[0].strip()
    img_url = urljoin(callback_url, img_url_text)
    print img_url

    # 保存验证码图片
    img_name = 'ganji_%s.jpg' % uuid
    img_content = s.get(img_url).content
    with open(img_name, 'w') as f:
        f.write(img_content)
    time.sleep(5)

    verify_code = raw_input('verify_code')

    print uuid
    print url
    print namespace
    print ip
    print r_g.cookies.__dict__
    data = {
        'namespace': namespace,
        'uuid': uuid,
        'url': url,
        'verify_code': verify_code
    }
    r_p = s.post(callback_url, data=data)
    r_p_json = r_p.json()  # {"msg":"验证码过期.","code":-1}
    print r_p_json
    if r_p_json.get('code') == 0:
        print u'识别成功'
    else:
        print r_p_json.get('msg')


if __name__ == '__main__':
    fuck()


"""
# 获取页面隐藏域表单
<input type="hidden" id="uuid" value="25f77df09ff249a0942c78e46c79dc89" />
<input type="hidden" id="url" value="http://anshan.ganji.com/banjia/" />
<input type="hidden" id="namespace" value="ganji_hy_list_pc" />
<input type="hidden" id="ip" value="1709685058" />

# 查看出口IP
➜  ~ curl ifconfig.me
101.231.185.66

# 验证IP
In [1]: 101*256*256*256 + 231*256*256 + 185*256 + 66
Out[1]: 1709685058

买一送一，童叟无欺
58也是一样的:
http://callback.58.com/firewall/valid/920593415.do?namespace=huangyedetailpc&url=http%3A%2F%2Finfodetail1.58.com%2Fsz%2Fjisuanji%2F27978971970226x.shtml
"""
