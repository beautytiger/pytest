# -*- coding:utf8 -*-

import requests
import json

# 获取会员当前活动期间的交易信息
url1 = "http://cre.test.hd123.cn:8280/cre-pos/service/coupon/mposcoupon/mulvoucher/getTradingInfo?channel=bigMemberCoupon&memberId=140090371026718720"

response = requests.get(url=url1)
print response.content

# 计算可赠送券信息
url2 = 'http://cre.test.hd123.cn:8280/cre-pos/service/coupon/mposcoupon/mulvoucher/calculateCoupon?channel=bigMemberCoupon'
data = {
    "memberId ": "140090371026718720",
    "cardNumber": "1234567890",
    "cardType": "",
    "gradeCode": "1",
    "tradingInfoList": [
        {
            "pos": u"POS号",
            "flowNo": "1712070037",
            "totalAmt": 48,
            "effectiveAmount": 20,
            "promBill": "3341823106059985812958467824408813201064976862105483780910868108",
            "promName": u"测试促销活动名称"
        }
    ]
}

response = requests.post(url=url2, json=data, headers={'content-type': 'application/json'})
print response.content

# 生成券兑换单
# url3 = 'http://cre.test.hd123.cn:8280/cre-pos/service/coupon/mposcoupon/mulvoucher/couponExchange?channel=bigMemberCoupon'
# data = {
#     "operator": {
#         "uuid": "2c918c8b58bc595f0158bd8701f34d76",
#         "code": "df",
#         "name": "丁枫"
#     },
#     "memberId": "140090371026718720",
#     "cardNo": "140090371026718720",
#     "memberName": "廖志",
#     "phoneNumber": "18616556160",
#     "terminal": "WX",
#     "billType": "exchange",
#     "couponList": [
#         {
#             "couponNum": "M1712040009",
#             "couponTypeCode": "000010",
#             "couponTypeName": "活动卡验证",
#             "startDate": "2017-12-04 12:12:12",
#             "endDate": "2017-12-05 12:12:12",
#             "amount": 15.6
#         }
#     ],
#     "tradingInfoList": [
#         {
#             "pos": "056",
#             "flowNo": "1712070037",
#             "tradingTime": "2017-12-07 15:59:15",
#             "totalAmt": 1677,
#             "promBill": "2c918c075e603eb3015e60ae373a06c0",
#             "promStartTime": "2017-09-08 16:50:47",
#             "promEndTime": "2023-09-10 00:00:00"
#         }
#     ]
# }
#
# response = requests.post(url=url3, json=data, headers={'content-type': 'application/json'})
# print response.content
