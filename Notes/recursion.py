# https://github.com/CyberTrainingUSAF/05-Python-Programming/blob/master/03_Flow_Control/08_recursion.md

# Recursion

# Recursion is a function that calls itself. In other words a function will continue to call itself until a certain condition is met.

# use recursion when you have a problem that needs to be broken into smaller similar problems and solve them first.

def recursive_factorial(n):
    #base case
    if n == 0:
        return 1
    #recursive case
    else:
        return n * recursive_factorial(n-1)

#print(recursive_factorial(4))
# Be sure that every time you write a recursive function that you can control the number of times it will be executed.

global count 
count = 0  

def forever_recursion(): 
    annoying_message()

def annoying_message():
    global count
    count +=1
    print(f'Nudge Nudge, Wink Wink, Say No More Say No More {count}')
    annoying_message()

#forever_recursion()

def forever_recursion2(times): 
    annoying_message2(times)

def annoying_message2(times):
    if times > 0:
        print(f'Nudge Nudge, Wink Wink, Say No More Say No More {times}')
        annoying_message2(times - 1)

# forever_recursion2(50)

# number of times = depth of the recursion


# This program demos the range_sum funtion
def range_sum_ex():
    # create a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # get the sum of the items at indexes 2 thru 5
    my_sum = range_sum(numbers, 2, 5)

    print('The sum of items 2 thru 5 is', my_sum)

# this function returns the sum of a specified range of litems in a list. the start parameter specifies the index of the starting ite,. the end paramenter specifies the index of the ending item
def range_sum(num_list, start, end):
    # base case
    if start > end:
        return 0
    # recursive case
    else:
        return num_list[start] + range_sum(num_list, start+1, end)

#range_sum_ex()

# the function return the nth number in the fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#this program demos recursion to print nums from the Fibanocci sequaence
def fib_test():
    for n in range(10):
        print(f'The fibanocci of {n} is {fibonacci(n)}')

# fib_test()



# this program uses recursion to find the GCD (greatest common denominator) "divisor" of two numbers

# if x can be evenly divided by y, then gcd(x,y) = y
# otherwise, gcd(x, y) = gcd(y, remainder of x/y)
def greatest_com_denom():
    # Get 2 numbers
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))

    # display the GCD
    print(f'The GCD of {num1} and {num2} is {gcd(num1, num2)}')

# the gcd function returns the greatest common divisor of two numbers
def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)

#greatest_com_denom()


# the Towers of Hanoi
# rules:
    # only one disk moved at a time
    # Disk cannot be placed on top of a smaller disk
    # All discs must be moved from the first to the third peg

# simulate the towers of hanoi games
global moves
moves = 0

def towers_prob():
    # set up initial values
    num_discs = 20
    from_peg = 1
    to_peg = 3
    temp_peg = 2


    # play the games
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the discs are moved')

# move_discs = display a disc move in  the game
#Params:
    #num:       the number of discs to move
    # from_peg: the peg to move from
    # to_peg:   the peg to move to
    # temp_peg:# the temporary peg
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        global moves
        move_discs(num-1, from_peg, temp_peg, to_peg)
        moves +=1
        print(f'Move a disc from Peg {from_peg} to Peg {to_peg} Move: {moves}')
        move_discs(num-1, temp_peg, to_peg, from_peg)
        moves +=1

towers_prob()
def towers_func():
    return 0
