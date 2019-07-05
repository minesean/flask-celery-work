import os

from flask import Flask
from flask_cors import CORS


def create_app():
    if not os.path.isdir('uploads'):
        os.makedirs('uploads')
    app = Flask(__name__)
    CORS(app)                                 # 解决跨域调用问题
    setup_blueprints(app)                     # 注册蓝图
    return app


def cleanup_app(): #清理app,如果需要
    return


def setup_blueprints(app):
    """
    注册蓝图
    """
    from api import blueprint as alg_api

    blueprints = [ 
            {'handler':alg_api , 'url_prefix' : '/api'}
    ] 

    for bp in blueprints:
        app.register_blueprint(bp['handler'],url_prefix = bp['url_prefix'])