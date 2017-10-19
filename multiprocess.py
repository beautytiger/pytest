# -*- coding: utf8 -*-

import multiprocessing as mp
import random
import time

# this code pieces show that no-thought data sharing in multiprocessing is not safe at all.

RECORD_SET = set()


def check_inside(key):
    if key in RECORD_SET:
        return True
    print len(RECORD_SET)
    RECORD_SET.add(key)
    return False


def func(len):
    out = []
    for i in range(len):
        time.sleep(0.001)
        i = random.randrange(0, 100)
        if check_inside(i):
            continue
        else:
            out.append(i)
    return out


def main():
    pool = mp.Pool()
    inputs = [10 for i in range(100)]
    start = time.time()
    total_successes = pool.map(func, inputs)  # Returns a list of lists
    duration = time.time()-start
    print duration
    print total_successes
    flatten = []
    for i in total_successes:
        for j in i:
            flatten.append(j)
    print len(flatten)
    print len(set(flatten))


if __name__ == "__main__":
    main()
