# encoding: utf-8
__author__ = 'zhanghe'

import os


def check(file_name=None):
    """
    性能检测
    """
    if file_name is None:
        print '请指定文件名称'
    else:
        cmd = "python -m cProfile %s" % file_name
        print cmd
        os.system(cmd)


if __name__ == '__main__':
    check('performance.py')


'''
测试结果：

/home/zhanghe/code/python/pyenv/bin/python /home/zhanghe/code/python/tools/check_profile.py
python -m cProfile performance.py
         807 function calls in 2.960 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      200    0.002    0.000    2.254    0.011 performance.py:12(slow)
        2    0.002    0.001    2.959    1.480 performance.py:16(very_slow)
        1    0.000    0.000    2.960    2.960 performance.py:2(<module>)
        1    0.000    0.000    2.959    2.959 performance.py:23(main)
      200    0.003    0.000    0.501    0.003 performance.py:8(fast)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      402    2.952    0.007    2.952    0.007 {time.sleep}



Process finished with exit code 0
'''