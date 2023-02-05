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
        # todo
        pass

    def remove_edge(self, i : int, j : int):
        # todo
        pass

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        pass

    def out_edges(self, i) -> List:
        # todo
        pass

    def in_edges(self, i) -> List:
        # todo
        pass

    def bfs(self, r : int):
        # todo
        pass

    def dfs(self, r : int):
        # todo
        pass

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s