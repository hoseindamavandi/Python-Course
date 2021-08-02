name=input("enter your name:")
score1=float(input("enter score1:"))
score2=float(input("enter score2:"))
score3=float(input("enter score3:"))

avg= (score1+score2+score3)/3

if avg >= 17:
    print(name ,"dear, you are great")
if 17> avg >= 12:
    print(name ,"dear, you are normal")
if avg < 12:
    print(name ,"dear, you are fail")