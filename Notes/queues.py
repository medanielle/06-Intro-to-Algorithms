"""
Queues
    "waiting in line"
    A linear collection that adds elements from one end and removed them from the other in a FIFO(first in first out) protocol

    Queues are implemented in many ways, some based on arrays, and some based on linked structures 

    rear - insertions are restricted this end
    front - removals are restricted to this end

    two fundamental opeartions, add and pop
        add - adds item to the rear
        pop - removed item from the front
        peek - see the item at the front of te queue

    THere are priority queues that schedule their elements using a rating scheme as well as FIFO. If two elements have same rating then they are scheduled in FIFO order. Elements are ranked from smallest to largest according to some attribute like a number or char, generally smallest are removed first no matter when they are added to the queue (Dijkstra's shortest path algoritm)
    (FastPass at amusement park)
"""

class Queue:
    def __init__(self):
        self.queue = []

    def push(self):
        item = input("what item would you like to push? ")
        self.queue.append(item)

    def pop(self):
        item = self.queue.pop(0)
        print("You popped", item)

    def peek(self):
        if self.queue:
            print(self.queue[0])
    
    def view_q(self):
        for i in range(len(self.queue)):
            print(f'Item {i} is {self.queue[i]}')
def test_q():
    q = Queue()

    while True:
        print('-'* 50)
        print('Your Queue Options')
        print("1. View Queue")
        print("2. See next in Queue")
        print("3. Push into Queue")
        print("4. Pop out of Queue")

        menu_choice = int(input("Choose your option: "))
        print()

        if menu_choice == 1:
            q.view_q()
        elif menu_choice == 2:
            q.peek()
        elif menu_choice == 3:
            q.push()
        elif menu_choice == 4:
            q.pop()

test_q()