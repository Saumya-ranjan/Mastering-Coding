class Solution:
    def sumZero(self, n: int):
        res = []
        if n%2 ==0 :
            for i in range(-int(n/2) , int(n/2)+1):
                if i != 0:
                    res.append(i)     
        else:
            for i in range(-int(n/2) , int(n/2) + 1):
                res.append(i)
        return res
            
        