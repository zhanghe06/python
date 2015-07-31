# encoding: utf-8
__author__ = 'zhanghe'

import requests
import time
import json
import os
import tools.html
import gevent
from gevent import monkey
monkey.patch_all()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    }

s = requests.session()
keywords_list = ['衣服']  # 爬虫待访问关键词列表
keywords_visited_list = []  # 爬虫已访问关键词列表


def get_keywords_list(keywords):
    """
    获取关键词列表
    :param keywords:
    :return:
    """
    # print keywords
    url = 'https://suggest.taobao.com/sug'
    payload = {
        'code': 'utf-8',
        'q': keywords,
        '_ksTS': str(int(1000*(time.time())))+'_2550',
        # 'callback': 'jsonp2551',
        'k': '1',
        'area': 'c2c',
        'bucketid': '19',
    }
    header['Host'] = 'suggest.taobao.com'
    header['Referer'] = 'https://top.taobao.com/index.php?spm=a1z5i.1.2.1.hUTg2J&topId=HOME'
    response = s.get(url, params=payload, headers=header)
    # print response.url
    content = response.text
    key_result_list = json.loads(content)['result']
    # print '新增关键词列表'
    # print json.dumps(key_result_list, indent=4, ensure_ascii=False)
    for i in key_result_list:
        item = tools.html.strip_html(i[0])  # 去除html标签
        if item is not None and item not in keywords_list and item not in keywords_visited_list:  # 去重
            keywords_list.append(item)
    keywords_visited_list.append(keywords)
    keywords_list.remove(keywords)


def save(result_list, file_name):
    """
    保存文件
    :param result_list:
    :param file_name:
    :return:
    """
    file_path = '../static/taobao/'
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    filename = file_path + file_name
    result_json = json.dumps(result_list, indent=4, ensure_ascii=False)
    with open(filename, 'wb') as f:
        f.write(result_json.encode('utf-8'))


def time_statistics(start_time):
    """
    计时统计
    """
    print "待访问节点：%s" % len(keywords_list)
    print "已访问节点：%s" % len(keywords_visited_list)
    end_time = time.time()
    print "耗时：%0.2f S" % (end_time - start_time)
    print '--------------'


def fuck():
    """
    爬虫主程序
    """
    start_time = time.time()
    while len(keywords_list) > 0:
        # get_keywords_list(keywords_list.pop(0))
        threads = [gevent.spawn(get_keywords_list, i) for i in keywords_list]
        gevent.joinall(threads)
        time_statistics(start_time)
        save(keywords_list, 'keywords_list.json')
        save(keywords_visited_list, 'keywords_visited_list.json')
    print '程序结束，打印结果'
    print json.dumps(keywords_list, indent=4, ensure_ascii=False)
    print json.dumps(keywords_visited_list, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    fuck()


"""

使用协程前后耗时的对比：

待访问节点：0
已访问节点：2493
耗时：153.60 S
--------------

--------------
待访问节点：0
已访问节点：2504
耗时：130.58 S
--------------

"""