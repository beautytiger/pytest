# -*- coding: utf8 -*-

import string
import random
import time

CANDIDATE = string.lowercase + string.digits


def uuid_like(length):
    return "".join(random.sample(CANDIDATE, length))


def total_count(length):
    return pow(len(CANDIDATE), length)


def find_twin(length):
    print "starting length: {}".format(length), "-"*20
    start = time.time()
    container = set()
    while True:
        gen_one = uuid_like(length)
        if gen_one in container:
            break
        else:
            container.add(gen_one)
    time_used = time.time() - start
    count_set = len(container)
    all_prob = total_count(length)
    # print "generate same object:    ", gen_one
    # print "time used of looping:    ", "{} s".format(time_used)
    # print "total count generated:   ", count_set
    # print "total count in existing: ", all_prob
    print "percentage of the two:   ", "{}%".format(float(count_set) / all_prob * 100)
    # print "time cost per looping:   ", "{} us".format(time_used / count_set * 10**6)


if __name__ == "__main__":
    for i in range(1, 9):
        find_twin(9)
