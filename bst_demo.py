import bst_operations as bo

class BST:
    def __init__(self):
        self.root = None

def get_menu(choice):
    menu = {
        1 : bo.insert,
        2 : bo.delete,
        3 : bo.update,
        4 : bo.in_order,
        5 : bo.pre_order,
        6 : bo.post_order,
        7 : bo.end
    }
    return menu[choice]

def run_menu():
    bst = BST() # created an instance of the class BST
    while True:
        print('\n 1:Insert 2:Delete 3:Update 4:InOrder 5:PreOrder 6:PostOrder 7:Exit')
        choice = int(input('Your choice please: '))
        if choice in [4, 5, 6] and bst.root is None:
            print('BST is empty')
            continue
        bst.root = get_menu(choice)(bst.root)
        if choice == 7:
            break

run_menu()