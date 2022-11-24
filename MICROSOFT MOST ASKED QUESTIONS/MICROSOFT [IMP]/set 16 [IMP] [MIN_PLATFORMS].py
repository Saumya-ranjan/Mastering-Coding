# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        per = []
        for i in range(n):
            per.append([arr[i], dep[i]])
        per.sort()
        
        ans = 1
        stack = [per[0][1]]
        for i in range(1 , len(per)):
            if per[i][0] <= stack[0]:
                ans+=1
                stack.append(per[i][1])
                stack.sort()
            else:
                stack[0] = per[i][1]
                stack.sort()
        return ans
                