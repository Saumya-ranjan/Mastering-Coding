class Solution:
    def productExceptSelf(nums):
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        count = 1
        for i in range(1 , len(nums)):
            count = count * nums[i-1]
            left[i] = count 
        count = 1
        for j in range(len(nums)-2, -1 , -1):
            count = count*nums[j+1]
            right[j] = count
        for i in range(len(nums)):
            left[i] = left[i]*right[i]
        return left
            
            
            
# INTUITION        
        
#         Numbers:     2    3    4     5
# Lefts:            2  2*3 2*3*4
# Rights:  3*4*5  4*5    5      
# Let’s fill the empty with 1:

# Numbers:     2    3    4     5
# Lefts:       1    2  2*3 2*3*4
# Rights:  3*4*5  4*5    5     1

# RESULT: 
# multiply left with right 
        