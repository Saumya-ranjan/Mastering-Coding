# def productSubSeqCount(arr, k):
#     dp = [[0 for _ in range(len(arr) + 1)]
#              for _ in range(k + 1)]
#     for i in range(1, k + 1):
#         for j in range(1, len(arr)+ 1):
#             dp[i][j] = dp[i][j - 1]
#             if arr[j - 1] <= i and arr[j - 1] > 0:  
#                 dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
#     return dp[k][len(arr)]
 
# A = [1,2,3,4]
# k = 10
# print(productSubSeqCount(A, k))

arr1 = []
k = 10
def func(arr, index, subarr):
    if index == len(arr):
        if len(subarr) != 0:
            arr1.append(subarr)
       
    else:
        func(arr, index + 1, subarr)
        func(arr, index + 1, subarr+[arr[index]])
    return
           
arr = [1, 2, 3, 4]

func(arr, 0, [])

arr3= []
for i in arr1:
    count = 1
    for j in i:
        count*=j
    if count<k:
        arr3.append(count)
print(len(arr3))
    
        