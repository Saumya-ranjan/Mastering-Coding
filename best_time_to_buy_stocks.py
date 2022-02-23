def func(prices):
    if len(prices) <= 1:
        return 0
    buy_idx, sell_idx, min_idx, ans = 0, 1, 0, 0
    while sell_idx < len(prices):
        if prices[buy_idx] > prices[min_idx]:
            buy_idx = min_idx
        ans = max(ans, prices[sell_idx]-prices[buy_idx])
        if prices[sell_idx] < prices[min_idx]:
            min_idx = sell_idx
        sell_idx += 1
    print(ans)
    

func([7,1,5,3,6,4])