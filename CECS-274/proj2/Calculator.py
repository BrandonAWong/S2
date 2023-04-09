import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
from re import split, findall


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()  
        for el in s:
            if el == '(':
                stack.push(el)
            elif el == ')':
                try:
                    stack.pop()
                except:
                    return False
        if stack.size() == 0:  
            return True
        return False 
    
    def print_expression(self, exp):
        YAHSDIKASHLKD = [x for x in split('\W+', exp) if x.isalnum()]
        bloop = split('\w+', exp)
        kerblam = ''
        for i in range(len(YAHSDIKASHLKD)):
            kerblam += bloop[i]
            yipyip = self.dict.find(YAHSDIKASHLKD[i])
            if yipyip != None:
                kerblam += str(yipyip)
            else:
                kerblam += str(YAHSDIKASHLKD[i])
        kerblam += bloop[-1]
        return kerblam

    def _build_parse_tree(self, exp: str) -> str:
        if not self.matched_expression(exp):
            raise ValueError
        variables = [x for x in split('\W+', exp) if x.isalnum()]
        exp = findall('[-+*/()]|\w+', exp)                      # https://docs.python.org/3/library/re.html
        tree = BinaryTree.BinaryTree()
        tree.r = tree.Node()
        currentNode = tree.r
        for el in exp:
            node = tree.Node()
            if el == '(':
                currentNode = currentNode.insert_left(node)
            elif el in '+-/*':
                currentNode.set_val(el)
                currentNode.set_key(el)
                currentNode = currentNode.insert_right(node)
            elif el in variables:
                currentNode.set_key(el)
                currentNode.set_val(self.dict.find(el))
                currentNode = currentNode.parent
            elif el == ')':
                currentNode = currentNode.parent
        return tree

    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left != None and u.right != None:
            fn  = op[u.k]
            return fn(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left == None and u.right == None:
            if u.v != None:
                return float(u.v)
            raise ValueError(f"Missing value for variable {u.k}")
        elif u.left != None:
            return self._evalulate(u.left)
        else:
            return self._evaluate(u.right)

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r) 