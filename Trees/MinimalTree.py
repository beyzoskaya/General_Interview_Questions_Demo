# Input: arr[] = {1, 2, 3}
# Output: A Balanced BST
#       2
#     /  \
#  1     3 
# Explanation: all elements less than 2 are on the left side of 2 , and all the elements greater than 2 are on the right side

# Input: arr[] = {1, 2, 3, 4}
# Output: A Balanced BST
#           3
#         /  \
#      2    4
#    /
# 1

# The idea is to find the middle element of the array and 
# make it the root of the tree, 
# then perform the same operation on the left subarray 
# for the root’s left child and the same operation on the right subarray for the root’s right child.

class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if not arr:
        return None
    
    mid = (len(arr)) // 2
    # Make the middle element the root
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root

def preOrder(node):
    if not node:
        return
    
    print.node.data,
    preOrder(node.left)
    preOrder(node.right)

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
print ("PreOrder Traversal of constructed BST ",
preOrder(root))

