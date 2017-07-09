#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import logging
import json
import urlparse
import random
import hmac
import uuid
import urllib
from hashlib import sha1
from datetime import datetime
from collections import OrderedDict


class CarSafe(object):
    '''
    一卡通APP应用接口
    公司:深圳市车安科技发展有限公司
    技术文档版本：Ver1.33 2017-03-20发布
    '''

    name = 'carsafe'
    version = '1.0'
    description = '深圳车安一卡通系统'

    def __init__(self):
        super(CarSafe, self).__init__()

    def set(self, url=None, appid="UT", key="123456", parkid="1"):
        # url should be something like this:
        # http://www.domain_name.com/api.aspx/
        self.__url = url
        # 商场代码
        self.__appid = appid
        # 商场的key
        self.__secret = key
        # 停车场代码
        self.__parkid = parkid

    def __key(self, *args):
        # all the arguments passed in should be str type.
        sign_string = "".join(sorted(args[:-1]))
        sign_string += args[-1]

        print u"sign_string:{}-secret:{}-".format(sign_string, self.__secret)

        if isinstance(self.__secret, unicode):
            sec = self.__secret.encode('utf8')
        else:
            sec = self.__secret
        if isinstance(sign_string, unicode):
            sign_string = sign_string.encode('utf8')

        hashed = hmac.new(sec, sign_string, sha1)
        return hashed.digest().encode('base64').rstrip('\n')

    def _query_data(self):
        data = OrderedDict([
                ("credentialtype", "1"),
                ("credential", u"湘AJN218"),
                ("starttime", "2015-10-21 09:20:00"),
                ("endtime", "2015-10-21 09:50:00")
            ])
        return data

    def _gen_time_stamp(self):
        return "2017-07-06 11:44:51"

    def query(self):
        time_stamp = self._gen_time_stamp()
        random_num = "21"

        query_data = self._query_data()
        data_str = json.dumps(query_data
                              , separators=(',', ':')
                              , ensure_ascii=False
                              )

        key = self.__key(self.__appid, time_stamp, random_num, data_str)
        print "key generated: {}".format(key)
        return

if __name__ == "__main__":
    a = CarSafe()
    a.set()
    a.query()