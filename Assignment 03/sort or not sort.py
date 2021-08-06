a = list(input('Enter your list and separate them with , :').split(','))
f= True
for i in range(len(a)):
    a[i]=int(a[i])

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        f = False
        break

if f :
    print('sort!')
else:
    print('not sort!')
