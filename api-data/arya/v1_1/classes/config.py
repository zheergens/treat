#-*- coding:utf-8 -*-
import configparser
import json

def getconfig(key, section=''):
   cf = configparser.ConfigParser()   #实例化
   cf.read('/home/online/treat/api-data/arya/v1_1/conf/production.ini', encoding="utf-8")   #读取配置文件
   cf_items = dict(cf.items(section)) if cf.has_section(section)  else {}  #判断SECTION是否存在,存在把数据存入字典,没有返回空字典
   return cf_items.get(key, '')

if __name__ == '__main__':
    print (getconfig('error_log', 'Log'))
    print ('ok')
