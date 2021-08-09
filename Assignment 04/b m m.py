def bmm(num1,num2):
    num1_list = []
    num2_list = []
    finally_list = []
    for i in range((num1//2)+1):
        for j in range(num1+1):
            if i * j == num1:
                num1_list.append(i)
    
    for i in range((num2//2)+1):
        for j in range(num2+1):
            if i * j == num2:
                num2_list.append(i)

    for i in range(len(num1_list)):
        if num1_list[i] in num2_list:
            finally_list.append(num1_list[i])
    #print(num1_list)
    #print(num2_list)
    print(finally_list)

num1 = int(input())
num2 = int(input())

bmm(num1,num2)
        
                    