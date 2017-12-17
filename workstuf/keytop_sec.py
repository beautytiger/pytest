#!/usr/bin/env python
# encoding: utf-8

import hmac
import json
import base64
from hashlib import sha1
from collections import OrderedDict

data = OrderedDict([
    ("credentialtype", "1"),
    ("credential", u"湘AJN218"),
    ("starttime", "2015-10-21 09:20:00"),
    ("endtime", "2015-10-21 09:50:00")
])


def gen_key(sec, msg):
    if isinstance(sec, unicode):
        sec = sec.encode('utf8')
    if isinstance(msg, unicode):
        msg = msg.encode('utf8')
    print sec
    print msg
    # msg = msg.replace(" ", "")
    # print msg
    hashed = hmac.new(sec, msg, sha1)
    digest = hashed.digest().encode('base64').rstrip('\n')
    print digest
    b64 = base64.encodestring(hashed.digest()).rstrip('\n')
    print b64
    return 0


def key_(*args):
    # all the arguments passed in should be str type.
    sign_string = "".join(sorted(args[:-1]))
    sign_string += args[-1]
    hashed = gen_key("123456", sign_string)
    return hashed


if __name__ == "__main__":
    data = json.dumps(data, separators=(',', ':'), ensure_ascii=False, encoding="utf8")
    key_("UT", "21", "2017-07-06 11:44:51", data)
