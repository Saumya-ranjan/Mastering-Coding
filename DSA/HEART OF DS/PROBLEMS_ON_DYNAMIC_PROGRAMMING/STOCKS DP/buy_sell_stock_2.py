def stock_second(prices):
    count = 0
    dp  = [0 for _ in range(len(prices))]
    for i in range(len(dp)-1):
        dp[i] = prices[i+1] - prices[i]
    for i in dp:
        if i>0:
            count+=i
    return count

stock_second([7,1,5,3,6,4])