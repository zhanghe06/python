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


def test_has_key(html=u''):
    """
    测试是否包含某关键字
    """
    # html = u'''某大型公司职位'''
    rule = ur'代招|某知名|猎头职位|某互联网|某.*公司'
    key_list = re.compile(rule, re.S).findall(html)
    print ' '.join(key_list)  # 匹配的关键词
    if key_list:
        print '代招职位'
    else:
        print '正常职位'


def test_group(line):
    """
    测试分组
    test_group('ip地址：127.0.0.1；')
    :return:
    """
    # reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    reip = re.compile(r'(?:\d{1,3}\.){3}\d{1,3}')
    for ip in reip.findall(line):
        print ip


def test_group_02():
    """
    测试分组
    :return:
    """
    line = u"""{rootcatentry:{dispid:'1',name:'房产信息',listname:'house'},catentry:{dispid:'14',name:'商铺租售/生意转让',listname:'shangpu'},locallist:[{dispid:'2', name:'上海', listname:'sh'},{dispid:'1399', name:'黄浦', listname:'huangpu'},{dispid:'1421', name:'人民广场', listname:'renminguangchang'}],infoid:'27083373898050',userid:'39050173763341',linkman:'李经理'"""
    # reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    re_local = re.compile(ur'(?:dispid:\'\d+\', name:\'(.*?)\')')
    for local in re_local.findall(line):
        print local


def test_03():
    rule_company_name = ur'{"I":\d+,"V":"(.*?公司)"}'
    company_name_re_compile = re.compile(rule_company_name, re.I)
    for i in company_name_re_compile.findall(u'etwret{"I":123,"V":"上海啥啥啥有限公司"}werery'):
        print i


if __name__ == '__main__':
    # print re_html(test_html)

    # html_test = '''邮箱：yy_y.it@gabc-xx.com +zhang_he06@163.com .zhanG_he06@163.com -zhang_he06@163.com _zhang_he06@163.com @zhang_he06@163.com @zhang-he06@163.com zhanghe@baidu.com 地址：上海市'''
    # email_result = get_email(html_test)
    # print json.dumps(email_result, ensure_ascii=False, indent=4)
    # test_has_key(u'''某大型公司职位''')
    test_group('127.0.0.1')
    test_group('ip地址：127.0.0.1；')
    test_group_02()
    test_03()

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

"""
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""