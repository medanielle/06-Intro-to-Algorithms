"""
1. Suppose that a list contains the values 20, 44, 48, 55, 62, 66, 74, 88, 93, 99 
at index positions 0 through 9. Trace the values of the variables left, right, and 
midpoint in a binary search of this list for the target value 90. Repeat for the 
target value 44.
"""


def my_bin(p_target, p_list):
    left = 0
    right = len(p_list) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, p_list[mid], right)
        if p_target == p_list[mid]:
            return mid
        elif p_target < p_list[mid]:
            right = mid - 1
        else: 
            left = mid + 1
    return -1

# the_list = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
# print(my_bin(90, the_list))

"""
2(challenge). The method that’s usually used to look up an entry in a phone book is not 
exactly the same as a binary search because, when using a phone book, you don’t always go 
to the midpoint of the sublist being searched. Instead, you estimate the position of the 
target based on the alphabetical position of the first letter of the person’s last name. 

For example, when you are looking up a number for “Smith,” you look toward the middle of 
the second half of the phone book first, instead of in the middle of the entire book. 
Suggest a modification of the binary search algorithm that emulates this strategy for a 
list of names. Is its computational complexity any better than that of the standard 
binary search? 

"""
import timeit
#def wrapper(func, *args, *...)

def my_name_bin(p_target, p_list):
    left = 0
    right = len(p_list) - 1
    # print(p_target, left, right)
    # left, right = get_start(p_target, p_list)
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, p_list[mid], right)
        if p_target == p_list[mid]:
            return mid
        elif p_target < p_list[mid]:
            right = mid - 1
        else: 
            left = mid + 1
    return -1

def get_start(p_target, p_list):
    #print(p_target, p_target[0].lower())
    if p_target[0].lower() < 'g':
        left = 0
        right = len(p_list) // 4
    elif p_target[0].lower() < 'm':
        left = len(p_list) // 4
        right = len(p_list) // 2
    elif p_target[0].lower() < 's':
        left = len(p_list) // 2
        right = int(len(p_list)*.75)
    else:
        left = int(len(p_list)*.75)
        right = len(p_list) - 1
    return left, right


def test():
    the_list = ['Amanda', 'Bambi', 'Charlie', 'Daniel', 'Eric', "Fox", "Gary", 'Henry', "Indy", 'James', 'Kelly', 'Linda', 'Molly', 'Nick', 'Oprah', 'Patty', "Q", "Randy",'Sally', 'Tammy', 'Ursula', 'Vicky', 'Wanda', 'Xena', 'Yolanda', 'Zip']
    for name in the_list:
        print(my_name_bin(name, the_list))

print(timeit.timeit('test()', setup="from __main__ import test", number=50))

"2.0554354 -> with get start"
"2.7081965 -> w/o get start"