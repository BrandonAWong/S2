import random
import time
from MobileCritter import MobileCritter


class Board:

    def __init__(self):
        """initializes a board with a random number of leaves placed in random locations"""
        self.board = [['*' for i in range(20)] for i in range(20)]
        for i in range(random.randint(50, 100)):
            rx = random.randint(0, 19)
            ry = random.randint(0, 19)
            self.board[rx][ry] = 'L'
        self.board[10][10] = 'S'

    def place_critter(self, critter: MobileCritter):
        """
        determines the position of the critter relative to the board; If critter lands on location with a leaf,
        critter collects the leaf.
        @:param critter - an object from a class implementing MobileCritter.
        @:return a list of two Boolean values.  The first value is True if the critter
        collected a leaf, False otherwise.  The second value is True if the critter landed on or crossed a boundary,
        False otherwise.
        """
        dx = critter.get_position()[0]
        dy = critter.get_position()[1]
        x, y = 10 + dx, 10 - dy
        leaf_collected = False
        hit_bdry = False
        if x >= 20 or y >= 20 or x <= -1 or y <= -1:
            hit_bdry = True
        else:
            if self.board[y][x] == 'L':
                critter.collect_leaf()
                leaf_collected = True
                self.board[y][x] = '*'
        return leaf_collected, hit_bdry

    def display(self, critter: MobileCritter):
        """displays the board with leaf, critter, and boundary locations"""
        print('B\t' * 22)

        for i in range(len(self.board)):
            print("B", end='\t')
            dx = critter.get_position()[0]
            dy = critter.get_position()[1]
            x, y = 10 + dx, 10 - dy
            for j in range(len(self.board[0])):
                if i == y and j == x:
                    print(critter, end='\t')
                elif self.board[i][j] == 'L':
                    print(u"\u2618", end='\t')
                else:
                    print(self.board[i][j], end='\t')
            print("B")
            time.sleep(0.01)

        print('B\t' * 22)
        print("Board loc:(%d, %d)" % (y, x))
