# -*- coding: utf8 -*-


# merge 2 sub-arrays of arr
# first array is arr[l, m]
# second array is arr[m+1, r]
def merge(arr, l, m, r):
    n1 = m - l + 1  # the length of sub-array arr[l, m]
    n2 = r - m  # the length of sub-array arr[m, r]
    # slice is making copy of list
    # pay attention to slice syntax when coping list
    L = arr[l:m+1]  # it's m+1 not m
    R = arr[m+1:r+1]  # and it's r+1 not r
    # init for list indexing
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # copy anything left into arr
    # only one of the two will enter while loop
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is left index of arr, that is the beginning.
# r is right index of arr, that is the ending.
def merge_sort(arr, l, r):
    if l < r:
        m = (l+r)/2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


# python -m sorting.006_merge_sort
if __name__ == '__main__':
    from .randlist import random_list
    a = random_list(1, 100, 20)
    print a
    merge_sort(a, 0, len(a)-1)
    print a

