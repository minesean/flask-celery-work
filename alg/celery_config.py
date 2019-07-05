# coding:utf-8

BROKER_URL = 'redis://:cv_lip@localhost:6379/1'                # 任务id存储
CELERY_RESULT_BACKEND = 'redis://:cv_lip@localhost:6379/2'     # 任务结果存储
CELERY_TIMEZONE = 'Asia/Shanghai'                              # 时区，默认UTF

CELERYD_MAX_TASKS_PER_CHILD = 100                              # 每个work执行100个任务就会死掉
#CELERYD_TASK_TIME_LIMIT = 20                                  # 统一超时时间
CELERYD_CONCURRENCY = 4                                        # 并发worker数
CELERYD_FORCE_EXECV = True                                     # 防止死锁


CELERY_IMPORTS = (                                             # 任务模块注册
'alg.some_alg',
)
