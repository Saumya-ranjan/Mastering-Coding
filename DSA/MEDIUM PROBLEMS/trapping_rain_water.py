# Optimized Solution:
def trapping_rain_water(height):
    count = 0
    dp = [[0 for _ in range(len(height))] for _ in range(3)]
    for i in range(len(dp)):
        for j in range(1,len(height)):
            if i == 0:
                dp[i][j]  = max(height[:j])
            elif i == 1:
                dp[i][j] = max(height[j:])
            elif i == 2:
                dp[i][j] = min(dp[i-1][j],dp[i-2][j]) - height[j]
    for i in dp[-1]:
        if i >0:
            count+=i
    print(count)
            



trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])