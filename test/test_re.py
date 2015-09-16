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


if __name__ == '__main__':
    print re_html(test_html)
