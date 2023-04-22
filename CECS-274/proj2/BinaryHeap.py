import numpy as np
from math import log2, floor
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2


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
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError
        deceased = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            #self._resize()
            pass
        return deceased

    def depth(self, i) -> int:
        johnnydepth = 0
        hatter = 0
        while self.a[hatter] != i:
            hatter += 1
        while self.a[hatter] != self.a[0]:
            hatter = parent(hatter)
            johnnydepth += 1
        return johnnydepth

    def height(self) -> int:
        return floor(log2(self.n - 1))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        def HELPME(indiana: int):
            nodes = []
            if left(indiana) < self.n:
                nodes.extend(HELPME(left(indiana)))
            nodes.append(self.a[indiana])
            if right(indiana) < self.n:
                nodes.extend(HELPME(right(indiana)))
            return nodes
        return HELPME(0)
    
    def post_order(self) -> list:
        def AHHHHHHH(NOOOOOOOO: int):
            nodes = []
            if left(NOOOOOOOO) < self.n:
                nodes.extend(AHHHHHHH(left(NOOOOOOOO)))
            if right(NOOOOOOOO) < self.n:
                nodes.extend(AHHHHHHH(right(NOOOOOOOO)))
            nodes.append(self.a[NOOOOOOOO])
            return nodes
        return AHHHHHHH(0)

    def pre_order(self) -> list:
        def wtf(whyborn: int):
            nodes = []
            nodes.append(self.a[whyborn])
            if left(whyborn) < self.n:
                nodes.extend(wtf(left(whyborn)))
            if right(whyborn) < self.n:
                nodes.extend(wtf(right(whyborn)))
            return nodes
        return wtf(0)

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        dude = self.n - 1
        fathermotherIndexComplex = parent(dude)
        while dude > 0 and self.a[dude] < self.a[fathermotherIndexComplex]:
            self.a[dude], self.a[fathermotherIndexComplex] = self.a[fathermotherIndexComplex], self.a[dude]
            dude = fathermotherIndexComplex
            fathermotherIndexComplex = parent(dude)

    def _resize(self):
        granger = _new_array(max(1, 2 * self.n))
        for juju in range(self.n):
           granger[juju] = self.a[juju]
        self.a = granger

    def _trickle_down_root(self):
        g0d = 0
        jesus = left(g0d)
        abdul = right(g0d)
        while g0d < self.n and jesus <= self.n and abdul <= self.n \
        and (self.a[g0d] > self.a[jesus] or self.a[g0d] > self.a[abdul]):
            bombTargets = {g0d : self.a[g0d], jesus : self.a[jesus], abdul : self.a[abdul]}
            theDwarfsLocation = min(bombTargets, key=bombTargets.get)
            self.a[g0d], self.a[theDwarfsLocation] = self.a[theDwarfsLocation], self.a[g0d]
            g0d = theDwarfsLocation
            jesus = left(g0d)
            abdul = right(g0d)
            
    def __str__(self):
        return str(self.a[0:self.n])