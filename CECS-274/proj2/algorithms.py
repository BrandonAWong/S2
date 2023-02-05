"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    # todo
    pass


def binary_search(a: List, x):
    # todo
    pass


def _merge(a0: List, a1: List, a: List):
    # todo
    pass


def merge_sort(a: List):
    # todo
    pass


def _quick_sort_f(a: List, start, end):
    # todo
    pass


def _quick_sort_r(a: List, start, end):
    # todo
    pass


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
