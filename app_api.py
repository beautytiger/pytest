# -*- coding: utf8 -*-

import requests
import json


login_url = "http://sm.andoner.cn/services/app/getuid"
coupon_url = "http://sm.andoner.cn/services/coupon/queryanduse"

login_data = {
    "usr": "root",
    "pwd": "root",
}

r1 = requests.post(login_url, json.dumps(login_data), auth=('wxmall', 'wxmall'))

uid = 'e33f31d372fdca4d811570a515ec96118bad125e'
code = "8800000038492588"

query_data = {
    "uid": uid,
    "code": code,
    "use": "0"  # 不重要
}

r2 = requests.post(coupon_url, json.dumps(query_data), auth=('wxmall', 'wxmall'))

code = "8800000038492588"
use_data = {
    "uid": uid,
    "code": code,
    'use': '1'
}

r3 = requests.post(coupon_url, json.dumps(use_data), auth=('wxmall', 'wxmall'))