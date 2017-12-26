# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import requests
from collections import namedtuple

from django.db import models

from wechat_status_code import WECHAT_STATUS_CODE as WSC

# the url template to get wechat access token
WECHAT_ACCESS_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
# the margin to expire time to refresh access token
EXPIRE_MARGIN = 60

RESULT = namedtuple("RESULT", "code result message")


class CommonBaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="record create time")
    modidy_time = models.DateTimeField(auto_now=True, verbose_name="record latest modify time")
    remark = models.CharField(max_length=64, verbose_name="remark about this record")

    class Meta:
        abstract = True


class WeChatApp(CommonBaseModel):
    # wechat app basic
    title = models.CharField(max_length=32, verbose_name="wechat title")
    appid = models.CharField(max_length=64, null=False, db_index=True, unique=True, verbose_name="wechat appid")
    appsecret = models.CharField(max_length=128, verbose_name="wechat appsecret")

    # accress token related fields
    access_token = models.CharField(default='', max_length=512, verbose_name="wechat access token")
    expire_in = models.PositiveIntegerField(default=7200, verbose_name="how long will access token expires in seconds")
    expire_time = models.PositiveIntegerField(default=0, verbose_name="wechat access token expire time in utc")

    # get local access token if possible
    def get_access_token(self):
        if self.access_token:
            current = int(time.time())
            if self.expire_time <= current:
                return self._fetch_access_token()
            else:
                return RESULT(0, self.access_token, u"请求成功")
        else:
            return self._fetch_access_token()

    # get access token from wechat server
    def _fetch_access_token(self):
        url = WECHAT_ACCESS_TOKEN_URL.format(appid=self.appid, appsecret=self.appsecret)
        response = requests.get(url)
        result = response.json()
        if "errcode" in result:
            return RESULT(result["errcode"], result["errmsg"], WSC.get(result["errcode"], u"未知错误"))
        else:
            self.expire_in = result["expires_in"]
            self.expire_time = int(time.time()) + self.expire_in - EXPIRE_MARGIN
            self.access_token = result['access_token']
            self.save()
            return RESULT(0, self.access_token, u"请求成功")