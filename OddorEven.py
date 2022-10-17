'''Prompt: Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.'''
def OddorEven():
    num = int(input("Enter a number: "));

    if num%2==0:
        print(f'{num} is even');
    else:
        print(f'{num} is odd');
    
'''Extra 1: If the number is a multiple of 4, print out a different message.'''
def multiple_of_4():
    num1 = int(input("Enter a number: "));
    
    if num1%4 == 0:
        print(f'{num1} is a multiple of 4');
    else:
        print(f'{num1} is not a multiple of 4');

'''Extra 2: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''
def num_check(num2, check):
    if num2%check == 0:
        print(f'{num2} is a multiple of {check}');
    else:
        print(f'{num2} is not a multiple of {check}');
        
num_check(10,2);