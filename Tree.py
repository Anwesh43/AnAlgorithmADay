class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def addLeftChild(self,data):
        self.left = Tree(data)
    def addRightChild(self,data):
        self.right = Tree(data)
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
