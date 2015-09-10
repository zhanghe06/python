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


def get_first_char(s):
    """
    获取字符串首字母数 (如果是中文 获取拼音首字母)
    """
    if s is None or s == '':
        return ''

    s = s.decode('utf-8', 'ignore')
    # 如果字符串首字符是字母，直接返回
    first_char = ord(s[0].upper())
    # print first_char
    if ord('A') <= first_char <= ord('Z'):
        return s[0].upper()
    # 处理汉字情况
    s = s.encode('gb18030', 'ignore')
    # print len(s)
    if len(s) < 2:
        return ''
    asc = ord(s[0])*256 + ord(s[1])-65536
    if -20319 <= asc <= -20284:
        return 'A'

    if -20283 <= asc <= -19776:
        return 'B'

    if -19775 <= asc <= -19219:
        return 'C'

    if -19218 <= asc <= -18711:
        return 'D'

    if -18710 <= asc <= -18527:
        return 'E'

    if -18526 <= asc <= -18240:
        return 'F'

    if -18239 <= asc <= -17923:
        return 'G'

    if -17922 <= asc <= -17418:
        return 'H'

    if -17417 <= asc <= -16475:
        return 'J'

    if -16474 <= asc <= -16213:
        return 'K'

    if -16212 <= asc <= -15641:
        return 'L'

    if -15640 <= asc <= -15166:
        return 'M'

    if -15165 <= asc <= -14923:
        return 'N'

    if -14922 <= asc <= -14915:
        return 'O'

    if -14914 <= asc <= -14631:
        return 'P'

    if -14630 <= asc <= -14150:
        return 'Q'

    if -14149 <= asc <= -14091:
        return 'R'

    if -14090 <= asc <= -13319:
        return 'S'

    if -13318 <= asc <= -12839:
        return 'T'

    if -12838 <= asc <= -12557:
        return 'W'

    if -12556 <= asc <= -11848:
        return 'X'

    if -11847 <= asc <= -11056:
        return 'Y'

    if -11055 <= asc <= -10247:
        return 'Z'

    return ''


if __name__ == '__main__':
    print is_chinese(u'你好啊')  # True
    print is_chinese(u'你abc')  # True
    print is_chinese(u'abc你')  # False
    print get_first_char('abc你')  # A
    print get_first_char('q')  # Q
    print get_first_char('你好')  # N
