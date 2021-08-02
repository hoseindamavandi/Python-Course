import math
import re

op=input("Select the operation:\n+\n-\n*\n/\nradical\nsin\ncot\ntan\nfactorial\n")
if op== "+" or op== "-" or op== "*" or op== "/":
    print("Selective operations is A" ,op ,"B\nenter A:")
    a=float(input())
    b=float(input("\nenter B:"))
    
    if op=="+":
        result=a+b

    if op=="-":
        result=a-b

    if op=="*":
        result=a*b
    
    if op=="/":
        if b==0:
            print("Error!!!")
        else:
            result=a/b
    
    print(a,op,b,"is: ",result)

elif op=="radical" or op=="sin" or op=="cot" or op=="tan" or op=="factorial":
    print("Selective operations is:" ,op ,"A\nenter A:")
    a=float(input())

    if op=="radical":
        result=math.sqrt(a)

    if op=="sin":
        result=math.sin(a*math.pi/180)

    if op=="cot":
        result=math.sin(a*math.pi/180)

    if op=="tan":
        result=math.sin(a*math.pi/180)

    if op=="factorial":
        result=math.factorial(int(a))

    print(op,a,"is: ",result)