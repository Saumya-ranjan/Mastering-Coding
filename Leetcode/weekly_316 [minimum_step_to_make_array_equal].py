# Hard Category But Easy Solution

class Solution:
    def makeSimilar(nums,target):
        target_even = []
        target_odd = []
        nums_even = []
        nums_odd = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums_even.append(nums[i])
            else:
                nums_odd.append(nums[i])
            if target[i]%2 == 0:
                target_even.append(target[i])
            else:
                target_odd.append(target[i])
        
        target_even.sort()
        target_odd.sort()
        nums_even.sort()
        nums_odd.sort()
        
        res = 0
        for k in range(len(nums_even)):
            if nums_even[k] - target_even[k] > 0:
                res+= nums_even[k] - target_even[k]
        for r in range(len(nums_odd)):
            if nums_odd[r] - target_odd[r] > 0:
                res+= nums_odd[r] - target_odd[r]
        return res//2
                
                