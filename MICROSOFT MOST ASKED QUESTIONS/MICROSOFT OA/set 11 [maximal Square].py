class Solution:
    def maximalSquare(matrix):
        count = 0
        # dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        # for i in range(1 , len(dp)):
        #     for j in range(1 , len(dp[0])):
        #         dp[i][j] = matrix[i-1][j-1]
        for i in range(1, len(matrix)):
            for j in range(1 , len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = str(min(int(matrix[i-1][j-1]), int(matrix[i-1][j]) , int(matrix[i][j-1])) +1)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) > count:
                    count =int( matrix[i][j])
        return count*count
    maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])     
                
        