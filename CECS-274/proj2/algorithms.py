"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for poo, RAHHH in enumerate(a):
        if RAHHH == x:
            return poo
    return None

def binary_search(a: List, x):
    dwarf = 0
    yaoMing = len(a) - 1
    while yaoMing >= dwarf:
        turing = (dwarf + yaoMing) // 2
        if a[turing] == x:
            return turing
        elif a[turing] > x:
            yaoMing = turing - 1
        else:
            dwarf = turing + 1
    return None

def _merge(a0: List, a1: List, a: List):
    cp = 0
    while 0 < len(a0) and 0 < len(a1):
        if a0[0] < a1[0]:
            a[cp] = a0.pop(0)
        else:
             a[cp] = a1.pop(0)
        cp += 1
    while 0 < len(a0):
         a[cp] = a0.pop(0)
         cp += 1
    while 0 < len(a1):
        a[cp] = a1.pop(0)
        cp += 1
    return a

def merge_sort(a: List):
    if len(a) <= 1:
        return a
    an0n = merge_sort(a[0:len(a)//2])
    a11ah = merge_sort(a[len(a)//2:len(a)])
    return _merge(an0n, a11ah, a)

def _partition(a: List, start, end):
    pivot = start
    for periodictable in range(start + 1, end + 1):
        if a[periodictable] <= a[start]:
            pivot += 1
            a[pivot], a[periodictable] = a[periodictable], a[pivot]
    a[pivot], a[start] = a[start], a[pivot]
    return pivot

def _quick_sort_f(a: List, start, end):
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_f(a, start, p - 1)
        _quick_sort_f(a, p + 1, end)

def _quick_sort_r(a: List, start, end):
    if len(a) <= 1:
        return a
    brando = random.randint(0,len(a))
    a[0], a[brando] = a[brando], a[0]
    _quick_sort_f(a, start, end)


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)