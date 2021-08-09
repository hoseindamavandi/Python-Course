import math

def Quadratic_Equation(a,b,c):
    if a==0:
        x = (-c)/b
        print('x is:',x)

    elif math.sqrt((b**2)-(4*a*c)) == 0:
        x = -b /(2*a*b)
        print('x is:',x)

    else:
        print('x1 is: ' ,(-(b) + math.sqrt((b**2)-(4*a*c)))/(2*a))
        print('x2 is: ' ,(-(b) - math.sqrt((b**2)-(4*a*c)))/(2*a))



a = float(input('enter \'A\' in Ax^2 + Bx + C = 0 : '))
b = float(input('enter \'B\' in Ax^2 + Bx + C = 0 : '))
c = float(input('enter \'C\' in Ax^2 + Bx + C = 0 : '))

Quadratic_Equation(a,b,c)