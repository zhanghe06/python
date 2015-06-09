# encoding: utf-8
__author__ = 'zhanghe'

import requests
from pyquery import PyQuery as Pq
import re
import json
import time
import gevent
from gevent import monkey
monkey.patch_all()


root_url = 'http://www.ycit.cn/'  # 爬虫入口
web_host = 'http://www.ycit.cn/'
web_domain = 'ycit.cn'
url_list = [root_url]  # 爬虫待访问url列表
url_visited_list = []  # 爬虫已访问url列表


def url_join(url_str, host):
    """
    url拼接
    :param url_str:
    :param host:
    :return:
    """
    if url_str is not None:
        if url_str.startswith(host) or url_str.startswith('http://'):
            return url_str
        return host.rstrip('/') + '/' + url_str.lstrip('/')


def url_filter(url_str, domain):
    """
    过滤其它域名
    :param url_str:
    :param domain:
    :return:
    """
    if url_str is not None:
        if domain in url_str:
            return url_str


def save(result_list, file_name):
    """
    保存文件
    :param result_list:
    :param file_name:
    :return:
    """
    import os

    file_path = 'static/url_list/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    filename = file_path + file_name
    result_json = json.dumps(result_list, indent=4, ensure_ascii=False)
    with open(filename, 'wb') as f:
        f.write(result_json.encode('utf-8'))


def web_crawler_pq(url_node=None):
    """
    基于PyQuery的网页爬虫
    """
    if url_node is None:
        print '待抓取列表为空'
    response = requests.get(url_node)
    text_pq = Pq(response.text)
    tags = text_pq('html').find('a')
    for tag in tags:
        url_pre = Pq(tag).attr('href')
        if url_pre != '#' and url_pre is not None:  # 过滤掉错误地址
            url = url_filter(url_join(url_pre, web_host), web_domain)
            if url is not None and url not in url_list and url not in url_visited_list:  # 去重
                url_list.append(url.rstrip('/'))
    # print json.dumps(url_list, indent=4, ensure_ascii=False)
    print "待访问节点：%s" % len(url_list)
    url_visited_list.append(url_node)
    print "已访问节点：%s" % len(url_visited_list)
    end_time = time.time()
    print "耗时：%0.2f S" % (end_time - start_time)
    print '--------------'
    # save(url_list, 'url_list.json')
    # save(url_visited_list, 'url_visited_list.json')


def web_crawler_re(url_node=None):
    """
    基于正则表达式的网页爬虫
    """
    if url_node is None:
        print '待抓取列表为空'
    response = requests.get(url_node)
    html = response.text
    reg = '<a .*?href="(.+?)".*?>'
    tags = re.compile(reg, re.I).findall(html)
    for tag in tags:
        if tag != '#' and tag is not None:  # 过滤掉错误地址
            url = url_filter(url_join(tag, web_host), web_domain)
            if url is not None and url not in url_list and url not in url_visited_list:  # 去重
                url_list.append(url.rstrip('/'))
    # print json.dumps(url_list, indent=4, ensure_ascii=False)
    print "待访问节点：%s" % len(url_list)
    url_visited_list.append(url_node)
    print "已访问节点：%s" % len(url_visited_list)
    end_time = time.time()
    print "耗时：%0.2f S" % (end_time - start_time)
    print '--------------'
    # save(url_list, 'url_list.json')
    # save(url_visited_list, 'url_visited_list.json')


if __name__ == "__main__":
    start_time = time.time()
    # while len(url_list) > 0:
        # web_crawler_pq(url_list.pop(0))  # PyQuery方式
        # web_crawler_re(url_list.pop(0))  # 正则方式

    # 基于协程的抓取
    while len(url_list) > 0:
        threads = [gevent.spawn(web_crawler_re, i) for i in url_list]
        gevent.joinall(threads)
    print '结束'


"""
查看测试结果：
$ tail -f ~/code/python/static/url_list/url_list.json
$ tail -f ~/code/python/static/url_list/url_visited_list.json

相同耗时下抓取速度比较

不使用协程：
--------------
待访问节点：539
已访问节点：24
耗时：42.85 S
--------------

使用协程：
--------------
待访问节点：1404
已访问节点：312
耗时：42.67 S
--------------

"""