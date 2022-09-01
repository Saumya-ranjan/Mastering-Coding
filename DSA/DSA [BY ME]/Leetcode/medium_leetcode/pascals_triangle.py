def func(x):
    a = [1]
    ans = []
    for i in range(x):
        ans.append(a* (i+1))
    

    for a in range(1,x):
        for b in range(1,a):
            ans[a][b] = ans[a-1][b] + ans[a-1][b-1]
    print(ans)
    # for i in range(1, x):
    #     for j in range(1, i):
    #         ans[i][j] = ans[i-1][j] + ans[i-1][j-1] # update each as sum of two elements from above row
    #     print(ans)




func(5)