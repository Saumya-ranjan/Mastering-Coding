def func(candies , extraCandies):
    count = 0
    hash = {}
    arr = []
    for i in range(len(candies)):
        hash[i] = candies[i] + extraCandies
                
    for v in (hash.values()):
        for j in (candies):
            if v >= j:
                count+=1
            else:
                count+=0
            
        if count==len(candies):
            arr.append('true')
        else:
            arr.append('false')
        count = 0
            
                   
    print(arr)


func([12,1,12],  10)