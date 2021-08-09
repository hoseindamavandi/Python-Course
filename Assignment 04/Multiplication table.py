def multiplication_table(m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(i*j,'\t',end='')
        print('\n')


m = int(input())
n = int(input())

multiplication_table(m,n)