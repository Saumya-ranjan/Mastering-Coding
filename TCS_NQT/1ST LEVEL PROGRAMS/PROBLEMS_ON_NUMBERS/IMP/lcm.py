# lcm = num1*num2 / gcd(num1, num2)

def func(num1,num2):
    arr = []
    arr1 = []
    arr2  =[]
    for i in range(2,num1+1):
        if num1%i == 0:
            arr.append(i)
    for i in range(2,num2+1):
        if num2%i == 0:
            arr1.append(i)
    for i in arr:
        if i in arr1:
            arr2.append(i)
    if len(arr2)== 0:
        lcm = (num1*num2)/1
    else:
        lcm = (num1*num2)/max(arr2)
        
    print(int(lcm))
    


func(13,15)