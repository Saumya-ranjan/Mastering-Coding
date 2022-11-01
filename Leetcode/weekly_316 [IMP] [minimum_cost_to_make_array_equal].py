class Solution:
    def minCost(nums,cost):
        a = zip(nums , cost)
        a = sorted(a , key = lambda x: x[0])
        nums.clear()
        cost.clear()
        for j in range(len(a)):
            nums.append(a[j][0])
            cost.append(a[j][1])
        ans = 0
        for i in range(len(a)):
            ans+=a[i][1]
        ans = ans//2
        char_get = 0
        coste = 0
        for k in range(len(nums)):
            coste+=cost[k]
            if coste >= ans:
                char_get = nums[k]
                break
        res = 0
        for r in range(len(nums)):
            res+= abs(nums[r] - char_get) * cost[r]
        return res
        
            