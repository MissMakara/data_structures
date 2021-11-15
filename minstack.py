class MinStack:

    def __init__(self):
        self.head=-1
        self.stack=[]
        
        

    def push(self, val: int) -> None:
        if (-2**31 <=val<= 2**31-1):
            self.head = self.head+1
            self.stack.insert(self.head, val)
            

    def pop(self) -> None:
        if (self.head == -1):
            return False
        
        else:
            elem=self.stack.pop(self.head)
            self.head = self.head-1
            
            return elem    

    def top(self) -> int: 
        if (self.head == -1):
            return False
        else:
            elem = self.stack[self.head]
            return elem

    def getMin(self) -> int:
        if (self.head == -1):
            return False
        
        else:
            elem = min(self.stack)
            return elem
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(27)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()