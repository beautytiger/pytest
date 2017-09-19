# -*- coding: utf8 -*-

import random


def no_repeat_random_list(start=1, length=1000):
    target = range(start, start+length)
    random.shuffle(target)
    return target


def random_list(start=1, end=1000, length=1000):
    target = []
    for i in range(length):
        target.append(random.randrange(start, end))
    return target
