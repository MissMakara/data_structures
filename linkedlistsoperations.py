#create a linked list with 3 nodes

class Node:
    def __init__(self, item):
        self.item=item
        self.pointer = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def inserthead(self, new_item):
        #create a new node with the new data
        new_node = Node(new_item)

        #point the next pointer of the new node to the old head node
        new_node.pointer = self.head

        #make the new node the head
        self.head = new_node

    #to insert a new node infront of a previous node
    def inserttoprev(self, prev, item):
        #check if the previous node exists
        if prev is None:
            print("The previous node must be in linkedlist")

        #create a new node with the new data
        new_node = Node(item)

        #make the pointer of the new node point to the next node
        new_node.pointer = prev.pointer

        #make the prev node point to the new_node
        prev.pointer = new_node

    #insert node at the end
    def insertend(self, item):
        #create a new node
        new_node = Node(item)

        #check if list is empty
        if self.head is None:
            self.head = new_node
            return

        #traverse to the last node
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def deletenode(self, item):
        #use a temp holder
        temp = self.head

        if temp is None:
            return

        #check if self.head is null
        #if not check if it holds the data to be deleted
        #if so delete the head and make the next node head
        if temp is not None:
            if temp.item == item:
                self.head = temp.pointer
                return

        #search for the element in the rest of the linkedlist
        while temp is not None:
            if temp.item == item:
                break
            prev = temp
            temp = temp.pointer
            prev.pointer = temp.pointer

    def reverse(self):
        prev = None
        current = self.head

        #check whether the list is empty
        if current is None:
            print("List is empty")
            return

        #
        while current is not None:
            next = current.pointer
            current.pointer = prev
            next.pointer = current







        


        










if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.head = Node(4)
    node2 = Node(3)
    node3 = Node(10)

    linkedlist.head.pointer= node2
    node2.pointer = node3

    while linkedlist.head != None:
        print(linkedlist.head.item, end=" ")
        linkedlist.head = linkedlist.head.pointer
