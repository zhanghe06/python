# encoding: utf-8
__author__ = 'zhanghe'

import requests
import re


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}


ID = '55919'
url_down = 'http://dl.pconline.com.cn/download/'+ID+'.html'
url_token = 'http://dlc2.pconline.com.cn/dltoken/'+ID+'_genLink.js'
s = requests.session()


def get_temp_url(url):
    """
    获取下载页面模板地址
    """
    response = s.get(url)
    html = response.text
    reg = '<a class="btn sbDownload" .*? tempUrl="(.+?)">'
    tags = re.compile(reg, re.I).findall(html)
    # http://dlc2.pconline.com.cn/filedown_55919_6912056/zhifubaoqianbao.apk
    return tags[0]


def get_token(url):
    """
    获取token
    """
    header['Host'] = 'dlc2.pconline.com.cn'
    header['Referer'] = 'http://dl.pconline.com.cn/download/'+ID+'.html'
    # 头部一定要加，不然只是返回 iaMs0RrY
    response = s.get(url, headers=header)
    html = response.text
    print html  # genLink('9qE4Wbcp')
    return html.split('\'')[1]


def get_link(url, token):
    """
    组装下载链接
    """
    file_name = url.split('/')[-1]
    print file_name
    print token
    down_link = url.rstrip(file_name)+token+'/'+file_name
    print down_link
    return down_link


def download(file_path):
    """
    执行下载，支持断点续传
    """
    import os
    file_name = file_path.split('/')[-1]
    save_file_path = '../static/download/'+file_name
    print file_name
    print save_file_path
    # 伪装浏览器，组装下载命令
    cmd = "wget --user-agent=\"%s\" -c -O %s %s" % (header['User-Agent'], save_file_path, file_path)
    print cmd
    os.system(cmd)


def fuck():
    """
    主程序
    """
    temp_url = get_temp_url(url_down)
    token_down = get_token(url_token)
    down_link = get_link(temp_url, token_down)
    download(down_link)


if __name__ == '__main__':
    fuck()


'''
这是一个 pconline APP下载页面获取真实下载地址的测试
分析页面

第一部分：
tempurl="http://dlc2.pconline.com.cn/filedown_55919_6912056/zhifubaoqianbao.apk"

第二部分
<script type="text/javascript">

    function genLink(token) {
        if(token) {
            $('a.sbDownload').each(function(){
                var linkUrl = $(this).attr("tempUrl");
                if(linkUrl.indexOf("http://dlc2.pconline.com.cn/filedown") != -1) {
                    var idx = linkUrl.lastIndexOf("/");
                    var file = linkUrl.substring(idx);
                    var newLink = linkUrl.substring(0,idx)+'/'+token+file;
                    $(this).attr("href", newLink).attr('target','_blank');
                }
            });
        }
    }

    (function(){
            setTimeout(function(){
                $.getScript('http://dlc2.pconline.com.cn/dltoken/55919_genLink.js');
            },1000);
        })();
</script>

先访问：
http://dlc2.pconline.com.cn/dltoken/55919_genLink.js
获取token
获取token后，再将token与tempurl组装为真实的下载地址
结构如下：
http://dlc2.pconline.com.cn/filedown_55919_6912056/xxxxxxxx/zhifubaoqianbao.apk"

'''