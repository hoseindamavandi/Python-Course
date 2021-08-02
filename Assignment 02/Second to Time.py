sec = int(input())

hour = int(sec // 3600) 
min = int((sec % 3600) // 60) 
second = ((sec % 3600) % 60)  

print(str(hour).zfill(2),':',str(min).zfill(2),':',str(second).zfill(2))
