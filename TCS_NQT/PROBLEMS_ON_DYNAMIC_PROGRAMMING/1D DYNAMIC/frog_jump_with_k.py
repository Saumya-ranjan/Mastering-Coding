# frog can jump k times .

def frog_jump_k(arr,k):
    dp = [0 for _ in range(len(arr))]
    for i in range(1,len(arr)):
        step  = 0
        min_step = 100000
        for j in range(1,k+1):
            if i-j >= 0:
                step = dp[i-j] + abs(arr[i] - arr[i-j])
        dp[i] = min(step , min_step)
        min_step = step
    print(dp)



frog_jump_k([10,20,40,50,60,30,40] , 2)