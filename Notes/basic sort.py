"""
Basic sort algo

the algo examined here are easy to write but are ineffiecient
Eacvh alog we discuss here will utilze a list of integers and the swap func defined below
"""

# the swap func
def swap(my_list, i, j):
    #exchange positions of i and j
    temp = my_list[i]
    my_list[i]= my_list[j]
    my_list[j]= temp

"""
*****************************  Selection Sort  ********************************
"""

# Each pass through the main loop selects a single item to be moved
# Searches the list for the position of the smallest item
# If that posistion is not the first position, it swaps the items at those positions
# it then finds the next smallest item and swaps the item in the second position and so on

def select_sort(my_list):
    i = 0
    # do n-1 searches for the smallest
    while i < len(my_list)-1:
        minIndex = i
        j = i+1
        # Start the search
        while j < len(my_list):
            if my_list[j] < my_list[minIndex]:
                minIndex = j
            j += 1
        # Exchange if needed
        if minIndex != i:
            swap(my_list, minIndex, i)
        i += 1

# Math(not important) = (n-1)+ (n-2) + ... + 1 =
'''
(1/2)n^2 - (1/2)n
O(n^2)
Because data items are swapped only in the outer loop, this additional cost for selection sort is linear in the worst and average cases
'''

"""
*****************************  Bubble Sort  ********************************
"""

# the strategy is to start at the begining of the list and compare pairs of data items as it moves down the end. Each time the items in the pair are out of order, the algoritm swaps them. THe largest item will eventually 'bubble' out to the end of the list. The algorithm repeats this process until the list is sorted from smallest to largest

def bubble_sort(my_list):
    n = len(my_list)
    # do n-1 searches
    while n > 1:
        i = 1
        # Start each bubble
        while i < n:
            if my_list[i] < my_list[i-1]:
                #exchange if needed
                swap(my_list, i, i-1)
            i += 1
        n -= 1

"""
(1/2)n^2 - (1/2)n

O(n^2)
"""

# update bubble sort  to linear time completely
# in our best case scenario where our list is already sorted, there are **no swaps**
# so we can modify our algoritm to be more effienct

def bubble_sort(my_list):
    n = len(my_list)
    # do n-1 searches
    while n > 1:
        swapped = False
        i = 1
        # Start each bubble
        while i < n:
            if my_list[i] < my_list[i-1]:
                #exchange if needed
                swap(my_list, i, i-1)
                swapped = True
            i += 1
            # return if no swaps
        if not swapped: return
        n -= 1


"""
***********************  INsertion Sort ***************************
"""
# On the ith pass thru the list, where i ranges from 1 thru n-1, the ith item should be inserted into its proper place among the first i items in the list

# After the ith pass, the first i items should be in sorted order

# This process is analogous to the way in which many people organize playing cards

# Insertion sort consostes of two loops. the outer loop traverses the positions from 1 to n-1. For each position i in this loop, you save the item and start the inner loop at position i-1. For each position j in this loop, you move the item to j+1 until you find the insertion point for the saved(ith) item

# Insertion sort is good for partially sorted list due to the inner loop

def insert_sort(my_list):
    i = 1
    while i < len(my_list):
        itemToInsert = my_list[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < my_list[j]:
                my_list[j+1]=my_list[j]
                j -= 1
            else:
                break
        my_list[j+1] = itemToInsert
        i += 1
