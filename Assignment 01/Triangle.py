print("We want to make a triangle with three numbers a, b, c")
a=float(input("enter A:"))
b=float(input("enter B:"))
c=float(input("enter C:"))
result=False
if a+b>c:
    result=True
if a+c>b:
    result=True
if b+c>a:
    result=True

if result==False:
    print("Error!!!")

if result==True:
    print("ok:)")