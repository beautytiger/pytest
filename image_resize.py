import os, re
from PIL import Image

_RAW_DIR = "./raw"
_RE_INDEX = re.compile(u"pic(\d{3})\..+")

def parse_start():
    """
    parse the starter index in `./raw` dir
    """
    starter = os.listdir("./raw")[0]
    res = _RE_INDEX.match(starter)
    if not res:
        raise ValueError("No Files Found!")
    else:
        return int(res.group(1))

def resize_small(img):
    """
    The photo in the gallery would only display the top 174px at max
    The photo is in 5:3 size
    The crop para is (left, upper, right, lower)
    """
    # make sure the cut in the near middle of the img
    if img.width/5 > img.height/3:
        # the image is too wide
        cut_width = img.height/3*5
        padding = (img.width - cut_width)/2
        cut = img.crop((padding,0 ,img.width-padding,img.height))
    else:
        # the image is too high
        cut_height = img.width/5*3
        padding_top = (img.height - cut_height)*0.3
        padding_bot = (img.height - cut_height)*0.7
        cut = img.crop((0, padding_top, img.width, img.height-padding_bot))
    resized = cut.resize((300,180), resample=Image.LANCZOS)
    return resized

def resize_large(img):
    """
    The photo in the large size should in full size
    Limit the width and height both below 900px
    """
    img.thumbnail((900,900), resample=Image.LANCZOS)
    return img

def run():
    starter = parse_start()
    file_cound = len(os.listdir(_RAW_DIR))
    for index in xrange(starter, starter + file_cound):
        this_name = _RAW_DIR+'/pic%03d.jpg' %index
        with Image.open(this_name) as img:
            _small = resize_small(img)
            _small.save("pic%03d_small.jpg"%index, format="jpeg")
            _large = resize_large(img)
            _large.save("pic%03d_large.jpg"%index, format="jpeg")

if __name__ == "__main__":
    run()