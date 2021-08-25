n = int(input())

for i in range(n):
    for j in range(1 , n-i):
        print(' ',end="")
    print('*'*((2*i + 1)))

for i in range(2 , n+1):
    for j in range(1 , i):
        print(' ',end="")
    print('*'*((2*(n-i) + 1)))