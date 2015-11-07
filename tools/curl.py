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


def get_headers(url, header_key=None):
    """
    仅仅获取头部信息
    """
    cmd = 'curl -I %s' % url
    response = os.popen(cmd).read().strip()
    header_list = response.split('\r\n')
    print header_list[0]
    headers = {}
    for item in header_list:
        header = item.split(': ')
        if len(header) == 2:
            if header[0] == 'Set-Cookie' and headers.get('Set-Cookie') is not None:
                headers['Set-Cookie'] = ' | '.join([headers.get('Set-Cookie'), header[1].strip()])
            else:
                headers[header[0]] = header[1].strip()

    if header_key is not None:
        return headers.get(header_key, None)
    else:
        return headers


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
    import json
    # print get('https://www.baidu.com/s?wd=python')
    # print post('http://www.wealink.com/passport/login', 'username=123456&password=123456')
    # print get_headers('http://jump.zhineng.58.com/clk?target=mv7V0A-b5HThmvqfpv--5HTdmYw-w-ICXjF_E1KpuNG7EhnoEy0q5iubpgPGujYQrj01P19knWTQrjbvnHc1PjEYrHT3nWDdPj0h0vQfIjd_pgPYUARhIaubpgPYUHYQPjEvPWcLn19YnHndFMF-uWdCIZwkrBtf0v98PH98mvqVsvF6UhGGmith0vqd0hP-5HDhIh-1Iy-b5HThIh-1Iy-k5HDkni3zn1D8nH9dsWmvFhR8IZwk5HTh0A7zmyYqFh-1ug6YuyOb5yu6UZP-FMK_uWYVniuGUyRG5iudpyEqnWb3nHcQP1TQP1T1P1NhmvQopyEquynQrH--uWcVmHnkmBYYnhmLsyF-mymVuH0QnAcYrjK6nvPBFMKGujYQFhR8IA-b5HEYnWnzPHTYnjm3Pjn1PHDkPau-UMwY0jY1FMKzpyP-5HDYrHmh0hRbpgcqpZwY0jCfsLIfI1NzPi3drjN3shPfUiubpgPkULnqniu1IyFGujYQnH9vn1n3PzuW0hR6IARb5HDYPHNLn1ndnHT1rjTknaukmgF6Uy-b5iubpgPWmHYOPBu1uyQhmvDqrHmhuA-1UAtqnBu1uyQhUAtqnBuQ5HD8njD1nWTLPjbOrjnLn1TvPBukmyI-UMRV5HDhmh-b5HDdnjThIv-_uAP60hEqniu60ZK-Uhwoug-LULFb5HTh0hRWmyQ_uhQfI1YkFh7BIjYznjDdnjnQnRqCIy78uL--g17tnE&adact=3&psid=187378020189612344490821547&entinfo=442325040684335104_3&PGTID=187378020189612344490821547&ClickID=1&iuType=q_2')
    print json.dumps(get_headers('http://www.baidu.com'), indent=4)


"""
保存请求页面结果
$ url -o page.html http://www.linuxidc.com
通过代理访问
$ curl -x 123.45.67.89:1080 -o page.html http://www.linuxidc.com
上传文件
$ curl --form "fileupload=@filename.txt" http://hostname/resource
网络限速，下载速度最大不会超过1000B/second
$ curl --limit-rate 1000B -O http://www.gnu.org/software/gettext/manual/gettext.html
断点续传
$ curl -C -O http://www.gnu.org/software/gettext/manual/gettext.html
"""