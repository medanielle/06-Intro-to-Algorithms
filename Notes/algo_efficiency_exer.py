"""
1. Write a tester program that counts and displays the number of iterations 
    of the following loop: 
    
    while problemSize > 0:
        problemSize = problemSize // 2
"""
def loop_counter(problemSize = 100):
    count = 0
    while problemSize > 0:
        #print(count, problemSize)
        problemSize = problemSize // 2
        count += 1
    #print('Count =', count)
    return count

#loop_counter()
"""
2. Run the program you created in Exercise 1 using problem sizes of 
    1000, 2000, 4000, 10,000, and 100,000. As the problem size doubles 
    or increases by a factor of 10, what happens to the number of iterations?
"""
def loop_examples():
    listy = [1000, 2000, 4000, 10000, 100000]
    for num in listy:
        print('Problem Size :', num, end='\t')
        my_count = loop_counter(num)
        print('Count :', my_count)

#loop_examples()

# Output:
# Problem Size : 1000     Count : 10
# Problem Size : 2000     Count : 11
# Problem Size : 4000     Count : 12
# Problem Size : 10000    Count : 14
# Problem Size : 100000   Count : 17

"""
3. The difference between the results of two calls of the function time.time() 
    is an elapsed time. Because the operating system might use the CPU for part 
    of this time, the elapsed time might not reflect the actual time that a 
    Python code segment uses the CPU. Browse the Python documentation for an 
    alternative way of recording the processing time, and describe how this 
    would be done.

"""

# def test():
#     """Stupid test function"""
#     L = []
#     for i in range(100):
#         L.append(i)

# def my_timeit():
#     import timeit
#     print(timeit.timeit("loop_counter()", setup="from __main__ import loop_counter", number=2))

def my_timeit():
    import timeit
    total_time = timeit.timeit("loop_counter()", setup="from __main__ import loop_counter", number=5000)
    avg = total_time/5000
    print('Total', total_time, '\tAvg', avg)

#my_timeit()

def my_repeat():
    import timeit
    time_list = timeit.repeat('loop_counter()',setup="from __main__ import loop_counter",number = 10, repeat=10)
    # "loop_counter()", setup="from __main__ import loop_counter", number=5000)
    avg = sum(time_list)/10
    print(f'Avg: {avg:.8f}')

#my_repeat()