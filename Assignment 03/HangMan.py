import random

list = []
empty_list = []
score = 10
words = ['book' , 'notebook' , 'laptop' , 'computer' , 'pen' , 'phone' , 'python' , 'programming']

word_selected = random.choice(words)

#print(word_selected)

for i in range(len(word_selected)):
        list.append(word_selected[i])
        empty_list.append('_')

while score:
    
    print('\nYour Score: ',score,'\n')

    for j in range(len(word_selected)):
            print(empty_list[j],end='')   

    user_word = input('\n')

    if user_word in word_selected:
        for i in range(len(word_selected)):
            if list[i] == user_word:
                empty_list[i] = list[i]   

    elif user_word not in word_selected:
        score = score - 1

        if score:
            print('Your Score: ',score,'\noh! this is wrong!! please enter another character:',end=' ') 
        elif score < 1:
            print('Your Score: ',score,'\noh! this is wrong')
        

    if list == empty_list:
        print('\nYou win!!!')
        break

    elif score < 1:
        print('\ngame over!!')
        break
    
