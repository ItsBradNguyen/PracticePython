'''Prompt: Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
list = [];

for A in a:
    for B in b:
        if B == A and list.count(B)<1:
            list.append(B)            
print(list)

'''Extra 1: Randomly generate two lists to test this'''
import random

list1 = []
randomlist1 = []
randomlist2 = []

for i in range(1,10):
    rng = random.randint(1,100);
    randomlist1.append(rng);

for I in range(1,10):
    RNG = random.randint(1,100);
    randomlist2.append(RNG)
    
for A in randomlist1:
    for B in randomlist2:
        if B == A and list.count(B)<1:
            list1.append(B)
print(randomlist1)
print(randomlist2)
print(list1)

'''Extra 2: Write this in one line of Python.'''
print(set(a).intersection(set(b)))
