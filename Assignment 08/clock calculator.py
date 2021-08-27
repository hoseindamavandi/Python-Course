from os import system , name

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def show_menu():
    print('1- second to time')
    print('2- time to second')
    print('3- sum of time')
    print('4- sub of time')
    print('5- exit')

def Second2Time():
    seconds = int(input('enter second:'))
    clock['s'] = seconds
    
    while clock['s'] >= 60:
        clock['s'] -= 60
        clock['m'] += 1

    while clock['m'] >=60:
        clock['m'] -= 60
        clock['h'] += 1

    return clock

def Time2Second():
    clock['s'] = int(input('emter second:'))
    clock['m'] = int(input('emter minutes:'))
    clock['h'] = int(input('enter hour:'))

    return clock['s'] + clock['m'] * 60 + clock['h'] * 3600

def SumOfTime():
    clock1 = {}
    clock2 = {}
    clock_result = {'h':0 , 'm':0 , 's':0}
    clock1['s'] = int(input('please enter second of time 1:'))
    clock1['m'] = int(input('please enter minutes of time 1:'))
    clock1['h'] = int(input('please enter hour of time 1:'))
    clock2['s'] = int(input('please enter second of time 2:'))
    clock2['m'] = int(input('please enter minutes of time 2:'))
    clock2['h'] = int(input('please enter hour of time 2:'))

    clock_result['s'] = clock1['s'] + clock2['s']
    clock_result['m'] = clock1['m'] + clock2['m']
    clock_result['h'] = clock1['h'] + clock2['h']

    while clock_result['s'] >= 60:
        clock_result['s'] -= 60
        clock_result['m'] += 1

    while clock_result['m'] >=60:
        clock_result['m'] -= 60
        clock_result['h'] += 1

    return clock_result

def SubOfTime():
    clock1 = {}
    clock2 = {}
    clock_result = {'h':0 , 'm':0 , 's':0}
    clock1['s'] = int(input('please enter second of time 1:'))
    clock1['m'] = int(input('please enter minutes of time 1:'))
    clock1['h'] = int(input('please enter hour of time 1:'))
    clock2['s'] = int(input('please enter second of time 2:'))
    clock2['m'] = int(input('please enter minutes of time 2:'))
    clock2['h'] = int(input('please enter hour of time 2:'))

    clock_result['s'] = clock1['s'] - clock2['s']
    clock_result['m'] = clock1['m'] - clock2['m']
    clock_result['h'] = clock1['h'] - clock2['h']

    while clock_result['s'] < 0:
        clock_result['s'] += 60
        clock_result['m'] -= 1

    while clock_result['m'] < 0:
        clock_result['m'] += 60
        clock_result['h'] -= 1

    return clock_result



while 1:
    clock = {'h' : 0 , 'm' : 0 , 's' : 0}
    show_menu()
    select = int(input('Choose one of the options:'))
    clear()

    if select == 1:
        print(Second2Time())

    if select == 2:
        print(Time2Second())

    if select == 3:
        print(SumOfTime())

    if select == 4:
        print(SubOfTime())
    
    if select == 5:
        break

