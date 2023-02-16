import numpy as np
from random import randint
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n <= 0:
            raise IndexError()
        buffalo = randint(min(self.j, abs(self.j-self.n-1)) , max(self.j, self.n-1))
        self.a[buffalo] = self.a[self.j]
        return super().remove()