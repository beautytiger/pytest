#!/usr/bin/env python3


import hashlib

#
# def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
#     for block in bytesiter:
#         hasher.update(block)
#     return (hasher.hexdigest() if ashexstr else hasher.digest())
#
#
# def file_as_blockiter(afile, blocksize=65536):
#     with afile:
#         block = afile.read(blocksize)
#         while len(block) > 0:
#             yield block
#             block = afile.read(blocksize)
#
#
# [(fname, hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.md5())) for fname in fnamelst]
#
#
#
# def md5(fname):
#     hash_md5 = hashlib.md5()
#     with open(fname, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()

ALGRITHEMS = {'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'}


def checksum(fname=None, blocksize=65536, algr='md5'):
    if fname is None:
        return -1
    if algr not in ALGRITHEMS:
        return -2
    hasher = getattr(hashlib, algr)()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(blocksize), b''):
            hasher.update(chunk)
    return hasher.hexdigest()
