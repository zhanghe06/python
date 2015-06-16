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
    print bin(0), bin(1), oct(255)  # 0b0 0b1 0377
    # 十进制转十六进制
    print bin(0), bin(1), hex(255)  # 0b0 0b1 0xff

if __name__ == "__main__":
    test()


"""
二进制 binary
八进制 octal
十进制 decimal
十六进制 hex
字节 byte

八进制数由前缀0以及后续的0-7的数字来表示。
十六进制适用于所有整数数据类型，以前缀0x或（0X）,后面跟随0-9或小写（或大写）的a-f来表示。
"""