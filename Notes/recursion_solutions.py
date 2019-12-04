"""
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.

2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The
    function should return the value of x times y. Remember, multiplication can be performed
    as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero
    integers.)

3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.

4. Largest List Item
    Design a function that accepts a list as an argument, and returns the largest value in the list.
    The function should use recursion to find the largest item.

5. Recursive List Sum
    Design a function that accepts a list of numbers as an argument. The function should recursively 
    calculate the sum of all the numbers in the list and return that value.

6. Sum of Numbers
    Design a function that accepts an integer argument and returns the sum of all the integers from 1 up 
    to the number passed as an argument. For example, if 50 is passed as an argument, the function will 
    return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.

7. Recursive Power Method
    Design a function that uses recursion to raise a number to a power. The function should
    accept two arguments: the number to be raised and the exponent. Assume that the exponent is a 
    nonnegative integer.

8. Ackermann’s Function
    Ackermann’s Function is a recursive mathematical algorithm that can be used to test how
    well a system optimizes its performance of recursion. Design a function ackermann(m, n),
    which solves Ackermann’s function. Use the following logic in your function:
        If m = 0 then return n + 1
        If n = 0 then return ackermann(m - 1, 1)
        Otherwise, return ackermann(m - 1, ackermann(m, n - 1))
    Once you’ve designed your function, test it by calling it with small values for m and n.

"""

# 1.
# def printNum(n):
#     if n > 1:
#         printNum(n - 1)
#     print (n, sep=" ")

# print(printNum(4))

# 2.
# def multiply(x,y):
#     if x == 0 or y == 0:
#         return 0
#     else:
#         return x + multiply(x, y - 1)
# print(multiply(7,4))

# 3.
# def printLines(n):
#     if n > 1:
#         printLines(n - 1)
#     for _ in range(n):
#         print ("*",end=""),
#     print()

# printLines(3)

# 4.
# numList = [3,8,5,6]
# def findLargest(numlist):
#     n = len(numlist)
#     if n == 1:
#         return numlist[0]
#     else:
#         temp = findLargest(numlist[0:n-1])
#         if numlist[n-1]> temp:
#             return numlist[n-1]
#         else:
#             return temp
# print(findLargest(numList))

# 5.
# numList = [3,4,5,6]
# def sum_nums(numlist):
#     n = len(numlist)
#     if len(numlist) == 1:
#         return numlist[0]
#     else:
#         return numlist[n-1] + sum_nums(numlist[0:n-1])

# print(sum_nums(numList))

# 6.
# def sumNums(n):
#     if n == 0:
#         return n
#     else:
#         return n + sumNums(n -1)
# print(sumNums(8))

# 7. 
# def power(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)
# print(power(3,3))

# 8.
# def main():
#     num1 = Ackermann(0,3)
#     print (num1)
#     num2 = Ackermann(2,0)
#     print (num2)
#     num3 = Ackermann(2,3)
#     print (num3)
# def Ackermann(m,n):
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return Ackermann(m-1, 1)
#     else:
#         return Ackermann(m-1, Ackermann(m,n-1))
# main()