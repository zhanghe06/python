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
    # ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
    print [hex(i).lstrip('0x').zfill(2) for i in range(0, 256)]

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