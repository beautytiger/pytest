# -*- coding: utf8 -*-

import os
import sys

ROOT = "/"


def parse_dir_content(path=ROOT):
    if os.path.isdir(path):
        files = dict()
        dirs = list()
        others = list()
        for i in os.listdir(path):
            full_path = os.path.join(path, i)
            if os.path.isfile(full_path):
                files[i] = file_size(full_path)
            elif os.path.isdir(full_path):
                dirs.append(i)
            else:
                others.append(i)
        print "files:", files
        print "dirs:", dirs
        print "others:", others
    else:
        print "error input of path!"


# https://stackoverflow.com/questions/2104080/how-to-check-file-size-in-python
def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


if __name__ == "__main__":
    # you may ry run this script like this:
    # python tree_like.py ....
    params = sys.argv
    target_dir = params[-1]
    if len(params) == 1 and target_dir == __file__:
        parse_dir_content()
    else:
        parse_dir_content(target_dir)
