n = int(input('print length of Snake:'))

for i in range(n):
    if i % 2:
        print('#',end='')
    if i % 2 == 0:
        print('*',end='')

        