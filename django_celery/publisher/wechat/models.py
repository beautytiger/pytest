# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import requests
import json
from collections import namedtuple

from django.db import models

from wechat_status_code import WECHAT_STATUS_CODE as WSC

RESULT = namedtuple("RESULT", "code result message")


class CommonBaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="record create time")
    modidy_time = models.DateTimeField(auto_now=True, verbose_name="record latest modify time")
    remark = models.CharField(max_length=64, verbose_name="remark about this record")

    class Meta:
        abstract = True


class WeChatApp(CommonBaseModel):

    # the url template to get wechat access token
    # https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140183
    WECHAT_ACCESS_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
    # the margin to expire time to refresh access token
    EXPIRE_MARGIN = 60

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
        url = self.WECHAT_ACCESS_TOKEN_URL.format(appid=self.appid, appsecret=self.appsecret)
        response = requests.get(url)
        result = response.json()
        if "errcode" in result:
            return RESULT(result["errcode"], result["errmsg"], WSC.get(result["errcode"], u"未知错误"))
        else:
            self.expire_in = result["expires_in"]
            self.expire_time = int(time.time()) + self.expire_in - self.EXPIRE_MARGIN
            self.access_token = result['access_token']
            self.save()
            return RESULT(0, self.access_token, u"请求成功")


class WeChator(CommonBaseModel):

    # https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140839
    WECHAT_USER_INFO = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={access_token}&openid={openid}&lang=zh_CN"
    BATCH_INFO = "https://api.weixin.qq.com/cgi-bin/user/info/batchget?access_token={access_token}"

    # the user using wechat
    subscribe = models.BooleanField(default=False, verbose_name="is user subscribed the app")
    appid = models.CharField(max_length=64, null=False, db_index=True, verbose_name="wechat appid")
    openid = models.CharField(max_length=128, null=False, db_index=True, verbose_name="wechator openid")
    nickname = models.CharField(max_length=128, default="", verbose_name="wechator nickname")
    sex = models.SmallIntegerField(default=0, verbose_name="user gender. 1:male, 2:famale, 0:secret")
    city = models.CharField(max_length=64, default="", verbose_name="wechator location city")
    country = models.CharField(max_length=64, default="", verbose_name="wechator location, country")
    province = models.CharField(max_length=64, default="", verbose_name="wechator location, province")
    language = models.CharField(max_length=16, default="", verbose_name="user language")
    headimgurl = models.TextField(default="", verbose_name="wechator head image url")
    last_subscribe_time = models.IntegerField(default=0, verbose_name="wechator last subscribe time")
    unionid = models.CharField(max_length=128, default="", db_index=True, verbose_name="union id for wechator")
    app_remark = models.CharField(max_length=64, default="", verbose_name="app owner remark to wechator")
    groupid = models.IntegerField(default=0, verbose_name="wechat group id")
    tagid_list = models.TextField(default="[]", verbose_name="tag id to this user")

    class Meta:
        unique_together = (("appid", "openid"), )

    @classmethod
    def fetch_wechator_info(cls, appid, access_token, openid):
        url = cls.WECHAT_USER_INFO.format(access_token=access_token, openid=openid)
        response = requests.get(url)
        result = response.json()
        if "errcode" in result:
            return RESULT(result["errcode"], result["errmsg"], WSC.get(result["errcode"], u"未知错误"))
        else:
            created, instance = cls.objects.create_or_get(appid=appid, openid=openid)
            if result.get("subscribe") == 1:
                instance.subscribe = True
                instance.nickname = result["nickname"]
                instance.sex = result["sex"]
                instance.language = result["language"]
                instance.city = result["city"]
                instance.country = result["country"]
                instance.province = result["province"]
                instance.headimgurl = result["headimgurl"]
                instance.last_subscribe_time = result["subscribe_time"]
                instance.unionid = result.get("unionid", "")
                instance.app_remark = result["remark"]
                instance.groupid = result.get("groupid", "")
                # below should be be json object
                instance.tagid_list = json.dumps(result["tagid_list"], "[]")
            else:
                instance.subscribe = False
            instance.save()
            return RESULT(0, instance, u"请求成功")

    @classmethod
    def batch_update_wechator_info(cls):
        for i in cls.objects.values("appid").annotate(count=models.Count("appid")):
            appid = i["appid"]
            access_token = WeChatApp.objects.get(appid=appid).get_access_token()
            data = {"user_list": []}
            for j in cls.objects.filter(appid=appid).values("appid", "language"):
                data["user_list"].append(j)
                if len(data["user_list"] < 100):
                    continue
                else:
                    cls._batch_update(appid, access_token, data)
                    data = {"user_list": []}
            if data["user_list"] != []:
                cls._batch_update(appid, access_token, data)

    @classmethod
    def _batch_update(cls, appid=None, access_token=None, data=None):
        url = cls.BATCH_INFO.format(access_token=access_token)
        response = requests.post(url, data=data)
        result = response.json()
        if "error_code" in result:
            return False
        else:
            for user in result["user_info_list"]:
                pass
            return True
