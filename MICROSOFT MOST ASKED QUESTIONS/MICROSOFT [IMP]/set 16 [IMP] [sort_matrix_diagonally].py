# In diagonal case do i-j:

class Solution:
    def diagonalSort(self, mat):
        hash = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i-j not in hash:
                    hash[i-j] = [mat[i][j]]
                else:
                    hash[i-j].append(mat[i][j])
        for k in hash.values():
            k.sort()
        dp = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i-j in hash:
                    dp[i][j] = hash[i-j][0]
                    hash[i-j].pop(0)
        return dp