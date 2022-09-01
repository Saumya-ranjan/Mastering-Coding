# Given an integer n, return the number 
# of strings of length n that consist only 
#  vowels (a, e, i, o, u) and are 
# lexicographically sorted.
# A string s is lexicographically sorted 
# if for all valid i, s[i] is the same as or 
# comes before s[i+1] in the alphabet


# Examples:
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that 
# consist of vowels only are ["a","e","i","o","u"].

# Example 2:
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings 
# that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei",
# "eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not 
# a valid string since 'e' comes after 'a' 
# in the alphabet

def countVowelStrings(n):
    dp = [[1 for _  in range(5)] for _ in range(n)]
    for i in range(1,len(dp)):
        for j in range(5):
            if j ==0:   
                dp[i][j]  = sum(dp[i-1])
            else:
                dp[i][j] = dp[i][j-1] - dp[i-1][j-1]             
    return sum(dp[n-1])
countVowelStrings(4)