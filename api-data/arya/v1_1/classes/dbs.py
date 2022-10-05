# -*- coding: utf-8 -*-
from arya.v1_1.common import singleton

from flask import g
import time
import pymongo
import pymysql
import redis

@singleton
class DB(object):
    def __init__(self):
        self.mysql = None
        self.redis = None
        self.dot_redis = None
        self.mongo = None
        self.mongo_conn = None

        self.init_connect()

    def __del__(self):
        pass

    def init_connect(self):
        # 连接 mongodb
        self.mongo_conn = pymongo.MongoClient(g.config('host', 'Mongo'), 27017)
        self.mongo = self.mongo_conn[g.config('database', 'Mongo')]
        self.mongo.authenticate(name=g.config('user', 'Mongo'),
                                password=g.config('password', 'Mongo'))

