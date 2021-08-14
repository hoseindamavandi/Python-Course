import random
from termcolor import colored

def check_win():
    draw=0
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            return 0
        elif game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            return 0
        elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
            return 0
        elif game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
            return 0
        elif game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            return 1
        elif game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            return 1
        elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
            return 1     
        elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
            return 1

        for j in range(3):
            if game[i][j] != '-':
                draw+=1
            if draw == 9:
                return -1

def print_game():
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                print(colored(game[i][j],'yellow'),end=' ')
            elif game[i][j] == 'O':
                print(colored(game[i][j],'red'),end=' ')
            else:
                print(game[i][j],end=' ')
        print('\n',end='')

def playerX_computer():
    print('Player 2:')
    row = random.randint(0,2)
    col = random.randint(0,2)
    if game[row][col] == '-' and 0 <= row <= 2 and 0 <= col <= 2:
        game[row][col] = 'X'
    else:
        playerX_computer()

def playerX():
    print('Player 2:')
    row = int(input('enter row:'))
    col = int(input('enter col:'))
    if game[row][col] == '-' and 0 <= row <= 2 and 0 <= col <= 2:
        game[row][col] = 'X'
    else:
        print('error! select enother location:')
        playerX()

def playerO():
    print('Player 1:')
    row = int(input('enter row:'))
    col = int(input('enter col:'))
    if game[row][col] == '-' and 0 <= row <= 2 and 0 <= col <= 2:
        game[row][col] = 'O'
    else:
        print('error! select enother location:')
        playerO()


print('Choose one of the following options:\n1-Playing with copiuter\n2-playing with your friend')
n = int(input())

game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

print_game()
f=1
while 1:
    if f == 1:
        playerO()
        print_game()
        check_win()
        if check_win() == 0:
            print('player X is win')
            f=0
        if check_win() == 1:
            print('player O is win')
            f=0
        if check_win() == -1:
                print('draw')
                f=0
        
    if f == 1:
        if n == 1:
            if check_win() == 0:
                print('player X is win')
                f=0
            if check_win() == 1:
                print('player O is win')
                f=0
            if check_win() == -1:
                print('draw')
                f=0

            playerX_computer()

        if n == 2:
            if check_win() == 0:
                print('player X is win')
                f=0
            if check_win() == 1:
                print('player O is win')
                f=0
            if check_win() == -1:
                print('draw')
                f=0

            playerX()

        print_game()
        
    elif check_win() == 0:
        break