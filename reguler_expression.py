# -*- coding: utf8 -*-

import re

# 汉字, 注意前面不加r而是加u
han = u'[\u4e00-\u9fa5]'
print re.match(han, u"你")

# 车牌
plate = u"^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$"
print re.match(han, u"京A66666")

# 手机号
phone = r"^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$"
print re.match(phone, "13720111234")

# 身份证号
idcard = r"(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)"
print re.match(idcard, "13720111234137201x")

# 邮箱, 下面这个表达式并不准确
mail = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
print re.match(mail, "qq@gmail.com")
