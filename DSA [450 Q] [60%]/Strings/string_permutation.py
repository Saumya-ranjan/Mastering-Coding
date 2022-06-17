arr = []
def permute(s, answer):
    if (len(s) == 0):
        arr.append(answer)
        return   
    for i in range(len(s)):
        mid = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + mid)
 
print("All possible strings are : ")
permute("123", "")
print(arr)