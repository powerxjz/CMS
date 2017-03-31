import os
import time
import pymongo
import requests
import json
record_data = {
    "_id" : "58705cb9d122d80f56c672af",
    "times" : "2017-01-07 11:12:57",
    "type" : "前置审核",
    "log" : [
        {
            "words" : '',
            "description" : "场景定制联系微信：tbg145",
            "publishTime" : 1483758767000,
            "createUser" : "ex10731134444123",
            "status" : '',
            "isReCheck" : '',
            "id" : 70334414,
            "links" : '',
            "code" : "QCl1Xy4F",
            "cover" : "o_1b4sf4ijs1apk1aoqfh01h7152u9.jpg",
            "totalPv" : 23,
            "pv" : 23,
            "reportTitle" : '',
            "reportNum" : 0,
            "name" : "【新春年会】大红阔气 传统风格",
            "joinTime" : 1483758768000,
            "userType" : 4,
            "isWorry" : '',
            "bizType" : 0,
            "type" : 1,
            "memberType" : ''
        }
    ]
}
def ring():
    api = 'https://oapi.dingtalk.com/robot/send?access_token=b20ccdca0f204af402207fe9901410c6c6ffe6bfd13cdbb9844aecb72cf7e03b'
    headers = {'content-type':'application/json',
               'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    con = {
        "msgtype":"text",
        "text":{
            "content":"召唤神兽"
        },
        "at":{
            "atMobiles":[
                "18782980480",
                "13154411666",
                "15108355293",
                "18682737460"

            ]
        }
    }
    requests.post(api, json.dumps(con), headers=headers)
def send_message(message):
    ring()
    api = 'https://oapi.dingtalk.com/robot/send?access_token=b20ccdca0f204af402207fe9901410c6c6ffe6bfd13cdbb9844aecb72cf7e03b'
    headers = {'content-type':'application/json',
               'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    context = {
        "msgtype":"markdown",
        "markdown":{
            "title":"前置审核",
            "text":"### 业务提醒\n" +
                   "** 业务来源:{}**\n\n".format(message['type']) +
                   "** 申请时间:{}**\n\n".format(message['times']) +
                   "** 场景标题: {}**\n".format(message['log'][0]['name'])

        }
    }
    requests.post(api, json.dumps(context), headers=headers)

send_message(record_data)