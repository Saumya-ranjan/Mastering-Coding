import heapq as heapq
from collections import Counter
class Solution:
    def reorganizeString(s):
        # Priority Queue -- >
        count = Counter(s)
        maxheap = []
        for i in count.keys():
            maxheap.append([-count[i] , i])
        heapq.heapify(maxheap)
        
        prev = None
        ans = ""

        while len(maxheap)!=0 or prev!=None:
            if prev !=None and len(maxheap) == 0:
                return ""
            cnt , char = heapq.heappop(maxheap)
            # print(cnt , char)
            ans+= char
            # print(ans)
            cnt+=1
            
            if prev!=None:
                heapq.heappush(maxheap , prev)
                prev = None
                
            if cnt != 0:
                prev = [cnt , char]
            # print(ans)
        return ans
            
            
            
                
            
        
        
        
                
        