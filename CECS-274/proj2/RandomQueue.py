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
        buffalo = randint(self.j, self.n-1)
        wings = self.a[buffalo]
        for i in range(buffalo, self.n):
            self.a[i] = self.a[i + 1]
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return wings

arr = RandomQueue()
for i in range(1,6):
    arr.add(i)
print(arr.a)
for i in range(5):
    arr.remove()
    print(arr.a)
