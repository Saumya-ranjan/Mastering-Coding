def func(arr):
    dp=[1]*len(arr)
    dp[0]=arr[0]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[j]+arr[i],dp[i])
            else:
                dp[i]=max(dp[i],arr[i])
    print(dp)

func([1, 101, 2, 3, 100])