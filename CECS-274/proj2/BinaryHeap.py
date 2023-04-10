import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    # todo
    pass


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # todo
    pass


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    # todo
    pass


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        # todo
        pass

    def remove(self):
        # todo
        pass

    def depth(self, u) -> int:
        # todo
        pass

    def height(self) -> int:
        # todo
        pass

    def bf_order(self) -> list:
        # todo
        pass

    def in_order(self) -> list:
        # todo
        pass

    def post_order(self) -> list:
        # todo
        pass

    def pre_order(self) -> list:
        # todo
        pass

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        # todo
        pass

    def _resize(self):
        # todo
        pass

    def _trickle_down_root(self):
        # todo
        pass

    def __str__(self):
        return str(self.a[0:self.n])