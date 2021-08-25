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
    #clear()
    print('1- Rock')
    print('2- Paper')
    print('3- Scissors')

selector = ['Rock' , 'Paper' , 'Scissors']
score = {'user1_score' : 0 , 'user2_score' : 0}
f = Figlet(font = 'standard')
print(colored(f.renderText('Roc\nPaper\nScissors'),'magenta'))

print(colored('1- Play with your freind','white'))
print(colored('2- Play with computer','white'))
select = int(input(colored('Select one of the following options:', 'white')))


# user1 = int(input(colored('User 1:','red')))
# user2 = 10




while 1:
    #clear()
    selection()
    user1 = int(input(colored('User 1:','red')))
    user2 = 10
    if select == 1: 
        selection()
        user2 = int(input(colored('User 2:','blue')))

    if select == 2:
        user2 = randint(1,3)

    print(user2)
    clear()
    print(colored(selector[user1-1] , 'red') , 'Vs' ,colored(selector[user2-1] , 'blue'))
    
    if (user1 == 1 and user2 == 1) or (user1 == 2 and user2 == 2) or (user1 == 3 and user2 == 3):
        pass
        #print('draw')

    if (user1 == 1 and user2 == 3) or (user1 == 2 and user2 == 1) or (user1 == 3 and user2 == 2):
        score['user1_score'] += 1
        #print(colored('user 1' , 'red'), 'WIN!!')

    if (user2 == 1 and user1 == 3) or (user2 == 2 and user1 == 1) or (user2 == 3 and user1 == 2):
        score['user2_score'] += 1
        #print(colored('user 2' , 'blue'), 'WIN!!')

    print(colored('score of user 1:' , 'red') , score['user1_score'] , colored('\nscore of user 2:' , 'blue') , score['user2_score'] )

    if score['user1_score'] == 3:
        print(colored('user 1' , 'red'), 'WIN!!')
        break
    
    if score['user2_score'] == 3:
        print(colored('user 2' , 'blue'), 'WIN!!')
        break
