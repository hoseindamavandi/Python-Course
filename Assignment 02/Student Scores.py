x = int(input('enter the number of student:'))
max = 0
min = 20
sum = 0 
score = []
for i in range(x):
    score.append(float(input('enter the programming score student:')))
    
    if score[i] > max:
        max = score[i]

    if score[i] < min:
        min = score[i]

    sum = sum + score[i]
    avg = sum / x

print(min,'/n',max,'/n',avg)
