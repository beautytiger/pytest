# -*- coding:utf8 -*-

from Crypto.Cipher import DES
from Crypto.Cipher import DES3

key = 'TMPAY888'
key1 = 'TMPAY8888'
vector = key
msg = '123456'
answer = '831D0C85791F1BCC'
print answer

E = DES.new(key, DES.MODE_CFB, vector)
out = E.encrypt(msg)
print out
out = out.encode('hex_codec')
print out
out = out.encode('base64')
print out

E = DES.new(key, DES.MODE_OPENPGP, vector)
out = E.encrypt(msg)
print out
out = out.encode('hex_codec')
print out
out = out.encode('base64')
print out

E = DES.new(key, DES.MODE_OFB, vector)
out = E.encrypt(msg)
print out
out = out.encode('hex_codec')
print out
out = out.encode('base64')
print out

E = DES.new(key, DES.MODE_CBC, vector)
out = E.encrypt(msg)
print out
out = out.encode('hex_codec')
print out
out = out.encode('base64')
print out

E = DES.new(key)
out = E.encrypt(msg)
print out
out = out.encode('hex_codec')
print out
out = out.encode('base64')
print out

# E = DES.new(key, DES.MODE_OPENPGP, vector)
# out = E.encrypt(msg)
# print 'out:', out
# out = out.encode('hex_codec').encode('base64')
# print 'decode out:', out

# E = DES.new(key, DES.MODE_OFB, vector)
# out = E.encrypt(msg)
# print 'out:', out
# out = out.encode('hex_codec').encode('base64')
# print 'decode out:', out

# # this mode not used anymore
# # E = DES.new(key, DES.MODE_PGP, vector)
# # out = E.encrypt(msg)
# # print 'out:', out
# # out = out.encode('hex_codec').encode('base64')
# # print 'decode out:', out

# E = DES.new(key, DES.MODE_CBC, vector)
# out = E.encrypt(msg)
# print 'out:', out
# out = out.encode('hex_codec').encode('base64')
# print 'decode out:', out

# E = DES3.new(key, DES3.MODE_CFB, vector)
# out = E.encrypt(msg)
# print 'out:', out
# out = out.encode('hex_codec').encode('base64')
# print 'decode out:', out