# this program is to demonstrate traversals in a tree

from sample_tree import root

#inorder traversal

print 'inorder traversal'

def inorder(curr):
    if not(curr == None):
        print curr.data
        inorder(curr.left)
        inorder(curr.right)

inorder(root)

print 'preorder traversal'

def preorder(curr):
    if not(curr == None):
        preorder(curr.left)
        print curr.data
        preorder(curr.right)

preorder(root)

print 'postorder traversal'

def postorder(curr):
    if not(curr == None):
        postorder(curr.left)
        postorder(curr.right)
        print curr.data

postorder(root)
