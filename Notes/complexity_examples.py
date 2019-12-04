# this prints the running times for problem sizes that double using a single loop

import time

def benchmark1():
    problem_size = 10000000

    for count in range(5):
        start = time.time()
        # the start of the slogrithm
        work = 1
        for x in range(problem_size):
            work += 1
            work -= 1

        # the end of the algorithm

        elapsed = time.time() - start
        print(f'{problem_size} - {elapsed}')
        problem_size *=2

#first()
        """ Output
    10000000 - 1.6076991558074951
    20000000 - 2.979032039642334
    40000000 - 5.941112995147705
    80000000 - 12.23102855682373
    160000000 - 23.845795392990112"""


def benchmark2():
    problem_size = 1000   # significatnly reduced!!!

    for count in range(5):
        start = time.time()
        # the start of the slogrithm
        work = 1
        for j in range(problem_size):
            for k in range(problem_size):
                work += 1
                work -= 1

        # the end of the algorithm

        elapsed = time.time() - start
        print(f'{problem_size} - {elapsed}')
        problem_size *=2
""" Output :
1000 - 0.0817406177520752
2000 - 0.3869640827178955
4000 - 1.554842233657837
8000 - 5.020118474960327
16000 - 19.252073049545288"""
#second()

def counting():

    problem_size = 1000   # significatnly reduced!!!

    for count in range(5):
        number = 0
        # the start of the slogrithm
        work = 1
        for j in range(problem_size):
            for k in range(problem_size):
                number += 1
                work += 1
                work -= 1

        # the end of the algorithm

        print(f'{problem_size} - {number}')
        problem_size *=2

# counting()

""" Output :
1000 - 1000000
2000 - 4000000
4000 - 16000000
8000 - 64000000
16000 - 256000000"""

# Prints the number of calls of a recursive Fibonacci function with problem sizes that double

# from collections import Counter
"""this import wouldn't work... had to comment out code...
"""
def fib(n, counter):
    # count the number of calls of the fib func
    # Counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)


def count_fib():
    for count in range(5):
        problemSize = 2
        counter = 0 # Counter()
        # The start of the algorithm
        fib(problemSize, counter)
        # the end of the algorithm
        print(problemSize, counter)
        problemSize *= 2

#count_fib()

