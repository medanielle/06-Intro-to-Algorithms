
# Doubly Linked List - Very similar to singly linked, however these have prev pointer and a tail node.

#           - Move left, to previous node, form a fiven node
#           - Move immediately to the last node

class DoubleNode:
    def __init__(self, data, next= None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display_linked(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # two cases to consider
    def append(self, data):
        new_node = DoubleNode(data)
        # is it empty?
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
        # there are items in the list
        else:                           # may be easier way with new tail function
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
            # probe = self.head
            # while probe.next != None:
            #     probe = probe.next
            # new_node.prev = probe
            # probe.next = new_node

def testing():
    d_list = DoublyLinkedList()
    d_list.append('First Node Data')
    d_list.append([1, 2, 'howdy'])
    d_list.append('C')
    d_list.display_linked()

testing()

def testing_2():
    d_list = DoublyLinkedList()
    #head = DoublyLinkedList.append(1)
    #tail = head

    #for data in range(2, 6):
        #tail.next = DoublyLinkedList.append(data)
        #tail = tail.next

    #pointer = tail
    #while  
    d_list.display_linked()

#testing_2()
