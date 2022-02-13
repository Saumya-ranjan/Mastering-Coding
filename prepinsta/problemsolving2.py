# Longest Substring Without Repeating Characters

# Input: s = "abcabcbb" first it will check a then b then c so count would be 3 abca 
# so there is a duplicate so it remove a from left then it continiues
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def func(x):
    start = max_len = 0
    hash = {}
    for i in range (len(x)):
        if x[i] in hash and start<=hash[x[i]]:
            start = hash[x[i]]+1
        else:
            max_len = max(max_len,i-start+1)
        hash[x[i]] = i
    print(max_len)


        

    


func("abccdabcbb")