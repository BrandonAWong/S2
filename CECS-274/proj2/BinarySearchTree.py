from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        newNode = self.Node(key, value)
        parentNode = self._find_last(key)
        return self._add_child(parentNode, newNode)

    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        node = self._find_eq(key)
        if node == None:
            return None
        return node.v

    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        node = self._find_eq(key)
        if node == None:
            raise ValueError
        value = node.v
        self._remove_node(node)
        return value

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        currentNode = self.r
        while currentNode != None:
            if key < currentNode.k:
                currentNode = currentNode.left
            elif key > currentNode.k:
                currentNode = currentNode.right
            else:
                return currentNode
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        currentNode = self.r
        parentNode = None
        while currentNode != None:
            parentNode = currentNode
            if key < currentNode.k:
                currentNode = currentNode.left
            elif key > currentNode.k:
                currentNode = currentNode.right
            else:
                return currentNode
        return parentNode

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        if p == None:
            self.r = u
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u has at most one child
        """
        if u.left != None:
            childNode = u.left
        else:
            childNode = u.right
        if u == self.r:
            self.r = childNode
            parentNode = None
        else:
            parentNode = u.parent
            if parentNode.left == u:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
        if childNode != None:
            childNode.parent = parentNode
        self.n -= 1

    def _remove_node(self, u: BinaryTree.Node):
        if u.left == None or u.right == None:
            self._splice(u)
        else:
            w = u.right
            while w.left != None:
                w = w.left
            u.k = w.k
            u.v = w.v
            self._splice(w)
    
    def find_greater_smallest_node(self, key: object):
        currentNode = self.r
        wakanda = None
        while currentNode != None:
            if key == currentNode.k:
                return currentNode
            if key < currentNode.k:
                currentNode = currentNode.left
                if key > currentNode.k:
                    return currentNode.parent 
            elif key > currentNode.k:
                currentNode = currentNode.right
                wakanda = currentNode
            else:
                break
        return wakanda

    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
