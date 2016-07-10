# encoding: utf-8
__author__ = 'zhanghe'


def test_doc_xpath():
    """
    测试document的xpath用法
    :return:
    """
    import lxml.html

    html = u'''
    <table cellspacing="0" cellpadding="0">
    <tbody>
    <tr>
    <td width="10%" nowrap="" style="padding-bottom: 5px;">数量: 1</td>
    <td width="90%" align="right" nowrap="" style="padding-right: 5px;"></td>
    </tr>
    </tbody>
    </table>

    '''
    doc = lxml.html.fromstring(html)

    num_list = doc.xpath('//td[@style="padding-bottom: 5px;" and @nowrap="" and not(@align="right")]/text()')
    print '-'*8
    print type(num_list[0])
    print num_list[0]


def test_etree_xpath():
    """
    测试etree的xpath用法
    :return:
    """
    from lxml import etree
    html = u'''
    <table cellspacing="0" cellpadding="0">
    <tbody>
    <tr>
    <td width="10%" nowrap="" style="padding-bottom: 5px;">数量: 1</td>
    <td width="90%" align="right" nowrap="" style="padding-right: 5px;"></td>
    </tr>
    </tbody>
    </table>

    '''
    tree = etree.HTML(html)
    num_list = tree.xpath('//td[@style="padding-bottom: 5px;" and @nowrap="" and not(@align="right")]/text()')
    num_element_list = tree.xpath('//td[@style="padding-bottom: 5px;" and @nowrap="" and not(@align="right")]')
    print '-'*8
    print type(num_list[0])
    print type(num_list[0]), num_list[0]
    print '-'*8
    print type(num_element_list[0])
    print type(num_element_list[0].text), num_element_list[0].text


if __name__ == '__main__':
    test_doc_xpath()
    test_etree_xpath()

"""
测试结果：
--------
<type 'lxml.etree._ElementUnicodeResult'>
数量: 1
--------
<type 'lxml.etree._ElementUnicodeResult'>
<type 'lxml.etree._ElementUnicodeResult'> 数量: 1
--------
<type 'lxml.etree._Element'>
<type 'unicode'> 数量: 1
"""