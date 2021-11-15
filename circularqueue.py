class CircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1

    #insert an element
    def enqueue(self, element):

        #check if the queue is full
        if (((self.head==0) and (self.tail==(self.k-1))) or (self.tail+1 == self.head)):
            print("circular queue is full")
            return self.queue

        #for first element check if head is at -1
        elif(self.head == -1):
            #move the pointers 1 step ahead
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = element
            print("head is at", self.head)
            print("tail is at", self.tail)
            return self.queue
        
        else:
            self.tail = self.tail + 1

            #check if the tail has reached the end
            #if so, change it to point to the beginning
            # of the queue(zero)
            if (self.tail == self.k):
                self.tail = 0
                self.queue[self.tail] = element
                print("head is at", self.head)
                print("tail is at", self.tail)
                return self.queue
            #else add the element to the next position in 
            #the queue
            else:

                self.queue[self.tail] = element
                print("head is at", self.head)
                print("tail is at", self.tail)
                return self.queue

    #remove an element
    def dequeue(self):
        #check if the queue is empty
        if (self.head == -1):
            print("queue is empty")

        #if you pop all elements
        elif self.head == self.tail:
            elem1 = self.queue[self.head]
            self.head = -1
            self.tail = -1
            print("head is at", self.head)
            print("tail is at", self.tail)

            return elem1
        
        #if you reach the end of the queue
        else:
            #return the value pointed by front
            elem1 = self.queue[self.head]
            self.head = self.head + 1

            if self.head > self.k:
                self.head=0
            
            print("head is at", self.head)
            print("tail is at", self.tail)
            return elem1

        

            






cqueue = CircularQueue(6)
cqueue.enqueue("ostrich")
cqueue.enqueue("crow")
cqueue.enqueue("chicken")
cqueue.enqueue("sparrow")
cqueue.enqueue("owl")
cqueue.enqueue("goose")
cqueue.dequeue()
cqueue.dequeue()
cqueue.enqueue("duck")
cqueue.enqueue("sparrow")
x = cqueue.enqueue("goose")

print(x)

