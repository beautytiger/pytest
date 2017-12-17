# -*- coding: utf8 -*-


# 需要检查的文件名以及路径
csv_path = 'store.csv'

codes = []
with open(csv_path) as f:
    for i in f.readlines():
        a = i.strip().split(',')
        codes.append(a[1].strip().decode('utf8'))

for index, code in enumerate(codes):
    if code in set(codes[index + 1:]):
        print "{:03d}: {}".format(index + 1, code)

print "Done!"
