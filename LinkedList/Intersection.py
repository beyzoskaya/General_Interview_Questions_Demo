class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.visited = False

def getIntersectNode(head1,head2):
    temp1 = head1
    while(temp1 is not None):
        temp1.visited = True
        temp1 = temp1.next
    
    temp1 = head2
    while(temp1 is not None):
        if(temp1.visited):
            return temp1.data
        else:
            temp1.visited = True
        temp1 = temp1.next
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
# list2
head2 = Node(10)
head2.next = Node(9)
head2.next.next = Node(8)
head2.next.next.next = head1.next.next.next
         
print("The node of intersection is : ")
print(getIntersectNode(head1, head2))