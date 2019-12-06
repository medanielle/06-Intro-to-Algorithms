"""
Binary Tree is a tree data structure in wich each node has at most two children which are left child and right child

Tope node is root

Complete binary tree - Every level, except possibly the last is completely filled and all nodes in the last level                          are as far left as possible

Full binary tree - a fill binary tree (refferred to as a propper or plane binary tree) is a tree where every node                      except the leaves has two children

"""

"""
leaves = no children

height starts at root = 0

ancestors = parent, grandparent

interior nodes = nont leaves

decendents = children and grandkids

"""

"""
Unlike linked lists, one-dimensional arrays, etc., which are travesed in a linear order, trees may be travesde in multiple ways

depth-first order - pre-order,      post-order,         in order
                 root left right                    left root right      


pre-order - check if current node is empty
          - display the data part of the root or current node
          - traverse the left subtree by recusrively calling the pre-order function
          - traverse the right subtree by recusrsively calling the pre-order function

in-order - check if the current node is empty
         - traverse the left subtree by recursively calling the in-order function
         - display the data part of the root or current node
         - traverse the right subtree by recursively calling the in-order function
"""
#travesal = process of visiting (checking and/or updating) each node in a tree data structure, exacly once

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def preorder_print(self, start, traversal):
        # root  => left => right
        if start:
            traversal += (str(start.value)+ '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def pretty_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "") # start with an empty string that will fill out
        if traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        if traversal_type == "postorder":
            return self.postorder_print(self.root, "")

    def inorder_print(self, start, traversal):
        #left  -> root  -> right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        # left -> right -> root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

def test():
    bt = BinaryTree('D')
    bt.root.left = TreeNode('B')
    bt.root.right = TreeNode('F')
    bt.root.left.left = TreeNode('A')
    bt.root.left.right = TreeNode('C')
    bt.root.right.left = TreeNode('E')
    bt.root.right.right = TreeNode('G')

    print(bt.pretty_tree("preorder"))
    print(bt.pretty_tree("inorder"))
    print(bt.pretty_tree("postorder"))

test()
