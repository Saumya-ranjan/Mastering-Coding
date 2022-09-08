def minEatingSpeed(piles , h):
    l = 1
    r = max(piles)
    res = r
    while l <= r:
        a = (l+r) //2
        count = 0
        for i in piles:
            if (i/a).is_integer():
                count+=int(i/a)
            else:
                count+= int(i/a)+1
                
        if count <= h :
            res = min(res,a)
            r = a-1
        else:
            l = a+1
    return res
minEatingSpeed([3,6,7,11], 8)
            
        
        
        
        #  Brute Force Method:
        
#         for i in range(1,max(piles)+1):
#             count = 0
#             for j in range(len(piles)):
#                 if (piles[j]/i).is_integer():
#                     count+= int(piles[j] / i)
#                 else:
#                     count+= int(piles[j] / i) +1
#                 if count > h:
#                     break
#             if count ==  h:
#                 return i 
            
        # Optimal Method Using Binary Search To tweak It a Little Bit with same Algorithm:
        
        
        # l = 0
        # r = max(piles)+1
        # for i in range(1,max(piles)+1):
        #     if l < r:
        #         count = 0
        #         for j in range(len(piles)):
        #             a = int((l+r) / 2)
        #             if (piles[j] / a).is_integer():
        #                 count+= int(piles[j] / a)
        #             else:
        #                 count+=  int(piles[j] / a) + 1
        #         if count == h:
        #             return a
        #         elif count < h:
        #             r = a
        #         else:
        #             l = a
        
                        
                        
                    
                
        