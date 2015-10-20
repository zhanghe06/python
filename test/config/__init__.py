# encoding: utf-8
__author__ = 'zhanghe'

import os
# print os.getcwd()
# print os.path.dirname(os.path.abspath(__file__))  # 应该使用这种方式


def get_env():
    """
    获取运行环境
    """
    file_name = '/'.join((os.path.dirname(os.path.abspath(__file__)), 'env.conf'))
    with open(file_name) as f:
        env = f.read()
        if env:
            return env.strip()
        else:
            return ''


def get_config(key=None):
    """
    获取配置文件
    :return:
    """
    config_db = None
    config_proxy = None
    env = get_env()
    if env == 'dev':
        import dev
        config_db = dev.db
        config_proxy = dev.proxy
    if env == 'online':
        import online
        config_db = online.db
        config_proxy = online.proxy
    if key is None:
        return {'db': config_db, 'proxy': config_proxy}
    if key == 'db':
        return config_db
    if key == 'proxy':
        return config_proxy


def set_config():
    pass


# 配置项目
db = get_config('db')
proxy = get_config('proxy')


if __name__ == '__main__':
    print get_config()
    print get_config('db')


"""
环境切换
$ echo 'dev' > test/config/env.conf
$ echo 'online' > test/config/env.conf

使用配置
from config import db
from config import proxy
"""
