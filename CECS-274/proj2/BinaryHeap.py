import numpy as np
from Interfaces import Queue



def left(i : int):
    # todo
    pass 

def right(i: int):
    # todo
    pass 

def parent(i : int):
    # todo
    pass 

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)

    def resize(self):
        # todo
        pass 

    def add(self, x : object):
        # todo
        pass 

    def bubble_up(self, i):
        # todo
        pass 

    def remove(self):
        # todo
        pass 

    def trickle_down(self, i):
        # todo
        pass 

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"


