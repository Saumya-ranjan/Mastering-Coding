def product_subarray(nums):
    res = max(nums)
    cur_min ,cur_max = 1,1

    for i in nums:
        if i ==0:
            cur_min , cur_max = 1,1
            continue
        tmp_max = cur_max * i
        cur_max = max(i*cur_max , cur_min * i ,i)   # as cur_max is changing here
        cur_min = min(tmp_max, cur_min * i, i)
        res = max(res, cur_max)

    return res


print(product_subarray([2,3,-2,4]))