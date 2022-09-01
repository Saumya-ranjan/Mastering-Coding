def func(n):
    # if (n % 400 == 0 or n% 4 == 0):
    #     print("leap year")
    # elif (n%100 ==0): 
    #     print("Not leap year")
    if n%400==0 or (n%100 != 0 and n%4 ==0):
        print("leap year")
    else:
        print("Not leap year")



func(2000)