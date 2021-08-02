n = int(input())
list = []
sum = 1
for i in range(n):
    if i < 2:
        list.append(1)

    else:
        list.append(list[i-1] + list[i-2])

print(list)