t = [[1],
     [1,1]]


# t = [[1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1],
#      [1,5,10,10,5,1],
#      [................]


n = int(input())
for i in range(2,n):
    t.append([1])
    for j in range(1,i+1):
        t_nested_list = t[i]
        if j == i:
            t_nested_list.append(1)
            break
        t_nested_list.append(t[i-1][j-1] + t[i-1][j])

for i in range(n):
   for j in range(i+1):
       print(t[i][j],'\t',end='')
   print("\n",end='')
   
#print(t)