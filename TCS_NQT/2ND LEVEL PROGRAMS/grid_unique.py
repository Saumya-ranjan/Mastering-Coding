#Tabulation --> dynamic programming

def func(r,c):
    dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
    # base case
    dp [1][1] = 1
    for i in range(r+1):
        for j in range(c+1):
            curr = dp[i][j]
            if i+1 <= r:
                dp[i+1][j] +=curr
            if j+1 <= c:
                dp[i][j+1] +=curr
    print(dp[-1][-1])


func(4,4)