def func(arr,target):
    arr1 = []
    dp = [None for i in range(target+1)]
    for i in range(len(dp)):
        if dp[i]!=None:
            for j in arr:
                if i+j <len(dp):                 
                    dp[i+j] = [*dp[i],j] 
        if dp[target] not in arr1:
            arr1.append(dp[target])
    print(arr1)
    return dp[target]




print(func([1,2,3],4))