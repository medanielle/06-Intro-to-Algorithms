        ############################  ALGORITHMS  ################################

"""
    Algorithm - describes a computation process that halts with a solution to a problem'
        There are many criterai for assessing he queailty of an algorim.

        The most essitential is correctness, It actually solves the problem it is meant to solve

        Readibilty and ease of maintenance are also important qualities

        Run time performance is one of the most important qualities

    Benchmarking - measure the time cost of an algorith to obtain actual run time

    Counting - another technique used to  estimate the efficiency of an algorithm with different problem sizes
        Keep in mind you are counting the instructions in the high-level code in which the algorithm

"""

        ############################  COMPLEXITY ANALYSIS  ############################

'''
Complexiity Analysis - a method of determining the efficiency of algorithms that allows you to rate them                    independently of platform-dependent timings or impractical instruction counts

Order of Complexity - the difference in performance of your algorithms

    linear - (n) - grows in direct proportion to thhe problem size
    
    quadratic - (n^2) - grows as a function of the square of the problem size

    constant - ... doesn't define, self-explanatory...

    logarithmic - proportional to the log base 2 of the problem size

    polynomial time - (n^3, etc) - grows at a rate of n raised to the k

    exponential - WORST PERFORMANCE - (2^n) - a growth rate of 2 rasied to the nth. These are 
            impracticcal to run with large problem sizes

'''
        c

"""
dominant - The term with for the ammount of work in an algorithm that becomes so large that 
        you can ignore the amount of work represented by the other terms

        (.5)n^2 -(.5)n
        n^2 is the dominant here

        Represented with Big-O Notation:
        O(n^2)

constants of proportionailty ( ignore the (.5) and the -n above, only keep n^2

"""
############################  BIG-O NOTATIONS PART 2  ############################

"""
Constatnt O(1)
        - Time taken is independent of the amount of data
        - Stack push, pop, and peek; Queue, dequeue, and enqueue; Insert a mode into a linked list

Linear O(n)
        - Time taken is directly proportional to the amount of data
        - linear search; count items in a list; compare a pair of strings

Quadratic O(n^2)
        - Time taken is proportional to the amount of data squared; twice as wichdata takes 4 times (3 = 9 times); poor scalability

Polynomial O(n^k)
        - Time taken is proportional to the emaount of data raised to the power of a constant

Logarithmic O(log n)
        - Time taken is proportional to the logarithm of the amount of data, good scalability.
        - Binary search a sorted list; search a binary tree; *** Divide and Conquer *** algoritm approaches

linearithmic O(n log n)
        - Time taken is proportional to the logarithm og the amount of data, multipled by the amount of data

exponential O(k^n)
        - Time taken is proportional to a constant  raised to the power of the amount of data, very poor scalability almost immediately 
        - if constant k is 10, then for each new pitem of data will slow the program down by 10 times

Logarithms - the inverse of exponentiation
    Generally
        x^z = y                         log base x of y = z

        2^0 = 1                         log base 2 of 1 = 0
        2^1 = 2                         log base 2 of 2 = 1
        2^2 = 4                         log base 2 of 4 = 2
        2^3 = 8                         log base 2 of 8 = 3
        2^4 = 16                        log base 2 of 16 = 14

        10^4 = 10000                    log base 10 of 10000 = 4

notice that each number we are calculating is ... 
