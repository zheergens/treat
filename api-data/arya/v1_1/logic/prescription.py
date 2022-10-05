from arya.v1_1.dao import *

def prescriptionAdd(data):
    dprescriptionAdd(data)
    return

def prescriptionIndexes():
    res = dprescriptionIndexes()
    return res

def prescriptionFetch(key, value, page):
    data = dprescriptionFetch(key, value, page)
    return list(data)
