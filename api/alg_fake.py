from alg import celery
"""
这个算法是假的，但是需要和alg/some_alg 实现同步，
但是 不需要写入核心代码，只需要封装一个壳子，告诉celery执行名字name的注册函数
关键位 celery.task(name)封装的函数
"""

import time
import random

@celery.task(name='lip_func',time_limit=5)
def lip_func(file_path,speechtext):
    """
    可以什么都不写
    """
    return None


@celery.task(name='asr_func',time_limit=5)
def asr_func(x,y):
    """
    可以什么都不写
    """
    return None