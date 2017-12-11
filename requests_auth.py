# -*- coding:utf8 -*-

import requests
from requests.auth import HTTPBasicAuth

user = 'guest'
password = 'guest'
headers = {'content-type': 'application/json'}
url = 'http://182.148.108.30:8183/hdcard-services/api/member/query_by_mobilenum?mobilenum=15502111710'
r = requests.get(url, headers=headers, auth=HTTPBasicAuth(user, password))
