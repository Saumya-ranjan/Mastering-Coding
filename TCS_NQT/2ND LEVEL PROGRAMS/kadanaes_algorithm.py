def func(arr):
    max_sum = curr_sum = arr[0]
    for i in arr[1:]:
        curr_sum = max(curr_sum+i,i)
        max_sum = max(curr_sum,max_sum)
    return max_sum


print(func([1] ))