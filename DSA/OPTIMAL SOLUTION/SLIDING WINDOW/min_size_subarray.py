def minSubArrayLen(target,nums):
    # O(N):
    # Sliding Window:
    l , total = 0,0
    count = float('inf')
    for i in range(len(nums)):
        total+=nums[i]
        while total >= target:
            if (i +1) - l < count:
                count = (i+1) - l
            total-=nums[l]
            l+=1    
    
    if count == float('inf'):
        return 0
    return count
minSubArrayLen(7,[2,3,1,2,4,3])
            
            
            
            
               