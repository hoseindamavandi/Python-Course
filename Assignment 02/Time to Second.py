time = list(input().split(':'))
sec = int(time[0])*3600
min = int(time[1])*60
hours = int(time[2])

second = sec + min + hours

print(second)