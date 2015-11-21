# encoding: utf-8
"""
大数运算的实现
"""
__author__ = 'zhanghe'


def add(x, y):
    """
    加法
    """
    result = [int(p)+int(q) for i_p, p in enumerate(('0'*(max(len(x), len(y))-len(x))+str(x))[::-1]) for i_q, q in enumerate(('0'*(max(len(x), len(y))-len(y))+str(y))[::-1]) if i_p == i_q]
    for index, v in enumerate(result):
        if v >= 10:
            result[index], k = v % 10, v / 10
            if index+1 < max(len(str(x)), len(str(y))):
                result[index+1] += k
            else:
                result.append(k)
    return ''.join([str(i) for i in result][::-1])


def multiply(x, y):
    """
    乘法
    """
    i, result = 0, '0'
    for m in [int(m) for m in x][::-1]:
        k, t = 0, []
        t.extend([0]*i)
        for n in [int(n) for n in y][::-1]:
            t.append((int(m)*int(n)+k) % 10)
            k = (int(m)*int(n)+k) / 10
        i += 1
        if k > 0:
            t.append(k)
        result = add(result, ''.join([str(item) for item in t[::-1]]))
    return result


def test_add():
    """
    加法测试
    """
    # 连续进位
    a = '8838'
    b = '3968'
    print add(a, b)
    print int(a)+int(b)

    a_1 = '821111111111111181'
    b_1 = '94222222222222226200'
    print add(a_1, b_1)
    print int(a_1)+int(b_1)

    a_2 = '8211111111111333311181'
    b_2 = '94222222222222226200'
    print add(a_2, b_2)
    print int(a_2)+int(b_2)

    # 和的长度超过原始数值
    a_3 = '82111111111116611181'
    b_3 = '94222222222222226200'
    print add(a_3, b_3)
    print int(a_3)+int(b_3)


def test_multiply():
    """
    乘法测试
    """
    a_1 = '821111111111111181'
    b_1 = '94222222222222226200'
    print multiply(a_1, b_1)
    print int(a_1)*int(b_1)

    a_2 = '8211111111111333311181'
    b_2 = '94222222222222226200'
    print multiply(a_2, b_2)
    print int(a_2)*int(b_2)

    a_3 = '82111111111116611181'
    b_3 = '94222222222222226200'
    print multiply(a_3, b_3)
    print int(a_3)*int(b_3)

if __name__ == '__main__':
    test_add()
    test_multiply()