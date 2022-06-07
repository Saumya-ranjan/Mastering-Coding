def func(arr):
    curr_sum = max_sum = arr[0]
    for i in arr[1:]:
        curr_sum = max(curr_sum+i,i)
        max_sum = max(curr_sum,max_sum)
    print(max_sum)

        



func([2,-1,-2,3,-4,-5,1,4,5,6,7,3])