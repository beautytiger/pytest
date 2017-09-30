# -*- coding: utf8 -*-

from console.models import Mall, GiftCouponStoreList

csv_path = 'store.csv'

stored = GiftCouponStoreList.objects.all()
if stored:
    mall = stored[0].mall
else:
    mall = Mall.objects.filter(enabled=True, name__contains=u"济南")
    mall = mall[0]
stored_code = {i.code for i in stored}

with open(csv_path) as f:
    for i in f.readlines():
        a = i.split(',')
        m = a[0].strip().decode('gbk')  # shop name
        n = a[1].strip().decode('gbk')  # shop code
        if n in stored_code:
            print '-'*30 + '>', m, n
            continue
        print "insert {} {}".format(m, n)
        try:
            GiftCouponStoreList.objects.create(mall=mall, title=m, code=n)
        except Exception:  # IntegrityError
            continue
print "Done!"
