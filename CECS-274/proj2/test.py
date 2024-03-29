'''
from ArrayStack import *


#lab
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
for i in range(1,6):
    arr.add(i)
print(arr.a)
for i in range(5):
    print(arr.remove())
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
print(arr.a, arr.j)
arr.remove(3)
print(arr, arr.j)
'''
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
'''

'''
#quiz : array list
from ArrayList import ArrayList
arr = ArrayList()
arr.append('1')
arr.append('A')
arr.append('B')
arr.append('C')
arr.append('D')
arr.append('E')
arr.append('F')
arr.remove(0)
print(arr.a)

arr.add(6,'G')
print(arr.a)
arr.add(5,'f')
print(arr.a)
arr.add(2,'c')
print(arr.a)
arr.remove(6)
print(arr.a)
'''
'''
#quiz : array stack
from ArrayStack import ArrayStack

arr = ArrayStack()
asidasdadas = ['A','B','C','D','E','F']
for asdeasds in asidasdadas:
    arr.push(asdeasds)
print(arr.a)

arr.remove(2)
arr.remove(3)
arr.remove(0)
print(arr.a)
print(arr)
arr.remove(1)
arr.add(1,'A')
print(arr.a)
arr.add(1,'B')
arr.add(0,'C')
print(arr.a)
'''

'''
#  sll stack
from SLLStack import SLLStack

sll = SLLStack()

for i in range(5,0,-1):
    sll.push(i)

print(sll)

for i in range(5):
    print(sll.pop())

'''

'''
#  sll queue
from SLLQueue import SLLQueue

sll = SLLQueue()

for i in range(1,6):
    sll.add(i)

print(sll)

for i in range(5):
    print(sll.remove())

'''

'''
#lab sll queue 
from SLLQueue import *
s = SLLQueue()

s.add('A')
s.add('C')
s.add('E')
print(s)

s.remove()
print(s)
s.remove()
print(s, s.head.x, s.tail.x)
s.add('X')
print(s, s.head.x, s.tail.x)
s.add('Y')
print(s, s.head.x, s.tail.x)
s.remove()
print(s, s.head.x, s.tail.x)
s.add('Z')
print(s, s.head.x, s.tail.x)
s.remove()
print(s, s.head.x, s.tail.x)

'''

# for index, char in enumerate(pal)

'''
#lab sll stack
from SLLStack import SLLStack
s = SLLStack()
s.push('E')
s.push('C')
s.push('A')
print(s, s.head.x, s.tail.x)
s.pop()
print(s, s.head.x, s.tail.x)
s.pop()
s.push('X')
print(s)
'''

'''
# dl list
import DLList
l = DLList.DLList()
l.add(0,4)
l.add(0,1)
l.add(1,3)
l.add(1,2)
l.add(4,5)
print(l)
print(l.get(1))
l.remove(2)
print(l)
l.remove(3)
print(l)
l.reverse()
print(l)
'''

'''
#max queue
from MaxQueue import MaxQueue

q = MaxQueue()
q.add(3)
print(q, q.max_deque)


import MaxQueue
l = MaxQueue.MaxQueue() 
l.max_deque.add_first(1)
print(l.max_deque)
'''

"""
# TESTER
import MaxQueue
mq = MaxQueue.MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
        
"""

'''
#hash table
from ChainedHashTable import *
t = ChainedHashTable()
print(t.remove(2))
t.add(1,'first')
print(len(t))
t.add(2,'second')
t.add(3,'third')
t.add(3,'fourth')
print(t.size())
t.remove(3)
print(t.size())
print(t.find(3))
t.add(3,'third')
t.add(4,'four')
t.add(5,'five')
print(t.size())
print(t)
print(t.find(3))
'''
'''from ChainedHashTable import *
t = ChainedHashTable()

t.add(23, 'A')
print(t.d)
t.add(15, 'B')
print(t.d)


t.add(11, 'C')
t.remove(23)
print(t.d)
t.remove(15)
print(t.d)
t.add(10, 'D')
print(t.d)
t.add(12,'A')

print(t)



l = [0, -1]

l.sort()
print(l)'''

import algorithms
a= [6, 8, -26, 7, -24, 7, 9, -12, -16, -8, -29, 27]

print(algorithms.merge_sort(a))

import ArrayList

ab = ArrayList.ArrayList()
for el in a:
    ab.append(el)
print(type(ab))
print(len(ab))


print(algorithms.merge_sort(ab))

print('a'>'b')