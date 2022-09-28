def higher_to_lower(arr):


    # Optimized method using gp:
    dp = [0 for _ in range(len(set(arr)) )]
    dp[0]  , dp[1]= 0 , 1
    counter =  2
    for i in range(2,len(dp)):
        dp[i] = dp[i-1] + counter
        counter+=1
    return dp[-1]



    #o(n^2)

    # arr.sort()
    # arr = arr[::-1]
    # count = 0
    # while len(set(arr))!=1:
    #     for i in range(len(arr)):
    #         if i == len(arr)-1:
    #             continue
    #         elif arr[i] == arr[i+1]:
    #             continue
    #         else:
    #             arr[i] = arr[i+1]
    #             count+=1
    # print(count)



print(higher_to_lower( [6,5,4,3,2,2,3,3,3,4,4,4,5,5,6,4,1]))