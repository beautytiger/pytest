# -*- coding:utf8 -*-

import requests

user = 'guest'
password = 'guest'
headers = {'content-type': 'application/json'}
url = 'http://120.76.213.253:8888/sms.aspx'
data = {
    "userid": "@@@",
    "account": "@@@",
    "password": "@@@",
    "mobile": "15502111710",
    "content": u"【成都世豪】您的验证码为1234。",
    "action": "send",
    "sendTime": None,
    "extno": None,
}
r = requests.post(url, data=data)

print r.content