# -*- coding: utf8 -*-


# the default order is ascending.
def recursive_insertion_sort(li):
    if len(li) == 1:
        return li
    else:
        new_li = recursive_insertion_sort(li[:-1])
        key = li[-1]
        new_li.append(key)
        j = len(li) - 2
        while j >= 0 and key < new_li[j]:
            new_li[j+1] = new_li[j]
            j -= 1
        new_li[j+1] = key
        return new_li


def recursive_insertion_sort2(li, index):
    if index == 0:
        return li
    else:
        recursive_insertion_sort2(li, index-1)
        key = li[index]
        i = index - 1
        while i >= 0 and key < li[i]:
            li[i+1] = li[i]
            i -= 1
        li[i+1] = key
        return li


# python -m sorting.selection_sort
if __name__ == '__main__':
    from .randlist import random_list
    a = random_list(1, 100, 20)
    b = a[:]
    print a
    a = recursive_insertion_sort(a)
    print a
    recursive_insertion_sort2(b, len(b)-1)
    print b

