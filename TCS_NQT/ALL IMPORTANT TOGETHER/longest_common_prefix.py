def func(arr):
    res = ""
    a = arr[0]
    for i in range(len(a)):  #coding
        for j in arr[1:]: #codezen
            if a[i] != j[i]:   #c  == c
                return res
        res+=a[i]
    return res




print(func(["codingvvvvv", "codezinenvv", "codingninvv", "codeinrsvvv"]))