# coding=utf-8
__author__ = 'zhanghe'


"""
字符处理的工具:
判断unicode是否是汉字，数字，英文，或者其他字符。
全角符号转半角符号。
"""


def is_alphabet(uchar):
    """
    判断一个unicode是否是英文字母
    """
    if (u'\u0041' <= uchar <= u'\u005a') or (u'\u0061' <= uchar <= u'\u007a'):
        return True
    else:
        return False


def is_chinese(uchar):
    """
    判断一个unicode是否是汉字
    """
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


def is_number(uchar):
    """
    判断一个unicode是否是数字
    """
    if u'\u0030' <= uchar <= u'\u0039':
        return True
    else:
        return False


def is_other(uchar):
    """
    判断是否非汉字，数字和英文字符
    """
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False


def b2q(uchar):
    """
    半角转全角
    """
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return unichr(inside_code)


def q2b(uchar):
    """
    全角转半角
    """
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return unichr(inside_code)


def string_q2b(ustring):
    """
    把字符串全角转半角
    """
    return "".join([q2b(uchar) for uchar in ustring])


def uniform(ustring):
    """
    格式化字符串，完成全角转半角，大写转小写的工作
    """
    return string_q2b(ustring).lower()


def string2list(ustring):
    """
    将ustring按照中文，字母，数字分开
    """
    ret_list = []
    u_tmp = []
    for uchar in ustring:
        if is_other(uchar):
            if len(u_tmp) == 0:
                continue
            else:
                ret_list.append("".join(u_tmp))
                u_tmp = []
        else:
            u_tmp.append(uchar)
    if len(u_tmp) != 0:
        ret_list.append("".join(u_tmp))
    return ret_list


if __name__ == '__main__':
    print is_chinese(u'你好啊')  # True
    print is_chinese(u'你abc')  # True
    print is_chinese(u'abc你')  # False
