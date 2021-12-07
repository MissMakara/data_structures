#implementing a stack with a linkedlist
class StackNode:
    def __init__(self, item):
        self.data = item
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True

        return False
    
    def pushtoStack(self, data):
        #create a new node
        newNode = StackNode(data)

        #make the pointer of the new node point to head
        #make the the new node the head
        newNode.next = self.head
        self.head = newNode
    
    def popFromStack(self):
        #check if it's empty
        if self.isEmpty is True:
            message = "Stack is empty"
            return message
        
        temp = self.head
        self.head = temp.next
        popped = temp.data

        return popped
    
    def peekStack(self):
        #check if empty
        if self.isEmpty():
            return None
        
        return self.head.data


if __name__ == "__main__":
    # Driver code
    stack = Stack()
    stack.pushtoStack(10)
    stack.pushtoStack(20)
    stack.pushtoStack(30)
    pop = stack.popFromStack()
    print("popped ", pop)

    temp = stack.head
    while temp !=None:
        print(temp.data)
        temp = temp.next