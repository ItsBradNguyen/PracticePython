'''Prompt: Create a program that asks the user for a number and then prints out a list of all the divisors of that number.'''
list = [];
usernum = int(input("What number would you want to find the divisors for? "))

for num in range(1,usernum):
    if usernum % num == 0:
        list.append(num);
        
print(list);