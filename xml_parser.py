# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import requests

template = """
<xml><appid><![CDATA[wx6713e3a589eddb88]]></appid>
<attach><![CDATA[惠州佳兆业]]></attach>
<bank_type><![CDATA[CFT]]></bank_type>
<cash_fee><![CDATA[800]]></cash_fee>
<fee_type><![CDATA[CNY]]></fee_type>
<is_subscribe><![CDATA[Y]]></is_subscribe>
<mch_id><![CDATA[1265026601]]></mch_id>
<nonce_str><![CDATA[dQM5D1zmsg0uIb0pPGFGaeo7BHtpMLqR]]></nonce_str>
<openid><![CDATA[otEZ6jvy2amhfSZPGZcLqQoTtsNM]]></openid>
<out_trade_no><![CDATA[95801380c5f711e7877000163e005b80]]></out_trade_no>
<result_code><![CDATA[SUCCESS]]></result_code>
<return_code><![CDATA[SUCCESS]]></return_code>
<sign><![CDATA[5E6E89D91D519D8A416D1704270C2937]]></sign>
<time_end><![CDATA[20170611154332]]></time_end>
<total_fee>500</total_fee>
<trade_type><![CDATA[JSAPI]]></trade_type>
<transaction_id><![CDATA[4002002001201706115266090371]]></transaction_id>
</xml>
"""
#
# root = ET.fromstring(template)
#
# print root
# print root.tag
# print root.attrib
#
# for child in root:
#     print child.tag, child.attrib, child.text
#     print list(child)
#
# print list(root)

url = "http://zd.andoner.cn/parking/th/pay/"
headers = {'Content-Type': 'application/xml'}  # set what your server accepts
res = requests.post(url, data=template, headers=headers)

print res.status_code
print res.content
