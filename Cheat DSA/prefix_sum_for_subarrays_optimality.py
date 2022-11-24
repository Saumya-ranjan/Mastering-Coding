# Refer this video for combinations and storage 
# https://www.youtube.com/watch?v=u9m-hnlcydk&t=18s

class Solution:
    def subarraysDivByK(self,nums , k):
        import math
        hash = {}
        res = 0
        for i in range(1 , len(nums) ):
            nums[i] = nums[i-1] + nums[i]
        
        for i in range(len(nums)):
            nums[i] = nums[i] % k 
        
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]]+=1
        
        for i in hash.keys():
            if i == 0 and hash[i]<2:
                res+=hash[i]
            elif i == 0 and hash[i] > 1:
                res+= hash[i] + ( math.factorial(hash[i]) / (math.factorial(hash[i] - 2) * 2))
            elif hash[i] > 1:
                res+=(math.factorial(hash[i]) / (math.factorial(hash[i] - 2) * 2))
        return int(res)
                



# One More Example -- > 

class Solution:
    def checkSubarraySum(nums , k):
        hash = {}
        arr = []
        for i in range(1 , len(nums)):
            nums[i] = nums[i-1] + nums[i]
        for i in range(len(nums)):
            nums[i] = nums[i] % k
        
        for i in range( len(nums)):
            if i!=0 and nums[i] == 0:
                return True
            elif nums[i] not in hash:
                hash[nums[i]] = [i]
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]].append(i)
        
        for i in hash.keys():
            if hash[i][-1] - hash[i][0] > 1:
                return True
        return False
        
            