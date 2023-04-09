from abc import abstractmethod
import sys

"""
    Abstract Data types: It provides the list of interfaces 
    (Stack, Queue, Deque, List, Set, Tree, Graph)
"""


class Queue:
    """
        Queue: The Queue interface represents a collection of elements to which we can
        add elements and remove the next element.
    """

    @abstractmethod
    def add(self, x: object):
        """
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove(self) -> object:
        """
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline
                    decides which element should be removed.
            Return: Object type
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the queue
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        """
            __len__: Returns the size of the queue when using len, i.e., len(q)
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()


class Stack:
    """
        Stack: It is a LIFO Queue, the most recently added element
                is the next one removed.
    """

    @abstractmethod
    def push(self, x: object):
        """
            push: Insert an element in the tail of the stack
            Inputs:
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def pop(self) -> object:
        """
            pop: Remove the last element in the stack
            Returns: the object of the tail if it is no empty
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        """
            __len__: Returns the size of the queue when using len, i.e., len(s)
            where s is a stack instance
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        """
        return self.size()


class Deque:
    """
        Deque: is the abstract data type of a Deque. The behavior depends on
        the implementation using arrays or linked list
    """

    @abstractmethod
    def add_first(self, x: object):
        """
            add_first: Insert an element in the head of the deque and increment
            the number of elements in the deque
            Inputs:
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def add_last(self, x: object):
        """
            add_last: Insert an element in the tail of the deque and increment
            the number of elements in the deque
            Inputs:
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove_first(self) -> object:
        """
            remove_first: Remove an element in the head of the deque and decrement
            the number of elements in the deque
            Inputs:
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove_last(self) -> object:
        """
            remove_last: Remove an element in the tial of the deque and decrement
            the number of elements in the deque
            Inputs:
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the deque
            Return: an integer greater or equal to zero representing the number
                    of elements in the deque
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        """
            __len__: Returns the size of the queue when using len, i.e., len(q) where
            q is an instance of queue.
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()


class List:
    """
        List: is the abstract data type of a List. The behavior depends on
        the implementation
    """

    @abstractmethod
    def add(self, i: int, x: object):
        """
            add: shift one position all the items j>=i, insert an element
            at position i of the list and increment the number of elements
            in the list
            Inputs:
                i: Index that is integer non negative and at most n
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def set(self, i: int, x: object):
        """
            Set: Set the value x in the index i of the list
            Inputs:
                i: Index that is integer non negative and at most n
                x: Object type, i.e., any object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def get(self, i: int) -> object:
        """
            get: returns the value x in the index i of the list
            Inputs:
                i: Index that is integer non negative and at most n
            Return: return the value x in the index i of the list
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove(self, i: int) -> object:
        """
            remove: remove th element i and shift all the elements j > i
            one position to the left and decrease n
            Return: return the value x to be remove.
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the list
            Return: an integer greater or equal to zero representing the number
                    of elements in the list
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __iter__(self):
        """
            __iter__: Initialize the iterator which is used in the for loops
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __next__(self):
        """
            __next__: Move to the next itme in the iterator. It  is used in the for loops
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self) -> int:
        """
            __len__: Returns the size of the queue when using len, i.e., len(l)
            where l is a list instance
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()

    def __getitem__(self, i) -> object:
        """
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input:
                i: positive integer less than n
            Return: the item at index i
        """
        if isinstance(i, slice):
            return [self.get(i) for i in range(i.start, i.stop)]
        else:
            return self.get(i)

    def __setitem__(self, i: int, x: object):
        """
            __setitem__: Sets the item x in the index  in array format, i.e., l[i] = x
            where l is a list instance
            Input:
                i: positive integer less than or equal n
                    if i in [0, n) then it sets x at index i
                    if i = n then it adds x at the end
                x: the item to set
        """
        if i == self.size():
            self.add(i, x)
        else:
            self.set(i, x)


class Set:
    """
        Set: It is the abstract data type of a set. The behavior depends on
        the implementation
    """

    @abstractmethod
    def add(self, key: object, value: object):
        """
            add: inserts the tuple(key, value) in the set
            Inputs:
                key: The key of the tuple
                value: the value to store
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def find(self, key: object) -> object:
        """
            find: find the key in the set
            Inputs:
                key: The key of the tuple
            Return:
                the value that corresponds to the key if exists, otherwise it return None
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove(self, key: object):
        """
            remove: remove the tuple (key, value) in the set if it exists
            Inputs:
                key: The key of the tuple

        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the set
            Return: an integer greater or equal to zero representing the number
                    of elements in the set
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self) -> int:
        """
            __len__: Returns the size of the queue when using len, i.e., len(q)
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()

    def __missing__(self, key: object) -> bool:
        """
            __missing__: return true if the key exists __getitem__ uses it
            Input:
                key: key of the tuple
        """
        return self.find(key) is None

    def __getitem__(self, key: object) -> object:
        """
            __getitem__: return the value of tuple (key,value) in the set using format, i.e., x = l[i]
            where l is a set instance
            Input:
                key: key of the tuple
        """
        return self.find(key)

    def __setitem__(self, key: object, value: object):
        """
            __setitem__: Add the tuple (key,value) in the set using format, i.e., l[i] = x
            where l is a set instance
            Input:
                key: key of the tuple
                value: the value of the tuple
        """
        self.add(key, value)


class Tree:
    @abstractmethod
    def depth(self, u) -> int:
        """
        computes the depth of node u
        Return: an integer greater or equal to zero representing the number
                of edges in the path from node u to the root
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def height(self):
        """
        computes the height of the tree
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self):
        """
        returns the number of nodes in the tree
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def bf_order(self):
        """
        returns the list of nodes in the tree as they are traversed using breadth-first order traversal
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def in_order(self):
        """
        returns the list of nodes in the tree as they are traversed using in-order traversal
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def post_order(self):
        """
        returns the list of nodes in the tree as they are traversed using post-order traversal
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def pre_order(self):
        """
        returns the list of nodes in the tree as they are traversed using pre-order traversal
        """
        raise NotImplementedError("Subclasses should implement this!")


class Graph:
    """
        Graph: It is the abstract data type of a graph.
    """

    @abstractmethod
    def add_edge(self, i: int, j: int):
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove_edge(self, i: int, j: int):
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def has_edge(self, i: int, j: int) -> bool:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def out_edges(self, i: int) -> List:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def in_edges(self, j: int) -> List:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the set
            Return: an integer greater or equal to zero representing the number
                    of elements in the set
        """
        raise NotImplementedError("Subclasses should implement this!")
