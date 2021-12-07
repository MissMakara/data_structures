class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def findmiddle(self):
        temp = self.head
        length = 0

        print("head is", temp.val)
        #traverse to get the length
        while temp !=None:
            length =length +1
            temp = temp.next
            

        #get the middle
        print("length is ", length)
        half = length/2
        temp2 = self.head
        while half != 0:
            if temp2 is not None:
                temp2 = temp2.next
                half = half- 1

            else: 
                print("end of nodes in the linkedlist")
                break

        else:
            print(temp2)
            return temp2

    def countelem(self, x):
        temp = self.head
        count = 0

        while temp != None:
            if temp.val == x:
                count = count + 1
                temp = temp.next

            else:
                temp = temp.next

        return count
    
    def detectloop():
        temp = self.head
        s = set()

        while temp != None:
            if temp in s:
                return True
            
            s.add(temp)
            temp = temp.next

        return False




if __name__ == "__main__":
    #create a linkedlist
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    linkedlist.head.next = second
    second.next = third
    third.next  = fourth
    fourth.next = fifth
    fifth.next = sixth

    while linkedlist.head !=None:
        print (linkedlist.head.val, end = " ")
        linkedlist.head = linkedlist.head.next

output = linkedlist.findmiddle(linkedlist.head)    
print(output)
            