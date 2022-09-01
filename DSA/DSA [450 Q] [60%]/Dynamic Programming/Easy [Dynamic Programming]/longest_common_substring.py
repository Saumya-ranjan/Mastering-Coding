def func(s1,s2):
    arr = []
    arr1 = []
    for i in range(len(s1)+1):
        for j in range(i+1,len(s1)+1):
            arr.append(s1[i:j])
    for i in range(len(s2)+1):
        for j in range(i+1,len(s2)+1):
            arr1.append(s2[i:j])
    arr.sort(key = len)
    arr = arr[::-1]
    for i in arr:
        if i in arr1:
            return len(i)

print(func("ABCDGH", "ACDGHR"))