def add_a(arr):
    overall_a = 0
    count_a = 0
    other = 0
    for i in range(len(arr)):
        if arr[i] == 'a':
            count_a+=1
        elif arr[i] != 'a':
            other+=1
            overall_a += count_a
            count_a = 0
        if count_a > 2:
            return -1
    if count_a > 2:
        return -1
    else:
        overall_a+= count_a 
    return 2*(other+1) - overall_a

print(add_a("aa"))