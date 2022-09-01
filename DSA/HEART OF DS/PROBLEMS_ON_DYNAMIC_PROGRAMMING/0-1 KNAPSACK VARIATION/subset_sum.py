# GENERAL VARIATION  -->UNBOUNDED KNAPSACK

# def subset_sum(arr,target):
#     dp = [False for _ in range(target+1)] 
#     dp[0] = True
#     for i in range(len(dp)):
#         for j in range(len(arr)):
#             if dp[i] == True:
#                 if i+arr[j] < len(dp):
#                     dp[i+arr[j]] = True
#     print(dp[-1])

# subset_sum([3,3,2],7)

# 0-1 KNAPSACK VARIATION

def subset_sum(arr,target):
    dp = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]        
    print(dp)

    
  
subset_sum([5,5,1],11)