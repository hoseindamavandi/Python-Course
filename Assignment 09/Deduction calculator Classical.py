class fraction:
    def __init__(self , s = None, m = None):
        self.s = s
        self.m = m

    def SumOfFraction(self, fr):
        result = fraction()
        self.fr = fr
        result.s = (fr.s * self.m) + (self.s * fr.m)
        result.m = fr.m * self.m

        return result

    def SubOfFraction(self, fr):
        result = fraction()
        self.fr = fr
        result.s = (fr.s * self.m) - (self.s * fr.m)
        result.m = fr.m * self.m

        return result

    def MullOfFraction(self, fr):
        result = fraction()
        self.fr = fr
        result.s = fr.s * self.s
        result.m = fr.m * self.m

        return result

    def DivOfFraction(self, fr):
        result = fraction()
        self.fr = fr
        result.s = fr.s * self.m
        result.m = fr.m * self.s

        return result

    def ShowFraction(self):
        print(self.s , '/', self.m)

    def ShowMenu(self):
        print('1- Sum of two fraction')
        print('2- Mull of two fraction')
        print('3- Sub of two fraction')
        print('4- Div of two fraction')
        print('5- input new fractions')
        print('6- Exit')

    def Select(self, select, a, b):
        # self.select = int(input('choose one of options:'))
        self.select = select
        self.a = a
        self.b = b
        fr = fraction(NOF1, DOF1)
        
        if select == 1:
            a.SumOfFraction(b).ShowFraction()

        if select == 2:
            a.MullOfFraction(b).ShowFraction()

        if select == 3:
            a.SubOfFraction(b).ShowFraction()

        if select == 4:
            a.DivOfFraction(b).ShowFraction()

        

select = 0
while select != 6:
    NOF1 = int(input('enter Numerator of fraction 1:')) 
    DOF1 = int(input('enter Denominator of fraction 1:'))
    NOF2 = int(input('enter Numerator of fraction 2:'))
    DOF2 = int(input('enter Denominator of fraction 2:'))
    a = fraction(NOF1 , DOF1)
    b = fraction(NOF2 , DOF2)

    while select != 5 and select != 6:
        fr = fraction(NOF1,DOF1)
        fr.ShowMenu()
        select = int(input('Choose one of options:'))
        fr.Select(select, a, b)

        
        


