def search(nums,target):
    l = 0
    r = len(nums) 
    for i in range(len(nums)):
        if r > l:
            a = int((l+r) /2)
            if nums[a] ==target:
                return a
            if nums[a] < target:
                l = a
            else:
                r = a
    return -1
search([-1,0,5], 5)            