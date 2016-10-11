#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: 23432.py
@time: 2016/10/10 下午10:43
"""


import xml.etree.ElementTree as ET


xml_str_test = """
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""


def print_node(node):
    # print "attrib:%s" % node.attrib
    print "tag:%s" % node.tag
    print "text:%s" % node.text


def read_nodes(em):
    print type(em), em
    for child in em:
        print_node(child)
        read_nodes(child)


def xml_to_dict(xml_str):
    """
    将xml转为dict
    """
    dict_data = {}
    root = ET.fromstring(xml_str)
    dict_data[root.tag] = {}
    print_node(root)
    read_nodes(root)


def run():
    xml_to_dict(xml_str_test)


if __name__ == '__main__':
    run()
