# *_* encoding=utf-8 *_*

import datetime


class DataBaseRecord(object):

    def __init__(self, rec_list):
        (self.wechatpayid,
        self.lamicpayid,
        create_date,
        modify_date,
        paytime,
        amount,
        self.coupon_num,
        self.phone,
        name,
        self.card_num,
        refund,
        coupon_name) = rec_list
        self.create_date = datetime.datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S.%f")
        self.modify_date = datetime.datetime.strptime(modify_date, "%Y-%m-%d %H:%M:%S.%f")
        self.paytime = datetime.datetime.strptime(paytime, "%Y%m%d%H%M%S")
        self.amount = float(amount)
        self.name = name.decode("utf8")
        self.refund = True if refund == "1" else False
        self.copon_name = coupon_name.decode("utf8")

    def __str__(self):
        return "{}: {}".format(self.name.encode("utf8"), self.coupon_num)

    def __repr__(self):
        return "{}: {}".format(self.name.encode("utf8"), self.coupon_num)


class LamiRecord(object):

    def __init__(self, rec_list):
        self.lamicpayid = rec_list[0]
        self.amount = float(rec_list[3])
        paytime = rec_list[-2].strip()
        self.paytime = datetime.datetime.strptime(paytime, "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return "{}: {}".format(self.lamicpayid, self.amount)

    def __repr__(self):
        return "{}: {}".format(self.lamicpayid, self.amount)


class LamiRefund(object):
    def __init__(self, rec_list):
        self.lamicpayid = rec_list[0]
        self.amount = float(rec_list[3])
        refundtime = rec_list[-1].strip()
        self.refundtime = datetime.datetime.strptime(refundtime, "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return "{}: {}".format(self.lamicpayid, self.amount)

    def __repr__(self):
        return "{}: {}".format(self.lamicpayid, self.amount)

database = []
# 仁恒数据库记录的所有现金券成功交易
with open("renheng_coupon.csv", "r") as coupon:
    for line in coupon.readlines():
        split_line = line.strip().split(",")
        c = DataBaseRecord(split_line)
        database.append(c)

lami = []
with open("renheng_all.csv", "r") as coupon:
    for line in coupon.readlines():
        split_line = line.strip().split(",")
        c = LamiRecord(split_line)
        lami.append(c)

lami_refund = []
with open("renheng_refund.csv", "r") as coupon:
    for line in coupon.readlines():
        split_line = line.strip().split(",")
        c = LamiRefund(split_line)
        lami_refund.append(c)

# 检查60元券
# 检查所有payid是否在莱米中存在
# 不存在则为失败支付。
fail_ids = []
payids = [i.lamicpayid for i in lami if i.amount == 60]
for i in database:
    if i.amount == 60 and i.lamicpayid not in payids:
        fail_ids.append(i.lamicpayid + "\n")

with open("failsinlami60.txt", "w") as f:
    f.writelines(fail_ids)

# 检查在莱米中存在，但在数据库中不存在的交易
not_exist_ids = []
rh_payids = [i.lamicpayid for i in database if i.amount == 60]
for i in lami:
    if i.amount == 60 and i.lamicpayid not in rh_payids:
        not_exist_ids.append(i.lamicpayid + "\n")

with open("notindatabase.txt", "w") as f:
    f.writelines(not_exist_ids)

# 找出那些已经在数据库中显示为failed记录
found = set()
with open("a.csv", "r") as a:
    with open("fail_ids.csv", "w") as f:
        lines = a.readlines()
        for l in lines:
            for i in fail_ids:
                if i.strip() in l:
                    found.add(i)
                    f.write(l)
                    break

print len(found) == len(set(fail_ids))

# 找出那些在我们数据库中不存在的记录
notexist_found = set()
with open("a.csv", "r") as a:
    with open("not_exist.csv", "w") as f:
        lines = a.readlines()
        for l in lines:
            for i in not_exist_ids:
                if i.strip() in l:
                    notexist_found.add(i)
                    f.write(l)
                    break

print len(notexist_found) == len(set(not_exist_ids))
