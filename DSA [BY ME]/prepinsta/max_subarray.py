def func(nums):
    if not nums:
            return 0

    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    print(maxSum)
        


func([-2,1,-3,4,-1,2,1,-5,4])