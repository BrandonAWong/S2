import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"

    def __init__(self):
        self.r = None

    def depth(self, u: Node) -> int:
        if u == None:
            return -1
        depth = 0
        currentNode = u
        while(currentNode != self.r):
            currentNode = currentNode.parent
            depth += 1
        return depth

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        if u == None:
            return -1
        return 1 + max(self._height(u.left), self._height(u.right))

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        if u == None:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def bf_order(self):
        nodes = []
        queue = SLLQueue.SLLQueue()
        if self.r != None:
            queue.add(self.r)
        while queue.size() > 0:
            removed = queue.remove()
            nodes.append(removed)
            if removed.left != None:
                queue.add(removed.left)
            if removed.right != None:
                queue.add(removed.right)
        return nodes

    def in_order(self) -> list:
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        nodes = []
        if u.left != None:
            nodes.extend(self._in_order(u.left))
        nodes.append(u)
        if u.right != None:
            nodes.extend(self._in_order(u.right))
        return nodes

    def post_order(self) -> list:
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        nodes = []
        if u.left != None:
            nodes.extend(self._post_order(u.left))
        if u.right != None:
            nodes.extend(self._post_order(u.right))
        nodes.append(u)
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        nodes = []
        nodes.append(u)
        if u.left != None:
            nodes.extend(self._pre_order(u.left))
        if u.right != None:
            nodes.extend(self._pre_order(u.right))
        return nodes

    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)