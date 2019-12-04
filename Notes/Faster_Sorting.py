"""
Faster Sorting

Up until now we have learned about sorting methods with a O(n^2) complexity. Even with modification they are only marginally faster.

Let's now discuss some algorithms with a complexity of O(logn) or O(n log n)
THe scret here is that we use out divide and conquer strategy

Each algorithm finds a way of breaking the list into smaller lists. Then, these sublists are sorted recursively. The number of subdivisionsis log(n) and the amount of work needed to rearrange the data on each subdivision is n, thus making our complexity O(n log n)

"""
# the swap func
def swap(my_list, i, j):
    #exchange positions of i and j
    temp = my_list[i]
    my_list[i]= my_list[j]
    my_list[j]= temp
"""
****************************  QUICK SORT  ********************************
"""
# The stregety here is that we start with a PIVOT. Pivot can be anywhere but lets just start by setting our pivot to the midpoint

# Partition items in the list so that all items less that the pivot are moved to the left of the pivot, and the rest are moved to its right. The final position of the pivot after the list is sorted could be at the end of the list or the begining of the list depending on the size of the item

# Divide and Conquer - Reapply the process recursively to the sublists formed by splitting the list at the pivot. One sublist consists of all items to the left of the pivot (now the smaller ones), and the other sublist has all the ite,s to the right (larger items)

# the process terminates each time it encounters a sublist with fewer that two items

def quick_sort(my_list):
    quick_helper(my_list, 0, len(my_list) - 1)

# recursive func to hide extra arguments
def quick_helper(my_list, left, right):
    if left < right:
        pivot_loc = partition(my_list, left, right)
        # recursively calls quick sort helper for the left of the partition
        quick_helper(my_list, left, pivot_loc - 1)
        #recursively calls quick sort helper for the right partition
        quick_helper(my_list, pivot_loc +1, right)

def partition(my_list, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = my_list[middle]
    my_list[middle] = my_list[right]
    my_list[right] = pivot 
    # set boundary point to first point
    boundary = left
    # move items less than pivot to the left
    for index in range(left, right):
        if my_list[index] < pivot:
            swap(my_list, index, boundary)
            boundary += 1
    #exchange the pivot item and the boundary item
    swap(my_list, right, boundary)
    return boundary

import random

def main(size = 20, sort_this = quick_sort):
    my_list = []
    for count in range(size):
        my_list.append(random.randint(1, size+1))
    print(my_list)
    sort_this(my_list)
    print(my_list)

#main()
""""
*************** Merge sort ***********************
- Divide and Conquer strategy
- Compute the middle positions of a list and recursively sort its left and right sublists
- Merge the two sorted sublists back into a single sorted list
- stop the process when sublists can no longer be subdivided
"""
from array import array

def merge_sort(my_list):
    # copyBuffer is temporary space needed during this merge
    copyBuffer = array(len(my_list))
    merge_sort_helper(my_list, copyBuffer, 0, len(my_list)-1)

# my_list = list being sorted
# copyBuffer = temp space needed during merge
# low, high = bounds of sublist
# middle = midpoint of sublist

def merge_sort_helper(my_list, copyBuffer, low, high):
    if low < high:
        middle = (low + high)//2
        merge_sort_helper(my_list, copyBuffer, low, middle) 
        merge_sort_helper(my_list, copyBuffer, middle+1, high)
        merge(my_list, copyBuffer, low, middle, high)

# my list, copybuffer, low, middle, high are all same as above
# low begingin of first sorted sublist, (middle is the end)
# middle + 1 = beginning of second sorted sublist (high is the end)
# initalize i1 and i2 to first items in each sublist

"""
- set up index pointers to the first ite,s in each sublist (low and middle+1)
- Starting with the first item in each sublist, repeatedly compare items. Copy the smaller item from its sublist to the copy buffer and advance to the next item in the sublist
- Copy the portion of copyBuffer between low and high back to the corresponding positions in my_list
"""
def merge(my_list, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle +1
    # put items from sublists into copyBuffer so order is maintained
    for i in range(low, high+1):
        if i1 > middle:
            #first subset exhausted
            copyBuffer[i] = my_list[i2]
            i2 += 1
        elif i2 > high:
            # second subset exhausted
            copyBuffer[i] = my_list[i1]
        elif my_list[i1] < my_list[i2]:
            copyBuffer[i] = my_list[i]
            i1 += 1
        else: 
            copyBuffer[i] =my_list[i2]
            i2 += 1
    # Copy sorted items back into proper positions in the list
    for i in range(low, high+1)
        my_list[i = copyBuffer[i]]
