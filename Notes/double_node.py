
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
        print("Show list data:")
        current_node = self.head
        while current_node:
            #print(current_node.next)
            print(current_node.data)
            #print(current_node.prev)
            current_node = current_node.next
        print("*"*50)

    # two cases to consider
    def append(self, data):
        new_node = DoubleNode(data)
        # is it empty?
        if self.head is None:
            new_node.prev = self.head
            new_node.next = None
            self.head = new_node
            self.tail = new_node
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

    def prepend(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            print(self.head)
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
        else:
            print(self.head)
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
   

    def delete_value(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                # if it's not the first or last element
                if current_node.prev is not None and current_node.next is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                # if it first element
                elif current_node.prev is None:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
                else:
                    self.tail = current_node.prev.next
                    current_node.prev.next = None
            current_node = current_node.next
        print(self.head)
        print(self.tail)
    
        #inserting node within the linked list
    def insert_node(self, index, data):
        # is linked list empty or index less than 0
        new_node = DoubleNode(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
        elif index <= 0:
            new_node.next = self.head
            print(self.head.next)
            new_node.prev = None
            self.head = new_node
        else:
            # search for node at position index -1 or last position
            pointer = self.head
            while index > 1 and pointer.next != None:
                pointer = pointer.next
                index -= 1
            # insert new node after node at position index -1 or last position
            #pointer.next(data, pointer.next)
            if pointer.next is None:
                new_node.next = pointer.next
                new_node.prev = pointer
                pointer.next = new_node
                self.tail = new_node
            else:
                new_node.next = pointer.next
                pointer.next.prev = new_node
                pointer.next = new_node
                new_node.prev = pointer

    def reverse(self):
        new_linked = DoublyLinkedList()
        pointer = self.tail
        count = 0
        self.display_linked()
        while pointer.prev is not None:
            print(self.head, self.tail)
            count+=1
            print(count)
            print(pointer.data)
            new_linked.append(pointer.data)
            print(pointer.prev)
            print(pointer.next)
            pointer = pointer.prev
            new_linked.display_linked()
        return new_linked

    def howard_rev(self):
        current = self.tail
        while current is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.next
        temp = self.head
        self.head = self.tail
        self.tail = temp








def testing():
    d_list = DoublyLinkedList()
    d_list.append('First Node Data')
    d_list.append([1, 2, 'howdy'])
    d_list.append('C')
    d_list.display_linked()

#testing()

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

def test_prepend():
    d_list = DoublyLinkedList()
    d_list.append('First Node Data')
    #print(d_list.head, d_list.tail)
    d_list.prepend('test')
    d_list.prepend('#2 test')
    #print(d_list.head, d_list.tail)
    d_list.display_linked()

# test_prepend()

def test_delete_value():
    d_list = DoublyLinkedList()
    d_list.append('A')
    d_list.append('B')
    d_list.append('C')
    d_list.display_linked()
    d_list.delete_value('C')
    d_list.display_linked()

#test_delete_value()

def test_insert():
    d_list = DoublyLinkedList()
    d_list.append('Soon #2')
    d_list.prepend('test')
    #d_list.prepend('#2 test')
    #d_list.display_linked()
    d_list.display_linked()
    print(d_list.head, d_list.tail)
    d_list.insert_node(2, "NEW FIRST")
    d_list.display_linked()
    print(d_list.head, d_list.tail)

#test_insert()

def test_reverse():
    d_list = DoublyLinkedList()
    d_list.append('first')
    d_list.append('Soon #2')
    d_list.prepend('test')
    d_list.insert_node(2, "NEW FIRST")
    d_list.display_linked()
    d_list.howard_rev()
    d_list.display_linked()

test_reverse()
