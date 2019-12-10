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

    def display_linked(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # add things to our linked list
    def append(self, data):
        # instantiate a new node
        newNode = Node(data)
        # is there something in our linked list yet?
        if self.head is None:           #could be => if self.head: (since None would be False)
            self.head = newNode
        # there are node(s) in our linked list
        else:
            # intialize our probe pointer
            current_node = self.head
            # is probe at the end of our linked list?
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = newNode


    # add Node to beginning
    def prepend(self, data):
        # instantiate a new node
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    #inserting node within the linked list
    def insert_node(self, index, data):
        # is linked list empty or index less than 0
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        # find our position to insert
        else:
            # search for node at position index -1 or last position
            pointer = self.head
            while index > 1 and pointer.next != None:
                pointer = pointer.next
                index -= 1
            # insert new node after node at position index -1 or last position
            #pointer.next(data, pointer.next)
            pointer.next = Node(data, pointer.next)

    # remove a node
    def delete_node(self, index):
        # is this the only node
        if index <= 0 or self.head.next is None:
            removed_node = self.head.data
            self.head = self.head.next
            return removed_node
        else:
            pointer = self.head
            while index > 1 and pointer.next.next != None:
                pointer = pointer.next
                index -= 1
            removed_node = pointer.next.data
            pointer.next = pointer.next.next
            return removed_node

    def replace_node(self, target_item, new_data):
        pointer = self.head 
        while pointer != None and target_item != pointer.data:
            pointer = pointer.next
        
        if pointer != None:   # meaning it equals SOMETHING, stopped before the end
            pointer.data = new_data
            return True
        else:
            return False

    def get_length(self):
        count = 0
        pointer = self.head
        while pointer != None:
            count += 1
            pointer = pointer.next
        return count

    def get_reverse(self):
        # length = self.get_length()
        pass

    def get_copy(self):
        pointer = self.head
        new_linked = LinkedList()
        while pointer != None:
            new_linked.append(pointer.data)
            pointer = pointer.next
        return new_linked

def test_apppend():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("Hello, I am the second Node!")
    linked_list.display_linked()

# test_apppend()

def test_prepend():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("Hello, I am the second Node!")
    linked_list.prepend('I should be at the begining')
    #linked_list.insert_node(0, "newer start") 
    linked_list.display_linked()

# test_prepend()

def test_insert():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("Hello, I am the second Node!")
    linked_list.prepend('I should be at the begining')
    linked_list.insert_node(2, 'inserted')
    # if we enter a too large index, it will add at end
    linked_list.insert_node(24, 'last')
    linked_list.display_linked()

# test_insert()

def test_delete():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("Hello, I am the second Node!")
    linked_list.prepend('I should be at the begining')
    #linked_list.insert_node(2, 'inserted')
    #linked_list.insert_node(24, 'last')
    linked_list.delete_node(2)
    linked_list.display_linked()

# test_delete()

def test_last_few():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("#2!")
    linked_list.prepend('I should be at the begining')
    linked_list.insert_node(2, 'inserted')
    linked_list.delete_node(3)
    linked_list.replace_node('A', "replaced")
    print(linked_list.get_length())
    linked_list.display_linked()
    new_linked = linked_list.get_copy()
    new_linked.display_linked()
    #linked_list.append("only in old")
    #new_linked.append("only in new")
    #linked_list.display_linked()
    #new_linked.display_linked()

# test_last_few()

'''
Circular Linked List - Special Case of Singly liked list
                     - Insertion and removal of the first node are special cases of the insert ith and remove ith operations  on a singly linked list. These are special because the head pointer must be reset. you can use circular linked list with a dummy header node. Contains a link from the last node to the first node in the structure
'''

class CircularLinked:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            pointer.next = new_node
            new_node.next = self.head

    def display_linked(self):
        current_node = self.head
        print(current_node.data)
        while current_node.next != self.head:
            current_node = current_node.next
            print(current_node.data)
            
    def Howard_reverse(self):
        current = self.head
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

# c_linked = CircularLinked()
# c_linked.append(5)
# c_linked.append(6)
# c_linked.append(7)
# c_linked.display_linked()





