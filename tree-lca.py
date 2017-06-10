# this program is to find lca in your program
from sample_tree import root

## adding code for children of a node
def get_children(tree,a):
    if not(tree == None):
        l_children = get_children(tree.left,a)
        r_children = get_children(tree.right,a)
        for (k,v) in r_children.items():
            l_children[k] = v
        if tree.data == a:
            print l_children.keys()
        else:
            l_children[tree.data] = 1
        return l_children
# def get_lca(tree,a,b):
    else:
        return {}
get_children(root,4)
# a = int(raw_input('Enter first node'))
# b = int(raw_input('Enter second node'))
# print 'least common ancestor of {0} and {1} is {2}'.format(a,b,get_lca(root,a,b,{}))
