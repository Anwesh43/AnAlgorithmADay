#creating a sample tree

from Tree import BinaryTree
root = BinaryTree(1)
root.addLeftChild(2)
root.addRightChild(3)
root.left.addLeftChild(4)
root.left.addRightChild(5)
root.left.left.addLeftChild(8)
root.left.left.addRightChild(9)
root.left.right.addLeftChild(10)
root.left.right.addRightChild(11)
root.right.addLeftChild(6)
root.right.addRightChild(7)
root.right.left.addLeftChild(12)
root.right.left.addRightChild(13)
root.right.right.addLeftChild(14)
root.right.right.addRightChild(15)

#               1
#
#         2                     3
#     4        5          6          7

#  8    9   10   11    12   13   14     15
