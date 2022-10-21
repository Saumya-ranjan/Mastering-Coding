class Solution:
    def prevPermOpt1(self, arr):
        # o(n) -- >
        a = -1
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                a = i
        if a == -1:
            return arr
            
        maxi = 0
        idx = 0
        for j in range(len(arr) - 1 , a, -1):
            if arr[j] >= maxi and arr[j] < arr[a]:
                maxi = arr[j]
                idx = j
        print(a , idx)
        arr[a] , arr[idx] = arr[idx] , arr[a]
        return arr
                
                
                    
                    
                    
        