# encoding: utf-8
__author__ = 'zhanghe'

import re
import json


def replace_html(input_html, reg_expression=r'', replace_text=''):
    """
    正则替换
    :param input_html:
    :param reg_expression:
    :param replace_text:
    :return:
    """
    p = re.compile(reg_expression, re.I)  # .*后面跟上? 非贪婪匹配 re.I大小写不敏感
    output_html = p.sub(replace_text, input_html)
    return output_html


def replace_all(input_html, replace_dict):
    """
    用字典实现批量替换
    """
    for k, v in replace_dict.iteritems():
        input_html = input_html.replace(k, v)
    return input_html


def strip_html(input_html):
    """
    去除html标签
    :param input_html:
    :return:
    """
    # p = re.compile('<[^>]+>')
    p = re.compile(r'<.*?>')  # .*后面跟上? 非贪婪匹配
    return p.sub("", input_html)


def replace_char_entity(html_str):
    """
    将html实体名称/实体编号转为html标签
    :param html_str:
    :return:
    """
    char_entities = {'&nbsp;': ' ', '&#160;': ' ',
                     '&lt;': '<', '&#60;': '<',
                     '&gt;': '>', '&#62;': '>',
                     '&amp;': '&', '&#38;': '&',
                     '&quot;': '"', '&#34;': '"',
                     }
    for char_key, char_value in char_entities.iteritems():
        html_str = html_str.replace(char_key, char_value)
    return html_str


def filter_tags(html_str):
    """
    将HTML中标签等信息去掉
    :param html_str:
    :return:
    """
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('</?br\s*?/?\s*?>', re.I)  # 处理文本换行
    re_p = re.compile('</?p\s*?/?\s*?>', re.I)  # 处理段落换行
    re_html = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', html_str)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_p.sub('\n', s)  # 将p转换为换行
    s = re_html.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replace_char_entity(s)  # 实体替换
    return s


def read_file(file_path):
    """
    一次读取全文件
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as f:
        return f.read()


def read_file_each_line(file_path, file_type='json'):
    """
    逐行读取文件
    :param file_path:
    :param file_type:
    :return:
    """
    with open(file_path, 'r') as f:
        for each_line in f:
            if file_type == 'json':
                yield json.loads(each_line)
            if file_type == 'csv':
                yield each_line


def save_file(file_path, text, save_type='w'):
    """
    保存文件
    :param file_path:
    :param text:
    :return:
    """
    with open(file_path, save_type) as f:
        f.write(text)


def replace_file_html(file_path, reg_rule=None):
    """
    html文件内容替换
    :param file_path:
    :param reg_rule:
    示例：
    reg_rule = [
        (r'<a href="http://(.*?).shtml"', '<a href="#"'),
        (r' onClick="analytical((.*?))"', '')
        ]
    :return:
    """
    if not reg_rule:
        reg_rule = []
    content = read_file(file_path)
    for rule in reg_rule:
        content = replace_html(content, rule[0], rule[1])
    save_file(file_path, content)


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


def test_replace_char_entity():
    """
    测试特殊字符转html标签
    """
    html_test = '''&nbsp;&nbsp;this is a test;&nbsp;&nbsp;'''
    print replace_char_entity(html_test)


def test_replace_all():
    """
    测试用字典实现批量替换
    """
    replacements = {'\\n': '', '\\r': ''}
    print replace_all('ffff\\n\\r\\ngggg\\ndfdf', replacements)

    replacements = {'\n': '', '\r': ''}
    print replace_all('ffff\n\r\ngggg\ndfdf', replacements)


def get_form(html, form_index=0, filter_tag_name_list=None, skip_tag_name_list=None):
    """
    获取表单
    :param html:
    :param form_index:
    :param filter_tag_name_list:设置需要的标签名称列表
    :param skip_tag_name_list:设置取消的标签名称列条
    :return:
    """
    from lxml.html import fromstring
    forms = fromstring(html).forms
    form = forms[form_index]
    data = {}
    for name, value in form.fields.iteritems():
        # 跳过
        if skip_tag_name_list:
            if name in skip_tag_name_list:
                continue
        # 字符串
        if value is None:
            value = ''
        # 过滤
        if filter_tag_name_list:
            if name in filter_tag_name_list:
                data[name] = value
        else:
            data[name] = value
    return data


if __name__ == '__main__':
    test_html = '''<h2>多云</h2>  '''
    print replace_html(test_html)
    print replace_html(test_html, r'<.*?>')
    print strip_html(test_html)
    # read_file_text = read_file('/home/zhanghe/code/php/secoo/app/views/partials/container/floor.volt')
    # print read_file_text
    # save_file('/home/zhanghe/code/php/secoo/app/views/partials/container/floor2.volt', read_file_text)
    reg_rule_html = [
        (r'<a href="http://(.*?)"', '<a href="#"'),
        (r'<a target="_blank" href="http://(.*?)"', '<a target="_blank" href="#"'),
        (r'<a style="width:56px;" href="http://(.*?).shtml"', '<a style="width:56px;" href="#"'),
        (r'(\s*)onClick="analytical((.*?))"', ''),
        # (r'(\n){2,}', '\n'),  # 这种不能去除空格组成的行
        (r'(\n[\s|\r]*\n)', '\n'),  # 贪婪匹配，去除多余换行和无意义空行
        ]
    # test_file_path = '/home/zhanghe/code/php/secoo/app/views/partials/container/slider.volt'
    test_file_path = '/home/zhanghe/code/php/secoo/app/views/partials/head.volt'
    replace_file_html(test_file_path, reg_rule_html)
    html = '''<div style="padding-bottom:30px;">好消息：有手机&nbsp;就可以做的好<br>兼职 空余</BR>时间生<p>活工作两<P>不误！！！！<br><br>郑重声明：我们是公司直招，不是中介，不收任何费用，有收费情况请投诉、<br>非常期待您成为我们的伙伴，加不加入没关系，了解一下也没有关系<br><br>有意者可直接联系我们的企业客服QQ:848304882【在线咨询】 承诺不收取任何费用<br><br>我们不需要用太华丽的语言去宣称自己，我们只想叫我们的客户每天都有固定的收入，<br>并且我们一直在努力。我们只需要你每天有一定的上网时间，有部分的电脑知识，无经验公司可以免费培训。<br>---------------------------------------------------------------------<br><br>有意者可直接联系我们的企业客服QQ:848304882【在线咨询】 承诺不收取任何费用<br>工作要求：<br>1，工作认真，有上进心，有团队精神，服从工作安排。<br>2，有具备手机（3G网络）或 电脑，每天有1小时的空余时间。<br>3、普通话标准、 语言沟通能力强、 有简单的评判能力；<br>4、态度积极，性格开朗，做事有激情，抗压能力强，有责任心，执行力强；<br>5、要有团队合作精神；<br>6、有相关工作经验者优先；<br>7，无不良嗜好，为人心态良好，逻辑思维及条理清晰 有较强责任心。<br>8，小学以上学历，电脑操作基础懂，会打字聊天。<br>---------------------------------------------------------------------<br>有意者可直接联系我们的企业客服QQ:848304882【在线咨询】承诺不收取任何费用<br>来应聘的有志者请联系客服QQ:848304882  （注：为节省工作资源不收取简历，请联系企业客服，谢谢合作。）</div>'''
    print filter_tags(html)
    test_replace_char_entity()
    test_replace_all()


'''
这个工具可以做为仿站辅助工具
下一步做个获取页面图片的辅助工具配合使用
'''