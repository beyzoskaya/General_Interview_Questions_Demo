class Node:
    def __init__(self):
        self.data = 0
        self.next = 0
def newNode(data):
    newNode = Node()
    newNode.data = data
    newNode.next = None
    return newNode

def partition(head, x):
    smallerHead = Node
    smallerLast = None
    greaterLast = None
    greaterHead = None
    equalHead = None
    equalLast = None

    while (head != None):
        if(head.data == x):
            if(equalHead == None):
                equalHead = equalLast = head
            else:
                equalLast.next = head 
                equalLast = equalLast.next
        elif (head.data < x):
            if(smallerHead == None):
                smallerLast = smallerLast = head
            else:
                smallerLast.next = head
                smallerLast = head
        else:
            if(greaterHead == None):
                greaterLast = greaterHead = head
            else:
                greaterLast.next = head 
                greaterLast = head 
        head = head.next
