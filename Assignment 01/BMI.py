w=float(input("enter your weight (Kilograms):"))
h=float(input("enter your height (Metres):"))
bmi= w/(h**2)

if bmi < 18.5:
    print("UNDERWEIGHT")
if 18.5 <= bmi <= 24.9:
    print("NORMAL")
if 25 <= bmi <= 29.9:
    print("OVERWEIGHT")
if 30 <= bmi <= 34.9:
    print("OBESE")
if 35 <= bmi :
    print("EXTREMELY OBESE")
