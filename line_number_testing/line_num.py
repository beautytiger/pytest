# -*- coding: utf8 -*-

import inspect


def PrintFrame(file=None):
    callerframerecord = inspect.stack()[1]  # 0 represents this line
    # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print info.filename  # __FILE__     -> Test.py
    if file:
        print file
    else:
        print __file__
    print info.function  # __FUNCTION__ -> Main
    print info.lineno  # __LINE__     -> 13


def main():
    PrintFrame()


if __name__ == '__main__':
    main()
