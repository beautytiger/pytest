# -*- coding: utf8 -*-


# the default order is ascending.
def insertion_sort(li):
    for i in xrange(1, len(li)):
        key = li[i]
        j = i-1
        while j >= 0 and key < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key
    return li


if __name__ == '__main__':
    from .randlist import random_list
    a = random_list(1, 100, 20)
    print a
    insertion_sort(a)
    print a
