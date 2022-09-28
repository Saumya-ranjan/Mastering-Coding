def func(arr):
    y_count = 0
    min_del = 0
    for i in range(len(arr)):
        if arr[i] == 'X':
            min_del = min(y_count , min_del+1)
        else:
            y_count+=1
    print(min_del)



func('XYXXYY')