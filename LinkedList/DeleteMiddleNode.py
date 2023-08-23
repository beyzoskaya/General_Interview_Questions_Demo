class Node:
    def __init__(self) :
        self.data = 0
        self.next = None

def countOfNodes(head):
    count = 0

    while (head != None):
        head = head.next
        count += 1
    return count

def deleteMid(head):
    if(head == None):
        return None
    if (head.next == None):
        del head
        return None
    copyHead = head
    count = countOfNodes(head)

    mid = count // 2

    while(mid > 1):
        mid -=1
    head = head.next
    return 
def printList(ptr):
  
    while (ptr != None):
        print(ptr.data, end = '->')
        ptr = ptr.next
      
    print('NULL')


def newNode(data):
  
    temp = Node()
    temp.data = data
    temp.next = None
    return temp
  
# Driver Code
if __name__=='__main__':
      
    # Start with the empty list
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(3)
    head.next.next.next = newNode(4)
   
    print("Given Linked List")
    printList(head)
   
    head = deleteMid(head)
   
    print("Linked List after deletion of middle")
    printList(head)