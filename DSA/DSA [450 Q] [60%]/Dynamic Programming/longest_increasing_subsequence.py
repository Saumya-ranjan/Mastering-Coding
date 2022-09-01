def func(a):
        dp = [1 for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(i):
                if a[i] > a[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        return dp[-1]
            

print(func([ 1, 101, 2, 3, 100]))