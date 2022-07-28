def frog_jump(heights):
    dp = [0 for _ in range(len(heights))]
    for i in range(1,len(dp)):
        ss = 10000
        if i>1:
            ss = abs(heights[i] - heights[i-2]) + dp[i-2]
        fs = abs(heights[i] - heights[i-1]) + dp[i-1]
        
        dp[i] = min(fs,ss)
    print(dp)


frog_jump([10,20,20,10])