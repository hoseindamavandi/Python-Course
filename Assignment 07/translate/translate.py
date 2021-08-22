from termcolor import colored
from os import close, system, name

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def loading():
    print('loading...')
    my_file = open('translate.txt' , 'r')
    tx_data = my_file.read()
    all_word_list = tx_data.split('\n')
    #print(all_word_list)
    
    for i in range(1,len(all_word_list),2):
        dictionary = {}
        dictionary['english'] = all_word_list[i-1]
        dictionary['persian'] = all_word_list[i]
        translate_list.append(dictionary)

    #print(translate_list)
    clear()
    print(colored('welcome','yellow'))

def show_menu():
    
    print('1- add new word')
    print('2- translation english2persian')
    print('3- translation persian2english')
    print('4- exit')

def add_new():
    clear()
    while 1:
        print(colored('adding new word','yellow'))
        new_english = input('plesae enter english:')
        new_persian = input('plesae enter persian:')

        new_dict = {}
        f = 0
        for i in range(len(translate_list)):
            if translate_list[i]['english'] == new_english:
                f = 1
            
        if f == 0:
            new_dict['english'] = new_english
            new_dict['persian'] = new_persian
            translate_list.append(new_dict)
            print(colored(new_english , 'green') , colored(' added to dictionary!' , 'green'))
        
        elif f == 1:
            print(colored('This word already exists!' , 'red'))

        continue_add = input('Are you planning to add a new word?(Y/N)')
        if continue_add == 'n' or continue_add == 'N':
            clear()
            break
        if continue_add == 'y' or continue_add == 'Y':
            pass

def english2persian():
    clear()
    while 1:
        print(colored('searching for translate from english to persian' , 'yellow'))
        search_english = input('enter english word:').split(' ')
        
        for j in range(len(search_english)):
            find = 0
            for i in range(len(translate_list)):
                if search_english[j] == translate_list[i]['english']:
                    print(translate_list[i]['persian'], end=' ')
                    find = 1
                    break
            if find == 0:
                print(search_english[j] , end=' ')

        continue_add = input('\nAre you planning to search another word?(Y/N)')
        if continue_add == 'n' or continue_add == 'N':
            clear()
            break
        if continue_add == 'y' or continue_add == 'Y':
            pass

def persian2english():
    clear()
    while 1:
        print(colored('searching for translate from persian to english' , 'yellow'))
        search_persian = input('enter persian word:').split(' ')

        for j in range(len(search_persian)):
            find = 0
            for i in range(len(translate_list)):
                if search_persian[j] == translate_list[i]['persian']:
                    print(translate_list[i]['english'], end=' ')
                    find = 1
                    break
            if find == 0:
                print(search_persian[j], end=' ')

        continue_add = input('\nAre you planning to search another word?(Y/N)')
        if continue_add == 'n' or continue_add == 'N':
            clear()
            break
        if continue_add == 'y' or continue_add == 'Y':
            pass

def choose():

    choice = int(input('choose a number:'))
    
    if choice == 1:
        add_new()
    if choice == 2:
        english2persian()
    if choice == 3:
        persian2english()
    if choice == 4:
        return -1
    
def save_dic():
    f = open("translate.txt", "w")
    for i in range(len(translate_list)):
        f.write(translate_list[i]['english'])
        f.write('\n')
        f.write(translate_list[i]['persian'])
        if i != len(translate_list) -1:
            f.write('\n')

translate_list = []
loading()
show_menu()
choice = choose()
while(choice != -1):  
    show_menu()
    choice = choose()

save_dic()