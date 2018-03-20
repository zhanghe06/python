#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: vote.py
@time: 2018-03-29 11:00
"""


from __future__ import print_function
from __future__ import unicode_literals

import json
import random

import requests
from requests.exceptions import ConnectTimeout, ReadTimeout, ConnectionError


REQUESTS_TIME_OUT = (5, 5)


user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
    'Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)',
    'Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; STF-AL00 Build/HUAWEISTF-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0; LEX626 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 6.0)',
    'Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2121 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.17 NetType/WIFI Language/zh_HK',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36',
    'MQQBrowser/5.3/Mozilla/5.0 (Linux; Android 6.0; TCL 580 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
    'Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 5.1; m3 note Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
]


def get_proxy_list_nghuyong():
    url = 'http://proxy.nghuyong.top/?country=China&type=http'
    return [i['ip_and_port'] for i in requests.get(url).json().get('data', [])]


def get_proxy_list_kuaidaili():
    url = 'http://ent.kuaidaili.com/api/getproxy/?orderid=922229983862136&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&b_android=1&b_iphone=1&protocol=1&method=2&an_tr=1&an_an=1&an_ha=1&sp1=1&sp2=1&quality=2&format=json&sep=1'
    result = requests.get(url).json()
    if result['code'] != 0:
        print(result['msg'])
        return []
    return result['data']['proxy_list']


proxy_list = [
    '110.76.185.162:16818',
    '43.226.165.51:16818',
    '182.61.35.179:16818',
    '117.48.199.243:16818',
    '43.226.164.66:16818',
    '42.51.206.58:16818',
    '120.25.71.27:16818',
    '125.65.82.248:16818',
    '120.24.68.197:16818',
    '121.42.177.10:16818',
]
proxy_list.extend(get_proxy_list_nghuyong())
proxy_list.extend(get_proxy_list_kuaidaili())
# TODO add your proxies

proxies_list = [
    {
        'http': 'http://%s' % proxy,
        'https': 'http://%s' % proxy,
    } for proxy in proxy_list
]


def fuck():
    """
    投票入口（默认华云），想什么呢，当然是投华云！
    :return:
    """
    c_vote_ok = 0
    c_vote_er = 0
    c_proxy_er = 0
    user_agent = random.choice(user_agent_list)
    for proxies in proxies_list:
        try:
            cookies = {
            }
            s = requests.session()
            headers = {
                'User-Agent': user_agent,
                'X-Requested-With': 'XMLHttpRequest',
            }
            list_url = 'http://www.zhiding.cn/vote/cloud?nomobile=&from=singlemessage&isappinstalled=0'
            vote_url = 'http://www.zhiding.cn/vote/cloud/action'
            data = {
                'ajax': 'true',
                'opid': 45,
            }

            request_headers = headers.copy()
            request_headers['Host'] = 'www.zhiding.cn'
            request_headers['Origin'] = 'http://www.zhiding.cn'

            request_cookie = cookies.copy()

            list_res = s.get(
                list_url,
                headers=request_headers,
                cookies=request_cookie,
                proxies=proxies,
                timeout=REQUESTS_TIME_OUT,
            )
            if list_res.status_code != 200:
                print('代理失效')
                c_proxy_er += 1
                continue

            request_headers['Referer'] = 'http://www.zhiding.cn/vote/cloud?nomobile=&from=singlemessage&isappinstalled=0'

            request_cookie.update(list_res.cookies)

            res = s.post(
                vote_url,
                data=data,
                headers=request_headers,
                cookies=request_cookie,
                proxies=proxies,
                timeout=REQUESTS_TIME_OUT,
            )
            if list_res.status_code != 200:
                print('代理失效')
                c_proxy_er += 1
                continue

            result = res.json()
            if result.get('code') == 10000:
                print('投票成功, 票数: %s' % result.get('msg'))
                c_vote_ok += 1
            elif result.get('code') == 10001:
                print('投票失败, 原因: %s' % '投票次数用完')
                c_vote_er += 1
            elif result.get('code') == 10002:
                print('投票失败, 原因: %s' % result.get('msg'))
                c_vote_er += 1
            else:
                print(json.dumps(result, indent=4, ensure_ascii=False))
                c_vote_er += 1
        except (ConnectTimeout, ReadTimeout, ConnectionError):
            print('代理失效')
            c_proxy_er += 1
        except Exception as e:
            print(e.message)
            c_vote_er += 1
    print('刷票成功: %s' % c_vote_ok)
    print('刷票失败: %s' % c_vote_er)
    print('代理失效: %s' % c_proxy_er)
    print('-'*12)
    print('暴力刷票: %s' % (c_vote_ok + c_vote_er + c_proxy_er))


if __name__ == '__main__':
    fuck()
