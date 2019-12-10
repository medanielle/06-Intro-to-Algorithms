"""
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.
"""

def r_print_func(n):    
    # base case
    if n == 1:
        print('1')
    # recursive case
    else: 
        r_print_func(n-1)
        print(n)

# r_print_func(10)

"""
2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The function should return the value of x times y. Remember, multiplication can be performed as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero integers.)
"""

def r_multi_func(x, y):
    # base case
    if y == 0:
        return 0
    # recursive case
    else:
        return x + r_multi_func(x, y-1)

#print(r_multi_func(4,7))

"""
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line showing 2 asterisks, up to the nth line which shows n asterisks.
"""
def r_lines_func(n):
    if n > 1:
        r_lines_func(n-1)
    print('*' * n)

def r_lines(n):
    # base case
    if n == 1:
        print("*")
        return
    # recursive case
    else:
        r_lines(n-1)
        print('*' * n)

# r_lines(4)

# r_lines_func(4)

"""
4. Largest List Item
    Design a function that accepts a list as an argument, and returns the largest value in the list. The function should use recursion to find the largest item.
"""
my_list = [10, 7, 11, 0]

def large_list(p_list):
    # set-up index
    idx = len(p_list) - 1
    # base case
    if idx == 0:
        print('Largest Value is', p_list[idx])
    # recursive case
    else:
        # check which one is larger and pop out the one that is smaller
        if p_list[idx] > p_list[idx - 1]:
            p_list.pop(idx-1)
        else:
            p_list.pop(idx)
        # run function again for recursive
        large_list(p_list)

    """
    else:
        num_find = lambda x , y, num_list: num_list.remove(x) if x<=y else num_list.remove(y)
        numfind
    """
# large_list(my_list)

"""
5. Recursive List Sum
    Design a function that accepts a list of numbers as an argument. The function should recursively calculate the sum of all the numbers in the list and return that value.
"""
def sum_list(p_list, sum_num=0):
    # set up index
    idx = len(p_list) - 1
    # base case
    if idx == 0:
        print('The sum is', sum_num)
    # recursive case
    else:
        return sum_list(p_list, sum_num + p_list.pop(idx))

    """
    if index < len(my_list):
        return my_list[index] + sum_list(my_list, index)
    else: 
        return 0
    """

#sum_list(my_list)

"""
6. Sum of Numbers
    Design a function that accepts an integer argument and returns the sum of all the integers from 1 up to the number passed as an argument. For example, if 50 is passed as an argument, the function will return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.
"""

def r_sum(n):
    # base case
    if n == 0:
        return 0
    # recursive case
    else:
        return n + r_sum(n-1)

#print(f'The sum of 1-10 is {r_sum(10)}')

"""
7. Recursive Power Method
    Design a function that uses recursion to raise a number to a power. The function should accept two arguments: the number to be raised and the exponent. Assume that the exponent is a nonnegative integer.
"""

def r_power(n, e):
    # base case
    if e == 0:          #if e ==1:
        return 1            #return n
    # recursive case
    else:
        return n * r_power(n, e - 1)

# print(f"2 raised to the power 6 is {r_power(2, 6)}")

"""
8. Ackermann’s Function
    Ackermann’s Function is a recursive mathematical algorithm that can be used to test how well a system optimizes its performance of recursion. Design a function ackermann(m, n), which solves Ackermann’s function. Use the following logic in your function:
        If m = 0 then return n + 1
        If n = 0 then return ackermann(m - 1, 1)
        Otherwise, return ackermann(m - 1, ackermann(m, n - 1))
    Once you’ve designed your function, test it by calling it with small values for m and n.
"""
def r_ackermann(m, n):
    # base case for 
    if m == 0:
        return n+1
    # 2 recursive cases
    elif n== 0:
        return r_ackermann(m - 1, 1)
    else:
        return r_ackermann(m - 1, r_ackermann(m, n - 1))

# print(r_ackermann(2,2))
