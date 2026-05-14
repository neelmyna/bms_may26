def insert():
    print('Element inserted')

def delete():
    print('Element deleted')

def update():
    print('Element updated')

def display():
    print('List displayed')

def end():
    print('End of Program')

def get_menu(choice):
    menu = {
        1 : insert,
        2 : delete,
        3 : update,
        4 : display,
        5 : end
    }
    return menu[choice]

def run_menu():
    count = 0
    while True:
        print('\n 1:Insert 2:Delete 3:Update 4:List 5:Exit')
        choice = int(input('Your choice please: '))
        get_menu(choice)()
        count += 1
        if choice == 5 or count == 10:
            break

run_menu()