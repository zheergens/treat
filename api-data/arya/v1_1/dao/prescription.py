from flask import g
import json

#药方写入
def prescriptionAdd(data):
    g.db.mongo.prescription_list.insert(data)
    
    index_dict = dict()
    for k,v in data.items():
        if k not in ['user_name', 'diagnosis', 'carded', 'hospital']:
            continue
        if v != '':
            index_dict[k] = v
    
    if len(index_dict) > 0:
        g.db.mongo.prescription_indexes.update({'index': 'check'}, {'$addToSet': index_dict}, upsert=True)
    g.log.outside_error(index_dict)
    return json.dumps({'code':0, 'msg':'ok'})

#索引提示
def prescriptionIndexes():
    res = g.db.mongo.prescription_indexes.find_one({'index': 'check'},{'_id':0, 'index':0})
    return res 

#查询
def prescriptionFetch(key, value, page):
    res = g.db.mongo.prescription_list.find({key: {'$regex': value}}).skip(page).limit(1)
    return res
