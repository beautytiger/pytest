# -*- coding: utf8 -*-

import requests
import json
from requests.auth import HTTPBasicAuth

url1 = 'http://sjjy.andoner.cn/services/parking/member/info?cardNo=9000000530&plateNo=京A9999'
url1 = 'http://wx.yanlordcd.com/services/parking/member/info?cardNo=9000000530&plateNo=京A9999'
r1 = requests.get(url1, auth=('wxmall', 'wxmall'))

url2 = 'http://wx.yanlordcd.com/services/parking/clearance'
datas = {
'cardNo':'8600104665',
'plateNo':'川A111BQ',
'freeparking':1800,
'coupons':[{"code":"C150157784698","fee":1200}]
}
datas = json.dumps(datas)
r2 = requests.post(url2, data=datas, auth=('wxmall', 'wxmall'))

http://wx.yanlordcd.com/services/parking/member/info
http://wx.yanlordcd.com/services/parking/clearance
