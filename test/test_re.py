# coding=utf-8
__author__ = 'zhanghe'

import re
import json


test_html = '''<dl class="lineDl">
<dt>工作年限：</dt>
<dd>
<div class="inptext_fl ">应届毕业生</div>
<input type="hidden" id="WorkYear" value="2"/>
</dd>
</dl>
<dl class="lineDl">
<dt>居住地：</dt>
<dd>
<div class="inptext_fl ">清远</div>
</dd>
</dl>
<dl class="lineDl">
<dt>求职状态：</dt>
<dd>
<div class="inptext_fl ">目前正在找工作</div>
</dd>
</dl>
<dl class="lineDl">
<dt>身高：</dt>
<dd class="dd_textW">
<div class="inptext_fl ">180cm&nbsp;</div>
</dd>
<dt>婚姻状况：</dt>
<dd>
<div class="inptext_fl ">&nbsp;</div>
</dd>
</dl>'''


def re_html(html):
    """
    通过正则表达式获取关键数据
    将两个有序的列表组合为无序的字典
    :param html:
    :return:
    """
    reg_dt = r'<dt>(.+?)：</dt>'
    reg_dd = r'<div class="inptext_fl ">(.+?)</div>'
    dt = re.compile(reg_dt)
    dd = re.compile(reg_dd)
    dt_list = re.findall(dt, html)
    dd_list = re.findall(dd, html)

    zip_list = zip(dt_list, dd_list)
    html_dict = dict((name, value) for name, value in zip_list)

    return json.dumps(html_dict, ensure_ascii=False, indent=4)


def get_email(html=None):
    """
    从文本中提取email
    """
    if html is None:
        return []
    email_rule = r'[^\_\@\s\W][\w\_\-\.]{1,}\@(?:[^\s\.]{1,}\.){1,}(?:[a-z]{2,4}\.?){1,2}'
    email_list = re.compile(email_rule, re.S).findall(html)
    # print json.dumps(email_list, ensure_ascii=False, indent=4)
    # email_list_new = []
    # for item in email_list:
    #     email_list_new.append(item.lower())
    # return email_list_new
    return [item.lower() for item in email_list]


if __name__ == '__main__':
    # print re_html(test_html)

    html_test = '''邮箱：yy_y.it@gabc-xx.com +zhang_he06@163.com .zhanG_he06@163.com -zhang_he06@163.com _zhang_he06@163.com @zhang_he06@163.com @zhang-he06@163.com zhanghe@baidu.com 地址：上海市'''
    email_result = get_email(html_test)
    print json.dumps(email_result, ensure_ascii=False, indent=4)

"""
测试结果
[
    "yy_y.it@gabc-xx.com",
    "zhang_he06@163.com",
    "zhang_he06@163.com",
    "zhang_he06@163.com",
    "zhang_he06@163.com",
    "zhang_he06@163.com",
    "zhang-he06@163.com",
    "zhanghe@baidu.com"
]
"""

"""
(?:pattern)
匹配 pattern 但不获取匹配结果
例如， 'industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式。
"""