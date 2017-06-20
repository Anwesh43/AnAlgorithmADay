class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def addNext(self,data):
        self.next = Node(data)
class LinkedList:
    def __init__(self):
        self.curr = None
        self.root = None
    def add(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
            self.curr = node
        else:
            self.curr.next = node
            self.curr = self.curr.next
