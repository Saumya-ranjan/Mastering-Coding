class Solution:
    def search(nums,target):
        l , r = 0 , len(nums)-1
        while l <=r:
            a = (l+r) //2
            if target == nums[a]:
                return a
            if nums[l] <= nums[a]:
                if target > nums[a] or target < nums[l]:
                    l =a+1
                else:
                    r =a-1
            else:
                if target < nums[a]  or target > nums[r]:
                    r= a-1
                else:
                    l = a+1
                    
        return -1
                        
                        
                       