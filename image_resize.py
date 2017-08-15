# -*- coding: utf8 -*-
# recursively resize image which width>1024.

import os
from PIL import Image

START_PATH = '/home/ethan/1'
MODE = {'jpg': 'JPEG',
        'jpeg': 'JPEG',
        'png':'PNG',
        }

def gen_file_path(path=START_PATH):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            yield file_path
        else:
            for subf in gen_file_path(path=file_path):
                yield subf

def resize_img(img):
    size = 1000, 1000
    to_save = img
    if any([img.lower().endswith(i) for i in ['.jpg', '.png', '.jpeg']]):
        img = Image.open(img)
        if img.width > 1000 or img.height > 1000:
            img.thumbnail(size, Image.ANTIALIAS)
            try:
                img.save(to_save, MODE[to_save.split('.')[-1].lower()])
            except IOError:
                print "cannot create thumbnail for '%s'" % to_save
                return False
            return True
    return False

def run():
    for image in gen_file_path():
        if resize_img(image):
            print image
    return

if __name__ == "__main__":
    run()