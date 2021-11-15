class Queue():
    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.head=self.tail=-1


    def addelement(self, element):
        #check if it's full
        if ((self.tail + 1) % self.k) == self.head:
        #if (self.head == 0 and self.tail==(self.k-1)):
            print("The queue is full")

        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = element
        
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = element

    def Rear(self) -> int:
        if (self.tail==-1):
            return -1
        else:
            elem= self.queue[self.tail]
            return elem

    def removeelement(self):
        #check if the queue has anything in it
        #check if the head is still pointing at -1
        if (self.head == -1):
            print("there is nothing in the queue")

        else:
            #remove the element pointed at by the head
            elem = self.queue.pop(self.head)
            self.head = self.head + 1
            return self.queue
        

    
    def checkvalue(self):
        print(self.head)
        print(self.tail)

        value = self.queue[self.tail]
        print(value)
        return value


queue = Queue(8)
queue.addelement("ostrich")
queue.addelement("chicken")
queue.addelement("goose")
#smaller_queue = queue.removeelement()
elem = queue.Rear()
#elem=queue
print(elem)