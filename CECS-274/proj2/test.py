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
    arr.push(i)
    print(arr.a)

print(arr.a)

removeList = []

for i in range(5):
    removeList.append(arr.pop())
    print(arr)

print(removeList)
'''
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

'''
'''
#lab
from ArrayQueue import ArrayQueue

arr = ArrayQueue()

arr.add('z')
arr.add('A')
arr.add('B')
arr.remove()
arr.add('C')

print(arr.a)
#call 1
arr.remove()
print(arr.a)
#call 2
arr.add('X')
print(arr.a)
#call 3
arr.add('Y')
print(arr.a)
#call 4
arr.add('Z')
print(arr.a)
#call 5
arr.remove()
print(arr.a)
#call 6
arr.remove()
print(arr.a)
'''

'''
#random queue test
from RandomQueue import RandomQueue
arr = RandomQueue()
for i in range(1,5):
    arr.add(i)
print(arr.a)
for i in range(4):
    arr.remove()
    print(arr.a)
'''

'''
#array list
from ArrayList import ArrayList

arr = ArrayList()
arr.add(0,4)
print(arr.a, arr.j)
arr.add(0,1)
print(arr.a, arr.j)
arr.add(1,3)
print(arr.a, arr.j)
arr.add(1,2)
print(arr.a, arr.j)
arr.add(4,5)
print(arr.a, arr.j)
arr.remove(2)
print(arr, arr.j)
arr.remove(3)
print(arr, arr.j)
'''

#array list lab
from ArrayList import ArrayList
arr = ArrayList()
arr.append('1')
arr.append('2')
arr.append('A')
arr.append('B')
arr.append('C')
arr.append('D')
arr.append('E')
arr.remove(0)
arr.remove(0)
print(arr.a)
#call 1
arr.add(2,'b')
print(arr.a)
print(arr.j, arr.n)

#call 2
arr.remove(3)
print(arr.a)
print(arr.j, arr.n)

#call 3
arr.add(1,'d')
print(arr.a)
print(arr.j, arr.n)

#call 4 
arr.add(0,'z')
print(arr.a)
print(arr.j, arr.n)

#call 5
arr.add(7,'e')
arr.add(5,'f')
print(arr.a)
print(arr.a[arr.j], arr.n)