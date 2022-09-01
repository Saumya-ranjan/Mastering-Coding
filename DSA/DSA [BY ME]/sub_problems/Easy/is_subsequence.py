def func(s,t):
    if len(s) > len(t):
        return False  #Here should be return so the lasr print doesnt work
    if len(s) == 0:
        return True
    subsequence=0
    for i in range(len(t)):
        if s[subsequence] == t[i]:
            subsequence+=1
        if len(s) == subsequence:
            return True
    return False

print(func( 'let','leetcode'))