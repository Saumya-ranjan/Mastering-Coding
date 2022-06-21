def longestPalindromeSubseq( s):  
    N = len(s)
    reversed_s = "".join(reversed(s))    
    def longestCommonSubseqTabulation(str1, str2, n, m):
        table = [[None for x in range(m + 1)] for x in range(n + 1)]     
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                else:
                    if str1[i- 1] == str2[j - 1]:
                        table[i][j] = 1 + table[i - 1][j - 1]
                    else:
                        table[i][j] = max(table[i - 1][j],table[i][j - 1])            
        return table[n][m]    
    res = longestCommonSubseqTabulation(s, reversed_s, N, N)
        
    return res
print(longestPalindromeSubseq("aaba"))