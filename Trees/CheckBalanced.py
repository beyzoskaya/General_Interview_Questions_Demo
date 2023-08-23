# A height balanced binary tree is a binary tree 
# in which the height of the left subtree and
# right subtree of any node does not differ 
# by more than 1 and both the left and 
# right subtree are also height balanced.

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def height(root):

    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def isBalanced(root):

    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if (abs(lh - rh) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True
    return False
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")