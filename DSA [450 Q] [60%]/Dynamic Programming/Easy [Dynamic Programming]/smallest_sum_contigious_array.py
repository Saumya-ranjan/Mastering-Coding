def func(arr):
    curr_summ = minn_summ = arr[0]
    for i in arr[1:]:
        curr_summ = min(curr_summ+i,i)
        minn_summ = min(curr_summ,minn_summ)
    return minn_summ
        



print(func([3, -4, 2, -3, -1, 7, -5]))