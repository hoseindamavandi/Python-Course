from random import randint
while True:
    select = input('write dice or exit:')
    if select == 'exit':
        break
    
    if select == 'dice' :
        dice = randint(1,6)
        print(dice)

        if dice == 6:
            print('wow You got an award!!')
        
        if dice != 6:
            print('ops! You lost')
            break

