def Checkered_page(m,n):
    for i in range(m):
        for j in range(n):
            if (i+j)%2 == 0:
                print('*',end='')
            elif (i+j)%2 != 0:
                print('#',end='')
            
        print('\n',end='')

m = int(input())
n = int(input())
Checkered_page(m,n)