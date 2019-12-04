"""
1. Using box and pointer notation, draw a picture of the nodes created by the 
first loop in the tester program. 
"""
# |head| => D1|pointer => D2|pointer => D3|pointer => D4|pointer => D5|None

"""

2. What happens when a programmer attempts to access a node’s data fields when 
the node variable refers to None? How do you guard against it?

"""
# AttributeError: 'NoneType' object has no attribute 'data'
# while head != None

"""

3. Write a code segment that transfers items from a full array to a singly linked 
structure. The operation should preserve the ordering of the items.

"""
# class Node():
#     def __init__(self, data, next = None):
#         # instantiates a Node with a default next of none
#         self.data = data
#         self.next = next

import random
from linked_structure import Node

def node_maker(p_list):
    head = None
    i = len(p_list)-1
    # Add 5 nodes to the begining of the the linked structure
    #for item in p_list:
    #    head = Node(item, head)

    while i >= 0:
        head = Node(p_list[i], head)
        i-=1

    # print the contents of the structure
    while head != None:
        print(head.data, end=', ')
        #print(head.next)
        head = head.next

def main(size = 8):
    the_list = []
    for count in range(size):
        the_list.append(random.randint(1, size+1))
    print(the_list)
    node_maker(the_list)

main(8)