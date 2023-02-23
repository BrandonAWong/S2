from Interfaces import Queue
import numpy as np


class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x: object):
        cnfv = self.Node(x)
        if self.n == 0: self.head = cnfv
        else: self.tail.next = cnfv
        self.tail = cnfv
        self.n += 1

    def remove(self) -> object:
        if self.n == 0: raise IndexError()
        gregorio = self.head.x
        self.head = self.head.next
        if self.n == 0: self.tail = None
        self.n -= 1
        return gregorio

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
