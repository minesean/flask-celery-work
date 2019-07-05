import json
import time
from flask import Blueprint,request,make_response,jsonify,Response
from api.alg_fake import lip_func,asr_func



blueprint = Blueprint('api',__name__)

@blueprint.route('/lip/',methods=["POST","GET"])
def something_rec():
    print(' * --------------start ------------------------------')
    file_path = request.form.get('file_path',None)
    speechtext = request.form.get('speechtext',None)
    print(file_path,speechtext)

    p1 = lip_func.delay(file_path,speechtext)
    result = p1.get()
    #result = {1:2}
    #time.sleep(2)
    print(" *-------------- finshed -----------------------------")
    response = make_response(json.dumps(result,ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response





"""
from api.alg_fake import lip_func,asr_func


p1 = lip_func.delay("/root","0527")
print(p1.result)
print(p1.get())

from celery_app.task1 import add
#from my import add
import time
from billiard.exceptions import TimeLimitExceeded
from celery.task.control import revoke

p1 = add.delay(2,4)
# task1.add.apply_async(2.4) 这种方法也可以
# task2.multiply.delay(4,5)
# celery worker -A celery_app -l INFO
# python app.py 看一下结果

print(p1)
print(p1.result)

time.sleep(3.55)
print(p1.result)  # 返回结果 result/None
print(p1.ready()) # 返回时候完成 True/False
try:
    # print(p1.get())   # 阻塞获取
    task_id = p1.task_id
    print(task_id)
    #revoke(task_id,terminate=True)
    print(p1.get())   # 阻塞获取
except TimeLimitExceeded as e:
    print(e)
    print(" time out ")
"""
