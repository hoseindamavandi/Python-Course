def is_fact(num):
    IsFact = 1
    f=0
    for i in range(num):
        IsFact = IsFact * (i+1)
        if IsFact == num:
            print('yes')
            f=1
            break
    if f==0 :
        print('no')


num = int(input())
is_fact(num)        
