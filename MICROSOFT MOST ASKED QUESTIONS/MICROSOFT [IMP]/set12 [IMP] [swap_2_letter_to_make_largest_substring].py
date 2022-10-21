class Solution:
    def maxRepOpt1(text):
        # Group By
        res = 0
        arr = []
        count = 0
        counter = text[0]
        hash = {}
        for k in range(len(text)):
            if text[k] not in hash:
                hash[text[k]] = 1
            else:
                hash[text[k]]+=1
        
        for i in range(len(text)):
            if text[i] == counter:
                count+=1
            else:
                arr.append((counter , count))
                counter = text[i]
                count = 1
                
        if len(arr) == 0:
            arr.append((counter , count))
        elif counter == arr[-1][0] :
            arr[-1][0]+=1
        else:
            arr.append((counter , count))
            
        # Actual Code -- >
        for j in range(len(arr)):
            if min(arr[j][1] + 1 , hash[arr[j][0]]) > res:
                res = min(arr[j][1] + 1 , hash[arr[j][0]])
                
                
                
        for i in range(1 , len(arr) - 1):
            if arr[i-1][0] == arr[i+1][0] and arr[i][1] == 1 :  
                res = max(res , min(arr[i-1][1] + arr[i+1][1] + 1 , hash[arr[i+1][0]]))
        return res
            
        
        # def maxRepOpt1(self, S):
        # # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        # A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        # # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        # count = collections.Counter(S)
        # # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        # res = max(min(k + 1, count[c]) for c, k in A)
        # # merge 2 groups together
        # for i in xrange(1, len(A) - 1):
        #     # if both sides have the same char and are separated by only 1 char
        #     if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
        #         # min here serves the same purpose
        #         res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        # return res
            
            