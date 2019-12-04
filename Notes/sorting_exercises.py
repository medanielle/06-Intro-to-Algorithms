"""
1. The list method reverse reverses the elements in the list. Define a function named reverse that 
reverses the elements in its list argument (without using the method reverse). Try to make this 
function as efficient as possible, and state its computational complexity using big-O notation. 
"""
import random

def my_reverse(p_list):
    new_list = []
    for item in p_list:
        new_list.insert(0, item)
    return new_list

def main(size = 8, reverse = my_reverse):
    the_list = []
    for count in range(size):
        the_list.append(random.randint(1, size+1))
    print(the_list)
    new_list = reverse(the_list)
    print(new_list)

main()

# big-O notation = O(log n)

"""
2. Python’s pow function returns the result of raising a number to a given power. Define a function 
expo that performs this task and state its computational com-plexity using big-O notation. The first 
argument of this function is the number, and the second argument is the exponent (nonnegative numbers only). 
You can use either a loop or a recursive function in your implementation, but do not use Python’s ** operator 
or pow function. 
"""

def recursive_power(x,y):
    if y == 0:
        return 1
    else:
        return x * recursive_power(x, y - 1)
print(recursive_power(3, 1))

def loop_power(x, y):
    ans = x
    for i in range(y-1):
        ans *= x
    return ans

print(loop_power(3, 1))

# big-O notation = O(log n)