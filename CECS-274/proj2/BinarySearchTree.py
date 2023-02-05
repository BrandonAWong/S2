from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        BinaryTree.__init__(self)
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        # todo
        pass 
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        # todo
        pass  

    def find_eq(self, x : object) -> object:
        # todo
        pass 
    
    def find(self, x: object) -> object:
        # todo
        pass 
        
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)
    
    def splice(self, u: BinaryTree.Node):
        # todo
        pass 

    def remove_node(self, u : BinaryTree.Node):
        # todo
        pass 

    def remove(self, x : object) -> bool:
        # todo
        pass 
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


            
