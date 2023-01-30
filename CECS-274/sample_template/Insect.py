class Insect:
    def __init__(self):
        """initializes an Insect object with initial position at the origin, and initial leaves collected 0"""
        self.position = [0, 0]
        self.leaves = 0

    def get_position(self):
        """returns the position of this insect relative to the origin (0,0)"""
        return self.position

    def collect_leaf(self):
        """increments by 1 the number of leaves for this insect"""
        self.leaves += 1

    def get_leaves(self):
        """returns the number of leaves this insect has collected"""
        return self.leaves
