# -*- coding: utf8 -*-


# the default order is ascending.
def recursive_bubble_sort(li):
    # discard the original list, not breaking it.
    target = li[:]
    if len(target) == 1:
        return target
    else:
        for i in xrange(len(target)-1):
            if target[i] > target[i+1]:
                target[i], target[i+1] = target[i+1], target[i]
        return recursive_bubble_sort(target[:-1]) + [target[-1]]


# index = len(target-1)
def recursive_bubble_sort2(target, index):
    if index == 0:
        return
    else:
        for i in xrange(index):
            if target[i] > target[i+1]:
                target[i], target[i+1] = target[i+1], target[i]
        recursive_bubble_sort2(target, index-1)


# run this script below to kill exception of ValueError
# python -m sorting.003_recursive_bubble_sort
if __name__ == '__main__':
    from .randlist import random_list
    a = random_list(1, 100, 100)
    b = a[:]
    print a
    # this sorting is not in place.
    # I found this break the original list, still, un-ordered
    a = recursive_bubble_sort(a)
    print a
    # this is in place
    recursive_bubble_sort2(b, len(b)-1)
    print b

