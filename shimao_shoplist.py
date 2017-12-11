# -*- coding: utf8 -*-

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wxmall.settings")
import django

if django.VERSION >= (1, 7):
    django.setup()

from console.models import Mall, GiftCouponStoreList

# 世茂济南满赠券商户列表
csv_path = 'store.csv'
# 整体更新商户列表
# 首先清空现有商户列表
print "delete existing records"
GiftCouponStoreList.objects.all().delete()

# 找到济南世茂这个商场
mall = Mall.objects.filter(enabled=True, name__contains=u"济南")
mall = mall[0]

with open(csv_path) as f:
    for i in f.readlines():
        a = i.strip().split(',')

        # windows excel导出的一般是gbk编码，
        # title = a[0].strip().decode('gbk')  # shop name
        # code = a[1].strip().decode('gbk')  # shop code

        # 文件最好还是转化为utf8格式的再进行操作
        title = a[0].strip().decode('utf8')  # shop name
        code = a[1].strip().decode('utf8')  # shop code

        print "insert {} {}".format(title, code)
        GiftCouponStoreList.objects.create(mall=mall, title=title, code=code)

print "Done!"
