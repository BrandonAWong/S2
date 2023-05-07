"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if 0 <= i  < self.n and 0 <= j < self.n:
            if j not in self.adj[i]:
                self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        for ku in range(len(self.adj[i])):
            if self.adj[i].get(ku) == j:
                self.adj[i].remove(ku)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        for nujab in range(len(self.adj[i])):
            if self.adj[i].get(nujab) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, j) -> List:
        incdecinc = []
        for y in range(self.n):
            if self.has_edge(y, j):
                incdecinc.append(y)
        return incdecinc

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