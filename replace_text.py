# -*- coding: utf8 -*-

import re

with open("wechat.txt")as f, open("output.txt", "w") as g:
    for i in f.readlines():
        g.write(re.sub(r"^(-?\d+)\s+(.*)\n$", lambda i: "{}: '{}',\n".format(i.group(1), i.group(2)), i))
