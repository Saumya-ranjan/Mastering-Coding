#  --> GREEDY APPROACH

# def func(arr,target):
#     arr1 = []
#     arr.sort()
#     arr  = arr[::-1]
#     for i in arr:
#         while target >= i:
#             target = target - i
#             arr1.append(i)
#     if target !=0:
#         return -1

#     return arr1
# print(func([2,1],11) )  

# IT WON'T WORK AS:
# LETS SAY : {9,6,5,1} --> target = 11
# By greedy approach --> 9+1+1  --> 3coins
# By Dynamic approach --> 6+5 (minimum)



# DYNAMIC APPROACH --> TABULATION

def coin_change(coins,target):
    dp = [[0 for _ in range(target+1)] for _ in range(len(coins)+1)]
    for i in range(len(dp)):
        for j in range(target+1):
            if i==0 and j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = float('inf')
            elif coins[i-1] <= j:
                dp[i][j] =min( dp[i-1][j],1+dp[i][j-(coins[i-1])])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)

coin_change([1,2,3],5)