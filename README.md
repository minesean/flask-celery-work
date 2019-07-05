
安装项目依赖程序
`pip install -r requirements.txt`


启动worker

`celery worker -A alg -l INFO`



启动flask

`uwsgi --ini uwsgi.ini`



```
测试
cd test
python flalsk_test.py
```



```
注意
···
flask多单线程访问 celery  会触发错误。
使用uwsgi代理flask,保证flask中线程只处理一个请求。
···


uwsgi.ini
processes = 4 # 4进程
threads = 1   # 每个进程1个线程
```

