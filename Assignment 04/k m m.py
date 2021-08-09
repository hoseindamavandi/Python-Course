def kmm(num1,num2):
    num1_list = []
    num2_list = []
    finally_list = []
    
    for i in range(1,(num1*num2)+1):
        num1_list.append(i*num1)
    
    for i in range(1,(num1*num2)+1):
        num2_list.append(i*num2)

    for i in range(len(num1_list)):
        if num1_list[i] in num2_list:
            print(num1_list[i])
            break


num1 = int(input())
num2 = int(input())

kmm(num1,num2)
    
