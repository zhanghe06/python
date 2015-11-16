# encoding: utf-8
__author__ = 'zhanghe'


bb = {'001': 'a', '000000002': 'bbbbbb', '0003': 'c', '0000004': 'ddd'}

for a, b in bb.items():
    print('%-20s: %s' % (a, b))


def print_fill_with():
    input_str_list = [
        "abc",
        "abcd",
        "abcde",
    ]

    for eachStr in input_str_list:
        # print '{:->10}'.format(eachStr)
        print '{0:->10}'.format(eachStr)
        # -------abc
        # ------abcd
        # -----abcde

    for eachStr in input_str_list:
        print '{0:-<20}'.format(eachStr)
        # abc-----------------
        # abcd----------------
        # abcde---------------

    for eachStr in input_str_list:
        print '{0:*^30}'.format(eachStr)
        # *************abc**************
        # *************abcd*************
        # ************abcde*************


if __name__ == "__main__":
    print_fill_with()

    a = '好长的汉字啊一定是...'
    b = '影视/媒体/艺术/文化'

    print len(a)
    print len(a.decode('utf-8'))
    print len(b.decode('utf-8'))