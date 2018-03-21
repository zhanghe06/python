# encoding: utf-8
__author__ = 'zhanghe'


import socket


def get_host_ip():
    """
    通过 UDP 获取本机 IP
    在 shell 中可以一行调用，获取到本机IP
    python -c "import socket;print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])"
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def get_local_ip_list():
    """
    获取本地ip地址
    """
    import os
    cmd = "LC_ALL=C ifconfig | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'"
    # result = os.system(cmd)
    result = os.popen(cmd).read()
    ip_list = result.strip().split('\n')
    return ip_list


def check_ip(ipaddr):
    """
    校验IP地址正确性
    :param ipaddr:
    :return:
    """
    addr = ipaddr.strip().split('.')  # 切割IP地址为一个列表
    if len(addr) != 4:  # 切割后列表必须有4个参数
        return False
    for ip in addr:
        if ip < 0 or ip > 255:
            return False
    return True


def check_local_ip(ip):
    """
    检测是否为本地ip
    :param ip:
    :return:
    """
    ip_list = get_local_ip_list()
    if ip in ip_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print(get_local_ip_list())
    print(get_host_ip())
