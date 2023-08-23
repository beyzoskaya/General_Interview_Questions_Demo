class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def maxValue(node):
    if node is None:
        return 0
    leftMax = maxValue(node.left)
    rightMax = maxValue(node.right)

    value = 0
    if leftMax > rightMax
        value = leftMax
    else:
        value = rightMax
    if value < node.data:
        value = node.data
    return value

def minValue(node):
    if node is None:
        return 1000000000
     
    leftMax = minValue(node.left)
    rightMax = minValue(node.right)
     
    value = 0
    if leftMax < rightMax:
        value = leftMax
    else:
        value = rightMax
     
    if value > node.data:
        value = node.data
     
    return value