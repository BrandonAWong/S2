from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree
from Interfaces import Set

red = 0
black = 1


class RedBlackTree(BinarySearchTree, Set):

    def _new_node(self, x, v):
        u = BinaryTree.Node(x, v)
        u.left = u.right = u.parent = self.nil
        u.color = black
        u.x = x
        u.v = v
        return u

    def __init__(self):
        BinarySearchTree.__init__(self)
        self.nil = self._new_node(None, None)
        self.nil.right = self.nil.left = self.nil.parent = self.nil
        self.r = self.nil

    def push_black(self, u):
        u.color -= 1
        u.left.color += 1
        u.right.color += 1

    def pull_black(self, u):
        u.color += 1
        u.left.color -= 1
        u.right.color -= 1

    def flip_left(self, u):
        self.swap_colours(u, u.right)
        self.rotate_left(u)

    def flip_right(self, u):
        self.swap_colours(u, u.left)
        self.rotate_right(u)

    def swap_colours(self, u, w):
        (u.color, w.color) = (w.color, u.color)

    def add(self, x: object, v: object):
        # todo
        pass

    def add_fixup(self, u):
        # todo
        pass

    def remove(self, x):
        # todo
        pass

    def remove_fixup(self, u):
        # todo
        pass

    def remove_fixup_case1(self, u):
        # todo
        pass

    def remove_fixup_case2(self, u):
        # todo
        pass

    def remove_fixup_case3(self, u):
        # todo
        pass

    def rotate_left(self, u: BinaryTree.Node):
        # todo
        pass

    def rotate_right(self, u: BinaryTree.Node):
        # todo
        pass
