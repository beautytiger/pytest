# -*- coding:utf8 -*-


with open("cardnum.txt") as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        # print line
        phone = line[0]
        # old_cardnum = line[13]
        new_cardnum = line[1]
        print "when phone=", phone, "then", new_cardnum
