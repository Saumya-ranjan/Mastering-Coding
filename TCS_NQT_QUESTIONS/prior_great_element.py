def prior_great(arr):
    count = 1
    for i in range(1,len(arr)):
        if max(arr[:i]) < arr[i]:
            count+=1
    print(count)


prior_great([3,4,5,8,9])