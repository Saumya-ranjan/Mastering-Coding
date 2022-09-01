def func(x):
    a = [1]
    ans = []
    for i in range(x):
        ans.append(a* (i+1))
    for a in range(1,x):
        for b in range(1,a):
            ans[a][b] = ans[a-1][b] + ans[a-1][b-1]
    print(ans)

func(5)