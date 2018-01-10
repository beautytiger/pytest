# -*- coding: utf8 -*-

from line_num import PrintFrame

PrintFrame()

print '-'*15

PrintFrame(__file__)

print '-' * 15


def testing():
    PrintFrame()
    print '-' * 15
    PrintFrame(__file__)

testing()
