from os import system , name

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def show_menu():
    print('1- SUM')
    print('2- SUB')
    print('3- MULL')
    print('4- EXIT')

def show_complex():
    if COMPLEX_result['b'] > 0:
        print(COMPLEX_result['a'] , 'i' , COMPLEX_result['b']) 
    else:
        print(COMPLEX_result['a'] , '+' , 'i' , COMPLEX_result['b']) 

def SumOfComplex():
    COMPLEX1['a'] = int(input('\'complex 1 = a + ib\' ; please enter a'))
    COMPLEX1['b'] = int(input('\'complex 1 = a + ib\' ; please enter b'))
    COMPLEX2['a'] = int(input('\'complex 2 = a + ib\' ; please enter a'))
    COMPLEX2['b'] = int(input('\'complex 2 = a + ib\' ; please enter b'))

    COMPLEX_result['a'] = COMPLEX1['a'] + COMPLEX2['a']
    COMPLEX_result['b'] = COMPLEX1['b'] + COMPLEX2['b']
    return COMPLEX_result

def SubOfComplex():
    COMPLEX1['a'] = int(input('\'complex 1 = a + ib\' ; please enter a'))
    COMPLEX1['b'] = int(input('\'complex 1 = a + ib\' ; please enter b'))
    COMPLEX2['a'] = int(input('\'complex 2 = a + ib\' ; please enter a'))
    COMPLEX2['b'] = int(input('\'complex 2 = a + ib\' ; please enter b'))

    COMPLEX_result['a'] = COMPLEX1['a'] - COMPLEX2['a']
    COMPLEX_result['b'] = COMPLEX1['b'] - COMPLEX2['b']
    return COMPLEX_result

def MullOfcopmlex():
    COMPLEX1['a'] = int(input('\'complex 1 = a + ib\' ; please enter a'))
    COMPLEX1['b'] = int(input('\'complex 1 = a + ib\' ; please enter b'))
    COMPLEX2['a'] = int(input('\'complex 2 = a + ib\' ; please enter a'))
    COMPLEX2['b'] = int(input('\'complex 2 = a + ib\' ; please enter b'))

    COMPLEX_result['a'] = COMPLEX1['a'] * COMPLEX2['a'] - COMPLEX2['b'] * COMPLEX2['b']
    COMPLEX_result['b'] = COMPLEX1['a'] * COMPLEX2['b'] + COMPLEX2['a'] * COMPLEX1['b'] 

    return COMPLEX_result




while 1:
    
    COMPLEX1 = {'a': 0 , 'b' : 0}
    COMPLEX2 = {'a': 0 , 'b' : 0}
    COMPLEX_result = {'a': 0 , 'b' : 0}
    x = ' '
    show_menu()
    select = int(input('choose one of the option'))
    clear()
    if select == 1:
        
        SumOfComplex()
        show_complex()

    if select == 2:
        
        SubOfComplex()
        show_complex()

    if select == 3:
        
        MullOfcopmlex()
        show_complex()

    if select == 4:
        break



