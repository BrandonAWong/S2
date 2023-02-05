import ArrayQueue

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        # todo
        pass 

    def size(self) -> int:
        return self._size(self.r)
    
    def _size(self, u : Node) -> int:
        # todo
        pass 
    
    def size2(self) -> int:
        # todo
        pass 

    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        # todo
        pass 
    
    def traverse(self, u : Node):
        # todo
        pass 

    def traverse2(self):
        # todo
        pass 

    def bf_traverse(self):
        # todo
        pass 
            
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def in_order(self, u : Node, l : list) :       
        # todo
        pass 

    def __str__(self):
        l = []
        self.in_order(self.r, l)
        return ', '.join(map(str, l))