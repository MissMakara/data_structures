class Node:
    #initialize the node variables
    def __init__(self, item):
        self.item = item
        self.leftNode = None
        self.rightNode = None

#create a function to print the nodes at odd levels
#to be revisited once we code breadth-first-traversal
def countNodes(root):
    depth = 0
    nodes =[]
    while (root is not None):
        depth = depth+1
        
        if (depth%2!=0):
            nodes.append(root.item)
        
        root = root.leftNode
        #countNodes(root.leftNode)
        #countNodes(root.rightNode)

    return nodes


root = Node(1)
root.leftNode = Node(2)
root.rightNode = Node(3)
root.leftNode.leftNode = Node(4)
root.leftNode.rightNode = Node(5)
root.leftNode.leftNode.leftNode = Node(6)
root.leftNode.rightNode.leftNode = Node(7)

x= countNodes(root)
print(x)

        



    