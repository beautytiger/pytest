# -*- coding: utf8 -*-


# the default order is ascending.
def selection_sort(target):
    for i in xrange(len(target)):
        for j in xrange(i+1, len(target)):
            if target[i] > target[j]:
                target[i], target[j] = target[j], target[i]
    return target


def selection_sort2(target):
    for i in xrange(len(target)):
        index = i
        for j in xrange(i+1, len(target)):
            if target[index] > target[j]:
                index = j
        target[index], target[i] = target[i], target[index]
    return target


# https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py
# run this script below to kill exception of ValueError
# python -m sorting.001_selection_sort
if __name__ == '__main__':
    from .randlist import random_list
    a = random_list(1, 100, 100)
    b = a[:]
    print a
    selection_sort(a)
    print a
    selection_sort2(b)
    print b

