class Node:
    def __init__(self,data):
        self.data = data
        self.ptr = None

def isPalindrome (head):

    temp = head
    stack = []
    isPalin = True

    while temp != None:
        stack.append(temp.data)
        temp = temp.ptr
    
    while head != None:

        top_most = stack.pop()

        if head.data == top_most:
            isPalin = True
        else:
            isPalin = False
            break

        head = head.ptr
    return isPalin

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)
 
# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None
 
# Call function to check palindrome or not
result = isPalindrome(one)
 
print("isPalindrome:", result)

