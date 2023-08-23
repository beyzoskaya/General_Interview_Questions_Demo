class KStacks:

    def __init__(self,k,n):
        self.k = k #number of stacks
        self.n = n #total size of array holding all the 'k' stacks

        #array which holds 'k' stacks
        self.arr = [0]* self.n
        # All stakcs are empty at first
        self.top = [-1]*self.k

        self.free = 0

        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    def isEmpty(self,sn):
        return self.top[sn] == -1
    def isFull(self):
        return self.free == -1
    
    def push(self,item,sn):
        if self.isFull():
            print("Stack Overflow!")
            return
        
        insert_at = self.free
        self.free = self.next[self.free]
