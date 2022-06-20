def func(s):
    count = 0

    arr1 = []
    arr = []
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            r = s[i:j]
            arr.append(r)
    for i in arr:
        if len(i) ==3:
            arr1.append(i)

    for i in arr1:
        j = set(i)
        if len(j) == 3:
            count+=1
    print(count)


func( "xyzzaz")