'''Prompt: Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old'''

username = str(input("What is your name? "));
userage = int(input("What is your age? "));

print(f'You will turn 100 in {100 - userage} years.');

'''Extra 1: Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.'''
num = int(input("How many copies of the previous message do you want? "));
print(num * f'You will turn 100 in {100 - userage} years.');

'''Extra 2: Print out that many copies of the previous message on separate lines.'''
num1 = int(input("How many copies of the previous message do you want? "));
print(num1 * f'You will turn 100 in {100 - userage} years.\n');