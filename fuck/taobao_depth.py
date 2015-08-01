# encoding: utf-8
__author__ = 'zhanghe'

import requests
import time
import json
import os
import tools.html

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    }

s = requests.session()
keywords_list = ['衣服', '鞋子']  # 关键词列表
keywords_result_dict = {}
depth = 3  # 最大深度


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
    content = response.text
    key_result_list = json.loads(content)['result']

    level_list = []
    for i in key_result_list:
        item = tools.html.strip_html(i[0])  # 去除html标签
        level_list.append(item)
    return level_list


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
    end_time = time.time()
    print "耗时：%0.2f S" % (end_time - start_time)
    print '--------------'


def data_statistics(data_dict):
    """
    数据统计
    """
    for key, item_list in data_dict.iteritems():
        print '关键词[%s]共%s级：' % (key, len(item_list))
        for i in range(len(item_list)):
            print '%s级共有%s个' % (i+1, len(item_list[i]))
        print '--------------'


def fuck():
    """
    爬虫主程序
    """
    # 定义数据结构
    for keywords in keywords_list:
        keywords_result_dict[keywords] = []
        for i in range(depth):
            keywords_result_dict[keywords].append([])
    print json.dumps(keywords_result_dict, indent=4, ensure_ascii=False)
    start_time = time.time()
    for i in range(depth):
        if i == 0:
            for item in keywords_list:
                keywords_result_dict[item][i] = get_keywords_list(item)
                time_statistics(start_time)
        else:
            for item in keywords_list:
                for j in keywords_result_dict[item][i-1]:
                    keywords_result_dict[item][i].extend(get_keywords_list(j))
                    time_statistics(start_time)
    print json.dumps(keywords_result_dict, indent=4, ensure_ascii=False)
    save(keywords_result_dict, 'keywords_result_dict.json')
    print '程序结束，统计如下'
    data_statistics(keywords_result_dict)


if __name__ == '__main__':
    fuck()


"""
数据结构：

{
    "衣服": [
        [],  # 一级关键词
        [],  # 二级关键词
        []   # 三级关键词
    ],
    "鞋子": [
        [],
        [],
        []
    ]
}


程序结束，结果如下
关键词[衣服]共3级：
1级共有10个
2级共有90个
3级共有878个
--------------
关键词[鞋子]共3级：
1级共有10个
2级共有90个
3级共有881个
--------------

"""