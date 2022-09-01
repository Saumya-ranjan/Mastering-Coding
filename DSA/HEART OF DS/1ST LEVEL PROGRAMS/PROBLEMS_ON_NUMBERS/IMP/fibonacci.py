def func(n):
    # if n == 0:
    #     print([0])
    # if n ==1:
    #     print([0 ,1])
    # if n ==2:
    #     print([0,1,1])
    # arr = [0,1]
    # a = 0
    # b=1
    # for i in range(n-1):
    #     c = a+b
    #     arr.append(c)
    #     a , b = b, c
    # print(arr)
    if n==0:
        return[0]
    if n == 1:
        return [0,1]
    if n==2:
        return [0,1,1]
    dp =  [0 for i in range(n+1)]
    dp[1] = 1
    for i in range(2,len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    for i  in dp:
        print(i,end = " ")
        


print(func(5))