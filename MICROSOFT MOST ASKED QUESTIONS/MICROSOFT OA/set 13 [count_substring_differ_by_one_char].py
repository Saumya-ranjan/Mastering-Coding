class Solution:
    def countSubstrings(s,t):
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                x = i
                y = j
                diff = 0
                while x < len(s) and y < len(t):
                    if s[x] != t[y]:
                        diff+=1
                    if diff ==1:
                        res+=1
                    if diff > 1:
                        break
                    x+=1
                    y+=1
        return res    
            
        
        
        
        
        
        # tle
#         counter = 0
#         def watching_same(a , b):
#             count = 0
#             for i in range(len(a)):
#                 if a[i] == b[i]:
#                     count+=1
#             if count == len(a) -1:
#                 return True
#             return False     
            
#         # print(watching_same("b" , "a"))
#         # Driver Code
#         arr = []
#         arr1 = []
#         for i in range(len(s)+1):
#             for j in range(i+1 , len(s)+1):
#                 arr.append(s[i:j])
#         for i in range(len(t)+1):
#             for j in range(i+1 , len(t)+1):
#                 arr1.append(t[i:j])
#         # print(arr , arr1)
#         for k in range(len(arr)):
#             for r in range(len(arr1)):
#                 if len(arr[k]) == len(arr1[r]):
#                     # print(arr[k] , arr1[r])
#                     if watching_same(arr[k] , arr1[r]) == True:
#                         counter+=1
#         return counter
                    
            
    
            