'''
Different search algorithms

******************************  Search for the minimum  ******************************
'''
# this function mimics Python's min function
# Use this func to study the complexity of this algorithm by returning the index of the minimum item .
# This algoritm assumes that the list is not empty anf that items are not in a specific order.
# this algorithm starts by treating the first positiom as that of the minimum item. It then searches to the right for a smaller item and if found, resets the position of min to the current position.
# When it reaches the end of the list it returns the position of the min item

def indexOfMin(my_list):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(my_list):                  # O(n) = linear => we iterate through my list only once
        if my_list[currentIndex] < my_list[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

the_list = [2, 3, 4, 1, 10, 7]
# print(indexOfMin(the_list))

'''
******************************  Sequential Search  ******************************
'''
# This function returns the position of the target item if found, or -1 otherwise

def seqSearch(p_target, p_list):
    position = 0
    while position < len(p_list):
        if p_target == p_list[position]:
            return position
        position += 1
    return -1



# the_list = [2, 3, 4, 1, 10, 7]
# print(seqSearch(9, the_list))
# print(the_list[-1])

# best case (its in the first position) (1 iteration)
# worst case (its in the last position) (lenght of list iterations)

"""
You can sometimes have a best, worst and average case performance

binary search
sorting algorithms
link-list
"""
'''
******************************  Binary Search of a Sorted List ******************************
'''
# like searching through a phone book.... looking for a M name... you open the book to the half way poiint to check where you are, then open to the next new point
# target is greater than ... idk very unhelpful teacher/students

#i hate my life so much....

# Used to search an ordered list for a particular value 
# Divide and conquer approach
# Target compared with middle value, then half of the list is "discarded", repeatedly until the target is found
# very effective for large sorted lists


def binarySearch(p_target, p_sortedList):
    left = 0
    right = len(p_sortedList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if p_target == p_sortedList[midpoint]:
            return midpoint
        elif p_target < p_sortedList[midpoint]:
            right = midpoint - 1
        else: 
            left = midpoint +1
    return -1

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(9, the_list))

"""
For a list of size n, we perform te reduction n/2/2 ... until we fet to 1

Let k be the number of times we divide n by 2 then we ger
    n/2^k = 1
    n = 2^k
    k = log base 2 of n

