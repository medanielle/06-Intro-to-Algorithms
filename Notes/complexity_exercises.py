"""
1. Assume that each of the following expressions indicates the number of 
operations performed by an algorithm for a problem size of n. Point out 
the dominant term of each algorithm and use big-O notation to classify it. 
"""
    # a. 2^n - 4n^2 + 5n      =       O(2^n) (exponential)
    # b. 3n^2 + 6             =       O(n^2) (quadratic)
    # c. n^3 + n^2 - n        =       O(n^3) (polynomial)
"""
2. For problem size n, algorithms A and B perform n^2 and (1/2)n^2 + (1/2)n 
instructions, respectively. Which algorithm does more work? Are there particular 
problem sizes for which one algorithm performs significantly better than the 
other? Are there particular problem sizes for which both algorithms perform 
approximately the same amount of work?
"""
# same order of complexity for each

# but more work is done on the second

"""

3. At what point does an n^4 algorithm begin to perform better than a 2^n algorithm?

"""

# mine = WRONG = ...After n = 4

# Right = 17 ... no idea ... print statements... FUCK OFF

def poly():
    num = 0
    work = 1
    for x in range(20):
        for y in range(20):
            work =+ 1
            work -= 1
            num += 1


#poly()