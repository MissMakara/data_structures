class Node:
    def __init__(self, item):
        self.item = item
        self.leftNode = None
        self.rightNode = None

#calculate the height of the tree
def getHeight(root):
    if root is None:
        return 0

    else:
        return max(getHeight(root.leftNode), getHeight(root.rightNode))+1

#check if the tree is a balanced tree
#the height of the left and the right should only have a disparity of one degree
#has a time complexity of 0(n**2)
def isBalancedTree(root):
    if root is None:
        return True

    else:
        lh =getHeight(root.leftNode)
        rh = getHeight(root.rightNode)

        if ((abs(lh-rh) <=1) and isBalancedTree(root.leftNode) is True and isBalancedTree(root.rightNode) is True):
            return True

        else:
            return False

#has a time complexity of 0(n)
def isBalancedTree2(root):
    if root is None:
        return True

    #create height functions for both subtrees
    lh = getHeight(root.leftNode)
    rh = getHeight(root.rightNode)

    #check if the subtrees are balanced
    l = isBalancedTree2(root.leftNode)
    r = isBalancedTree2(root.rightNode)

    if abs(lh - rh) <=1:
        return l and r
    
    else:
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)




root = Node(1)
root.leftNode = Node(2)
root.rightNode = Node(3)
root.leftNode.leftNode = Node(4)
root.leftNode.rightNode = Node(5)
root.rightNode.leftNode = Node(8)   

output = isBalancedTree2(root)
print("The balanced tree is", output)
