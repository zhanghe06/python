# encoding: utf-8
__author__ = 'zhanghe'


def system_to_decimal(string, hex_format=2):
    """
    将二进制[八进制/十六进制]转为十进制
    """
    if hex_format in [2, 8, 16]:
        return int(string, base=hex_format)


def hex_to_bytes(string):
    """
    十六进制字符串转为字节列表
    """
    length = len(string)
    tmp = []
    for i in range(0, length, 2):
        tmp.append(int("0x" + string[i:i + 2], base=16))
    return bytes(tmp)


def test_unescape():
    # unicode编码后的汉字的解析
    str_xx = '&#21152;&#20837;&#21040;&#34;&#25105;&#30340;&#20070;&#30446;&#36873;&#21333;&#34;&#20013;'
    from HTMLParser import HTMLParser
    h = HTMLParser()
    print h.unescape(str_xx)


def test_unicode():
    a = '\u6211\u6765\u4e86'
    print a.decode('raw_unicode_escape')  # 我来了

    # =============
    # 通用转换方法：

    # python 2.x str 转 unicode:
    # str_string.decode('original_encoding')
    print repr('我来了'.decode('utf-8')), '我来了'.decode('utf-8')

    # unicode 转 str:
    # unicode_string.encode('target_encoding')
    print repr(u'\u6211\u6765\u4e86'.encode('utf-8')), u'\u6211\u6765\u4e86'.encode('utf-8')  # 每个汉子占3个字节
    print repr(u'\u6211\u6765\u4e86'.encode('GBK')), u'\u6211\u6765\u4e86'.encode('GBK')  # 每个汉子占2个字节


def test():
    """
    转换测试
    """
    print hex_to_bytes('01ff')  # [1, 255]
    # 二进制转十进制
    print system_to_decimal('10')  # 2
    # 八进制转十进制
    print system_to_decimal('10', 8)  # 8
    # 十六进制转十进制
    print system_to_decimal('10', 16)  # 16
    # 十六进制转十进制
    print system_to_decimal('0x10', 16)  # 16
    # 整形转字符
    print chr(65), chr(90), chr(97), chr(122)  # A Z a z
    # 字符转整形
    print ord('A'), ord('Z'), ord('a'), ord('z')  # 65 90 97 122
    # 十进制转二进制
    print bin(0), bin(1), bin(255)  # 0b0 0b1 0b11111111
    # 十进制转八进制
    print oct(0), oct(1), oct(255)  # 0 01 0377
    # 十进制转十六进制
    print hex(0), hex(1), hex(255)  # 0x0 0x1 0xff

if __name__ == "__main__":
    test()
    print system_to_decimal('000000001b2025f6', 16)
    print system_to_decimal('0001000100010001', 2)
    test_unescape()
    test_unicode()


"""
二进制 binary
八进制 octal
十进制 decimal
十六进制 hex
字节 byte

八进制数由前缀0以及后续的0-7的数字来表示。
十六进制适用于所有整数数据类型，以前缀0x或（0X）,后面跟随0-9或小写（或大写）的a-f来表示。
"""