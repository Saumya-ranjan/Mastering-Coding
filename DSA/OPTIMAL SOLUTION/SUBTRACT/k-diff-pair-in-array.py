from distutils.spawn import find_executable


def findPairs(nums,k):
    hash = {}
    arr = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] - k not in hash:
            hash[nums[i]] = i
        else:
            if [nums[i] , nums[i] - k] not in arr:
                arr.append([nums[i] , nums[i] - k])
            hash[nums[i]] = i
    return len(arr)
findPairs([1,2,3,4,5] , 1)
                
                