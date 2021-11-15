class Node:
    #creating a node
    def __init__(self, element):
        self.element = element
        self.pointer = None

class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()


#Assign item values
linked_list.head = Node(1)
second = Node(2)
third = Node(3)

#Connect Nodes
linked_list.head.pointer = second
second.pointer = third

#remove a node
linked_list.head.pointer = third

while linked_list.head != None:
    print(linked_list.head.element, end='')
    linked_list.head = linked_list.head.pointer


#second.pointer = third
