# *_* encoding=utf-8 *_*

import hashlib
import random

body = {"datasrc": "starlight68", "mediaNo": u"\u6e1dA90X11", "parkNo": "ZP00001", "rsv1": "", "rsv2": ""}
T = "1c41e43dee735ad7921cb816b5d248e4"
print T
body1 = {"parkNo": "ZP0001", "datasrc": "starlight68", "mediaNo": u"浙A88888", "rsv2": "", "rsv1": ""}

print "1d8ce6e88d94b690c343532a91e7a681"


def key(body):
    s = "qwe123fgh765cvbi76gvbn67sdbyhjkrbfhgjk89pcvmn69sdflkjsdzdsfj0934jsdnzxck0sdij034"
    l = sorted(body.keys())
    for c in l:
        s += body[c].encode("utf8")
    print s
    r = hashlib.md5(s).hexdigest()
    print r


key(body)
key(body1)

a = {"header": {"versionNo": "3.0.0", "transCode": "10711001", "accessType": "02", "reqChannel": "107",
                "desChannel": "127", "reqDateTime": "20171010181359", "respDateTime": "",
                "reqSeqNo": "338b276e44ac37af437522d90bb0f63d", "respSeqNo": "", "rsv1": "", "rsv2": "", "rsv3": ""},
     "body": {"datasrc": "starlight68", "mediaNo": u"\u6e1dA90X11", "parkNo": "ZP00001", "rsv1": "", "rsv2": "",
              "dataMac": "1c41e43dee735ad7921cb816b5d248e4"}}
b = {"body": {"parkNo": "ZP0001", "datasrc": "starlight68", "dataMac": "1d8ce6e88d94b690c343532a91e7a681",
              "mediaNo": "\u6d59A88888", "rsv2": "", "rsv1": ""},
     "header": {"respDateTime": "", "reqDateTime": "20171013175052", "accessType": "02", "versionNo": "3.0.0",
                "transCode": "10711001", "desChannel": "127", "reqChannel": "107",
                "reqSeqNo": "00418396affc11e7917700163e000f47", "respSeqNo": "", "rsv3": "", "rsv2": "", "rsv1": ""}}
