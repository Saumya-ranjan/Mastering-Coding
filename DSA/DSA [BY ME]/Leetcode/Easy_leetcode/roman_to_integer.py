def func(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    value= 0
    for i in range(len(s)-1,-1,-1):
        num = roman[s[i]]
        if 3*num < value: 
            value = value-num
        else: 
            value = value+num
    print( value)
            

func(str(input("Enter a Roman Number: ")))