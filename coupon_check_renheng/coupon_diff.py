# *_* encoding=utf-8 *_*

database_code = []
with open("allrec2.csv", "r") as f:
    lines = f.readlines()
    for i in lines:
        code = i.split(",")[5][1:-1]
        database_code.append(code)

crm_code = []
with open("crm60.csv", "r") as f:
    lines = f.readlines()
    for i in lines:
        code = i.split(",")[3][1:-1]
        crm_code.append(code)

database_60code = []
with open("coupon2.csv", "r") as f:
    lines = f.readlines()
    for i in lines:
        code = i.split(",")[2][1:-1]
        database_60code.append(code)

# 数据库中没有的crm券号
for i in crm_code:
    if i not in database_60code:
        print i

print "------"
# crm中没有的数据中券号
for i in database_60code:
    if i not in crm_code:
        print i
