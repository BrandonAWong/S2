from Interfaces import Deque
from DLList import DLList
import numpy as np


class DLLDeque(Deque, DLList):
    def __init__(self):
        DLList.__init__(self)

    def add_first(self, x: object):
        self.add(0, x)

    def add_last(self, x: object):
        self.add(self.n, x)

    def remove_first(self) -> object:
        return self.remove(0)

    def remove_last(self) -> object:
        return self.remove(self.n - 1)
