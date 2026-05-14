class Node:
    def __init__(self, data=0):
        self.left = None
        self.data = data
        self.right = None

def insert(root):
    data = int(input('Enter data of the new node'))
    new_node = Node(data)
    # new_node = Node()
    # new_node.data = int(input('Enter data of the new node'))

    if root is None: # if the tree is empty
        return new_node # make the 
        
    temp1 = root
    temp2 = None
    while temp1 != None:
        temp2 = temp1
        if new_node.data < temp1.data:
            temp1 = temp1.left
        else:
            temp1 = temp1.right
    if new_node.data < temp2.data:
        temp2.left = new_node
    else:
        temp2.right = new_node
    return root

def in_order(link):
    if link is None:
        return
    in_order(link.left)
    print(link.data, '  ', end='')
    in_order(link.right)

def delete(root):
    print('Element deleted')

def update(root):
    print('Element updated')

def pre_order(root):
    print('List displayed')

def post_order(root):
    print('List displayed')

def end(root):
    print('End of Program')