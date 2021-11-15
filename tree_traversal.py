class node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val= item

    def inorder(root):
        if root:
            Inorder(root.left)
            print(root.val, end=" ")
            Inorder(root.right)

    def preorder(root):
        if root:
            print(root.val, end=" ")
            preorder(root.left)
            preorder(root.right)

    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=" ")

    root = node(30)
    root.left=node(29)
    root.right=node(40)
    root.left.left=node(20)


