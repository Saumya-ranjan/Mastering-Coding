def swapping_array(arr):
    sort_arr = sorted(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] == sort_arr[i]:
            continue
        else:
            count+=1
            arr[arr.index(min(arr[i:]))],arr[i]  =  arr[i],arr[arr.index(min(arr[i:]))]
    
    print(count)



swapping_array([2, 8, 5, 4])