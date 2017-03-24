import requests
import pymongo
import json
import re
import time
from multiprocessing.dummy import Pool as ThreadPool
from wxpy import *

S = requests.session()


DATABASE_CLIENT = pymongo.MongoClient('192.168.2.170',27017)
CMS_DATABASE = DATABASE_CLIENT['CMS']
ORDER_COLLECTION = CMS_DATABASE['order']


def login():

    login_data={
        'username':'zhangleilei@eqxiu.com',
        'password':'123456'
    }

    login_url = 'http://max.eqxiu.com/login'
    S.post(login_url,login_data)


def total():
    list_json = 'http://max.eqxiu.com/m/profit/tg/order/list.json'
    parameter = {
        'sortOrder':'asc',
        'pageSize':'100',
        'pageNumber':'1',
        'startTime':'',
        'endTime':'',
        'plan':'',
        'absenseselect':'',
        'status':'13',
        'eqsOrderNo':''
    }
    total = json.loads(S.post(list_json,parameter).text)['total']
    return total

def make_page():
    stop_page = [0,1]
    page = round(total()/100)
    if page in stop_page:
        end_page = 2
        page_list=range(1,end_page)
        return page_list

def start_insert():
    tpool = ThreadPool(5)
    page_list = make_page()
    tpool.map(rows,page_list)

def rows(page):
    list_json = 'http://max.eqxiu.com/m/profit/tg/order/list.json'
    parameter = {
        'sortOrder': 'asc',
        'pageSize': '100',
        'pageNumber': page,
        'startTime': '',
        'endTime': '',
        'plan': '',
        'absenseselect': '',
        'status': '13',
        'eqsOrderNo': ''
    }
    rows = json.loads(S.post(list_json,parameter).text)['rows']
    insert_order(rows)

def insert_order(rows):
    for order in rows:
        if ORDER_COLLECTION.find({'eqsOrderNo':order['eqsOrderNo']}).count() != 0:
            pass
        else:
            if order['xdActual'] == '暂无数据':
                order['xdActual'] = 0
            order['time'] = int(change_time(time.time()))
            order['lock'] = '0'
            order['checkNo'] = 0
            order['createTime'] = int(change_time(order['createTime']))
            ORDER_COLLECTION.insert(order)


def change_time(time):
    _time = str(time)[0:10]
    return _time


def Surplus_xd():
    for i in ORDER_COLLECTION.find():
        if i['xdSurplus'] == '暂无数据':
            pass
            #微信通知


def checkNo():
    for i in ORDER_COLLECTION.find():
        checkNo = i['checkNo']
        i['checkNo'] = checkNo + 1
        del i['_id']
        i['time'] = int(change_time(time.time()))
        ORDER_COLLECTION.insert(i)

def checkNo_len():
    pass
def function_1():
    pass

def send_message():
    pass

def percent_time():
    create_time = []

def percent_xd():
    pass


if __name__ == '__main__':
    login()
    start_insert()
    Surplus_xd()
    checkNo()