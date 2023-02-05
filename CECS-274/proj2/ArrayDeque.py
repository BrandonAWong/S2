from Interfaces import Deque
from ArrayList import ArrayList


class ArrayDeque(Deque, ArrayList):
    '''
        ArrayDeque: Implementation of a Deque interface using ArrayBase list. 
        It inheritances from an ArrayList
    '''
    def __init__(self):
        '''
        __init__: Initialization of the base class ArrayList
        '''
        ArrayList.__init__(self)

    def add_first(self, x : object):
        '''
        add_first: Insert x in the head of the deque. It just calls add(0, x) of the
        base class ArrayList to insert in the head
        '''
        self.add(0, x)

    def add_last(self, x : object):
        '''
        add_last: Insert x in the tail of the deque. It just calls add(self.n, x) of the
        base class ArrayList to insert in the tail
        '''
        self.add(self.n, x)
    
    def remove_first(self) -> object:
        '''
        remove_first: Remove from the head of the  deque. It just calls remove(0) of the
        base class ArrayList to remove in the head
        '''
        return self.remove(0)

    def remove_last(self) -> object:
        '''
        remove_last: Remove from the tail of the  deque. It just calls remove(self.n) of the
        base class ArrayList to remove in the tail
        '''
        return self.remove(self.n-1)

   