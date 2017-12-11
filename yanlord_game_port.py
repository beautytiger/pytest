# -*- coding:utf8 -*-

import requests

url1 = "http://renheng.andoner.cn/services/game/member_info"
url2 = "http://renheng.andoner.cn/services/game/result"
url3 = "http://renheng.andoner.cn/services/game/coupons"
appid = "wx9d90b054b95addec"
openid = "ojDdO012jrJFTbcnSm59KyxDUs18"


def get(url, **kwargs):
    response = requests.get(url=url, params=kwargs, auth=('wxmall', 'wxmall'))
    return response.content


def post(url, **kwargs):
    response = requests.post(url=url, data=kwargs, auth=("wxmall", "wxmall"))
    return response.content


# 检查用户是否为会员
print get(url1, appid=appid, openid=openid)

# 检查所有可用的券
print get(url3, appid=appid)

# 生成游戏结果: 积分
print post(url2, appid=appid, openid=openid, point_costed=0, game_name="大转盘", result="win", win_type="point",
           coupon_name=None, point_count=100)

# 生成游戏结果: 券
print post(url2, appid=appid, openid=openid, point_costed=0, game_name="大转盘", result="win", win_type="coupon",
           coupon_name=u"测试餐饮券", point_count=None)
