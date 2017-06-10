#creating a sample tree

from Tree import BinaryTree
root = BinaryTree(1)
root.addLeftChild(2)
root.addRightChild(3)
root.left.addLeftChild(4)
root.left.addRightChild(5)
root.right.addLeftChild(6)
root.right.addRightChild(7)


#              1
#
#       2             3
#   4      5      6       7
