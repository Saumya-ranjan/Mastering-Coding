def min_subset_sum(arr):
    target = sum(arr)
    arr1=  []
    dp = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    for i in range(len(dp[-1])):
        if dp[-1][i] == True:
            arr1.append(i)
    if len(arr1) %2 == 0:
        a = arr1[int(len(arr1)/2)]
        b = arr1[int((len(arr1)/2)-1)]
        return abs(a-b)
    else:
        a = arr1[int((len(arr1)+1)/2)]
        b =  arr1[int(((len(arr1)+1)/2)-2)]
        return abs(a-b)
print(min_subset_sum([1,2,7,10]))