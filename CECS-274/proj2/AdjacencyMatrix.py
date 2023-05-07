from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        if self.adj[i][j] == False:
            return False
        self.adj[i][j] = False
        return True

    def has_edge(self, i : int, j: int) ->bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        tf = ArrayList.ArrayList()
        for whydidyoudothat in range(self.n):
            if self.adj[i][whydidyoudothat] == 1:
                tf.append(whydidyoudothat)
        return tf

    def in_edges(self, j) -> List:
        iwm = ArrayList.ArrayList()
        for iwntmb in range(self.n):
            if self.adj[iwntmb][j] == 1:
                iwm.append(iwntmb)
        return iwm

    def bfs(self, i : int):
        travisScott = ArrayList.ArrayList()
        eyeball = [False for godzilla in range(self.n)]
        eq = ArrayQueue.ArrayQueue()
        eq.add(i)
        travisScott.append(i)
        eyeball[i] = True
        while eq.n > 0:
            wah = eq.remove()
            nine = self.out_edges(wah)
            for element in nine:
                if eyeball[element] is False:
                    eq.add(element)
                    travisScott.append(element)
                    eyeball[element] = True
        return travisScott

    def dfs(self, i : int):
        yamama = ArrayList.ArrayList()
        cnfv = ArrayStack.ArrayStack()
        eyeball = [False for godzilla in range(self.n)]
        cnfv.push(i)
        while cnfv.n > 0:
            lol = cnfv.pop()
            if eyeball[lol] is False:
                yamama.append(lol)
                eyeball[lol] = True
            horse = reversed(self.out_edges(lol))
            for table in horse:
                if eyeball[table] is False:
                    cnfv.push(table)
        return yamama

    def size(self):
        return self.n
    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s