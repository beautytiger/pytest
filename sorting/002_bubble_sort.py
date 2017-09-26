# -*- coding: utf8 -*-


# the default order is ascending.
def bubble_sort(target):
    for i in xrange(len(target)):
        for j in xrange(len(target)-1-i):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    return target


# run this script below to kill exception of ValueError
# python -m sorting.002_bubble_sort
if __name__ == '__main__':
    from .randlist import random_list
    a = random_list(1, 100, 100)
    print a
    bubble_sort(a)
    print a
