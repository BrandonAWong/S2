from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x : object):
        """
        adds an element to the end of this max queue
        INPUT: x the element to add
        """
        super().add(x)
        if x > self.max():
            for _ in range(self.max_deque.n):
                self.max_deque.remove(0)
            self.max_deque.add_first(x)
        else:
            for i in range(1, self.max_deque.n + 1):
                if x > self.max_deque.get(i):
                    self.max_deque.add(i, x)
                    break
                    
    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        """
        valorant = super().remove()
        if valorant == self.max():
            self.max_deque.remove_first() 
            #if self.max_deque.n == 0:
                
        return valorant

    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)