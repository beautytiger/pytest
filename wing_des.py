# -*- coding:utf8 -*-

from Crypto.Cipher import DES
from base64 import b64encode


def pad(s):
    return s + (DES.block_size - len(s) % DES.block_size) * chr(DES.block_size - len(s) % DES.block_size)


def des_encrypt(plain_text, key):
    des = DES.new(key[0:8])
    return des.encrypt(pad(plain_text))


result = des_encrypt("123456", "TMPAY8888")
print(result)
print(result.encode('hex_codec'))
print(b64encode(result))
