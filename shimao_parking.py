# -*- coding: utf-8 -*-

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wxmall.settings")

import django
django.setup()

from parking.models import ParkingRecord
from weixin.models import WeChatSubscribeUser

rec = ParkingRecord.objects.filter(wxpay__isnull=False)
pays = [i.wxpay for i in rec]

with open("pay.csv") as f:
    lines = f.readlines()
    with open("diff.csv", "w") as d:
        for l in lines:
            mid = l.split(',')[5][1:]  # 交易编号
            inside = False
            for pay in pays:
                if mid in pay:
                    inside = True
                    break
            if not inside:
                print mid
                openid = l.split(',')[7][1:]
                try:
                    user = WeChatSubscribeUser.objetcts.get(openid=openid)
                except Exception as e:
                    d.write(e)
                d.write(l)
print "process ending..."
