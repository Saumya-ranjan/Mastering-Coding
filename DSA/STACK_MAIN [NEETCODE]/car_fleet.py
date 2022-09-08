def carFleet(target,position , speed):
    # Optimal 
    hash = {}
    res = 0
    curr = 0
    for i in range(len(position)):
        hash[position[i]] =   (target - position[i]) / speed[i]# Time Taken
            
    a = sorted(hash.items() ,  key = lambda x:-x[0])
    for i in range(len(a)):
        if a[i][1] >  curr:
            curr = a[i][1]
            res+=1
    return res
carFleet(12 , [10,8,0,5,3] , [2,4,1,1,3])