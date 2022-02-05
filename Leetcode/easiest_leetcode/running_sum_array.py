def func(nums):                    # big o(n)
    arr = []              
    count = 0
    for i in range(len(nums)):
        count+=nums[i]
        arr.append(count)
    nums.clear()
    nums+=arr
    print(nums)
    

func([1,2,3,4])