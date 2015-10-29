# encoding: utf-8


import urllib2
import re

root_url = 'http://www.sohu.com'

rule_src = 'src="(.+?)"'
rule_a = '<a .*?href="(.+?)".*?>'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

url_list = [root_url]  # 爬虫待访问url列表
url_visited_list = []  # 爬虫已访问url列表

file_path = 'sohu.txt'
url_file = open(file_path, 'a')


def read_src(src_url=None):
    """
    页面处理
    """
    if src_url is None:
        print '待抓取列表为空'
    try:
        request = urllib2.Request(src_url)
        request.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(request)
        html = response.read()
        src_list = re.compile(rule_src, re.S).findall(html)
        a_list = re.compile(rule_a, re.S).findall(html)
        link_list = list(set(src_list + a_list))
        for url in link_list:
            print_static(url)
            if re.match(r"http:\/\/.+?sohu\.com\/.*?", url) and (not (url.endswith('.jpg') or url.endswith('.gif') or url.endswith('.png') or url.endswith('.js') or url.endswith('.css') or url.startswith('mailto:') or url.startswith('javascript:'))):
                if url not in [None, '', '#'] and url not in url_list and url not in url_visited_list:  # 去重
                    url_list.append(url)
        url_visited_list.append(src_url)
    except Exception, e:
        print e


def print_static(src):
    """
    输出静态资源文件地址
    """
    if src.startswith('http://') and src.startswith('/') and (src.endswith('.jpg') or src.endswith('.gif') or src.endswith('.png')):
        if src.startswith('/'):
            src = ''.join([root_url, src])
            url_file.write(src)
            url_file.write('\n')
            print '图片：%s' % src
    if src.endswith('.js'):
        if src.startswith('/'):
            src = ''.join([root_url, src])
            url_file.write(src)
            url_file.write('\n')
            print 'js文件：%s' % src
    if src.endswith('.css'):
        if src.startswith('/'):
            src = ''.join([root_url, src])
            url_file.write(src)
            url_file.write('\n')
            print 'css文件：%s' % src


def run():
    """
    主程序
    """
    try:
        count = 0
        while len(url_list) > 0:
            read_src(url_list.pop(0))
            count += 1
            if count % 10 == 0:
                url_file.flush()
    except KeyboardInterrupt:
        url_file.close()
        print '程序退出'


if __name__ == '__main__':
    run()
