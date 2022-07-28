def stock(prices):
    # TLE:
    # dp = [0 for _ in range(len(prices))]
    # for i in range(len(prices)-1):
    #     dp[i] =  max(prices[i+1:]) - prices[i]
    # return (max(dp))

    min_price = float('inf')
    output = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > output:
            output = prices[i] - min_price
    return output
    
stock([7,1,5,3,6,4])