"""
Stacks
    Linear collections in which access is completely restricted to just one end called to the top

    LIFO - Last in First out protocol, think of dishes atacked at a buffet

    push - put items on the stack
    pop - remove the top item from the stack
    peek - examine the top element on the stack

    THe stack is not built into Python so we use a list to emulate an array-bassed stack

    We're going to use the lith methods append and pop

    It's possible to utilize other list methods such as insert, replace, and remove but that defeats the purpose and spirit of the stack

"""

class Stack:
    def __init__(self):
        self.my_stack = []

    def push(self, item):
        self.my_stack.append(item)
        #self.my_stack.insert(0, item)

    def get_stack(self):
        return self.my_stack
    
    def pop(self):
        return self.my_stack.pop()
        #return self.my_stack.pop(0)

    def is_empty(self):
        return self.my_stack == []

    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]

def test_stack():
    s = Stack()
    s.push("first in")
    print(s.get_stack())
    s.push("next one")
    print(s.get_stack())
    s.push("top item")
    print(s.get_stack())
    print(s.peek())
    print(s.pop())
    print(s.get_stack())

#test_stack()


"""
Use a stack to check whether or not a string has balanced usage of parenthesis
Example
    Balanced = (), ()(), (({[]}))
    Unbalanced = ((), {{{)}], [][]]], ([)]

"""

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else: 
        return False

def is_paren_bal(p_string):
    s = Stack()
    # an initial flag
    is_balanced = True
    #keep track of where we are
    index = 0
    # loop through our string
    while index < len(p_string) and is_balanced:
        paren = p_string[index]
        # is it a n open paren?
        if paren in "({[":
            s.push(paren)
        # is it closed
        elif paren in "]})":
            try:
                top = s.pop()
                # the popped item and the current item 
                if not is_match(top, paren):
                    # not a match
                    is_balanced = False
            except:
                is_balanced = False
        #increment
        index += 1

    if s.is_empty and is_balanced:
        return True
    else:
        return False

print(is_paren_bal("()"))
print(is_paren_bal("([)]"))
print(is_paren_bal("(({[]}))"))
print(is_paren_bal("[][]]]"))
print(is_paren_bal("()()"))
print(is_paren_bal("{{{)}]"))


