def show_menu():
    print('1- Sum')
    print('2- Multiply')
    print('3- Subtraction')
    print('4- Division')

def makhraj_moshtarak_sum():
    s = franction1['s'] * franction2['m']
    m = franction2['s'] * franction1['m']
    return s + m

def makhraj_moshtarak_sub():
    s = franction1['s'] * franction2['m']
    m = franction2['s'] * franction1['m']
    return s - m

def SumOfFraction():
    franction_result['s'] = makhraj_moshtarak_sum()
    franction_result['m'] = franction1['m'] * franction2['m']

def DivOfFraction():
    franction_result['s'] = franction1['s'] * franction2['m']
    franction_result['m'] = franction1['m'] * franction2['s']

def SubOfFraction():
    franction_result['s'] = makhraj_moshtarak_sub()
    franction_result['m'] = franction1['m'] * franction2['m']

def MullOfFraction():
    franction_result['s'] = franction1['s'] * franction2['s']
    franction_result['m'] = franction1['m'] * franction2['m']

franction1 = {}
franction2 = {}
franction_result = {}

franction1['s'] = int(input('sorat kasr 1:'))
franction1['m'] = int(input('makhraj kasr 1:'))
franction2['s'] = int(input('sorat kasr 2:'))
franction2['m'] = int(input('makhraj kasr 2:'))

show_menu()
select = int(input('select a number:'))

if select == 1:
    SumOfFraction()

if select == 2:
    MullOfFraction()

if select == 3:
    SubOfFraction()

if select == 4:
    DivOfFraction()

print(franction_result['s'] , '/' , franction_result['m'])