# encoding: utf-8
"""
python调用linux系统命令获取当前脚本运行内存
"""
__author__ = 'zhanghe'


import os


def test_memory_usage():
    # 获取当前脚本的进程ID
    print os.getpid()

    # 获取当前脚本占用的内存
    # cmd = 'ps -p %s -o rss=' % os.getpid()
    cmd = 'ps -p 6666 -o rss='
    print cmd

    print('\n------system--------')
    result = os.system(cmd)
    print(type(result))
    print(result)

    print('\n------popen--------')
    output = os.popen(cmd)
    result = output.read()
    if result == '':
        memory_usage = 0
    else:
        memory_usage = int(result.strip())
    print(type(memory_usage))
    print(memory_usage)
    memory_usage_format = memory_usage/1000.0

    print '内存使用%.2fM' % memory_usage_format

    raw_input('回车结束程序')


def test_get_local_ip():
    """
    获取本地ip地址
    """
    cmd = "LC_ALL=C ifconfig | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'"
    print cmd
    # result = os.system(cmd)
    result = os.popen(cmd).read()
    print(type(result))
    print(result)
    ip_list = result.strip().split('\n')
    print ip_list
    return ip_list


if __name__ == '__main__':
    # test_memory_usage()
    test_get_local_ip()

"""
测试结果：

8305
回车结束程序

zhanghe@ubuntu:~/code/python$ ps -aux | grep python
root      2473  0.0  0.3  11892  7388 ?        S    19:52   0:02 /usr/bin/python /usr/local/bin/sslocal -c /home/zhanghe/shadowsocks.json
lp        3384  0.0  0.4  30912  9764 ?        S    20:02   0:00 /usr/bin/python /usr/lib/cups/backend/hpfax
zhanghe   4875  0.1  1.7 221536 35248 ?        Rl   20:28   0:12 /usr/bin/python /usr/bin/terminator
zhanghe   8305  0.1  0.1  10760  3796 ?        S    22:41   0:00 /usr/bin/python2.7 /home/zhanghe/code/python/test_system.py
zhanghe   8309  0.0  0.0   6128   824 pts/1    S+   22:41   0:00 grep --color=auto python

zhanghe@ubuntu:~/code/python$ top -p 8305
top - 22:48:27 up  2:56,  3 users,  load average: 1.01, 1.21, 1.26
Tasks:   1 total,   0 running,   1 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.7 us,  0.5 sy,  0.0 ni, 98.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   2063820 total,  1939520 used,   124300 free,    75264 buffers
KiB Swap:  1046524 total,      308 used,  1046216 free.   609820 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 8305 zhanghe   20   0   10760   3800   2152 S   0.0  0.2   0:00.02 python2.7

zhanghe@ubuntu:~/code/python$ ps -p 8418 -o rss='
 3800



LC_ALL=C ifconfig | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'
<type 'str'>
192.168.1.107
192.168.111.129
192.168.1.106

['192.168.1.107', '192.168.111.129', '192.168.1.106']
"""


"""
USER       PID  %CPU    %MEM    VSZ   RSS TTY      STAT    START   TIME COMMAND
解释：
linux 下的ps命令
USER 进程运行用户
PID    进程编号
%CPU 进程的cpu占用率
%MEM 进程的内存占用率
VSZ 进程所使用的虚存的大小，以K为单位。
RSS 进程使用的驻留集大小或者是实际内存的大小，以K为单位。
TTY 与进程关联的终端（tty）
STAT 检查的状态：进程状态使用字符表示的，如R（running正在运行或准备运行）、S（sleeping睡眠）、I（idle空闲）、Z (僵死)、D（不可中断的睡眠，通常是I/O）、P（等待交换页）、W（换出,表示当前页面不在内存）、N（低优先级任务）T(terminate终止)、W has no resident pages
START （进程启动时间和日期）
TIME ;（进程使用的总cpu时间）
COMMAND （正在执行的命令行命令）
NI (nice)优先级
PRI 进程优先级编号
PPID 父进程的进程ID（parent process id）
SID 会话ID（session id）
WCHAN 进程正在睡眠的内核函数名称；该函数的名称是从/root/system.map文件中获得的。
FLAGS 与进程相关的数字标识
"""


"""
os.system 返回为状态
os.popen 返回值可以接收
"""
