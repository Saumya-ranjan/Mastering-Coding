def func(nums):                 # big o(n)
    arr = []
    for i in range(len(nums)):
        arr.append(nums[nums[i]])
    nums.clear()
    nums+=arr
    print(nums)

func([1,2,3,4])