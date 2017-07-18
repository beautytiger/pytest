# -*- coding: utf8 -*-

import requests
import json
from requests.auth import HTTPBasicAuth

url1 = 'http://127.0.0.1:8000/service/parking/member/info?phone=15502111710'
r1 = requests.get(url1, auth=('goodday', 'goodday'))

url2 = 'http://127.0.0.1:8000/service/parking/clearance'
datas = {
    'coupons':[
        {
        'code':'CPI201708030121',
        'fee': 1000
    },
        {
        'code':'CPI201709050667',
        'fee': 500
    },
    ],
    'freeparking':500
}
datas = json.dumps(datas)
r2 = requests.post(url2, data=datas, auth=('goodday', 'goodday'))