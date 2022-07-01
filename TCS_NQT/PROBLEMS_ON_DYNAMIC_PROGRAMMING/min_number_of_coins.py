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

def func(arr,target):
    arr.sort()
    # base case:
    if len(arr) == 0 or target ==0:
        return 0
    dp = [[0 for _ in range(target+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(1,target+1):
            dp[0][j] = float('inf')
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i-1]]+1)
    print(dp)


func([9,6,5,1],11)