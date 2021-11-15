#create the node instance
class Node:
    def __init__(self, item):
        self.item = item
        self.leftNode = None
        self.rightNode = None

    
#calculate the depth of the tree
def calculateDepth(root):
    depth = 0 

    while root is not None:
        depth = depth +1
        root = root.leftNode
    return depth

#check if the tree is a perfect tree
def isPerfect(root, depth, level=0):
    #check if root is empty
    if root is None:
        return True

    elif root.leftNode is None and root.rightNode is None:
        return (depth == level+1)
    
    elif root.leftNode is None and root.rightNode is not None:
        return False

    elif root.leftNode is not None and root.rightNode is None:
        return False

    return (isPerfect(root.leftNode, depth, level+1) and 
    isPerfect(root.rightNode, depth, level+1) )


root = Node(1)
root.leftNode = Node(2)
root.rightNode = Node(3)
root.leftNode.leftNode = Node(4)
root.leftNode.rightNode = Node(5)
root.rightNode.leftNode = Node(6)
root.rightNode.rightNode = Node(7)

output = isPerfect(root,calculateDepth(root))
print("The perfect tree is", output)



