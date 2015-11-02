# encoding: utf-8
__author__ = 'zhanghe'


import os

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'


def get(url, with_user_agent=1):
    """
    GET请求
    get('https://www.baidu.com/s?wd=python')
    """
    if with_user_agent == 1:
        cmd = 'curl -A "%s" %s' % (user_agent, url)
    else:
        cmd = 'curl %s' % url
    response = os.popen(cmd).read()
    return response


def post(url, data, with_user_agent=1):
    """
    POST请求 自动跳转（参数-L） 自动保存cookie到文件head_cookies
    post('http://www.wealink.com/passport/login', 'username=123456&password=123456')
    """
    if with_user_agent == 1:
        cmd = 'curl -D head_cookies -L -A "%s" -d "%s" %s' % (user_agent, data, url)
    else:
        cmd = 'curl -D head_cookies -L -d "%s" %s' % (data, url)
    response = os.popen(cmd).read()
    return response


def get_head(url):
    """
    仅仅获取头部信息
    """
    cmd = 'curl -I %s' % url
    response = os.popen(cmd).read()
    return response


def save_cookie(url):
    """
    保存cookie到运行命令的目录下，并命名为head_cookies
    """
    cmd = 'curl -D head_cookies %s' % url
    response = os.popen(cmd).read()
    return response


def with_cookie(url):
    """
    使用cookie
    """
    cmd = 'curl -b head_cookies %s' % url
    response = os.popen(cmd).read()
    return response


if __name__ == '__main__':
    # print get('https://www.baidu.com/s?wd=python')
    print post('http://www.wealink.com/passport/login', 'username=123456&password=123456')
