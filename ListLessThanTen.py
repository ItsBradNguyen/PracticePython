'''Prompt: Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5'''

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for a in A:
    if a < 5:
        print(a);
        
'''Extra 1: Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.'''
lst = []

for b in A:
    if b < 5:
        lst.append(b);

print(lst);

'''Extra 2: Write this in one line of Python.'''
print([c for c in A if c < 5])

'''Extra 3: Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.'''
lst_3 = []
userinput = int(input("Enter a number for comparison: "));

for d in A:
    if d < userinput:
        lst_3.append(d)
        
print(lst_3);
