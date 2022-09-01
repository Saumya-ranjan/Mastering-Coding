def func(n):
    arr = []
    x = str(n)[::-1]
    
    count = 0
    for i in x:
        arr.append(int(i)*(2**count))
        count+=1
    print(sum(arr))
    

    
#FORMULA IS (REVERSE STRING) AND THEN (NUM * 2^0)....
func(100)