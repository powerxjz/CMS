import os
import time
import pymongo
import requests
import json
def send_dingding(info):
    api = 'https://oapi.dingtalk.com/robot/send?access_token=b20ccdca0f204af402207fe9901410c6c6ffe6bfd13cdbb9844aecb72cf7e03b'
    headers = {'content-type':'application/json',
               'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    context = {
     "msgtype": "markdown",
     "markdown": {
         "title":"前置审核",
         "text": "### 前置审核\n" +
                 "** 场景标题:{}**\n\n".format('欢迎转发(测试)') +
                 "** 入库时间:{}**\n\n".format(time.time())  +
                 "#### 场景链接 [点击]({})\n".format('http://max.eqxiu.com')
     }
 }
    json_context = json.dumps(context)

    send = requests.post(api, json_context, headers=headers)

    print(send.text)

send_dingding(1)