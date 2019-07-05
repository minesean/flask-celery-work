from alg import celery
"""
将算法接口封装为 可celery启动。实现异步调用
"""

import time
import random

@celery.task(name='lip_func',time_limit=5)
def lip_func(file_path,speechtext):
    print(file_path)
    print(speechtext)
    time.sleep(2)
    data = {"code":1,"info":"lip ok"}
    return data


@celery.task(name='asr_func',time_limit=5)
def asr_func(x,y):
    data = {"code":2,"info":"asr ok"}
    return data
