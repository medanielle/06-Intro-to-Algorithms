"""
Running things concurrently is known as multithreading
running things in parallel is known as multiprocessing

I/O bound tasks - Waiting for input to be completed,
                  reading and writing from file system, 
                  network operations.
                  These all benefit more from threading 
                  You get the illusion of running code at the same time,
                    however other code starts running while other code is waiting

CPU bound tasks - Good for number crunching
                    using CPU
                    data crunching
                    These benefit more from multiprocessing and running in parallel
                    Using multiprocessing might be slower if you have overhead from creating and destoying files

"""

import time

def do_something():
        print('Sleeping 1 sec')
        time.sleep(1)
        print('Done Sleeping')

def without_thread():
    start = time.perf_counter()

    do_something()
    """ Output:
    Sleeping 1 sec
    Done Sleeping
    Finished in 1.0015156 second(s)
    """
    do_something()
    """ Output:
    Sleeping 1 sec
    Done Sleeping
    Sleeping 1 sec
    Done Sleeping
    Finished in 2.005114 second(s)
    """
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')

#without_thread()


# Multithreading 2.py

import threading
def with_thread():
    start = time.perf_counter()

    # create 2 threads
    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)

    # start the thread
    t1.start()
    t2.start()

    # make sure the threads complete before moving on to calculate finish time
    t1.join()
    t2.join()

    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')
""" Output with 1 thread created & started:
Sleeping 1 sec
Finished in 0.0010092999999999977 second(s)
Done Sleeping
"""
"""output with 2 threads but no join:
Sleeping 1 sec
Sleeping 1 sec
Finished in 0.0013084999999999972 second(s)
Done Sleeping
Done Sleeping
"""
# with_thread()
""" Final Output:
Sleeping 1 sec
Sleeping 1 sec
Done Sleeping
Done Sleeping
Finished in 1.0035284 second(s)
"""

# Multithreading 2.py

#Run 10 threads

def run_10_threads():
    start = time.perf_counter()

    #intialize list of threads
    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_some_with_var)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')

# run_10_threads()

""" Output:
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Sleeping 1 sec
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Done Sleeping
Finished in 1.052076 second(s)
"""

def do_some_with_var(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    #print("Done Sleeping") commented out in multithreading 3
    return f"Done Sleeping ... {seconds}"

# Multithreading 3.py

# Using multithreading is the older way 
#python 3.2 introduced something called thread pull execturot
# no longer need threading module /  we use concurrent.futures module instead

import concurrent.futures
import time

def run_new_threads():
    start = time.perf_counter()

    # using a context manager
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # submit schedules a func to be excuted one at a time and returns a future object
        f1 = executor.submit(do_some_with_var, 1)
        f2 = executor.submit(do_some_with_var, 2)

        print(f1.result())
        print(f2.result())
    
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')

""" Output:
Sleeping 1 second(s)
Sleeping 2 second(s)
Done Sleeping
None
Done Sleeping
None
Finished in 2.0072525999999997 second(s)
"""

#run_new_threads()

def run_10_new_threads():
    start = time.perf_counter()

    # using a context manager
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #list comprehension to create multiple threads
        results = [executor.submit(do_some_with_var, 1) for _ in range(10)]
        #to get the results we can use another function, as completed() from future object that gives us an iterator
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')

# run_10_new_threads()


# Multithreading 4.py
"""
Prove that these are actually coming is as they are completed 
    lets pass i a range of seconds
    start 5 second thread first
"""


def run_range_threads():
    start = time.perf_counter()

    # using a context manager
    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds_list = [5, 4, 3, 2, 1]
        #list comprehension to create multiple threads
        results = [executor.submit(do_some_with_var, sec) for sec in seconds_list]
        #to get the results we can use another function, as completed() from future object that gives us an iterator
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')
""" Out put:
Sleeping 5 second(s)
Sleeping 4 second(s)
Sleeping 3 second(s)
Sleeping 2 second(s)
Sleeping 1 second(s)
Done Sleeping ... 1
Done Sleeping ... 2
Done Sleeping ... 3
Done Sleeping ... 4
Done Sleeping ... 5
Finished in 5.0071624 second(s)
"""
# start 5 second thread first, but since we use as completed() method it prints the reults in the order they are completed

# run_range_threads()


# Multithreading 5.py
"""
with the submit method, it submits each function one at a time, so we can use submit method on an entire list
"""
def run_map_threads():
    start = time.perf_counter()

    # using a context manager
    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds_list = [5, 4, 3, 2, 1]

        # map will apply the function do_some_with_var to every item in the seconds_list instead of running the results as they complete, map returns in the order that they were started
        results = executor.map(do_some_with_var, seconds_list)

        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')

run_map_threads()
""" Output:
Sleeping 5 second(s)
Sleeping 4 second(s)
Sleeping 3 second(s)
Sleeping 2 second(s)
Sleeping 1 second(s)
Done Sleeping ... 5
Done Sleeping ... 4
Done Sleeping ... 3
Done Sleeping ... 2
Done Sleeping ... 1
Finished in 5.0084417000000006 second(s)
"""