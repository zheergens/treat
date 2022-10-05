from arya.v1_1 import template
from arya.v1_1.logic import *
from flask import render_template, request, g, make_response
import json
import time

@template.route('/', methods=['POST', 'GET', 'OPTIONS'])
def index():
    response = {'code': 0, 'msg': '', 'data': 'ok'}
    response = json.dumps(response, default=str)
    response = make_response(response)
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Access-Control-Allow-Headers"] = '*'
    response.headers["Access-Control-Allow-Method"] = '*'
    return response

@template.route('/prescription/u', methods=['POST', 'GET', 'OPTIONS'])
def prescribing():
    data = dict(
        user_name=request.args.get('user_name', type=str, default=''),                                   #姓名
        carded=request.args.get('carded', type=str, default=''),                                         #身份证
        sex=request.args.get('sex', type=str, default=0),                                                #性别
        age=request.args.get('age', type=int, default=0),                                                #年龄
        hospital=request.args.get('hospital', type=str, default=''),                                     #就诊医院
        address=request.args.get('address', type=str, default=''),                                       #住址
        phone_num=request.args.get('phone_num', type=str, default=''),                                   #电话号
        department=request.args.get('department', type=str, default=''),                                 #科别
        medical_certificate_number=request.args.get('medical_certificate_number', type=str, default=''), #医疗证号
        date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))),                       #日期
        diagnosis=request.args.get('diagnosis', type=str, default=''),                                   #临床诊断
        prescription=request.args.get('prescription', type=str, default=''),                             #药方
        physician=request.args.get('physician', type=str, default=''),                                   #医师
        pharmacist=request.args.get('pharmacist', type=str, default=''),                                 #调药药师
        toll_collector=request.args.get('toll_collector', type=str, default=''),                         #收费员
        reviewed=request.args.get('reviewed', type=str, default=''),                                     #审核
        drug_fee=request.args.get('drug_fee', type=float, default=0),                                    #药费
        inspection_fee=request.args.get('inspection_fee', type=float, default=0),                        #检查费
        disposal_fee=request.args.get('disposal_fee', type=float, default=0),                            #处置费
        preferential=request.args.get('preferential', type=float, default=0),                            #优惠费用
        created_at=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
    )
    if data['user_name'] != '' and request.method != 'OPTIONS':
      lprescriptionAdd(data)
    response = {'code': 0, 'msg': '', 'data': 'ok'}
    response = json.dumps(response, default=str)
    response = make_response(response)
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Access-Control-Allow-Headers"] = '*'
    response.headers["Access-Control-Allow-Method"] = '*'
    return response

@template.route('/index/c', methods=['POST'])
def prescribingIndex():
    response = lprescriptionIndexes()
    return json.dumps(response)

@template.route('/prescription/c', methods=['POST', 'GET', 'OPTIONS'])
def prescriptionFetch():
    key = request.args.get('key', type=str, default='')
    value = request.args.get('value', type=str, default='')
    page = request.args.get('page', type=int, default=0)
    response = lprescriptionFetch(key, value, page) if page >= 0 else []
    response = {'code': 0, 'msg': '', 'data': response}
    response = json.dumps(response, default=str)
    response = make_response(response)
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Access-Control-Allow-Headers"] = '*'
    response.headers["Access-Control-Allow-Method"] = '*'
    return response

@template.route('/login', methods=['POST', 'GET', 'OPTIONS'])
def login():
    param = request.get_json()
    user_name = param.get('username', '')
    password = param.get('password', '')
    if user_name == 'yfadmin' and password == 'yf2019abxy':
      response = {'code': 0, 'msg': '登录成功', 'data': {'username' : user_name, 'uuid': 'user1-uuid', 'name': user_name, 'token': 'asjdasdasdas' + str(int(time.time()))}}
    else:
      response = {'code': 401, 'msg': '用户名密码失败', 'data': {}, 'un': user_name, 'dt': param}
    response = json.dumps(response, default=str)
    response = make_response(response)
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Access-Control-Allow-Headers"] = '*'
    response.headers["Access-Control-Allow-Method"] = '*'
    return response
