class time:
    def __init__(self , s = None , m = None , h = None):
        self.s = s
        self.m = m
        self.h = h
    
    def sumoftime(self , timee):
        result = time()
        self.timee = timee
        result.s = self.s + timee.s
        result.m = self.m + timee.m
        result.h = self.h + timee.h

        while result.s >= 60:
            result.s -= 60
            result.m += 1

        while result.m >=60:
            result.m -= 60
            result.h += 1

        return result


    def suboftime(self , timee):
        result = time()
        self.timee = timee
        result.s = self.s - timee.s
        result.m = self.m - timee.m
        result.h = self.h - timee.h

        while result.s < 0:
            result.s += 60
            result.m -= 1

        while result.m < 0:
            result.m += 60
            result.h -= 1

        return result

    def secondtotime(self , s):
        result = time()
        result.s = s

        while result.s >= 60:
            result.s -= 60
            result.m += 1

        while result.m >=60:
            result.m -= 60
            result.h += 1

        return result

    def timetosecond(self):
        result = time()

        result.s = self.s
        result.m = self.m
        result.h = self.h

        return self.s + self.m * 60 + self.h * 3600

    def ShowResultTime(self):
        return(str(self.h) + ':' + str(self.m) + ':' + str(self.s))


def show_menu():
    print('1- SUM Of Time')
    print('2- SUB Of Time')
    print('3- Second To Time')
    print('4- Time To Second')
    print('5- Input New Times')
    print('6- Exit')


select = 0
while select != 6:
    second1 = int(input('please enter second of time 1:'))
    minute1 = int(input('please enter minute of time 1:'))
    hour1 = int(input('please enter hour of time 1:'))
    second2 = int(input('please enter second of time 2:'))
    minute2 = int(input('please enter minute of time 2:'))
    hour2 = int(input('please enter hour of time 2:'))

    a = time(second1 , minute1 , hour1)
    b = time(second2 , minute2 , hour2)

    while select != 5 and select != 6 : 
        show_menu()
        select = int(input('choose one of options:'))
        timeCAL = time()
        if select == 1:
            print(a.sumoftime(b).ShowResultTime())

        if select == 2:
            print(a.suboftime(b).ShowResultTime())

        if select == 3:
            
            second_select = int(input('enter second: '))
            print(timeCAL.secondtotime(second_select).ShowResultTime())

        if select == 4:
            print('1- ', a.ShowResultTime() , '\n2- ' , b.ShowResultTime() ,'\nwhich time?(1 or 2):')
            tts_select = int(input())
            if tts_select == 1:
                print(a.timetosecond())

            if tts_select == 2:
                print(b.timetosecond())

        

