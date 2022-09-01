def func(str1):
    arr = []
    for i in range(len(str1)+1):
        for j in range(i+1,len(str1)+1):
            arr.append(str1[i:j])

    arr.sort(key = len)
    arr = arr[::-1]
  
    for i in arr:
        if i == i[::-1]:
            return i




print(func("babad"))