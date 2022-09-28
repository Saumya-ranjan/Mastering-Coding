def func(a):
    # Optimze the code -- > 
    # o(n) --> Two Pointer:
    max_len = 0
    l  = 0
    for r in range(2 , len(a)):
        if a[r] == a[r-1] == a[r-2]:
            max_len = max(max_len , r-l)
            l = r-1
        elif r == len(a)-1:
            max_len = max(max_len , r-l +1)
    return max_len

# BRUTE FORCE -- > 

    # arr =[]
    # for i in range(len(a)+1):
    #     for j in range(i+1 , len(a)+1):
    #         arr.append(a[i:j])
    # arr1 = sorted(arr , key = len)

    # arr1 = arr1[::-1]
    # print(arr1)

    # for i in range(len(arr1)):
    #     if 'bbb' not in arr1[i] and 'aaa' not in arr1[i]:
    #         return len(arr1[i])

print(func("abaaaa"))