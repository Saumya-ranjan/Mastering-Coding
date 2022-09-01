def max_sum_subarray(arr):
    curr_sum = max_sum = arr[0]
    for i in arr[1:]:
        curr_sum = max(i,curr_sum+i)
        max_sum  = max(curr_sum,max_sum)
    print(max_sum)



max_sum_subarray([2,3,-2,4])