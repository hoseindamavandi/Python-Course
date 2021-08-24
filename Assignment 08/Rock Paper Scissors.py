from random import randint
from termcolor import colored
from pyfiglet import Figlet
from os import close, system, name

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')


def selection():
    clear()
    print('1- Rock')
    print('2- Paper')
    print('3- Scissors')

selector = ['Rock' , 'Paper' , 'Scissors']

f = Figlet(font = 'standard')
print(colored(f.renderText('Roc\nPaper\nScissors'),'magenta'))

print(colored('1- Play with your freind','white'))
print(colored('2- Play with computer','white'))
select = int(input(colored('Select one of the following options:', 'white')))
selection()
user1 = int(input(colored('User 1:','red')))
user2 = 10

if select == 1: 
    selection()
    user2 = int(input(colored('User 2:','blue')))

if select == 2:
    user2 = randint(1,3)

clear()
print(colored(selector[user1-1] , 'red') , 'Vs' ,colored(selector[user2-1] , 'blue'))

if (user1 == 1 and user2 == 1) or (user1 == 2 and user2 == 2) or (user1 == 3 and user2 == 3):
    print('draw')

if (user1 == 1 and user2 == 3) or (user1 == 2 and user2 == 1) or (user1 == 3 and user2 == 2):
    print(colored('user 1' , 'red'), 'WIN!!')

if (user2 == 1 and user1 == 3) or (user2 == 2 and user1 == 1) or (user2 == 3 and user1 == 2):
    print(colored('user 2' , 'blue'), 'WIN!!')
