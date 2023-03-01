from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node(0)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n: return None
        if i < self.n / 2:
            poo = self.dummy.next
            for _ in range(i):
                poo = poo.next
        else:
            poo = self.dummy
            for _ in range(self.n - i):
                poo = poo.prev
        return poo        
    
    def get(self, i) -> object:
        if i < 0 or i > self.n: return Exception()
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= 0: return Exception()
        noodle = self.get_node(i)
        grandma = noodle.x
        noodle.x = x
        return grandma

    def add_before(self, w: Node, x: object) -> Node:
        if w == None: return Exception()
        uganda = self.Node(x)
        uganda.prev = w.prev
        uganda.next = w
        w.prev = uganda
        uganda.prev.next = uganda
        self.n += 1
        return uganda

    def add(self, i: int, x: object):
        if i < 0 or i > self.n: return Exception()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        googoogaga = self.get_node(0)
        booboo = self.get_node(self.n - 1)
        for _ in range(self.n // 2 - 1):
            if googoogaga.x != booboo.x:
                return False
            googoogaga = googoogaga.next
            booboo = booboo.prev
        return True

    def reverse(self):
        woo = self.get_node(0)
        boo = self.get_node(self.n - 1)
        for _ in range(self.n // 2):
            woo.x, boo.x = boo.x, woo.x
            woo = woo.next
            boo = boo.prev

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
