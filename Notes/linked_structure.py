'''
*****************  Linked Structures  ***************************

A linked Structure is a concrete data type that implements many types of collections, including lists.

As the names implies, a linked structure consists of items that are linked to other items. The two that we'll go over are Singly Linked Structures and Doubly-Linked Structures

 - Head Link - the first item of a linked structure
 - Tail Link - an external link in a doubly linked structure to access the last item directly
 - Empty Link - the absence of a link, indicated by the slash in the diagram

 - The last item in either strucure has no link to the next item

 - Node - The basic unit of representation in a linked structure
    - comprised of two items
        - A Data Item
        - A link to the next node in the structure

In python, we set up nodes and linked strucutres by using references to objects
'''

# this class will represent a singly linked structure

class Node():
    def __init__(self, data, next = None):
        # instantiates a Node with a default next of none
        self.data = data
        self.next = next


# This linkedlist class will instantiate Node objects and we'll add methods to this class to add functionality
class LinkedList:
    def __init__(self):
        self.head = None


def example():
    # just an empty link
    node1 = None

    # A node containing data and empty link
    node2 = Node('A', None)

    # a node with a link
    node3 = Node('B', node2)

    print(node3.data)


def test_node():
    head = None
    # Add 5 nodes to the begining of the the linked structure
    for count in range(5, 0, -1):
        head = Node(count, head)

    # print the contents of the structure
    while head != None:
        print(head.data)
        # print(head.next)
        head = head.next

# test_node()

"""
- One pointer, head, generates the linked structure. This pointer is manipulated in such a way that the most recently inserted item is alwaysat the beginining of the structure

- When the data is displayed, they appear in the reverse order of their insertion

- Also, when the data are displayed, the head poointer is reset to the next node, until the head pointer becomes none. Thus, at the end of this process, the nodes are effectively deleted from the linked structure. They are no longer available to the program and are recycled during the next garbage collection
"""

"""
*****************  Operations on Linked Structures  ***************************
"""
"""
- Arrays are already index based, because the indices are an integral part of the array structure

- We must emulate index-based operations on a linked structure by manipulating link within the structure.
"""
def create_nodes():
    head = None
    # Add 5 nodes to the begining of the the linked structure
    for count in range(1, 6):
        head = Node(count, head)
    return head

def print_node(head):
    # print the contents of the structure
    while head != None:
        print(head.data)
        # print(head.next)
        head = head.next

"""
- Traversal - uses a temporary pointer variable named probe. THis variable is initialized to the link structure's           head pointer and then controls a loop as follows:
"""
        # probe = head
        # while probe != None:
        #     # other code here
        #     probe = probe.next

"""
- Searching - The sequential search of a linked structure resembles a traversal in that you must start at the first         node and follow links until you reach a sentinel

        - two possible sentinels, empty link( end of structure), or you find your item
"""
        # probe = head 
        # while probe != None and target_item != probe.data:
        #     probe = probe.next
        
        # if probe != None:   # meaning it equals SOMETHING, stopped before the end
        #     # if you found your item, some code
        # else:
        #     # your target isn't in the the list

def test_search(head, target_item = 3):
    probe = head 
    while probe != None and target_item != probe.data:
        probe = probe.next
    
    if probe != None:   # meaning it equals SOMETHING, stopped before the end
        print(target_item, '=', probe.data)
    else:
        print(target_item, '= Not there')

# print_node(create_nodes())
# print()
# test_search(create_nodes(),4)
# test_search(create_nodes(),10)

"""
- Accessing our ith item
    Similar to a sequesntial search, we can't go straight to i

    start at the first node and count the number of links until you reach the ith node
    
    Link
"""
            # index = (what item # you are looking for)
            # # Assumes 0 <= index < n
            # probe = head
            # while index > 0:
            #     probe = probe.next
            #     index -= 1 
            # return probe.data

def test_access_index(head):
    index = 0 # (what item # you are looking for)
    # Assumes 0 <= index < n
    probe = head
    while index > 0:
        probe = probe.next
        index -= 1 
    return probe.data
# print_node(create_nodes())
# print(test_access_index(create_nodes()))

"""
Replacement = Also, employs the traversal pattern. you search for a given item or position and replace that item when found. If If you no item is found then no replacement happend and the operation returns False. If replacement occurs the operation returns True.
"""
        # probe = head 
        # while probe != None and target_item != probe.data:
        #     probe = probe.next
        
        # if probe != None:   # meaning it equals SOMETHING, stopped before the end
        #     probe.data = newItem
        #     return True
        # else:
        #     return False

def test_replace(head, target_item=2):
    probe = head 
    while probe != None and target_item != probe.data:
        probe = probe.next
    
    if probe != None:   # meaning it equals SOMETHING, stopped before the end
        probe.data = 10
        return True, probe.data
    else:
        return False

#print_node(create_nodes())
#print(test_replace(create_nodes()))


"""
Inserting at the Begining - better than linear complexity on a linked structure

"""

        # head = Node(newItem, head)

"""
Inserting at the End - Consider two cases
        The head pointer is None, so the head pointer is set to the new node
        The head pointer is not None, so the code searches for the last node and aims its next pointer at the new node.

"""
        # newNode = Node(newItem)   # next=None by default, so you don't need to add it
        # if head is None:
        #     head = newNode
        # else:
        #     probe = head
        #     while probe.next != None:
        #         probe = probe.next
        #     probe.next = newNode


def test_add_end_node(head):
    newNode = Node(10)   # next=None by default, so you don't need to add it
    if head is None:
        head = newNode
    else:
        probe = head
        while probe.next != None:
            probe = probe.next
        probe.next = newNode

    return head

print_node(test_add_end_node(create_nodes()))
"""
Removing at beginning - this operation returns the removed item
"""

        # Assumes at least one node in the structure
        # removed_item = head.data
        # head = head.next
        # return removed_item


"""
Removing at the End - Two cases to consider
        There is just one node. THe Head pointer is set to None.
        There is a node before the last node. the code searchs for the second-to last node and sets its next pointer to None
"""

        # removed_item = head.data
        # if head.next is None:
        #     head = None
        # else: 
        #     probe = head
        #     while probe.next.next !=  None:
        #         probe = probe.next
        #     removed_item = probe.next.data
        #     probe.next = None
        # return removed_item

def remove_from_end(head):
    removed_item = head.data
    if head.next is None:
        head = None
    else: 
        probe = head
        while probe.next.next !=  None:
            probe = probe.next
        removed_item = probe.next.data
        probe.next = None
    return removed_item

# print_node(create_nodes())
# print('\n', remove_from_end(create_nodes()))
"""
Insert at any position - two cases to consider
        1. the node's next pointer is None. This means that i>=n, so you should place the new item at the end of the linked structure
        2. the node's next pointer is not None. that means that 0 < i < n, so you must place the new item between the node at position i-1 and the node at i

"""
    # index = 2
    # if head is None or index <= 0:
    #     head = Node(newItem, head)
    # else:
    #     # search for node at position index -1 or the last position
    #     probe = head
    #     while index > 1 and probe.next != None:
    #         probe = probe.next
    #         index -= 1
    #     # Insert new node after node at posotion i -1 or the last position
    #     probe.next = Node(newItem, probe.next)

def test_insert_node(head, index = 2):
    if head is None or index <= 0:
        head = Node(10, head)
    else:
        # search for node at position index -1 or the last position
        probe = head
        while index > 1 and probe.next != None:
            #print(index, probe.data)
            probe = probe.next
            index -= 1
        # Insert new node after node at posotion i -1 or the last position
        probe.next = Node(10, probe.next)
    return head

# print_node(test_insert_node(create_nodes()))

"""
Removing an item - Consider 3 cases
        1. i<= 0 - you can use the code to remove the first item
        2. 0<i<n - you can search for the node at position i-1, as in insertion, and remove the following Node
        3. i>= n - you remove the last node
"""

    # #Assume that the linked strucutre has at least one item
    # if index <= 0 or head.next is None:
    #     removed_item = head.data
    #     head = head.next
    #     return removed_item
    # else:
    #     # search for node at position index -1 or next to last position
    #     probe = head
    #     while index > 1 and probe.next.next != None:
    #         probe = probe.next
    #         index -= 1
    #     removed_item = probe.next.data
    #     probe.next = probe.next.next
    #     return removed_item

def test_remove_any(head, index = 3):
    #Assume that the linked strucutre has at least one item
    if index <= 0 or head.next is None:
        removed_item = head.data
        head = head.next
        #return removed_item
    else:
        # search for node at position index -1 or next to last position
        probe = head
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        removed_item = probe.next.data
        probe.next = probe.next.next
        #return removed_item
    print(removed_item, '\n')
    return head

# print_node(test_remove_any(create_nodes()))
