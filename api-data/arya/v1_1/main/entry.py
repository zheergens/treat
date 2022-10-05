from arya.v1_1 import api
from arya.v1_1.classes import DB

from flask import render_template, request, g

@api.after_app_request
def after_app_request(response):
    return response

@api.route('/<name>', methods=['POST'])
def api(name: str) -> str:
    g.log.outside_error('tesy')
    return g.ip
