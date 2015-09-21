# encoding: utf-8
__author__ = 'zhanghe'


# 代理服务配置
proxy_config = {
    'PROXY_A': {'http': 'http://192.168.111.129:8880'},
    'PROXY_B': {'http': 'http://192.168.111.129:8890'},
}

# 绑定出口配置
bind_config = {
    'BIND_A': ('192.168.3.2', 0),
    'BIND_B': ('192.168.3.7', 0),
}


bind_ip = '0.0.0.0'


def get_proxy_info(proxy_key):
    """
    获取代理信息
    :param proxy_key:
    :return:
    """
    return proxy_config.get(proxy_key)


def get_bind_info(bind_key):
    """
    获取绑定信息
    :param bind_key:
    :return:
    """
    return bind_config.get(bind_key)