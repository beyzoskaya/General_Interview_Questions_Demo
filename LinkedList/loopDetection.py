class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def newNode(key):
    temp = Node(key)
    return temp

def printList(head):

    while(head != None):
        print(head.key, end = ' ')
        head = head.next
    print()

def detectAndRemoveLoop(head):
    if (head == None or head.next == None):
        return None
    
    slow = head
    fast = head

    slow = slow.next
    fast = fast.next.next

    while (fast and fast.next):
        if(slow == fast):
            break
        slow = slow.next
        fast = fast.next.next
    if(slow != fast):
        return None
    slow = head

    while(slow != fast):
        slow = slow.next 
        fast = fast.next
    return slow


if __name__=='__main__':
     
    head = newNode(50)
    head.next = newNode(20)
    head.next.next = newNode(15)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(10)

    printList(head)
  
    # Create a loop for testing
    head.next.next.next.next.next = head.next.next

    res = detectAndRemoveLoop(head)
     
    if (res == None):
        print("Loop does not exist")
    else:
        print("Loop starting node is " +
              str(res.key))
