from pyfiglet import Figlet
from os import system, name
from termcolor import colored

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def show_menu():
    print('1 - Add Pruduct')
    print('2 - Edit Pruduct')
    print('3 - Delete Pruduct')
    print('4 - Search')
    print('5 - Show List')
    print('6 - Buy')
    print('7 - Exit')

def show_list():
    for i in range(len(PRODUCT)):
        print(PRODUCT[i])

def Choice():

    choice = int(input('Please choose a number: '))

    if choice == 1:
        Add_product()

    elif choice == 2:
        Edit_product()
    
    elif choice == 3:
        Delete_product()
    
    elif choice == 4:
        Search_product()
    
    elif choice == 5:
        show_list()
    
    elif choice == 6:
        buy_product()
    
    elif choice == 7:
        clear()
        f = Figlet(font = 'standard')
        print(f.renderText('goodbye'))
        return -1

def loading():
    print('loading ...')
    my_file = open('data.txt', 'r')
    tx_data = my_file.read()
    product_list = tx_data.split('\n')
    print(product_list)

    
    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = int(product_info[3])

        PRODUCT.append(mydict)
    print('welcome!')

def show_banner():
    f = Figlet(font = 'standard')
    print(f.renderText('Hosein Store'))

def show_edit_menu():
    print('1 - edit id')
    print('2 - edit name')
    print('3 - edit price')
    print('4 - edit count')

def Add_product():
    clear()
    print(colored('Adding...' , 'yellow'))
    f = 1
    while 1:
        new_dict = {}
        new_dict['id'] = input('Enter id:')
        new_dict['name'] = input('Enter name:')
        new_dict['price'] = input('Enter price:')
        new_dict['count'] = int(input('Enter count:'))
        PRODUCT.append(new_dict)
        print('Product Added!')
        adding = input('add enother product(Y/N):')
        if adding == 'n' or adding == 'N':
            break
        elif adding == 'y' or adding == 'Y':
            f += 1

    clear()

    if f == 1:
        print(colored('Product Added!' , 'green'))
    elif f > 1:
        print(colored('Product\'s Added!' , 'green'))

def Edit_product():
    clear()
    print(colored('Edditing...' , 'yellow'))
    f =1
    while 1:
        edit_id = input('Enter the id of the product you want to edit:')
        for i in range(len(PRODUCT)):
            if edit_id == PRODUCT[i]['id']:
                show_edit_menu()
                edit_item = int(input('Please choose a number:'))
                if edit_item == 1:
                    PRODUCT[i]['id'] = input('enter new id:')
                if edit_item == 2:
                    PRODUCT[i]['name'] = input('enter new name:')
                if edit_item == 3:
                    PRODUCT[i]['price'] = input('enter new price:')
                if edit_item == 4:
                    PRODUCT[i]['count'] = int(input('enter new count:'))
        print('Product edited!')
        editing = input('edit enother product(Y/N):')
        if editing == 'n' or editing == 'N':
            break
        elif editing == 'y' or editing == 'Y':
            f += 1
        
    clear()

    if f == 1:
        print(colored('Product Edited!' , 'green'))
    elif f > 1:
        print(colored('Product\'s Edited!' , 'green'))

def Search_product():
    clear()
    print(colored('Searching...' , 'yellow'))
    while 1:
        search_id = input('Enter the product ID/NAME you want to search:')
        find = 0
        for i in range(len(PRODUCT)):
            if search_id == PRODUCT[i]['id']:
                find = 1
                print(PRODUCT[i])
                break
        if find == 0 :
            print(colored('not find' , 'red'))

        searching = input('search enother product(Y/N):')
        if searching == 'n' or searching == 'N':
            break
        elif searching == 'y' or searching == 'Y':
            pass
        
    clear()

def Delete_product():
    clear()
    print(colored('Deleting...' , 'yellow'))
    f = 1
    while 1:
        delete_id = input('Enter the product ID/NAME you want to delete:')
        for i in range(len(PRODUCT)):
            if delete_id == PRODUCT[i]['id']:
                PRODUCT.remove(PRODUCT[i])
                break
        
        deleting = input('delete enother product(Y/N):')
        if deleting == 'n' or deleting == 'N':
            break
        elif deleting == 'y' or deleting == 'Y':
            f += 1

    clear()
    if f == 1:
        print(colored('Product Deleted!' , 'green'))
    elif f > 1:
        print(colored('Product\'s Deleted!' , 'green'))

def buy_product():
    clear()
    print(colored('Buying...' , 'yellow'))
    f = 1
    while 1:
        buy_id = input('Enter the product ID/NAME you want to buy:')
        for i in range(len(PRODUCT)):
            PRODUCT[i]['count'] = int(PRODUCT[i]['count']) - 1

        buying = input('buy enother product(Y/N):')
        if buying == 'n' or buying == 'N':
            break
        elif buying == 'y' or buying == 'Y':
            f +=1
        
        
    clear()
    if f == 1:
        print(colored('Product Buy!' , 'green'))
    elif f > 1:
        print(colored('Product\'s Buy!' , 'green'))

def write_on_list():
    f = open("data.txt", "w")
    for i in range(len(PRODUCT)):
        f.write(PRODUCT[i]['id'])
        f.write(',')
        f.write(PRODUCT[i]['name'])
        f.write(',')
        f.write(PRODUCT[i]['price'])
        f.write(',')
        f.write(str(PRODUCT[i]['count']))
        if i != len(PRODUCT) -1:
            f.write('\n')
    

    f.close()

PRODUCT = []
t = 0

loading()
show_banner()

while t != -1: 
    show_menu()
    t = Choice()

write_on_list()


