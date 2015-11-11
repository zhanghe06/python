# encoding: utf-8
__author__ = 'zhanghe'


def data_filter(source_str, return_type='str'):
    """
    数据类型过滤(转换)
    :param source_str:
    :param return_type:
    :return:
    """
    value = ''
    if return_type == 'str':
        try:
            value = str(source_str)
        except ValueError:
            value = ''
    if return_type == 'int':
        try:
            value = int(source_str)
        except ValueError:
            value = 0
    if return_type == 'float':
        try:
            value = float(source_str)
        except ValueError:
            value = 0.0
    return value


def clean_none(data, default=''):
    """
    过滤记录中的None(数据库中的null)
    :param data:
    :param default:
    :return:
    """
    if isinstance(data, list):
        for index in range(len(data)):
            if data[index] is None:
                data[index] = default
    if isinstance(data, dict):
        for key, value in data.items():
            if value is None:
                data[key] = default
    return data


if __name__ == '__main__':
    print data_filter('python', 'float')
    print clean_none(['a', None, 3])
    print clean_none({'a': None, 'b': 2})
    print clean_none({})

"""
数据过滤器
"""