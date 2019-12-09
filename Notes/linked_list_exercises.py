"""
Core Exercises:

    1. Finish out your doubly and circular linked list to add more functionality
        - prepend
        - insert
        - delete
        - print

    2. Implement a swap_node method to singly and doubly.

    3. Implement a reverse method to singly and doubly.

    4. Modify delete to find the data you want to delete rather than an index.
        Modify delete to take in either an index or data.

    5. Implement a count_ocurrences method.

    6. Create a new file and modify your code to have DoublyLinkedList inherit from your 
        SinglyLinkedList class.

Extras Exercises:

    7. Define a length function that returns the number of items in your linked structure.

    8. Define a function makeDoubly that expects a singly linked structure as its argument. The 
        function builds and returns a doubly linked structure that contains the items in the singly
        linked structure. 

"""

class Node:

    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:

    def __init__(self):
        # constructor
        self.head = None
        self.tail = None

    def display_dlist(self):
        current = self.head
        while current is not None:
            print("Next: ", current)
            current = current.next
        print('-'*30)
        rev = self.tail
        while rev is not None:
            print("Prev: ", rev)
            rev = rev.prev
        print('*'*30)

    def append(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = self.head
        else:
            prev_node = self.tail
            self.tail = new_node
            new_node.prev = prev_node
            prev_node.next = self.tail

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = self.head

    def insert(self, index, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            current = self.head
            while index > 1 or current.next is not self.tail:
                index -= 1
                current = current.next
            if current.next is None:
                new_node.next = current
                new_node.prev = current.prev
                self.tail.next = new_node
                current.prev = new_node
                self.tail = new_node
            else:            
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                
                



    




dlist = DoublyLinkedList()
dlist.append('A')
#dlist.append('B')
#dlist.display_dlist()
#dlist.prepend('1')
#dlist.prepend('-1')
#dlist.display_dlist()
dlist.insert(10, 'test')
dlist.display_dlist()
dlist.insert(3, 'last')