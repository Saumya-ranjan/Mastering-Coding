def findMaxLength(nums):
    arr1 = []
    arr = []
    hash = {}
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count+= -1
        else:
            count+=nums[i]
        arr.append(count)
    for i in range(len(arr)):
        if arr[i] == 0:
            arr1.append(i+1)
        elif arr[i] not in hash:
            hash[arr[i]] = i
        elif arr[i] in hash:
            arr1.append(i - hash[arr[i]])
    if len(arr1) == 0:
        return 0
    return max(arr1)
findMaxLength([0,0,1,0,0,0,1,1])