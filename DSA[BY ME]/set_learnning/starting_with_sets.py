def func(x):
    arr = []
    count  =0
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            arr.append(x[i:j])
    print(arr)
    for i in arr:
        if set(i) == set('aeiou'):
            count+=1
    print(count)
func("aeiouu")

