def twoSum(numbers,target):  
    # Dictionary   
      
    hash = {}
    for i,j in enumerate(numbers):
        if target - j in hash:
            return [hash[target-j]+1 , i+1]
        else:
            hash[j] = i
    

    # Two Pointer (as it's sorted )
    l = 0
    r = len(numbers)-1
    for i in range(len(numbers)):
        if l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1
    return 0

twoSum([2,7,11,15],9)
        
            