from LinkedList import *

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
root = ll.root
msg = root.data
root = root.next
while not(root == None):
    msg = "{0}->{1}".format(msg,root.data)
    root = root.next
print msg
