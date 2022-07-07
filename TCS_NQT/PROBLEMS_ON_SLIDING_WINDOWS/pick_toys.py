def pick_toys(str1,target):
    arr2 = []
    arr = []
    for i in range(len(str1)+1):
        for j in range(i+1,len(str1)+1):
            arr.append(str1[i:j])
    for i in arr:
        if len(set(i)) == target:
            arr2.append(i)
    arr2.sort(key = len)
    print(len(arr2[-1]))




pick_toys("abaccab",2)