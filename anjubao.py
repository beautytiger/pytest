# *_* encoding=utf-8 *_*

import sys
import os
import logging
import json
import urlparse
import random
import hmac
import uuid
import time
import requests
from hashlib import sha1
import datetime
from collections import OrderedDict

class AnJuBao(object):

    def __init__(self, plate_no=u'粤J00001'):
        self.plate_no = plate_no
        # url should be something like this:
        # http://tianhuanwechatapi.test.dyajb.com/
        self.__url = u'http://tianhuanwechatapi.test.dyajb.com'
        # 商场代码， 对应安居宝的secretId
        self.__appid = u'bcc7fdfe586e48228421da4fc46156090'
        # 商场的key, 对应安居宝的secretKey
        self.__secret = u'anjubaotest'
        # 停车场代码
        self.__parkid = u'20053310001'

    def __key(self, ordered_data, command):
        concat_str = ''
        for k, v in ordered_data.iteritems():
            concat_str += (k + '=' + v +'&')
        concat_str = urlparse.urljoin(self.__url, command) + '?' + concat_str[:-1]
        print 'concat string:{}'.format(concat_str.encode('utf8'))
        sec_key = self.__secret.encode('utf8')
        concat_str = concat_str.encode('utf8')
        hashed = hmac.new(sec_key, concat_str, sha1)
        self.h = hashed
        print hashed.hexdigest()
        base64_hashed = hashed.hexdigest().encode('base64').rstrip('\n')
        print "base64 hashed string:{}".format(base64_hashed)
        return base64_hashed

    @staticmethod
    def _gen_order_num():
        return 'AJB000' + str(int(time.time()*1000)) + '{:03}'.format(random.randint(0, 999))

    def _common_data(self):
        data = dict([
            ("secretId", self.__appid),
            ("parkCode", self.__parkid),
            ("timeStamp", str(int(time.time()))),
        ])
        return data

    @staticmethod
    def _sorted_data(data):
        ordered_data = OrderedDict()
        for key in sorted(data):
            ordered_data[key] = data[key]
        return ordered_data

    def _query_data_by_plate(self):
        data = self._common_data()
        data["carNo"] = self.plate_no
        return self._sorted_data(data)

    def _create_order_data(self, trade_no, value):
        data = self._common_data()
        data['carNo'] = self.plate_no
        data['tradeNo'] = trade_no
        data['value'] = value
        return self._sorted_data(data)

    def _pay_data(self, trade_num):
        data = self._common_data()
        data["tradeNo"] = trade_num
        data["payType"] = "1"
        data["payTime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self._sorted_data(data)

    def query(self):
        command = '/SQ-Charge/GetCost'
        query_data = self._query_data_by_plate()
        query_data['signature'] = self.__key(query_data, command)
        print query_data
        code, result = self.__Post(command, query_data)
        print code, result
        return

    def create_order_num(self, tradeNo, amount):
        command = '/SQ-Order/Place'
        create_data = self._create_order_data(tradeNo, amount)
        create_data['signature'] = self.__key(create_data, command)
        print create_data
        code, result = self.__Post(command, create_data)
        print code, result
        return code, result

    def pay_by_order(self, amount):
        tradeNo = self._gen_order_num()
        # 先创建一个缴费订单
        code, result = self.create_order_num(tradeNo, amount)
        if code is not 0:
            return -2, result
        if result['status'] is False:
            return -1, result['msg']
        # 接下才才是正式的停车场确认缴费流程
        command = '/SQ-Order/Confirm'
        pay_data = self._pay_data(tradeNo)
        pay_data['signature'] = self.__key(pay_data, command)
        print pay_data
        code, result = self.__Post(command, pay_data)
        print code, result
        return

    def __Post(self, command, data):
        url = urlparse.urljoin(self.__url, command)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        print "url", url
        # data = json.dumps(data)
        print "data", data
        # data = dict(data)
        # data = self.to_utf8(data)
        # print "data!!!", data
        try:
            resp = requests.post(url, data=data, headers=headers, timeout=5)
            self.r = resp
        except Exception as e:
            print e
            return -2, u"连接失败"
        if resp.status_code != 200:
            return -2, resp.text
        try:
            ret = resp.json()
        except Exception, e:
            return -1, e
        return 0, ret

    @staticmethod
    def to_utf8(data):
        for k, v in data.iteritems():
            if isinstance(v, unicode):
                data[k] = v.encode('utf8')
        return data

    def __Get(self, command, data):
        url = urlparse.urljoin(self.__url, command)
        # headers = {'content-type': 'application/json; charset=utf-8'}
        print "url", url
        # data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        print "data", data
        data1 = dict(data)
        print "data!!!", data1
        try:
            resp = requests.get(url, params=data1)
            self.r = resp
        except Exception as e:
            print e
            return -2, u"连接失败"
        if resp.status_code != 200:
            return -2, resp.text
        try:
            ret = resp.json()
        except Exception, e:
            return -1, e
        return 0, ret
