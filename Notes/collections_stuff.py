              ######################### COLLECTION TYPES ################################
"""
collection - a group of zero or more objects that can be treated as a conceptual unit. Things like strings, list,               tuples, dictionaries

            other types of collection include queues, priority queues, binary search trees, heaps graphs and bags

linear collection - like people in a line, they are ordered by position; each item except the first has a unique                predessor(or place in line)

        EX: grocery list, stack of dinner plates, line at the ATM 

Hierarchical collection - ordered in s structure resembling and updaide down tree. Each data item ex ept the one at             the top has just one predecessor called its parent, but potentially has manny successors called children

        EX: a file directory system, a company's organizational tree, and a book's table of contents

Graph collection - also called a graph, each item can have many predecessors and many successors. 
            These are alos called neighbors.

        EX:  airline routes between cities, electrical wiring diagram, the world wide web

Unordered Collections - These are not in any particular order, and its not possible to meaningfully speak of an                 items predecessor or successor.

        EX: a bag of marbles

"""



              ######################### OPERATION TYPES ################################

"""
Determine the size - Use Python's len function to obtain the number of items currently in the collection

Test for item membership - use Python's in operator to search for a given target item in the collections. Returns               True if item is found and False otherwise

Traverse the collection - loops - Use python's for loop to visit each item in the collection.
            The order which items are visited depends on the type of collection

Obtain a string representation - use python's str function to obtain the string representation of the collection

Test for equality ** IMPORTANT ** - use python's == operator to determine whether the two collections are equal.
            Two collections are equal if they are of tthe same type and contain the same items. The order in which pairs of items are compared depends on the type of collection

Concatenate two collection - use python's + operator to obtain a new collection of the same type as the operands
            and containing the items in the two operands

Insert an item - add an item to the collection, possible at a given position

Remove an item - Remove an item from the collection, possible at a given position

Replace an item - combine removal and insertion into one operation

Access or Retrieve an item - obtain an item, possibly at a given position

EX: pop, popitem, remove (set or list)

"""

# Next algorith.py

