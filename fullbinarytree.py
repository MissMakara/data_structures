#to check is a binary tree is a full binary tree
#every node has either 2 or no children

#create a node instance for the tree
class Node:
    def __init__(self, item):
        self.leftchild =None
        self.rightchild = None
        self.item = item

#check if it's a full binary tree
def isFullTree(root):

    #if the tree is empty
    if root is None:
        return True
    
    #check if there are no child nodes
    elif root.leftchild is None and root.rightchild is None:
        return True

    #check if there are both child nodes
    #if there are call the check function again for each node
    elif root.leftchild is not None and root.rightchild is not None:
        return(isFullTree(root.leftchild) and isFullTree(root.rightchild))

    else:
        return False


root = Node(1)
root.rightchild = Node(3)
root.leftchild = Node(2)

root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)
root.leftchild.rightchild.leftchild = Node(6)
root.leftchild.rightchild.rightchild = Node(7)

output = isFullTree(root)
print("The tree is", output)



