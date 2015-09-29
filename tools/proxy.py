# encoding: utf-8
__author__ = 'zhanghe'


import json
import html

ProxyList = []
# IP地址	端口号	代理类型	匿名度	地域分布	响应速度	最后检测时间
ProsyItem = {
    'Ip': '',
    'Port': '',
    'Type': '',
    'AnonymousDegree': '',
    'Area': '',
    'Speed': '',
    'ScanTime': ''
}

# 真实端口映射关系（class 端口号）
PortDict = {
    'GEA': '80',
    'GEGEA': '8080',
    'GEHAE': '8088',
    'DBZAE': '3988',
    'HBBAE': '8888',
    'CFACE': '3128',
    # 'HGCBG': '',
    'GEZIE': '8123',
    'GEZEE': '8118',
    'HCAAA': '9000',
    'BEFEII': '18161',
    'HIDHG': '9797'
}


def scan_proxy_qiaodm():
    """
    扫描代理资源
    :return:
    """
    import requests
    from pyquery import PyQuery as Pq

    source_site = 'http://ip.qiaodm.com/'

    header = {
        'Host': 'ip.qiaodm.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
    }

    s = requests.session()
    # 抓取页面
    file_html = s.get(source_site).content

    # 保存文件
    # with open('test.html', 'a') as f:
    #     f.write(file_html.encode('utf-8'))
    #
    # # 读取抓取的页面
    # with open('test.html', 'r') as f:
    #     file_html = f.read()

    text_pq = Pq(file_html)
    tr_list = text_pq('tbody').find('tr[style="text-align: center;"]')
    print '单页共 %s 条记录' % len(tr_list)
    for tr_item in tr_list:
        # print Pq(tr_item).html()
        # print('---------------------')
        td_list = Pq(tr_item).find('td')
        # print '单条共 %s 列字段' % len(td_list)
        field_list = []
        for td_item in Pq(td_list):
            field = Pq(td_item).text()
            field_list.append(field)
            # print field
            # print('++++++++++++++++++')

        # 特殊处理ip地址
        ip = Pq(td_list).eq(0).html()
        # 去除干扰信息
        ip = html.replace_html(ip, r'<p style="display:none;"/>')
        ip = html.replace_html(ip, r'<p style="display: none;"/>')
        ip = html.replace_html(ip, r'<p style=.*?display:.*?none;.*?>.*?</p>')
        # 去除标签
        ip = html.strip_html(ip)
        # print ip
        # 过滤掉非法ip地址
        if len(ip.split('.')) != 4:
            continue

        # 特殊处理端口
        port_key = Pq(td_list).eq(1).attr('class').split()[1]
        if port_key not in PortDict:
            print '发现新端口: %s' % port_key
            continue
        port = PortDict.get(port_key, '')

        ProsyItem['Ip'] = ip.replace(' ', '')
        ProsyItem['Port'] = port
        ProsyItem['Type'] = field_list[2].strip()
        ProsyItem['AnonymousDegree'] = field_list[3].strip()
        ProsyItem['Area'] = field_list[4].strip()
        ProsyItem['Speed'] = field_list[5].strip()
        ProsyItem['ScanTime'] = field_list[6].strip()
        # print ProsyItem
        proxy_item = json.dumps(ProsyItem, ensure_ascii=False)
        html.save_file('proxy.json', proxy_item + '\n', 'a')


def scan_proxy_xicidaili():
    """
    扫描代理资源
    :return:
    """
    import requests
    from pyquery import PyQuery as Pq

    source_site = 'http://www.xicidaili.com/'

    header = {
        'Host': 'www.xicidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
    }

    s = requests.session()
    # 抓取页面
    file_html = s.get(source_site).content

    # 保存文件
    # with open('test.html', 'a') as f:
    #     f.write(file_html.encode('utf-8'))
    #
    # # 读取抓取的页面
    # with open('test.html', 'r') as f:
    #     file_html = f.read()

    text_pq = Pq(file_html)
    pass


def get_list():
    """
    获取代理列表
    :return:
    """
    proxy_list = []
    for each_line in html.read_file_each_line('proxy.json'):
        item = json.loads(each_line)
        proxy_list.append(item)
    # print json.dumps(proxy_list, ensure_ascii=False, indent=4)
    return proxy_list


def get_item():
    """
    随机获取一个可用代理
    :return:
    """
    import random
    proxy_list = get_list()
    random.shuffle(proxy_list)
    print json.dumps(proxy_list[0], ensure_ascii=False, indent=4)
    return proxy_list[0]


def rm_item():
    """
    删除一个不可用代理
    :return:
    """
    pass


def scan_proxy(name):
    if name is None:
        print '请输入代理名称'
    else:
        scan_fun = eval('scan_proxy_%s' % name)
        return scan_fun()


if __name__ == "__main__":
    scan_proxy('qiaodm')
    scan_proxy('xicidaili')
    # get_list()
    # get_item()


"""
因为此网站对关键信息（IP 和 端口）做了防爬虫处理
所以多了几行特殊处理的代码，整体效果还是可以的
"""