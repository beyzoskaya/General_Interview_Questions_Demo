
class Node:
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next
    
    # def getKthFromEnd(head, k):
    #     n = 0
    #     current_node = head

    #     while current_node.next != None:
    #         current_node = current_node.next
    #         n += 1
        
    #     if n >= k:
    #         current_node = head
    #         for i in range( n - k):
    #             current_node = current_node.next
    #     return current_node
    # if __name__ == '__main__':
    #    head = None
    # for i in reversed(range(5)):
    #     head = Node(i + 1, head)
 
    # k = 3
    # node = getKthFromEnd(head, k)
 
    # if node:
    #     print('k\'th node from the end is', node.data)

def findKthNode(head, k):
    current = head
    for i in range(k):
        if current is None:
            return None
        current = current.next
    while current:
        head = head.next
        current = current.next
    return head
if __name__ == '__main__':
 
        # input keys
    keys = [1, 2, 3, 4, 5]
    
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)
    
    k = 3
    node = findKthNode(head, k)
    
    if node:
        print('k\'th node from the end is', node.data)