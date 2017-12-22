# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CommonBaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="record create time")
    modidy_time = models.DateTimeField(auto_now=True, verbose_name="record latest modify time")
    remark = models.CharField(max_length=64, verbose_name="remark about this record")

    class Meta:
        abstract = True


class WeChatApp(CommonBaseModel):

    title = models.CharField(max_length=32, verbose_name="wechat title")
    appid = models.CharField(max_length=64, null=False, db_index=True, verbose_name="wechat appid")
    appsecret = models.CharField(max_length=128, verbose_name="wechat appsecret")

    class Meta:
        unique_together = (("appid", "appsecret"), )


class AccessTokenManager(CommonBaseModel):

    belong_to = models.PositiveIntegerField(unique=True, db_index=True, verbose_name="which wechat app does the access token belongs to")
    access_token = models.CharField(max_length=512, verbose_name="wechat access token")
    expire_in = models.PositiveIntegerField(default=7200, verbose_name="how long will access token expires in seconds")
    expire_time = models.TimeField(verbose_name="wechat access token expire time in utc")
