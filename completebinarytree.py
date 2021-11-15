#checking is a binary tree is a complete binary tree
class Node:
    def __init__(self, item):
        self.item= item
        self.leftNode = None
        self.rightNode = None

#count the number of Nodes
def countNodes(root):
    if root is None:
        return 0
    return (1+ countNodes(root.leftNode) + countNodes(root.rightNode))

#check if the tree is a complete binary tree
def isCompleteTree(root, index, numberofNodes):
    
    #check if the tree is empty
    #An empty tree is complete Binary tree
    if root is None:
        return True
    
    # If index assigned to current nodes is more than
    # number of nodes in tree, then tree is not complete
    elif index >= numberofNodes:
        return False

    # Recur for left and right subtress
    return (isCompleteTree(root.leftNode, 2*index+1, numberofNodes) and 
    isCompleteTree(root.rightNode, 2*index+2, numberofNodes))


root = Node(1)
root.leftNode = Node(2)
root.rightNode = Node(3)
root.leftNode.leftNode = Node(4)
root.leftNode.rightNode = Node(5)
root.rightNode.rightNode = Node(6)
 
node_count = countNodes(root)
index = 0
 
state = isCompleteTree(root, index, node_count)
print("The complete tree is", state)
    