from arya.v1_1.classes import Logger, getconfig, DB

from flask import Flask, render_template, request, g, make_response
import os, json

def create_app():

    app = Flask(__name__, static_url_path='/v1_1/static')
    app.static_folder = app.root_path + app.static_url_path
    app.template_folder = os.path.join(app.root_path, 'v1_1', 'templates')

    @app.before_request
    def before_request_init():
        if request.method == 'OPTIONS':
            response = {'code': 0, 'msg': '', 'data': 'ok'}
            response = json.dumps(response, default=str)
            response = make_response(response)
            response.headers["Access-Control-Allow-Origin"] = '*'
            response.headers["Access-Control-Allow-Headers"] = '*'
            response.headers["Access-Control-Allow-Method"] = '*' 
            return response
        g.config = getconfig
        g.db = DB()
        g.ip = request.remote_addr
        g.log = Logger(info_log=g.config('info_log', 'Log'),
                       error_log=g.config('error_log', 'Log'),
                       slow_action=g.config('slow_action', 'Log'),
                       level_no=g.config('level_no', 'Log'), client_identification=g.ip) 
    
    #api路由
    from arya.v1_1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')
   
    #显示前端页面路由
    from arya.v1_1 import template as view_blueprint
    app.register_blueprint(view_blueprint, url_prefix='/qyburn')

    return app
