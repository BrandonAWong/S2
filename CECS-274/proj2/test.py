from ArrayStack import *

'''
lab
arr = ArrayStack()
letters = ['A','B','C','D','E','F']
for l in letters:
    arr.push(l)

print(arr.a)


arr.remove(0)
print(arr.a)
arr.remove(3)
print(arr.a)
arr.remove(0)
print(arr.a)
arr.remove(1)
print(arr.a)
arr.add(1,'R')
print(arr.a)
arr.add(1,'A')
#print(arr.a)
arr.add(3,'T')
print(arr.a)
arr.add(1,'H')
print(arr.a)
arr.add(6,'B')
print(arr.a)

arr.pop()
print(arr.a)
arr.pop()
print(arr.a)

removeList = []

for i in range(5):
    removeList.append(arr.pop())

print(removeList)
'''
'''
from ArrayStack import *


arr = ArrayStack()
for i in range(5, 0, -1):
    print(arr.a)
    arr.push(i)

print(arr.a)

removeList = []

for i in range(5):
    removeList.append(arr.pop())
    print(arr.a)

print(removeList)
'''

from ArrayQueue import ArrayQueue

queue = ArrayQueue()

for i in range(1,9):
    queue.add(i)
print(queue.a)

for i in range(2):
    queue.remove()
    print(queue.a)

for i in range(9,15):
    queue.add(i)    
    print(queue.a)

for i in range(3):
    queue.remove()
    print(queue.a)

