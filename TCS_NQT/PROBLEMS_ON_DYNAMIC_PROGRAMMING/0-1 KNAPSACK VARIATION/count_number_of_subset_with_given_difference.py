# 0-1 Knapsack Variaton:
def count_of_subset_diff(arr,diff):
    if (diff +sum(arr)) %2 !=0:
        return 0
    else:
        s1 = int((diff+sum(arr))/2)
    dp =  [[0 for _ in range(s1+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(s1+1):
            if j == 0:
                dp[i][j] = 1
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)

count_of_subset_diff([1,1,2,3],1)