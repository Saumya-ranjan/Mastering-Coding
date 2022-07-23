# Easy code:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(s)>len(t):
            return False
        
        if s[0]==t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])



# Time Limit Exceeding

def isSubsequence(s, t):
    arr = []
    def func(s,t,output,arr):
        if len(t) == 0:
            if output == s:
                arr.append(tuple(output))
            return 
        func(s,t[1:],output+t[0],arr)
        func(s,t[1:],output,arr)

    res = func(s,t,"",arr)
    if len(arr) > 0:
        return True
    return False
print(isSubsequence('abc','ahgbdc'))