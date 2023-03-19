import numpy as np
import ArrayStack
#import BinaryTree
import ChainedHashTable
import DLList
#import operator
from re import split


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
        kerblam = []
        for i in range(len(YAHSDIKASHLKD)):
            kerblam.append(bloop[i])
            yipyip = str(self.dict.find(YAHSDIKASHLKD[i]))
            if yipyip != 'None':
                kerblam.append(yipyip)
            else:
                kerblam.append(str(YAHSDIKASHLKD[i]))
        kerblam.append(bloop[-1])
        print("".join(kerblam))


    def build_parse_tree(self, exp: str) -> str:
        # todo
        pass

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        pass

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r) 
